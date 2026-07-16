import sys
import os
from types import SimpleNamespace
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import run_diarization

WAV = "/tmp/norm.wav"
FAKE_BIN = "/fake/speakrs/bench_turns"


def _completed(stdout="", returncode=0, stderr=""):
    return SimpleNamespace(stdout=stdout, returncode=returncode, stderr=stderr)


def test_invokes_binary_with_audio_path():
    with patch("transcribe._speakrs_binary", return_value=FAKE_BIN), \
         patch("transcribe.subprocess.run", return_value=_completed("0.0\t1.0\tSPEAKER_00\n")) as run:
        run_diarization(WAV)
    cmd = run.call_args[0][0]
    assert cmd == [FAKE_BIN, WAV]


def test_sets_openblas_dyld_path_in_env():
    with patch("transcribe._speakrs_binary", return_value=FAKE_BIN), \
         patch("transcribe.subprocess.run", return_value=_completed("")) as run:
        run_diarization(WAV)
    env = run.call_args.kwargs["env"]
    assert "/opt/homebrew/opt/openblas/lib" in env["DYLD_LIBRARY_PATH"]


def test_parses_stdout_into_turns():
    out = "0.385\t0.993\tSPEAKER_03\n1.195\t1.651\tSPEAKER_00\n"
    with patch("transcribe._speakrs_binary", return_value=FAKE_BIN), \
         patch("transcribe.subprocess.run", return_value=_completed(out)):
        turns = run_diarization(WAV)
    assert turns == [(0.385, 0.993, "SPEAKER_03"), (1.195, 1.651, "SPEAKER_00")]


def test_nonzero_returncode_raises():
    with patch("transcribe._speakrs_binary", return_value=FAKE_BIN), \
         patch("transcribe.subprocess.run", return_value=_completed("", returncode=1, stderr="boom")):
        with pytest.raises(RuntimeError, match="boom"):
            run_diarization(WAV)
