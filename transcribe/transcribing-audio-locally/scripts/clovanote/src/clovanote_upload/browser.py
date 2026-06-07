import json
import subprocess
from pathlib import Path

PROFILE = str(Path.home() / ".clovanote")
SESSION = "clovanote"


class BrowserError(Exception):
    pass


def run(args: list[str]) -> str:
    cmd = ["agent-browser", "--profile", PROFILE, "--session-name", SESSION] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise BrowserError(result.stderr or result.stdout)
    return result.stdout


def run_json(args: list[str]) -> dict:
    stdout = run(args + ["--json"])
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as e:
        raise BrowserError(f"JSON parse failed: {e}") from e


def eval_js(script: str) -> str:
    cmd = ["agent-browser", "--profile", PROFILE, "--session-name", SESSION, "eval", "--stdin"]
    result = subprocess.run(cmd, input=script, capture_output=True, text=True)
    if result.returncode != 0:
        raise BrowserError(result.stderr or result.stdout)
    return result.stdout


def get_cdp_browser_url() -> str:
    return run(["get", "cdp-url"]).strip()
