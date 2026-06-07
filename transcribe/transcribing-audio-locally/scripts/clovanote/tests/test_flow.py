from pathlib import Path
from unittest.mock import call, patch

import pytest

from clovanote_upload.flow import (
    NotLoggedInError,
    attach_file,
    capture_note_url,
    copy_to_clipboard,
    create_new_note,
    ensure_logged_in,
    extract_transcript,
    is_transcription_complete,
    open_clovanote,
    set_note_title,
)

CLOVA_URL = "https://clovanote.naver.com/"
LOGGED_IN_URL = "https://clovanote.naver.com/w/GLVDMYPdLrayfB5tnY2w/home"


class TestOpenClovanote:
    def test_opens_clovanote_url(self):
        with patch("clovanote_upload.flow.run") as mock_run:
            mock_run.return_value = ""
            open_clovanote(headed=False)

        calls = [c[0][0] for c in mock_run.call_args_list]
        assert ["open", CLOVA_URL] in calls

    def test_headed_flag_passed_when_true(self):
        with patch("clovanote_upload.flow.run") as mock_run:
            mock_run.return_value = ""
            open_clovanote(headed=True)

        all_args = [arg for c in mock_run.call_args_list for arg in c[0][0]]
        assert "--headed" in all_args

    def test_no_headed_flag_when_false(self):
        with patch("clovanote_upload.flow.run") as mock_run:
            mock_run.return_value = ""
            open_clovanote(headed=False)

        all_args = [arg for c in mock_run.call_args_list for arg in c[0][0]]
        assert "--headed" not in all_args


class TestEnsureLoggedIn:
    def test_returns_true_when_url_contains_w_path(self):
        with patch("clovanote_upload.flow.run", return_value=LOGGED_IN_URL):
            assert ensure_logged_in() is True

    def test_raises_when_redirected_to_naver_login(self):
        with patch("clovanote_upload.flow.run", return_value="https://nid.naver.com/nidlogin.login"):
            with pytest.raises(NotLoggedInError):
                ensure_logged_in()

    def test_raises_when_still_on_landing_page(self):
        with patch("clovanote_upload.flow.run", return_value=CLOVA_URL):
            with pytest.raises(NotLoggedInError):
                ensure_logged_in()


class TestCreateNewNote:
    def test_clicks_new_note_button_by_text(self):
        with patch("clovanote_upload.flow.run") as mock_run:
            mock_run.return_value = ""
            create_new_note()

        all_calls = [c[0][0] for c in mock_run.call_args_list]
        assert any("새 노트" in str(cmd) for cmd in all_calls)

    def test_waits_after_clicking(self):
        with patch("clovanote_upload.flow.run") as mock_run:
            mock_run.return_value = ""
            create_new_note()

        all_calls = [c[0][0] for c in mock_run.call_args_list]
        assert any("wait" in cmd for cmd in all_calls)


class TestSetNoteTitle:
    def test_calls_eval_js_with_execcommand(self):
        with patch("clovanote_upload.flow.eval_js") as mock_eval:
            mock_eval.return_value = '"done"'
            set_note_title("My Meeting")

        script = mock_eval.call_args[0][0]
        assert "My Meeting" in script
        assert "execCommand" in script or "insertText" in script or "innerText" in script


class TestAttachFile:
    def test_calls_set_file_input_with_correct_args(self):
        path = Path("/home/user/audio.m4a")
        with (
            patch("clovanote_upload.flow.get_cdp_browser_url", return_value="ws://127.0.0.1:9222/devtools/browser/abc"),
            patch("clovanote_upload.flow.set_file_input") as mock_cdp,
        ):
            attach_file(path)

        mock_cdp.assert_called_once()
        call_args = mock_cdp.call_args
        assert call_args[0][0] == "ws://127.0.0.1:9222/devtools/browser/abc"
        assert call_args[0][1] == path

    def test_waits_after_attaching(self):
        path = Path("/home/user/audio.m4a")
        with (
            patch("clovanote_upload.flow.get_cdp_browser_url", return_value="ws://x"),
            patch("clovanote_upload.flow.set_file_input"),
            patch("clovanote_upload.flow.run") as mock_run,
        ):
            mock_run.return_value = ""
            attach_file(path)

        all_calls = [c[0][0] for c in mock_run.call_args_list]
        assert any("wait" in cmd for cmd in all_calls)


NOTE_URL = "https://clovanote.naver.com/w/WSP123/note-detail/note-abc-123"


