import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import parse_speakrs_turns


def test_parses_tab_separated_turns():
    # speakrs bench_turns prints "start\tend\tspeaker" per line (see speakrs_turns.txt)
    stdout = "0.385\t0.993\tSPEAKER_03\n1.195\t1.651\tSPEAKER_00\n"
    assert parse_speakrs_turns(stdout) == [
        (0.385, 0.993, "SPEAKER_03"),
        (1.195, 1.651, "SPEAKER_00"),
    ]


def test_start_and_end_are_floats():
    (start, end, spk), = parse_speakrs_turns("8.148\t8.232\tSPEAKER_00\n")
    assert isinstance(start, float) and isinstance(end, float)
    assert spk == "SPEAKER_00"


def test_ignores_blank_lines():
    stdout = "\n0.0\t1.0\tSPEAKER_00\n\n"
    assert parse_speakrs_turns(stdout) == [(0.0, 1.0, "SPEAKER_00")]


def test_empty_output_yields_no_turns():
    assert parse_speakrs_turns("") == []
