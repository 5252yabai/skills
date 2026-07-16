import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import build_parser, validate_args


def test_diarize_only_flag_parses():
    args = build_parser().parse_args(["audio.m4a", "--diarize-only"])
    assert args.diarize_only is True


def test_no_diarize_flag_parses():
    args = build_parser().parse_args(["audio.m4a", "--no-diarize"])
    assert args.no_diarize is True


def test_no_normalize_flag_parses():
    args = build_parser().parse_args(["audio.m4a", "--no-normalize"])
    assert args.no_normalize is True


def test_model_default_is_large_v3():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.model == "large-v3"


def test_language_default_is_ko():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.language == "ko"


def test_diarize_only_and_no_diarize_conflict_raises():
    parser = build_parser()
    args = parser.parse_args(["audio.m4a", "--diarize-only", "--no-diarize"])
    with pytest.raises(SystemExit):
        validate_args(args, parser)


def test_removed_pyannote_options_are_gone():
    # speakrs takes no device/speaker-count/batch-size knobs; those flags are removed.
    parser = build_parser()
    for flag in ["--token", "--device", "--num-speakers", "--profile", "--embedding-batch-size"]:
        with pytest.raises(SystemExit):
            parser.parse_args(["audio.m4a", flag, "x"])
