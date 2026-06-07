import sqlite3
from pathlib import Path
from unittest.mock import patch

import pytest

from clovanote_upload.cli import get_title_map, list_recordings, main

SUPPORTED_EXTS = ["m4a", "mp3", "aac", "amr", "wav"]


@pytest.fixture
def sample_m4a(tmp_path):
    f = tmp_path / "audio.m4a"
    f.write_bytes(b"fake")
    return f


class TestCLIValidation:
    def test_exits_when_file_does_not_exist(self):
        with pytest.raises(SystemExit):
            main(["/nonexistent/audio.m4a"])

    @pytest.mark.parametrize("ext", ["txt", "pdf", "mp4"])
    def test_exits_on_unsupported_extension(self, tmp_path, ext):
        f = tmp_path / f"audio.{ext}"
        f.write_bytes(b"x")
        with pytest.raises(SystemExit):
            main([str(f)])


class TestCLIFlow:
    def test_calls_upload_flow_in_order(self, sample_m4a):
        call_order = []
        with (
            patch("clovanote_upload.cli.open_clovanote", side_effect=lambda **kw: call_order.append("open")),
            patch("clovanote_upload.cli.ensure_logged_in", side_effect=lambda: call_order.append("login")),
            patch("clovanote_upload.cli.create_new_note", side_effect=lambda: call_order.append("new_note")),
            patch("clovanote_upload.cli.set_note_title", side_effect=lambda t: call_order.append("title")),
            patch("clovanote_upload.cli.attach_file", side_effect=lambda p: call_order.append("attach")),
        ):
            main([str(sample_m4a), "--name", "My Note"])

        assert call_order == ["open", "login", "new_note", "title", "attach"]

    def test_skips_set_note_title_when_no_name(self, sample_m4a):
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.set_note_title") as mock_title,
            patch("clovanote_upload.cli.attach_file"),
        ):
            main([str(sample_m4a)])

        mock_title.assert_not_called()

    def test_no_path_exits_with_error(self):
        with pytest.raises(SystemExit) as exc:
            main([])
        assert exc.value.code != 0

    def test_headed_flag_forwarded_to_open(self, sample_m4a):
        with (
            patch("clovanote_upload.cli.open_clovanote") as mock_open,
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.set_note_title"),
            patch("clovanote_upload.cli.attach_file"),
        ):
            main([str(sample_m4a), "--headed"])

        mock_open.assert_called_once_with(headed=True)


class TestListRecordings:
    def test_returns_m4a_files_sorted_newest_first(self, tmp_path):
        older = tmp_path / "20260101 120000.m4a"
        newer = tmp_path / "20260507 090000.m4a"
        older.write_bytes(b"x")
        newer.write_bytes(b"x" * 1000)
        import time; time.sleep(0.01)
        older.touch()
        newer.touch()
        # newer was touched last
        result = list_recordings(tmp_path, n=10)
        assert result[0].name == newer.name

    def test_ignores_non_m4a_files(self, tmp_path):
        (tmp_path / "audio.m4a").write_bytes(b"x")
        (tmp_path / "audio.waveform").write_bytes(b"x")
        (tmp_path / "CloudRecordings.db").write_bytes(b"x")
        result = list_recordings(tmp_path, n=10)
        assert len(result) == 1
        assert result[0].suffix == ".m4a"

    def test_respects_n_limit(self, tmp_path):
        for i in range(5):
            (tmp_path / f"2026050{i} 090000.m4a").write_bytes(b"x")
        result = list_recordings(tmp_path, n=3)
        assert len(result) == 3

    def test_list_flag_prints_recordings_and_exits_zero(self, tmp_path, capsys):
        (tmp_path / "20260507 090000.m4a").write_bytes(b"x" * 2048)
        with patch("clovanote_upload.cli.VOICE_MEMOS_DIR", tmp_path):
            with pytest.raises(SystemExit) as exc:
                main(["--list"])
        assert exc.value.code == 0
        out = capsys.readouterr().out
        assert "20260507 090000.m4a" in out
        assert "1." in out

    def test_list_flag_shows_user_title(self, tmp_path, capsys):
        (tmp_path / "20260507 090000.m4a").write_bytes(b"x" * 2048)
        title_map = {"20260507 090000.m4a": "회의 녹음"}
        with (
            patch("clovanote_upload.cli.VOICE_MEMOS_DIR", tmp_path),
            patch("clovanote_upload.cli.get_title_map", return_value=title_map),
        ):
            with pytest.raises(SystemExit):
                main(["--list"])
        out = capsys.readouterr().out
        assert "회의 녹음" in out


