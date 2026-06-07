import json
import subprocess
import time
from pathlib import Path

from clovanote_upload.browser import eval_js, get_cdp_browser_url, run
from clovanote_upload.cdp import set_file_input

CLOVA_URL = "https://clovanote.naver.com/"

_SET_TITLE_JS = """
(function(title) {{
  var el = document.querySelector('[contenteditable="true"]');
  if (!el) return 'no contenteditable';
  el.focus();
  document.execCommand('selectAll');
  document.execCommand('insertText', false, title);
  el.dispatchEvent(new Event('input', {{bubbles: true}}));
  el.blur();
  return 'done: ' + el.innerText;
}})('{title}')
"""

# Clova Note UI selectors — CSS module hash suffix varies per build; match by prefix.
_IS_DONE_JS = "document.querySelector('[class*=\"NoteDetailWebStatusDone\"]') !== null"

_EXTRACT_TRANSCRIPT_JS = """
(function() {
  var els = document.querySelectorAll('[class*="NoteDetailSttListItem_organism_text"]');
  var parts = [];
  els.forEach(function(el) {
    var t = el.innerText.trim();
    if (t) parts.push(t);
  });
  return parts.join('\\n\\n');
})()
"""


class NotLoggedInError(Exception):
    pass


def open_clovanote(headed: bool) -> None:
    prefix = ["--headed"] if headed else []
    run(prefix + ["open", CLOVA_URL])
    run(["wait", "--load", "networkidle"])


def ensure_logged_in() -> bool:
    current_url = run(["get", "url"]).strip()
    if "/w/" not in current_url:
        raise NotLoggedInError(
            "Not logged in. Run with --headed first and log in manually."
        )
    return True


def create_new_note() -> None:
    run(["find", "role", "button", "click", "--name", "새 노트"])
    run(["wait", "--load", "networkidle"])


def set_note_title(title: str) -> None:
    safe_title = title.replace("'", "\\'")
    eval_js(_SET_TITLE_JS.format(title=safe_title))


def attach_file(path: Path) -> None:
    browser_ws = get_cdp_browser_url()
    set_file_input(browser_ws, path)
    run(["wait", "--load", "networkidle"])


def capture_note_url(timeout_s: float = 15.0) -> str:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        url = run(["get", "url"]).strip()
        if "/note-detail/" in url:
            return url
        time.sleep(0.5)
    raise RuntimeError("Timed out waiting for note URL")


def _navigate_to_if_needed(note_url: str) -> None:
    current = run(["get", "url"]).strip()
    if note_url not in current:
        run(["open", note_url])
        run(["wait", "--load", "networkidle"])


def is_transcription_complete(note_url: str) -> bool:
    _navigate_to_if_needed(note_url)
    return json.loads(eval_js(_IS_DONE_JS).strip())


def extract_transcript(note_url: str) -> str:
    _navigate_to_if_needed(note_url)
    return json.loads(eval_js(_EXTRACT_TRANSCRIPT_JS).strip())


def copy_to_clipboard(text: str) -> None:
    subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)
