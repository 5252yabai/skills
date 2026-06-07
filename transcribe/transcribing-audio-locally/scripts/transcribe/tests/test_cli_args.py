import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import build_parser, validate_args


def test_profile_flag_parses():
    args = build_parser().parse_args(["audio.m4a", "--profile"])
    assert args.profile is True


def test_profile_flag_default_is_false():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.profile is False


def test_diarize_only_flag_parses():
    args = build_parser().parse_args(["audio.m4a", "--diarize-only"])
    assert args.diarize_only is True


def test_device_auto_is_default():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.device == "auto"


def test_device_mps_parses():
    args = build_parser().parse_args(["audio.m4a", "--device", "mps"])
    assert args.device == "mps"


def test_device_cpu_parses():
    args = build_parser().parse_args(["audio.m4a", "--device", "cpu"])
    assert args.device == "cpu"


def test_invalid_device_exits():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["audio.m4a", "--device", "cuda"])


def test_num_speakers_parses_as_int():
    args = build_parser().parse_args(["audio.m4a", "--num-speakers", "3"])
    assert args.num_speakers == 3


def test_num_speakers_default_is_none():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.num_speakers is None


def test_min_max_speakers_parse():
    args = build_parser().parse_args(["audio.m4a", "--min-speakers", "2", "--max-speakers", "5"])
    assert args.min_speakers == 2
    assert args.max_speakers == 5


def test_embedding_batch_size_default_is_32():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.embedding_batch_size == 32


def test_segmentation_batch_size_default_is_32():
    args = build_parser().parse_args(["audio.m4a"])
    assert args.segmentation_batch_size == 32


def test_embedding_batch_size_overrideable():
    args = build_parser().parse_args(["audio.m4a", "--embedding-batch-size", "8"])
    assert args.embedding_batch_size == 8


def test_diarize_only_and_no_diarize_conflict_raises():
    parser = build_parser()
    args = parser.parse_args(["audio.m4a", "--diarize-only", "--no-diarize"])
    with pytest.raises(SystemExit):
        validate_args(args, parser)
