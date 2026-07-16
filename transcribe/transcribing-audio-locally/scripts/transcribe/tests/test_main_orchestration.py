import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import contextlib
import json
from unittest.mock import patch

from transcribe import diarize_only, emit


def test_emit_writes_text_to_output_file(tmp_path):
    out_file = tmp_path / "result.txt"
    emit("화자 텍스트", None, output_path=str(out_file), json_path=None)
    assert out_file.read_text(encoding="utf-8") == "화자 텍스트"


def test_emit_prints_text_to_terminal_when_no_output_path(capsys):
    emit("화자 텍스트", None, output_path=None, json_path=None)
    out = capsys.readouterr().out
    assert "=" * 50 in out
    assert "화자 텍스트" in out


def test_emit_saves_json_payload(tmp_path):
    json_file = tmp_path / "out.json"
    emit("text", {"segments": [], "raw": {"k": "v"}}, output_path=None, json_path=str(json_file))
    assert json.loads(json_file.read_text(encoding="utf-8")) == {"segments": [], "raw": {"k": "v"}}


def test_emit_skips_json_when_payload_none(tmp_path):
    json_file = tmp_path / "out.json"
    emit("text", None, output_path=None, json_path=str(json_file))
    assert not json_file.exists()


def test_diarize_only_returns_turns_from_run_diarization():
    turns = [(0.0, 1.0, "SPEAKER_00")]
    with patch("transcribe.maybe_normalized", return_value=contextlib.nullcontext("/tmp/norm.wav")), \
         patch("transcribe.run_diarization", return_value=turns) as mock_rd:
        result = diarize_only("/tmp/in.m4a", True)
    assert result == turns
    # diarizes the normalized wav, not the original
    assert mock_rd.call_args[0][0] == "/tmp/norm.wav"
