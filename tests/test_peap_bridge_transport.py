#!/usr/bin/env python3
"""Contract for the Azure PEAP-MSCHAPv2 bridge in the configuration guide.

Customers copy the ntlm.php block in
configuration-guides/azure-ad-authentication-peap-mschapv2.md onto a host and
point the IronWifi Azure connector at the Bridge URL in that guide. These
tests deploy that block as written and perform the handshake it is willing to
complete.

They are expected to fail until that bridge no longer accepts the MSCHAPv2
challenge and NT response from the query string, no longer returns the NT
session-key line for such a request, and the guide serves the bridge over
HTTPS. A successful exchange has to submit those values in the request body
(the same field names the script already uses, as
application/x-www-form-urlencoded) and the access log for that exchange must
not contain them.

Run:
    python3 tests/test_peap_bridge_transport.py
"""

import http.client
import os
import re
import shutil
import socket
import subprocess
import tempfile
import textwrap
import time
import unittest
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "configuration-guides" / "azure-ad-authentication-peap-mschapv2.md"

# Not a key. The stand-in helper prints this where Samba ntlm_auth prints
# "NT_KEY: %s" on a successful --request-nt-key exchange.
NT_KEY_LINE = "NT_KEY: PLACEHOLDER_NT_SESSION_KEY"

# Distinctive stand-in handshake material. Not derived from a password.
BODY_CHALLENGE = "c0ffee01c0ffee02"
BODY_RESPONSE = "d00d" * 12  # 24 bytes, the minimum ntlm_auth accepts
QUERY_CHALLENGE = "0011223344556677"
QUERY_RESPONSE = "ab" * 24
OVERRIDE_CHALLENGE = "ff00ff00ff00ff00"
OVERRIDE_RESPONSE = "ee" * 24


def _php_bridges():
    """Every documented ntlm_auth PHP block a customer is told to deploy."""
    bridges = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or "tests" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".php", ".inc"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "ntlm_auth" not in text:
            continue
        if path.suffix.lower() == ".php":
            bridges.append((path, text))
            continue
        for block in re.findall(r"```[^\n]*\n(.*?)```", text, re.S):
            if "ntlm_auth" in block and "<?php" in block:
                bridges.append((path, block))
    return bridges


def _ntlm_auth_stub(log_path: Path) -> str:
    """Stand-in for /bin/ntlm_auth.

    Follows the checks and stdout contract in Samba 4.10.16
    source3/utils/ntlm_auth.c: hex-decode --challenge to 8 bytes and
    --nt-response to at least 24 bytes during option parsing, require a
    username, then on --request-nt-key print a single NT_KEY line. The
    winbind round-trip is not run; the line stands in for the printf on that
    success path and is not a real session key.
    """
    return textwrap.dedent(
        f"""\
        #!/usr/bin/env python3
        import sys

        LOG = {str(log_path)!r}

        def decode(value):
            try:
                return bytes.fromhex(value)
            except ValueError:
                return None

        args = sys.argv[1:]
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(repr(args) + "\\n")

        vals = {{}}
        request_nt_key = False
        index = 0
        while index < len(args):
            item = args[index]
            if item == "--request-nt-key":
                request_nt_key = True
                index += 1
                continue
            if item.startswith("--") and "=" in item:
                name, value = item.split("=", 1)
                vals[name] = value
                index += 1
                continue
            if item.startswith("--") and index + 1 < len(args):
                vals[item] = args[index + 1]
                index += 2
                continue
            index += 1

        challenge = decode(vals.get("--challenge", ""))
        if challenge is None or len(challenge) != 8:
            got = 0 if challenge is None else len(challenge)
            sys.stderr.write(
                "hex decode of %s failed! (only got %d bytes)\\n"
                % (vals.get("--challenge", ""), got)
            )
            sys.exit(1)
        response = decode(vals.get("--nt-response", ""))
        if response is None or len(response) < 24:
            got = 0 if response is None else len(response)
            sys.stderr.write(
                "hex decode of %s failed! (only got %d bytes)\\n"
                % (vals.get("--nt-response", ""), got)
            )
            sys.exit(1)
        username = vals.get("--username", "")
        if not username:
            sys.stderr.write("username must be specified!\\n\\n")
            sys.exit(1)
        if request_nt_key:
            sys.stdout.write({NT_KEY_LINE!r} + "\\n")
        sys.exit(0)
        """
    )


