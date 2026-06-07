import argparse
import sqlite3
import sys
import time
from pathlib import Path

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

SUPPORTED = {".m4a", ".mp3", ".aac", ".amr", ".wav"}
VOICE_MEMOS_DIR = Path.home() / "Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings"
CLOUD_RECORDINGS_DB = VOICE_MEMOS_DIR / "CloudRecordings.db"


def get_title_map(db_path: Path | None = None) -> dict[str, str]:
    """Return {filename: user_title} from CloudRecordings.db; empty dict on any failure."""
    if db_path is None:
        db_path = CLOUD_RECORDINGS_DB
    if not db_path.exists():
        return {}
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        rows = con.execute("SELECT ZPATH, ZENCRYPTEDTITLE FROM ZCLOUDRECORDING").fetchall()
        con.close()
        return {zpath: title for zpath, title in rows if zpath and title}
    except Exception:
        return {}


def list_recordings(directory: Path | None = None, n: int = 10) -> list[Path]:
    if directory is None:
        directory = VOICE_MEMOS_DIR
    files = sorted(
        (f for f in directory.iterdir() if f.suffix.lower() == ".m4a"),
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )
    return files[:n]


def _print_recordings(files: list[Path], title_map: dict[str, str] | None = None) -> None:
    if title_map is None:
        title_map = {}
    for i, f in enumerate(files, 1):
        size_mb = f.stat().st_size / 1_048_576
        title = title_map.get(f.name, "")
        title_part = f"  {title}" if title else ""
        print(f"{i:2}. {f.name}{title_part}  ({size_mb:.1f} MB)")


def _poll_and_copy(note_url: str, poll_interval: float, poll_timeout: float) -> None:
    deadline = time.monotonic() + poll_timeout
    while time.monotonic() < deadline:
        if is_transcription_complete(note_url):
            transcript = extract_transcript(note_url)
            copy_to_clipboard(transcript)
            print(f"Copied transcript to clipboard ({len(transcript)} chars)")
            return
        time.sleep(poll_interval)
    print("[warn] timeout before transcription completed", file=sys.stderr)
    sys.exit(2)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Upload audio file to Clova Note")
    parser.add_argument("path", type=Path, nargs="?", help="Audio file path (omit to list Voice Memos)")
    parser.add_argument("--note-url", metavar="URL", help="Extract transcript from existing note URL (skips upload)")
    parser.add_argument("--name", help="Note title (optional)")
    parser.add_argument("--headed", action="store_true", help="Open visible browser (required for first login)")
    parser.add_argument("--list", action="store_true", help="List recent Voice Memos recordings and exit")
    parser.add_argument("--copy-when-done", action="store_true", help="Copy transcript to clipboard when transcription completes")
    parser.add_argument("--poll-interval", type=float, default=30.0, metavar="N", help="Seconds between transcription status checks (default: 30)")
    parser.add_argument("--poll-timeout", type=float, default=1800.0, metavar="N", help="Max seconds to wait for transcription (default: 1800)")
    args = parser.parse_args(argv)

    if args.path is not None and args.note_url is not None:
        parser.error("cannot use a file path together with --note-url")

    if args.note_url:
        try:
            open_clovanote(headed=args.headed)
            ensure_logged_in()
            _poll_and_copy(args.note_url, args.poll_interval, args.poll_timeout)
        except NotLoggedInError as e:
            print(f"[error] {e}", file=sys.stderr)
            print("Run with --headed to log in first.", file=sys.stderr)
            sys.exit(1)
        return

    if args.list:
        files = list_recordings()
        if not files:
            print("No recordings found in Voice Memos directory.")
        else:
            print(f"Recent recordings in {VOICE_MEMOS_DIR}:\n")
            _print_recordings(files, get_title_map())
        sys.exit(0)

    if args.path is None:
        files = list_recordings()
        if files:
            print("No file specified. Recent Voice Memos recordings:\n")
            _print_recordings(files, get_title_map())
            print(f"\nRun with a path to upload, e.g.:\n  clovanote-upload \"{files[0]}\"")
        else:
            parser.print_help()
        sys.exit(1)

    path: Path = args.path
    if not path.exists():
        parser.error(f"File not found: {path}")
    if path.suffix.lower() not in SUPPORTED:
        parser.error(f"Unsupported format {path.suffix!r}. Supported: {', '.join(sorted(SUPPORTED))}")

    # --name 우선, 없으면 DB에서 사용자 지정 제목 자동 사용
    title = args.name or get_title_map().get(path.name)

    try:
        open_clovanote(headed=args.headed)
        ensure_logged_in()
        create_new_note()
        if title:
            set_note_title(title)
        attach_file(path)
        note_url = capture_note_url()
        print(f"Uploaded: {path.name}")
        print(f"Note URL: {note_url}")

        if args.copy_when_done:
            _poll_and_copy(note_url, args.poll_interval, args.poll_timeout)
    except NotLoggedInError as e:
        print(f"[error] {e}", file=sys.stderr)
        print("Run with --headed to log in first.", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"[error] {e}", file=sys.stderr)
        sys.exit(1)
