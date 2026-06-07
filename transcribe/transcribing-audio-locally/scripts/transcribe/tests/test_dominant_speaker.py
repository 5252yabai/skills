import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import _dominant_speaker


def test_picks_speaker_with_most_overlap():
    turns = [(0.0, 3.0, "SPEAKER_00"), (3.0, 5.0, "SPEAKER_01")]
    assert _dominant_speaker(0.0, 4.0, turns) == "SPEAKER_00"


def test_none_when_no_overlap():
    turns = [(0.0, 3.0, "SPEAKER_00")]
    assert _dominant_speaker(5.0, 6.0, turns) is None


def test_boundary_touch_is_no_overlap():
    # turn ends exactly when interval starts → zero overlap → None
    turns = [(0.0, 5.0, "SPEAKER_00")]
    assert _dominant_speaker(5.0, 8.0, turns) is None


def test_tie_broken_by_speaker_label():
    # equal overlap (1.0 each) → larger label wins, deterministically
    turns = [(0.0, 1.0, "SPEAKER_00"), (1.0, 2.0, "SPEAKER_01")]
    assert _dominant_speaker(0.0, 2.0, turns) == "SPEAKER_01"


def test_overlap_accumulates_across_turns():
    # SPEAKER_00 contributes from two separate turns → beats SPEAKER_01
    turns = [(0.0, 1.0, "SPEAKER_00"), (1.0, 2.0, "SPEAKER_01"), (2.0, 4.0, "SPEAKER_00")]
    assert _dominant_speaker(0.0, 4.0, turns) == "SPEAKER_00"


def test_empty_turns_returns_none():
    assert _dominant_speaker(0.0, 5.0, []) is None