class TestCaptureNoteUrl:
    def test_returns_url_when_already_on_note_detail(self):
        with patch("clovanote_upload.flow.run", return_value=NOTE_URL + "\n"):
            result = capture_note_url()
        assert result == NOTE_URL

    def test_polls_until_note_detail_url_appears(self):
        landing = "https://clovanote.naver.com/w/WSP123/home\n"
        side_effects = [landing, landing, NOTE_URL + "\n"]
        with (
            patch("clovanote_upload.flow.run", side_effect=side_effects),
            patch("clovanote_upload.flow.time") as mock_time,
        ):
            mock_time.monotonic.side_effect = [0, 1, 2, 3]
            mock_time.sleep = lambda _: None
            result = capture_note_url(timeout_s=10)
        assert result == NOTE_URL

    def test_raises_on_timeout(self):
        with (
            patch("clovanote_upload.flow.run", return_value="https://clovanote.naver.com/w/WSP123/home\n"),
            patch("clovanote_upload.flow.time") as mock_time,
        ):
            mock_time.monotonic.side_effect = [0, 20]
            mock_time.sleep = lambda _: None
            with pytest.raises(RuntimeError, match="Timed out"):
                capture_note_url(timeout_s=10)


class TestIsTranscriptionComplete:
    def test_returns_true_when_done_element_exists(self):
        with (
            patch("clovanote_upload.flow.run", return_value=NOTE_URL + "\n"),
            patch("clovanote_upload.flow.eval_js", return_value="true"),
        ):
            assert is_transcription_complete(NOTE_URL) is True

    def test_returns_false_when_done_element_absent(self):
        with (
            patch("clovanote_upload.flow.run", return_value=NOTE_URL + "\n"),
            patch("clovanote_upload.flow.eval_js", return_value="false"),
        ):
            assert is_transcription_complete(NOTE_URL) is False

    def test_navigates_to_note_url_when_on_different_page(self):
        other_url = "https://clovanote.naver.com/w/WSP123/home"
        with (
            patch("clovanote_upload.flow.run", return_value=other_url + "\n") as mock_run,
            patch("clovanote_upload.flow.eval_js", return_value="false"),
        ):
            is_transcription_complete(NOTE_URL)
        all_calls = [c[0][0] for c in mock_run.call_args_list]
        assert any("open" in cmd and NOTE_URL in cmd for cmd in all_calls)


class TestExtractTranscript:
    def test_returns_transcript_text(self):
        with (
            patch("clovanote_upload.flow.run", return_value=NOTE_URL + "\n"),
            patch("clovanote_upload.flow.eval_js", return_value='"안녕하세요.\\n\\n반갑습니다."'),
        ):
            result = extract_transcript(NOTE_URL)
        assert "안녕하세요" in result
        assert "반갑습니다" in result

    def test_navigates_to_note_url_when_on_different_page(self):
        other_url = "https://clovanote.naver.com/w/WSP123/home"
        with (
            patch("clovanote_upload.flow.run", return_value=other_url + "\n") as mock_run,
            patch("clovanote_upload.flow.eval_js", return_value='"text"'),
        ):
            extract_transcript(NOTE_URL)
        all_calls = [c[0][0] for c in mock_run.call_args_list]
        assert any("open" in cmd and NOTE_URL in cmd for cmd in all_calls)


class TestJsStringValidity:
    """JS 상수 내 단일 인용 문자열 리터럴에 raw newline이 없어야 한다.
    Python \\n이 실제 줄바꿈이 되면 eval --stdin에서 SyntaxError가 난다."""

    def _assert_no_raw_newlines_in_js_strings(self, js_source: str) -> None:
        import re
        for m in re.finditer(r"'(?:[^'\\]|\\.)*'", js_source, re.DOTALL):
            assert "\n" not in m.group(0), (
                f"raw newline inside JS string literal: {m.group(0)!r}"
            )

    def test_extract_transcript_js_no_raw_newline(self):
        from clovanote_upload.flow import _EXTRACT_TRANSCRIPT_JS
        self._assert_no_raw_newlines_in_js_strings(_EXTRACT_TRANSCRIPT_JS)

    def test_is_done_js_no_raw_newline(self):
        from clovanote_upload.flow import _IS_DONE_JS
        self._assert_no_raw_newlines_in_js_strings(_IS_DONE_JS)


class TestCopyToClipboard:
    def test_pipes_text_to_pbcopy(self):
        with patch("clovanote_upload.flow.subprocess") as mock_subp:
            copy_to_clipboard("hello world")
        mock_subp.run.assert_called_once_with(
            ["pbcopy"], input="hello world".encode("utf-8"), check=True
        )

    def test_encodes_korean_text(self):
        with patch("clovanote_upload.flow.subprocess") as mock_subp:
            copy_to_clipboard("안녕하세요")
        call_kwargs = mock_subp.run.call_args
        assert call_kwargs[1]["input"] == "안녕하세요".encode("utf-8")
