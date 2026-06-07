import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import assign_speakers_by_word


def w(word, start, end):
    return {"word": word, "start": start, "end": end}


def seg(start, end, text, words=None):
    s = {"start": start, "end": end, "text": text}
    if words is not None:
        s["words"] = words
    return s


# ──────────────────────────────────────────────
# 핵심 기능: word 단위 화자 분리
# ──────────────────────────────────────────────

def test_single_speaker_segment_stays_as_one():
    segments = [seg(0.0, 3.0, "안녕 반가워요", [w("안녕", 0.0, 1.0), w("반가워요", 1.5, 3.0)])]
    turns = [(0.0, 3.0, "SPEAKER_00")]
    result = assign_speakers_by_word(segments, turns)
    assert len(result) == 1
    assert result[0]["speaker"] == "SPEAKER_00"


def test_segment_split_when_words_belong_to_different_speakers():
    # "안녕" → SPEAKER_00 (turn 0-1.5), "반가워" → SPEAKER_01 (turn 2-4)
    segments = [seg(0.0, 4.0, "안녕 반가워", [w("안녕", 0.0, 1.0), w("반가워", 2.5, 4.0)])]
    turns = [(0.0, 1.5, "SPEAKER_00"), (2.0, 4.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    assert len(result) == 2
    assert result[0]["speaker"] == "SPEAKER_00"
    assert result[1]["speaker"] == "SPEAKER_01"


def test_consecutive_same_speaker_words_merged():
    segments = [seg(0.0, 3.0, "좋은 아침이에요", [
        w("좋은", 0.0, 0.5), w("아침이에요", 0.5, 3.0)
    ])]
    turns = [(0.0, 3.0, "SPEAKER_00")]
    result = assign_speakers_by_word(segments, turns)
    assert len(result) == 1
    assert result[0]["speaker"] == "SPEAKER_00"


def test_split_preserves_word_timestamps():
    segments = [seg(0.0, 4.0, "A B", [w("A", 0.0, 1.0), w("B", 3.0, 4.0)])]
    turns = [(0.0, 1.5, "SPEAKER_00"), (2.5, 4.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["start"] == 0.0
    assert result[0]["end"] == 1.0
    assert result[1]["start"] == 3.0
    assert result[1]["end"] == 4.0


def test_split_across_multiple_input_segments():
    segments = [
        seg(0.0, 2.0, "A B", [w("A", 0.0, 1.0), w("B", 1.0, 2.0)]),
        seg(2.0, 4.0, "C D", [w("C", 2.0, 3.0), w("D", 3.0, 4.0)]),
    ]
    turns = [(0.0, 1.5, "SPEAKER_00"), (1.5, 4.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    speakers = [r["speaker"] for r in result]
    assert "SPEAKER_00" in speakers
    assert "SPEAKER_01" in speakers


# ──────────────────────────────────────────────
# UNKNOWN 제거: nearest turn fallback
# ──────────────────────────────────────────────

def test_no_overlap_falls_back_to_nearest_turn_not_unknown():
    # word at [5, 6], turns at [0, 3] and [8, 10]
    segments = [seg(5.0, 6.0, "음", [w("음", 5.0, 6.0)])]
    turns = [(0.0, 3.0, "SPEAKER_00"), (8.0, 10.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["speaker"] != "UNKNOWN"


def test_nearest_fallback_picks_closer_turn():
    # word midpoint at 5.5, SPEAKER_00 ends at 3 (distance 2.5), SPEAKER_01 starts at 6 (distance 0.5)
    segments = [seg(5.0, 6.0, "음", [w("음", 5.0, 6.0)])]
    turns = [(0.0, 3.0, "SPEAKER_00"), (6.0, 9.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["speaker"] == "SPEAKER_01"


def test_nearest_fallback_is_deterministic_on_tie():
    # word midpoint equidistant from two turns → same result every time
    segments = [seg(4.0, 6.0, "음", [w("음", 4.0, 6.0)])]
    turns = [(0.0, 3.0, "SPEAKER_01"), (7.0, 10.0, "SPEAKER_00")]
    r1 = assign_speakers_by_word(segments, turns)
    r2 = assign_speakers_by_word(segments, turns)
    assert r1[0]["speaker"] == r2[0]["speaker"]
    assert r1[0]["speaker"] != "UNKNOWN"


# ──────────────────────────────────────────────
# word 없는 segment 처리 (fallback)
# ──────────────────────────────────────────────

def test_segment_without_words_uses_segment_level_overlap():
    segments = [seg(0.0, 3.0, "안녕하세요")]  # words 없음
    turns = [(0.0, 3.0, "SPEAKER_00")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["speaker"] == "SPEAKER_00"


def test_segment_without_words_also_uses_nearest_fallback():
    segments = [seg(5.0, 6.0, "음")]  # words 없음, 겹침 없음
    turns = [(0.0, 3.0, "SPEAKER_00"), (8.0, 10.0, "SPEAKER_01")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["speaker"] != "UNKNOWN"


def test_empty_turns_returns_unknown():
    segments = [seg(0.0, 3.0, "안녕", [w("안녕", 0.0, 3.0)])]
    result = assign_speakers_by_word(segments, [])
    assert result[0]["speaker"] == "UNKNOWN"


# ──────────────────────────────────────────────
# 출력 구조 검증
# ──────────────────────────────────────────────

def test_output_has_required_keys():
    segments = [seg(0.0, 2.0, "안녕", [w("안녕", 0.0, 2.0)])]
    turns = [(0.0, 2.0, "SPEAKER_00")]
    result = assign_speakers_by_word(segments, turns)
    assert "start" in result[0]
    assert "end" in result[0]
    assert "text" in result[0]
    assert "speaker" in result[0]


def test_merged_segment_text_combines_words():
    segments = [seg(0.0, 3.0, "A B C", [
        w(" A", 0.0, 1.0), w(" B", 1.0, 2.0), w(" C", 2.0, 3.0)
    ])]
    turns = [(0.0, 3.0, "SPEAKER_00")]
    result = assign_speakers_by_word(segments, turns)
    assert result[0]["text"].strip() != ""
