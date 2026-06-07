import json
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from clovanote_upload.browser import BrowserError, eval_js, get_cdp_browser_url, run, run_json


PROFILE = str(Path.home() / ".clovanote")


def make_completed(stdout="", stderr="", returncode=0):
    result = MagicMock(spec=subprocess.CompletedProcess)
    result.stdout = stdout
    result.stderr = stderr
    result.returncode = returncode
    return result


class TestRun:
    def test_prepends_profile_and_session_flags(self):
        with patch("subprocess.run", return_value=make_completed()) as mock_run:
            run(["open", "https://example.com"])
            cmd = mock_run.call_args[0][0]

        assert cmd[:5] == [
            "agent-browser",
            "--profile",
            PROFILE,
            "--session-name",
            "clovanote",
        ]
        assert cmd[5:] == ["open", "https://example.com"]

    def test_raises_browser_error_on_nonzero_exit(self):
        with patch("subprocess.run", return_value=make_completed(returncode=1)):
            with pytest.raises(BrowserError):
                run(["open", "https://example.com"])

    def test_returns_stdout(self):
        with patch("subprocess.run", return_value=make_completed(stdout="hello")):
            result = run(["get", "url"])

        assert result == "hello"


class TestRunJson:
    def test_appends_json_flag_and_parses_output(self):
        payload = {"ref": "@e1", "role": "button"}
        with patch("subprocess.run", return_value=make_completed(stdout=json.dumps(payload))) as mock_run:
            result = run_json(["snapshot", "-i"])
            cmd = mock_run.call_args[0][0]

        assert "--json" in cmd
        assert result == payload

    def test_raises_browser_error_on_invalid_json(self):
        with patch("subprocess.run", return_value=make_completed(stdout="not-json")):
            with pytest.raises(BrowserError, match="JSON"):
                run_json(["snapshot", "-i"])


class TestEvalJs:
    def test_sends_script_via_stdin(self):
        with patch("subprocess.run", return_value=make_completed(stdout='"done"')) as mock_run:
            result = eval_js("document.title")
            cmd = mock_run.call_args[0][0]

        assert "eval" in cmd
        assert "--stdin" in cmd
        assert result == '"done"'

    def test_raises_browser_error_on_nonzero_exit(self):
        with patch("subprocess.run", return_value=make_completed(returncode=1, stderr="SyntaxError")):
            with pytest.raises(BrowserError):
                eval_js("invalid js <<<")


class TestGetCdpBrowserUrl:
    def test_calls_get_cdp_url_command(self):
        ws = "ws://127.0.0.1:9222/devtools/browser/abc"
        with patch("subprocess.run", return_value=make_completed(stdout=ws + "\n")) as mock_run:
            result = get_cdp_browser_url()
            cmd = mock_run.call_args[0][0]

        assert ["get", "cdp-url"] == cmd[-2:]
        assert result == ws
