import sys
import os
import re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import timed_step


def test_done_template_gets_elapsed_in_one_decimal_seconds(capsys):
    with timed_step("    모델 로드: {}"):
        pass
    out = capsys.readouterr().out
    assert re.fullmatch(r"    모델 로드: \d+\.\d{1}s\n", out)


def test_parenthesized_done_template(capsys):
    with timed_step("    완료 ({})"):
        pass
    out = capsys.readouterr().out
    assert re.fullmatch(r"    완료 \(\d+\.\d{1}s\)\n", out)


def test_start_message_printed_before_body(capsys):
    with timed_step("    완료 ({})", start="[화자 구분] foo"):
        print("body")
    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "[화자 구분] foo"
    assert lines[1] == "body"
    assert re.fullmatch(r"    완료 \(\d+\.\d{1}s\)", lines[2])


def test_no_start_message_emits_only_done_line(capsys):
    with timed_step("    완료 ({})"):
        pass
    assert len(capsys.readouterr().out.splitlines()) == 1


def test_multiline_start_message(capsys):
    with timed_step("    전사 완료 ({})", start="[1/3] 전사 중... (a.wav)\n    모델: m  언어: ko"):
        pass
    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "[1/3] 전사 중... (a.wav)"
    assert lines[1] == "    모델: m  언어: ko"