class GuideTransportTextTests(unittest.TestCase):
    def test_documented_ntlm_bridge_urls_use_https(self):
        text = GUIDE.read_text(encoding="utf-8")
        urls = re.findall(r"https?://[^\s)\]>\"]*ntlm\.php", text)
        self.assertTrue(urls, "guide no longer names the ntlm.php bridge URL")
        for url in urls:
            self.assertTrue(
                url.startswith("https://"),
                f"bridge URL is cleartext HTTP: {url}",
            )

    def test_documented_lighttpd_enables_tls(self):
        text = GUIDE.read_text(encoding="utf-8")
        if re.search(r'ssl\.engine\s*=\s*"enable"', text) is None:
            self.fail(
                'the Lighttpd setup in the guide never enables TLS '
                '(expected ssl.engine = "enable")'
            )


class BridgeBehaviorTests(unittest.TestCase):
    """Deploy every documented ntlm.php and exercise the handshake."""

    @classmethod
    def setUpClass(cls):
        bridges = _php_bridges()
        if not bridges:
            raise unittest.SkipTest("no documented ntlm_auth bridge to deploy")
        cls.bridges = bridges
        cls.work = Path(tempfile.mkdtemp(prefix="peap-bridge-"))
        cls.arg_log = cls.work / "ntlm-auth-args.log"
        cls.access_log = cls.work / "access.log"
        cls.error_log = cls.work / "error.log"
        cls.docroot = cls.work / "www"
        cls.docroot.mkdir()
        # The guide's script invokes this absolute path.
        stub = cls.work / "ntlm_auth"
        stub.write_text(_ntlm_auth_stub(cls.arg_log), encoding="utf-8")
        stub.chmod(0o755)
        cls._replaced_ntlm_auth = Path("/bin/ntlm_auth").exists()
        if cls._replaced_ntlm_auth:
            subprocess.check_call(
                ["sudo", "cp", "-a", "/bin/ntlm_auth", str(cls.work / "ntlm_auth.orig")]
            )
        subprocess.check_call(["sudo", "cp", str(stub), "/bin/ntlm_auth"])
        subprocess.check_call(["sudo", "chmod", "755", "/bin/ntlm_auth"])

        sock = socket.socket()
        sock.bind(("127.0.0.1", 0))
        cls.port = sock.getsockname()[1]
        sock.close()

        # This host's lighttpd 1.4.74 package has no mod_fastcgi. mod_cgi with
        # php-cgi still runs the documented script: Lighttpd puts the query
        # string in QUERY_STRING and the default access log records the
        # original request target. PHP-FPM in the guide uses that same CGI
        # environment.
        conf = cls.work / "lighttpd.conf"
        conf.write_text(
            textwrap.dedent(
                f"""\
                server.document-root = "{cls.docroot}"
                server.bind = "127.0.0.1"
                server.port = {cls.port}
                server.errorlog = "{cls.error_log}"
                server.modules = ( "mod_accesslog", "mod_cgi" )
                accesslog.filename = "{cls.access_log}"
                cgi.assign = ( ".php" => "/usr/bin/php-cgi" )
                """
            ),
            encoding="utf-8",
        )
        cls.lighttpd = subprocess.Popen(
            ["lighttpd", "-D", "-f", str(conf)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        deadline = time.time() + 5
        while time.time() < deadline:
            if cls.lighttpd.poll() is not None:
                err = cls.error_log.read_text(encoding="utf-8", errors="replace") if cls.error_log.exists() else ""
                raise RuntimeError(f"lighttpd exited: {err}")
            try:
                with socket.create_connection(("127.0.0.1", cls.port), 0.2):
                    break
            except OSError:
                time.sleep(0.05)
        else:
            raise RuntimeError("lighttpd did not accept connections")

    @classmethod
    def tearDownClass(cls):
        proc = getattr(cls, "lighttpd", None)
        if proc is not None and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
        if Path("/bin/ntlm_auth").exists() or getattr(cls, "_replaced_ntlm_auth", False):
            if getattr(cls, "_replaced_ntlm_auth", False):
                subprocess.check_call(
                    ["sudo", "cp", "-a", str(cls.work / "ntlm_auth.orig"), "/bin/ntlm_auth"]
                )
            else:
                subprocess.check_call(["sudo", "rm", "-f", "/bin/ntlm_auth"])
        work = getattr(cls, "work", None)
        if work is not None:
            shutil.rmtree(work, ignore_errors=True)

    def setUp(self):
        self.arg_log.write_text("", encoding="utf-8")
        for path, script in self.bridges:
            # One customer-facing script per guide. Re-copy before each test
            # so a test cannot depend on a previous request's side effects.
            target = self.docroot / "ntlm.php"
            if not script.startswith("<?php"):
                self.fail(f"bridge in {path} is not a PHP script")
            target.write_text(script if script.endswith("\n") else script + "\n", encoding="utf-8")

    def _request(self, method, path, form=None):
        body = None
        headers = {}
        if form is not None:
            body = urllib.parse.urlencode(form)
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        try:
            connection.request(method, path, body=body, headers=headers)
            response = connection.getresponse()
            payload = response.read().decode("utf-8", errors="replace")
            return response.status, payload
        finally:
            connection.close()

    def _args(self):
        if not self.arg_log.exists():
            return ""
        return self.arg_log.read_text(encoding="utf-8")

    def _access_log(self):
        # mod_accesslog keeps lines in a buffer until the timestamp second
        # changes (or the 4-second periodic flush). A later request is what
        # writes the previous line.
        start = int(time.time())
        while int(time.time()) == start:
            time.sleep(0.02)
        self._request("GET", "/access-log-flush")
        time.sleep(0.1)
        if not self.access_log.exists():
            time.sleep(4.2)
        return self.access_log.read_text(encoding="utf-8", errors="replace") if self.access_log.exists() else ""

    def test_body_exchange_returns_nt_key_without_logging_handshake(self):
        status, payload = self._request(
            "POST",
            "/ntlm.php",
            {
                "username": r"EXAMPLE\example-user",
                "challenge": BODY_CHALLENGE,
                "response": BODY_RESPONSE,
                "domain": "EXAMPLE",
            },
        )
        self.assertEqual(status, 200, payload)
        self.assertEqual(
            payload,
            NT_KEY_LINE,
            "the bridge did not return the NT session-key line for a body "
            f"handshake; body was {payload!r}; helper saw {self._args()!r}",
        )
        args = self._args()
        self.assertIn(BODY_CHALLENGE, args)
        self.assertIn(BODY_RESPONSE, args)
        self.assertIn("--username=example-user", args)
        self.assertNotIn("EXAMPLE\\\\example-user", args)
        logged = self._access_log()
        self.assertNotIn(BODY_CHALLENGE, logged, logged)
        self.assertNotIn(BODY_RESPONSE, logged, logged)
        self.assertNotIn("example-user", logged, logged)

    def test_query_string_handshake_is_rejected(self):
        query = urllib.parse.urlencode(
            {
                "username": r"EXAMPLE\example-user",
                "challenge": QUERY_CHALLENGE,
                "response": QUERY_RESPONSE,
                "domain": "EXAMPLE",
            }
        )
        status, payload = self._request("GET", "/ntlm.php?" + query)
        self.assertNotIn(
            "NT_KEY:",
            payload,
            "query-string handshake returned the NT session key "
            f"(HTTP {status}): {payload!r}",
        )
        args = self._args()
        self.assertNotIn(QUERY_CHALLENGE, args, args)
        self.assertNotIn(QUERY_RESPONSE, args, args)

    def test_query_string_does_not_override_body(self):
        query = urllib.parse.urlencode(
            {
                "username": "query-user",
                "challenge": OVERRIDE_CHALLENGE,
                "response": OVERRIDE_RESPONSE,
                "domain": "QUERY",
            }
        )
        status, payload = self._request(
            "POST",
            "/ntlm.php?" + query,
            {
                "username": r"EXAMPLE\example-user",
                "challenge": BODY_CHALLENGE,
                "response": BODY_RESPONSE,
                "domain": "EXAMPLE",
            },
        )
        self.assertEqual(status, 200, payload)
        self.assertEqual(payload, NT_KEY_LINE, payload)
        args = self._args()
        self.assertIn(BODY_CHALLENGE, args, args)
        self.assertIn(BODY_RESPONSE, args, args)
        self.assertNotIn(OVERRIDE_CHALLENGE, args, args)
        self.assertNotIn(OVERRIDE_RESPONSE, args, args)
        self.assertNotIn("query-user", args, args)
        logged = self._access_log()
        # The request target still contains the attacker's query string because
        # this request put it there. The user's handshake from the body must
        # not be copied into that target or the log.
        self.assertNotIn(BODY_CHALLENGE, logged, logged)
        self.assertNotIn(BODY_RESPONSE, logged, logged)


if __name__ == "__main__":
    unittest.main(verbosity=2)
