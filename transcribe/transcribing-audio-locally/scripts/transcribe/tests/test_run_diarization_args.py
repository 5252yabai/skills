import sys
import os
import contextlib
import pytest
from unittest.mock import MagicMock, patch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import run_diarization, _select_device, DiarizationConfig


def make_mock_pipeline():
    """Mock pyannote Pipeline — returns an annotation with no tracks."""
    mock_annotation = MagicMock(spec=["itertracks"])
    mock_annotation.itertracks.return_value = []

    mock_pipeline = MagicMock()
    mock_pipeline.return_value = mock_annotation
    return mock_pipeline


WAV_PATH = "/tmp/test.wav"
TOKEN = "fake_token"


def _run(mock_pipeline, **kwargs):
    """Call run_diarization with load + hook patched, real torch."""
    config = DiarizationConfig(**kwargs)
    with patch("transcribe._load_pipeline", return_value=mock_pipeline), \
         patch("transcribe._build_hook", return_value=contextlib.nullcontext(None)):
        return run_diarization(WAV_PATH, TOKEN, config)


# ──────────────────────────────────────────────
# _select_device unit tests (no mock needed)
# ──────────────────────────────────────────────

def test_select_device_cpu_returns_cpu():
    device = _select_device("cpu")
    assert device.type == "cpu"


def test_select_device_mps_returns_mps():
    import torch
    if not torch.backends.mps.is_available():
        pytest.skip("MPS not available on this machine")
    device = _select_device("mps")
    assert device.type == "mps"


def test_select_device_auto_returns_valid_device():
    device = _select_device("auto")
    assert device.type in ("mps", "cpu")


# ──────────────────────────────────────────────
# DiarizationConfig defaults
# ──────────────────────────────────────────────

def test_config_defaults_match_argparse_defaults():
    config = DiarizationConfig()
    assert config.num_speakers is None
    assert config.min_speakers is None
    assert config.max_speakers is None
    assert config.device_pref == "auto"
    assert config.embedding_batch_size == 32
    assert config.segmentation_batch_size == 32
    assert config.profile is False


# ──────────────────────────────────────────────
# run_diarization argument-passing tests
# ──────────────────────────────────────────────

def test_num_speakers_passed_to_pipeline():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline, num_speakers=3)

    _, kwargs = mock_pipeline.call_args
    assert kwargs.get("num_speakers") == 3


def test_min_max_speakers_without_num_speakers():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline, min_speakers=2, max_speakers=5)

    _, kwargs = mock_pipeline.call_args
    assert "num_speakers" not in kwargs
    assert kwargs.get("min_speakers") == 2
    assert kwargs.get("max_speakers") == 5


def test_num_speakers_overrides_min_max():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline, num_speakers=3, min_speakers=2, max_speakers=5)

    _, kwargs = mock_pipeline.call_args
    assert kwargs.get("num_speakers") == 3
    assert "min_speakers" not in kwargs
    assert "max_speakers" not in kwargs


def test_embedding_batch_size_set_on_pipeline():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline, embedding_batch_size=32)

    assert mock_pipeline.embedding_batch_size == 32


def test_segmentation_batch_size_set_on_pipeline():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline, segmentation_batch_size=16)

    assert mock_pipeline.segmentation_batch_size == 16


def test_wav_path_wrapped_into_pyannote_input_dict():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline)

    positional_args = mock_pipeline.call_args[0]
    file_dict = positional_args[0]
    assert file_dict["audio"] == WAV_PATH
    assert file_dict["uri"] == "test.wav"


def test_no_num_speakers_passes_no_speaker_kwargs():
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline)  # no num/min/max speakers

    _, kwargs = mock_pipeline.call_args
    assert "num_speakers" not in kwargs
    assert "min_speakers" not in kwargs
    assert "max_speakers" not in kwargs


def test_returns_list_of_tuples():
    mock_pipeline = make_mock_pipeline()
    result = _run(mock_pipeline)

    assert isinstance(result, list)


def test_model_load_progress_line_preserved(capsys):
    import re
    mock_pipeline = make_mock_pipeline()
    _run(mock_pipeline)

    out = capsys.readouterr().out
    assert re.search(r"^    모델 로드: \d+\.\d{1}s$", out, re.MULTILINE)


def test_profile_timing_printed_from_internal_dict(capsys):
    # TimingHook populates the input dict in place; run_diarization owns that dict
    # internally and must still surface timing under --profile.
    mock_annotation = MagicMock(spec=["itertracks"])
    mock_annotation.itertracks.return_value = []
    mock_pipeline = MagicMock()

    def fake_call(file_dict, **kwargs):
        file_dict["timing"] = {"segmentation": 1.23}
        return mock_annotation

    mock_pipeline.side_effect = fake_call
    _run(mock_pipeline, profile=True)

    out = capsys.readouterr().out
    assert "segmentation" in out
    assert "1.23" in out
