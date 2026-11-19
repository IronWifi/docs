#!/usr/bin/env python3
"""Security spec for the Azure AD PEAP-MSCHAPv2 bridge published in this repo.

The guide tells a customer to install the fenced PHP block as
/var/www/lighttpd/ntlm.php and to point the IronWifi Azure connector at
http://that-host/ntlm.php. These tests run that block, unchanged, under PHP.

They fail while the published script calls /bin/ntlm_auth for a caller that
has not presented the bridge secret. They pass once that script refuses such
callers before executing ntlm_auth, and still performs the domain check for a
caller that presents the secret on the same request.

Contract the published PHP must meet:

- Read the shared secret from the environment variable IRONWIFI_BRIDGE_SECRET.
- Take the caller's secret only from the query parameter named secret.
- If the environment variable is missing or empty, do not execute ntlm_auth.
- If secret is missing, is not a string, or is not exactly equal to the
  environment variable, do not execute ntlm_auth. A prefix, a suffix, the
  value in a different parameter, or the value only in a request header does
  not authorize the request.
- Do not execute ntlm_auth, and do not return a line beginning with NT_KEY,
  unless that check succeeded for this same request. Authorization does not
  carry to a later request.
- On an authorized request, keep the published behavior: strip a DOMAIN\\user
  username at the last backslash when that backslash is not at index 0, pass
  username, challenge, and nt-response from this request to
  /bin/ntlm_auth --request-nt-key, and echo the first output line.
- Do not place the bridge secret on the ntlm_auth command line.
- Keep shell quoting around the three values so a username cannot break out
  of the command.

Run:
  python3 tests/ntlm_bridge_auth_test.py

The runner re-executes itself under a private mount namespace so the published
absolute path /bin/ntlm_auth is the stand-in in tests/support/ntlm_auth_samba410.py
and the host binaries are left unchanged. php-cli is required.

These tests are expected to fail until the vulnerability is fixed.

Not covered, because they are not a second copy of this bridge: the unused
domain query parameter, a username whose only backslash is at index 0, and
rate limiting of calls that already presented the secret. The published
command does not pass --allow-mschapv2; the stand-in follows that command.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GUIDE = REPO_ROOT / "configuration-guides" / "azure-ad-authentication-peap-mschapv2.md"
STANDIN = Path(__file__).resolve().parent / "support" / "ntlm_auth_samba410.py"
PLACEHOLDER_BRIDGE_SECRET = "PLACEHOLDER_BRIDGE_SECRET"
INJECTION_MARKER = Path("/tmp/ntlm-bridge-injection-marker")

# Imported after the namespace re-exec so the stand-in file is the one we ship.
sys.path.insert(0, str(STANDIN.parent))
from ntlm_auth_samba410 import LOGON_FAILURE_LINE, strhex_to_str  # noqa: E402


STRHEX_C = r"""
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stddef.h>
static size_t strhex_to_str(char *p, size_t p_len, const char *strhex, size_t strhex_len)
{
	size_t i = 0;
	size_t num_chars = 0;
	unsigned char lonybble, hinybble;
	const char *hexchars = "0123456789ABCDEF";
	char *p1 = NULL, *p2 = NULL;
	if (strncasecmp(strhex, "0x", 2) == 0) {
		i += 2;
	}
	for (; i+1 < strhex_len && strhex[i] != 0 && strhex[i+1] != 0; i++) {
		p1 = strchr(hexchars, toupper((unsigned char)strhex[i]));
		if (p1 == NULL) break;
		i++;
		p2 = strchr(hexchars, toupper((unsigned char)strhex[i]));
		if (p2 == NULL) break;
		hinybble = (unsigned char)(p1 - hexchars);
		lonybble = (unsigned char)(p2 - hexchars);
		if (num_chars >= p_len) break;
		p[num_chars] = (hinybble << 4) | lonybble;
		num_chars++;
		p1 = NULL;
		p2 = NULL;
	}
	return num_chars;
}
int main(int argc, char **argv) {
	char buf[256];
	size_t n;
	size_t i;
	if (argc != 2) return 2;
	memset(buf, 0, sizeof(buf));
	n = strhex_to_str(buf, sizeof(buf), argv[1], strlen(argv[1]));
	printf("%zu", n);
	for (i = 0; i < n; i++) printf(" %02X", (unsigned char)buf[i]);
	printf("\n");
	return 0;
}
"""


def _ensure_mount_namespace() -> None:
    if os.environ.get("NTLM_BRIDGE_TEST_NS") == "1":
        return
    script = str(Path(__file__).resolve())
    os.execvp(
        "sudo",
        [
            "sudo",
            "unshare",
            "--mount",
            "env",
            "NTLM_BRIDGE_TEST_NS=1",
            sys.executable,
            script,
            *sys.argv[1:],
        ],
    )


def _install_standin() -> None:
    """Bind an overlay over /usr so /bin/ntlm_auth (a /usr/bin symlink) is ours."""
    upper = Path("/tmp/ntlm-bridge-ovl-upper")
    work = Path("/tmp/ntlm-bridge-ovl-work")
    merged = Path("/tmp/ntlm-bridge-ovl-merged")
    for path in (upper, work, merged):
        if path.exists():
            subprocess.check_call(["rm", "-rf", str(path)])
        path.mkdir(parents=True)
    subprocess.check_call(
        [
            "mount",
            "-t",
            "overlay",
            "overlay",
            "-o",
            "lowerdir=/usr,upperdir=%s,workdir=%s" % (upper, work),
            str(merged),
        ]
    )
    destination = merged / "bin" / "ntlm_auth"
    shutil.copy(STANDIN, destination)
    destination.chmod(0o755)
    subprocess.check_call(["mount", "--bind", str(merged), "/usr"])


def extract_published_php(guide_text: str) -> str:
    blocks = re.findall(r"```\n(.*?)```", guide_text, re.S)
    for block in blocks:
        if "<?php" in block and "/bin/ntlm_auth" in block:
            return block.strip() + "\n"
    raise AssertionError("the guide has no fenced ntlm.php block")


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class BridgeHarness:
    def __init__(self, php_source: str, secret: str | None, log_path: Path, fixture_path: Path):
        self.root = Path(tempfile.mkdtemp(prefix="ntlm-bridge-"))
        (self.root / "ntlm.php").write_text(php_source, encoding="utf-8")
        self.log_path = log_path
        self.fixture_path = fixture_path
        self.port = _free_port()
        env = os.environ.copy()
        env["NTLM_AUTH_LOG"] = str(log_path)
        env["NTLM_AUTH_FIXTURE"] = str(fixture_path)
        if secret is None:
            env.pop("IRONWIFI_BRIDGE_SECRET", None)
        else:
            env["IRONWIFI_BRIDGE_SECRET"] = secret
        self.server_log = self.root / "php-server.log"
        self._server_log_handle = open(self.server_log, "w", encoding="utf-8")
        self.proc = subprocess.Popen(
            [
                "php",
                "-d",
                "display_errors=0",
                "-d",
                "log_errors=1",
                "-S",
                "127.0.0.1:%d" % self.port,
                "-t",
                str(self.root),
            ],
            env=env,
            stdout=self._server_log_handle,
            stderr=subprocess.STDOUT,
        )
        self._wait_until_listening()

    def _wait_until_listening(self) -> None:
        deadline = time.time() + 5
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(
                    "php built-in server exited: %s" % self.server_log.read_text(encoding="utf-8")
                )
            try:
                with socket.create_connection(("127.0.0.1", self.port), timeout=0.2):
                    return
            except OSError:
                time.sleep(0.05)
        raise RuntimeError(
            "php built-in server did not accept connections: %s"
            % self.server_log.read_text(encoding="utf-8")
        )

    def request(
        self,
        params: dict[str, str] | None = None,
        *,
        query: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> tuple[int, str]:
        if query is None:
            query = urllib.parse.urlencode(params or {})
        url = "http://127.0.0.1:%d/ntlm.php" % self.port
        if query:
            url += "?" + query
        req = urllib.request.Request(url, headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status, response.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as error:
            return error.code, error.read().decode("utf-8", "replace")

    def close(self) -> None:
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self._server_log_handle.close()
        shutil.rmtree(self.root, ignore_errors=True)


class NtlmBridgeAuthTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _install_standin()
        cls.php_source = extract_published_php(GUIDE.read_text(encoding="utf-8"))
        cls.tmp = Path(tempfile.mkdtemp(prefix="ntlm-bridge-state-"))
        cls.log_path = cls.tmp / "ntlm_auth.log"
        cls.fixture_path = cls.tmp / "fixture.json"
        cls.challenge = "0011223344556677"
        cls.correct_response = "aa" * 24
        cls.session_key = "00112233445566778899AABBCCDDEEFF"
        cls.fixture_path.write_text(
            json.dumps(
                {
                    "users": {
                        "bob": {
                            "nt_response_hex": cls.correct_response,
                            "session_key_hex": cls.session_key,
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        cls.with_secret = BridgeHarness(
            cls.php_source, PLACEHOLDER_BRIDGE_SECRET, cls.log_path, cls.fixture_path
        )
        cls.without_secret = BridgeHarness(
            cls.php_source, None, cls.log_path, cls.fixture_path
        )
        cls._compile_strhex()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.with_secret.close()
        cls.without_secret.close()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    @classmethod
    def _compile_strhex(cls) -> None:
        source = cls.tmp / "strhex.c"
        binary = cls.tmp / "strhex"
        source.write_text(STRHEX_C, encoding="utf-8")
        subprocess.check_call(
            ["gcc", "-O2", "-o", str(binary), str(source)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        cls.strhex_bin = binary

    def setUp(self) -> None:
        self.log_path.write_text("", encoding="utf-8")
        if INJECTION_MARKER.exists():
            INJECTION_MARKER.unlink()

    def _invocations(self) -> list[dict]:
        text = self.log_path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    def _assert_not_forwarded(self, status: int, body: str) -> None:
        self.assertEqual(
            self._invocations(),
            [],
            "ntlm_auth ran before the caller was authorized; body=%r status=%s" % (body, status),
        )
        self.assertNotIn("NT_KEY", body)
        self.assertNotIn(self.session_key, body.upper())
        self.assertNotIn("hex decode of ", body)
        self.assertNotIn(LOGON_FAILURE_LINE, body)
        self.assertFalse(INJECTION_MARKER.exists())

    def _authorized_params(self, **overrides: str) -> dict[str, str]:
        params = {
            "secret": PLACEHOLDER_BRIDGE_SECRET,
            "username": "bob",
            "challenge": self.challenge,
            "response": self.correct_response,
        }
        params.update(overrides)
        return params

    def test_standin_hex_decode_matches_samba_util(self) -> None:
        samples = ["", "0x0011223344556677", "0011223344556677", "zz", "ABC", "aa" * 24, "GG11"]
        for sample in samples:
            completed = subprocess.run(
                [str(self.strhex_bin), sample],
                check=True,
                capture_output=True,
                text=True,
            )
            count_text, *hex_bytes = completed.stdout.strip().split()
            expected = bytes(int(part, 16) for part in hex_bytes)
            self.assertEqual(int(count_text), len(expected))
            self.assertEqual(strhex_to_str(sample), expected)

    def test_standin_prints_nt_key_only_for_the_accepted_response(self) -> None:
        env = os.environ.copy()
        env["NTLM_AUTH_FIXTURE"] = str(self.fixture_path)
        env["NTLM_AUTH_LOG"] = str(self.log_path)
        success = subprocess.run(
            [
                "/bin/ntlm_auth",
                "--request-nt-key",
                "--username=bob",
                "--challenge=%s" % self.challenge,
                "--nt-response=%s" % self.correct_response,
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertEqual(success.returncode, 0)
        self.assertEqual(success.stdout, "NT_KEY: %s\n" % self.session_key)
        failure = subprocess.run(
            [
                "/bin/ntlm_auth",
                "--request-nt-key",
                "--username=bob",
                "--challenge=%s" % self.challenge,
                "--nt-response=%s" % ("bb" * 24),
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertNotEqual(failure.returncode, 0)
        self.assertEqual(failure.stdout, LOGON_FAILURE_LINE + "\n")
        empty = subprocess.run(
            [
                "/bin/ntlm_auth",
                "--request-nt-key",
                "--username=bob",
                "--challenge=",
                "--nt-response=",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertNotEqual(empty.returncode, 0)
        self.assertEqual(empty.stderr, "hex decode of  failed! (only got 0 bytes)\n")

    def test_unauthenticated_correct_guess_does_not_return_nt_key(self) -> None:
        status, body = self.with_secret.request(
            {
                "username": "bob",
                "challenge": self.challenge,
                "response": self.correct_response,
            }
        )
        self._assert_not_forwarded(status, body)

    def test_wrong_secret_does_not_call_ntlm_auth(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(secret="PLACEHOLDER_BRIDGE_SECRET_WRONG")
        )
        self._assert_not_forwarded(status, body)

    def test_prefix_of_secret_does_not_call_ntlm_auth(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(secret=PLACEHOLDER_BRIDGE_SECRET[:-1])
        )
        self._assert_not_forwarded(status, body)

    def test_secret_with_extra_suffix_does_not_call_ntlm_auth(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(secret=PLACEHOLDER_BRIDGE_SECRET + "X")
        )
        self._assert_not_forwarded(status, body)

    def test_secret_in_the_wrong_parameter_does_not_authorize(self) -> None:
        params = self._authorized_params()
        params.pop("secret")
        params["token"] = PLACEHOLDER_BRIDGE_SECRET
        status, body = self.with_secret.request(params)
        self._assert_not_forwarded(status, body)

    def test_secret_only_in_header_does_not_authorize(self) -> None:
        params = self._authorized_params()
        params.pop("secret")
        status, body = self.with_secret.request(
            params,
            headers={"X-IronWifi-Bridge-Secret": PLACEHOLDER_BRIDGE_SECRET},
        )
        self._assert_not_forwarded(status, body)

    def test_secret_array_does_not_authorize(self) -> None:
        query = urllib.parse.urlencode(
            [
                ("secret[]", PLACEHOLDER_BRIDGE_SECRET),
                ("username", "bob"),
                ("challenge", self.challenge),
                ("response", self.correct_response),
            ]
        )
        status, body = self.with_secret.request(query=query)
        self._assert_not_forwarded(status, body)

    def test_missing_bridge_secret_fails_closed(self) -> None:
        status, body = self.without_secret.request(
            {
                "secret": PLACEHOLDER_BRIDGE_SECRET,
                "username": "bob",
                "challenge": self.challenge,
                "response": self.correct_response,
            }
        )
        self._assert_not_forwarded(status, body)

    def test_empty_verification_url_does_not_call_ntlm_auth(self) -> None:
        # The guide's own check is a browser GET of /ntlm.php with no query.
        status, body = self.with_secret.request({})
        self._assert_not_forwarded(status, body)

    def test_repeated_unauthenticated_guesses_do_not_reach_ntlm_auth(self) -> None:
        for _ in range(5):
            status, body = self.with_secret.request(
                {
                    "username": "bob",
                    "challenge": self.challenge,
                    "response": "cc" * 24,
                }
            )
            self._assert_not_forwarded(status, body)

    def test_authorization_does_not_carry_to_the_next_request(self) -> None:
        status, body = self.with_secret.request(self._authorized_params())
        self.assertIn("NT_KEY: %s" % self.session_key, body, "authorized status=%s body=%r" % (status, body))
        self.log_path.write_text("", encoding="utf-8")
        status, body = self.with_secret.request(
            {
                "username": "bob",
                "challenge": self.challenge,
                "response": self.correct_response,
            }
        )
        self._assert_not_forwarded(status, body)

    def test_authenticated_correct_response_returns_nt_key_for_that_request(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(username="TESTGMAIL\\bob")
        )
        self.assertIn("NT_KEY: %s" % self.session_key, body, "status=%s body=%r" % (status, body))
        parsed = [entry for entry in self._invocations() if entry.get("stage") == "parsed"]
        self.assertEqual(len(parsed), 1)
        entry = parsed[0]
        self.assertEqual(entry["username"], "bob")
        self.assertEqual(entry["challenge"], self.challenge)
        self.assertEqual(entry["nt_response"], self.correct_response)
        joined = " ".join(entry["argv"])
        self.assertNotIn(PLACEHOLDER_BRIDGE_SECRET, joined)

    def test_authenticated_wrong_response_does_not_return_nt_key(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(response="dd" * 24)
        )
        self.assertNotIn("NT_KEY", body)
        self.assertIn(LOGON_FAILURE_LINE, body, "status=%s body=%r" % (status, body))
        self.assertEqual(len([e for e in self._invocations() if e.get("stage") == "parsed"]), 1)

    def test_authenticated_empty_challenge_returns_hex_decode_error(self) -> None:
        status, body = self.with_secret.request(
            self._authorized_params(challenge="", response="")
        )
        self.assertIn("hex decode of  failed! (only got 0 bytes)", body)
        self.assertNotIn("NT_KEY", body)
        self.assertTrue(self._invocations(), "status=%s body=%r" % (status, body))

    def test_authenticated_fields_come_from_the_authorized_request(self) -> None:
        other_challenge = "ffeeddccbbaa9988"
        other_response = "11" * 24
        status, body = self.with_secret.request(
            self._authorized_params(
                username="bob",
                challenge=other_challenge,
                response=other_response,
            )
        )
        parsed = [entry for entry in self._invocations() if entry.get("stage") == "parsed"]
        self.assertEqual(len(parsed), 1, "status=%s body=%r log=%r" % (status, body, self._invocations()))
        self.assertEqual(parsed[0]["username"], "bob")
        self.assertEqual(parsed[0]["challenge"], other_challenge)
        self.assertEqual(parsed[0]["nt_response"], other_response)
        self.assertNotIn(self.session_key, body.upper())

    def test_authenticated_username_cannot_break_out_of_the_command(self) -> None:
        username = "bob' $(touch %s)" % INJECTION_MARKER
        status, body = self.with_secret.request(self._authorized_params(username=username))
        parsed = [entry for entry in self._invocations() if entry.get("stage") == "parsed"]
        self.assertEqual(len(parsed), 1, "status=%s body=%r" % (status, body))
        self.assertEqual(parsed[0]["username"], username)
        self.assertFalse(
            INJECTION_MARKER.exists(),
            "the username was executed by the shell before ntlm_auth",
        )


if __name__ == "__main__":
    _ensure_mount_namespace()
    unittest.main(verbosity=2)
