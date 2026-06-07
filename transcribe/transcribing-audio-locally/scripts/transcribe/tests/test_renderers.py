import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import render_diarize_only, render_diarized, render_plain


def diar_seg(start, speaker, text):
    return {"start": start, "end": start + 1.0, "speaker": speaker, "text": text}


def test_diarize_only_single_turn():
    turns = [(0.0, 5.0, "SPEAKER_00")]
    assert render_diarize_only(turns) == "[00:00-00:05] SPEAKER_00"


def test_diarize_only_multiple_turns_one_line_each():
    turns = [
        (0.0, 5.0, "SPEAKER_00"),
        (5.0, 70.0, "SPEAKER_01"),
    ]
    assert render_diarize_only(turns) == (
        "[00:00-00:05] SPEAKER_00\n"
        "[00:05-01:10] SPEAKER_01"
    )


def test_diarize_only_empty_is_empty_string():
    assert render_diarize_only([]) == ""


def test_diarized_single_speaker_one_header():
    segs = [
        diar_seg(0.0, "SPEAKER_00", "안녕하세요"),
        diar_seg(2.0, "SPEAKER_00", "반갑습니다"),
    ]
    assert render_diarized(segs) == (
        "[SPEAKER_00]\n"
        "  [00:00] 안녕하세요\n"
        "  [00:02] 반갑습니다"
    )


def test_diarized_speaker_switch_emits_new_header_with_blank_line():
    segs = [
        diar_seg(0.0, "SPEAKER_00", "질문"),
        diar_seg(3.0, "SPEAKER_01", "답변"),
        diar_seg(5.0, "SPEAKER_00", "다시"),
    ]
    assert render_diarized(segs) == (
        "[SPEAKER_00]\n"
        "  [00:00] 질문\n"
        "\n"
        "[SPEAKER_01]\n"
        "  [00:03] 답변\n"
        "\n"
        "[SPEAKER_00]\n"
        "  [00:05] 다시"
    )


def test_diarized_empty_is_empty_string():
    assert render_diarized([]) == ""


def test_plain_returns_text_unchanged():
    assert render_plain("그냥 텍스트\n둘째 줄") == "그냥 텍스트\n둘째 줄"
