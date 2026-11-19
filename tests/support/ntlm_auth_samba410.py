#!/usr/bin/env python3
"""Stand-in for Samba 4.10.16 /bin/ntlm_auth.

This is the helper the Azure PEAP guide executes. Argument parsing, hex
decoding, the username split, and the NT_KEY / hex-decode messages follow
source3/utils/ntlm_auth.c and lib/util/util.c at tag samba-4.10.16.

The one step that is not Samba code is the domain controller. Samba sends the
challenge and NT response to winbind (contact_winbind_auth_crap ->
winbindd_dual_pam_auth_crap -> rpccli_netlogon_network_logon) and, on success,
copies the 16-byte user session key out of the SamLogon validation info.
NTLM_AUTH_FIXTURE is that reply: a username maps to the NT response the domain
accepts and the session key it would return. Any other response is a logon
failure. No password is stored here.
"""

from __future__ import annotations

import json
import os
import sys

# check_auth_crap prints this shape. error_string is filled by set_auth_errors
# from get_friendly_nt_error_msg, which falls back to nt_errstr. The generated
# friendly table is not in the samba-4.10.16 git tree (nterr.c includes
# nterr_gen.c). nt_errstr's symbolic name for this status is used so the line
# stays tied to code that was read (libcli/util/nterr.c nt_status_squash and
# nt_errstr). NT_STATUS_LOGON_FAILURE is 0xC000006D; printf uses 0x%x.
LOGON_FAILURE_LINE = "NT_STATUS_LOGON_FAILURE (0xc000006d)"


def strhex_to_str(strhex: str) -> bytes:
    """lib/util/util.c strhex_to_str at samba-4.10.16 (lines 819-859)."""
    hexchars = "0123456789ABCDEF"
    i = 0
    out = bytearray()
    if len(strhex) >= 2 and strhex[:2].lower() == "0x":
        i += 2
    length = len(strhex)
    while i + 1 < length and strhex[i] != "\0" and strhex[i + 1] != "\0":
        p1 = hexchars.find(strhex[i].upper())
        if p1 < 0:
            break
        i += 1
        p2 = hexchars.find(strhex[i].upper())
        if p2 < 0:
            break
        out.append((p1 << 4) | p2)
        i += 1
    return bytes(out)


def _hex_decode_failure(original: str, decoded: bytes) -> None:
    # ntlm_auth.c fprintf(stderr, "hex decode of %s failed! (only got %d bytes)\n"
    sys.stderr.write(
        "hex decode of %s failed! (only got %d bytes)\n" % (original, len(decoded))
    )
    raise SystemExit(1)


def _log(entry: dict) -> None:
    path = os.environ.get("NTLM_AUTH_LOG")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, sort_keys=True) + "\n")


def _option_value(args: list[str], index: int) -> tuple[str, int]:
    token = args[index]
    if "=" in token:
        return token.split("=", 1)[1], index + 1
    if index + 1 >= len(args):
        sys.stderr.write("missing value for %s\n" % token)
        raise SystemExit(1)
    return args[index + 1], index + 2


def _split_username(username: str) -> str:
    # ntlm_auth.c main(), after option parsing: split on the winbind separator.
    # The default separator is '\\'. Only the first separator is removed.
    separator = "\\"
    position = username.find(separator)
    if position == -1:
        return username
    return username[position + 1 :]


def _load_fixture() -> dict:
    path = os.environ.get("NTLM_AUTH_FIXTURE")
    if not path or not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str]) -> int:
    # Record the invocation before any authentication result is produced.
    # A caller that reaches this process has already paid for the side effect
    # the bridge is not allowed to cause (a domain password check).
    request_nt_key = False
    username = None
    challenge_text = None
    nt_response_text = None
    decoded_challenge = None
    index = 0
    while index < len(argv):
        token = argv[index]
        if token == "--request-nt-key":
            request_nt_key = True
            index += 1
            continue
        if token == "--username" or token.startswith("--username="):
            username, index = _option_value(argv, index)
            continue
        if token == "--challenge" or token.startswith("--challenge="):
            challenge_text, index = _option_value(argv, index)
            decoded = strhex_to_str(challenge_text)
            if len(decoded) != 8:
                _log(
                    {
                        "argv": argv,
                        "stage": "hex_decode_challenge",
                        "challenge": challenge_text,
                    }
                )
                _hex_decode_failure(challenge_text, decoded)
            decoded_challenge = decoded
            continue
        if token == "--nt-response" or token.startswith("--nt-response="):
            nt_response_text, index = _option_value(argv, index)
            decoded_nt = strhex_to_str(nt_response_text)
            if len(decoded_nt) < 24:
                _log(
                    {
                        "argv": argv,
                        "stage": "hex_decode_nt_response",
                        "nt_response": nt_response_text,
                    }
                )
                _hex_decode_failure(nt_response_text, decoded_nt)
            continue
        if token == "--":
            index += 1
            continue
        sys.stderr.write("unexpected argument %s\n" % token)
        raise SystemExit(1)

    _log(
        {
            "argv": argv,
            "stage": "parsed",
            "username": username,
            "challenge": challenge_text,
            "nt_response": nt_response_text,
            "request_nt_key": request_nt_key,
        }
    )

    if not username:
        # ntlm_auth.c: "username must be specified!\n\n" then the help text.
        sys.stderr.write("username must be specified!\n\n")
        raise SystemExit(1)

    if not decoded_challenge:
        sys.stderr.write("username must be specified!\n\n")
        raise SystemExit(1)

    winbind_user = _split_username(username)
    fixture = _load_fixture().get("users", {}).get(winbind_user)
    supplied = strhex_to_str(nt_response_text or "")
    accepted = b""
    session_key = b""
    if fixture:
        accepted = strhex_to_str(fixture.get("nt_response_hex", ""))
        session_key = strhex_to_str(fixture.get("session_key_hex", ""))

    if not fixture or supplied != accepted:
        # check_auth_crap: printf("%s (0x%x)\n", error_string, NT_STATUS_V(...))
        sys.stdout.write(LOGON_FAILURE_LINE + "\n")
        return 1

    # Success copies user_session_key (16 bytes) and prints it when
    # --request-nt-key was set and the key is not all zeros.
    if request_nt_key and session_key and any(session_key):
        encoded = session_key.hex().upper()
        sys.stdout.write("NT_KEY: %s\n" % encoded)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except BrokenPipeError:
        raise SystemExit(1)