class TestGetTitleMap:
    def _make_db(self, tmp_path: Path, rows: list[tuple]) -> Path:
        db = tmp_path / "CloudRecordings.db"
        con = sqlite3.connect(db)
        con.execute("CREATE TABLE ZCLOUDRECORDING (ZPATH TEXT, ZENCRYPTEDTITLE TEXT)")
        con.executemany("INSERT INTO ZCLOUDRECORDING VALUES (?, ?)", rows)
        con.commit()
        con.close()
        return db

    def test_returns_filename_to_title_mapping(self, tmp_path):
        db = self._make_db(tmp_path, [("20260507 133159.m4a", "20260507 daily")])
        result = get_title_map(db)
        assert result == {"20260507 133159.m4a": "20260507 daily"}

    def test_returns_empty_dict_when_db_missing(self, tmp_path):
        result = get_title_map(tmp_path / "nonexistent.db")
        assert result == {}

    def test_skips_rows_with_null_fields(self, tmp_path):
        db = self._make_db(tmp_path, [("20260507 133159.m4a", None), (None, "title")])
        result = get_title_map(db)
        assert result == {}


class TestCopyWhenDone:
    def test_copy_when_done_polls_then_copies(self, sample_m4a):
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.attach_file"),
            patch("clovanote_upload.cli.capture_note_url", return_value="https://clovanote.naver.com/w/x/note-detail/abc"),
            patch("clovanote_upload.cli.is_transcription_complete", return_value=True),
            patch("clovanote_upload.cli.extract_transcript", return_value="transcript text"),
            patch("clovanote_upload.cli.copy_to_clipboard") as mock_copy,
            patch("clovanote_upload.cli.get_title_map", return_value={}),
        ):
            main([str(sample_m4a), "--copy-when-done"])
        mock_copy.assert_called_once_with("transcript text")

    def test_polls_multiple_times_until_done(self, sample_m4a):
        complete_sequence = [False, False, True]
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.attach_file"),
            patch("clovanote_upload.cli.capture_note_url", return_value="https://clovanote.naver.com/w/x/note-detail/abc"),
            patch("clovanote_upload.cli.is_transcription_complete", side_effect=complete_sequence),
            patch("clovanote_upload.cli.extract_transcript", return_value="text"),
            patch("clovanote_upload.cli.copy_to_clipboard"),
            patch("clovanote_upload.cli.get_title_map", return_value={}),
            patch("clovanote_upload.cli.time") as mock_time,
        ):
            mock_time.monotonic.side_effect = [0, 1, 2, 3, 4]
            mock_time.sleep = lambda _: None
            main([str(sample_m4a), "--copy-when-done"])

    def test_exits_2_on_poll_timeout(self, sample_m4a):
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.attach_file"),
            patch("clovanote_upload.cli.capture_note_url", return_value="https://clovanote.naver.com/w/x/note-detail/abc"),
            patch("clovanote_upload.cli.is_transcription_complete", return_value=False),
            patch("clovanote_upload.cli.get_title_map", return_value={}),
            patch("clovanote_upload.cli.time") as mock_time,
        ):
            mock_time.monotonic.side_effect = [0, 99999]
            mock_time.sleep = lambda _: None
            with pytest.raises(SystemExit) as exc:
                main([str(sample_m4a), "--copy-when-done", "--poll-timeout", "10"])
        assert exc.value.code == 2


_NOTE_URL = "https://clovanote.naver.com/w/GLVDMYPdLrayfB5tnY2w/note-detail/34a8ee0e-6d56-4271-8afc-9c8d86daaaefn"


class TestNoteUrlFlag:
    def test_skips_upload_steps_and_copies_transcript(self):
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note") as mock_new_note,
            patch("clovanote_upload.cli.attach_file") as mock_attach,
            patch("clovanote_upload.cli.capture_note_url") as mock_capture,
            patch("clovanote_upload.cli.is_transcription_complete", return_value=True),
            patch("clovanote_upload.cli.extract_transcript", return_value="transcript text"),
            patch("clovanote_upload.cli.copy_to_clipboard") as mock_copy,
        ):
            main(["--note-url", _NOTE_URL])
        mock_new_note.assert_not_called()
        mock_attach.assert_not_called()
        mock_capture.assert_not_called()
        mock_copy.assert_called_once_with("transcript text")

    def test_path_and_note_url_are_mutually_exclusive(self, sample_m4a):
        with pytest.raises(SystemExit):
            main([str(sample_m4a), "--note-url", _NOTE_URL])


class TestAutoTitle:
    def test_upload_uses_db_title_when_no_name_flag(self, sample_m4a):
        title_map = {sample_m4a.name: "DB에서 온 제목"}
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.set_note_title") as mock_title,
            patch("clovanote_upload.cli.attach_file"),
            patch("clovanote_upload.cli.get_title_map", return_value=title_map),
        ):
            main([str(sample_m4a)])
        mock_title.assert_called_once_with("DB에서 온 제목")

    def test_explicit_name_overrides_db_title(self, sample_m4a):
        title_map = {sample_m4a.name: "DB 제목"}
        with (
            patch("clovanote_upload.cli.open_clovanote"),
            patch("clovanote_upload.cli.ensure_logged_in"),
            patch("clovanote_upload.cli.create_new_note"),
            patch("clovanote_upload.cli.set_note_title") as mock_title,
            patch("clovanote_upload.cli.attach_file"),
            patch("clovanote_upload.cli.get_title_map", return_value=title_map),
        ):
            main([str(sample_m4a), "--name", "직접 입력한 제목"])
        mock_title.assert_called_once_with("직접 입력한 제목")
