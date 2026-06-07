#!/usr/bin/env python3
"""Audio transcription with optional speaker diarization using mlx-whisper + pyannote."""

import argparse
import contextlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass


DEFAULT_KO_PROMPT = "다음은 한국어 음성입니다."


@dataclass(frozen=True)
class DiarizationConfig:
    """Bundle of pyannote diarization tuning parameters. Defaults match argparse defaults."""
    num_speakers: int | None = None
    min_speakers: int | None = None
    max_speakers: int | None = None
    device_pref: str = "auto"
    embedding_batch_size: int = 32
    segmentation_batch_size: int = 32
    profile: bool = False

MODEL_ALIASES: dict[str, str] = {
    "large-v3":       "mlx-community/whisper-large-v3-mlx",
    "large-v3-turbo": "mlx-community/whisper-large-v3-turbo",
}


def _dominant_speaker(
    start: float,
    end: float,
    speaker_turns: list[tuple[float, float, str]],
) -> str | None:
    """Return the speaker with the most overlap over [start, end], tie-broken by
    speaker label for determinism. Returns None when no turn overlaps. Pure function."""
    overlap: dict[str, float] = {}
    for turn_start, turn_end, speaker in speaker_turns:
        ov = min(end, turn_end) - max(start, turn_start)
        if ov > 0:
            overlap[speaker] = overlap.get(speaker, 0.0) + ov
    if not overlap:
        return None
    return max(overlap, key=lambda s: (overlap[s], s))


def _nearest_speaker(time_point: float, speaker_turns: list[tuple[float, float, str]]) -> str:
    """Return speaker of the turn nearest to time_point. Tie-break by speaker label (deterministic)."""
    best_speaker: str = speaker_turns[0][2]
    best_dist = float("inf")
    for turn_start, turn_end, speaker in speaker_turns:
        if turn_start <= time_point <= turn_end:
            dist = 0.0
        else:
            dist = min(abs(time_point - turn_start), abs(time_point - turn_end))
        if dist < best_dist or (dist == best_dist and speaker < best_speaker):
            best_dist = dist
            best_speaker = speaker
    return best_speaker


def _speaker_for_word(word: dict, speaker_turns: list[tuple[float, float, str]]) -> str:
    """Assign speaker to a word by overlap; fall back to nearest turn when no overlap."""
    word_start = word["start"]
    word_end = word["end"]
    speaker = _dominant_speaker(word_start, word_end, speaker_turns)
    if speaker is not None:
        return speaker
    return _nearest_speaker((word_start + word_end) / 2, speaker_turns)


def assign_speakers_by_word(
    segments: list[dict],
    speaker_turns: list[tuple[float, float, str]],
) -> list[dict]:
    """Assign speakers at word level; merge consecutive same-speaker words into new segments.

    Falls back to segment-level overlap for segments without word timestamps.
    Falls back to nearest turn when a word/segment has no overlap with any turn.
    Returns UNKNOWN only when speaker_turns is empty.
    """
    if not speaker_turns:
        return [{**seg, "speaker": "UNKNOWN"} for seg in segments]

    result: list[dict] = []

    for segment in segments:
        words = segment.get("words")

        if not words:
            seg_start = segment["start"]
            seg_end = segment["end"]
            assigned = _dominant_speaker(seg_start, seg_end, speaker_turns)
            if assigned is None:
                assigned = _nearest_speaker((seg_start + seg_end) / 2, speaker_turns)
            result.append({**segment, "speaker": assigned})
            continue

        word_speakers = [(_speaker_for_word(w, speaker_turns), w) for w in words]

        i = 0
        while i < len(word_speakers):
            speaker = word_speakers[i][0]
            run: list[dict] = [word_speakers[i][1]]
            j = i + 1
            while j < len(word_speakers) and word_speakers[j][0] == speaker:
                run.append(word_speakers[j][1])
                j += 1
            result.append({
                "start": run[0]["start"],
                "end": run[-1]["end"],
                "text": "".join(w["word"] for w in run),
                "speaker": speaker,
                "words": run,
            })
            i = j

    return result


@contextlib.contextmanager
def timed_step(done_template: str, *, start: str | None = None):
    """Time the body and report it. Prints `start` (if given) on entry, then
    `done_template` with the elapsed time substituted into its `{}` placeholder
    as a `:.1f`-second string. Centralizes the measurement and time format."""
    if start is not None:
        print(start)
    t0 = time.perf_counter()
    yield
    print(done_template.format(f"{time.perf_counter() - t0:.1f}s"))


def format_time(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def render_plain(text: str) -> str:
    """Render plain transcription text as-is. Pure function."""
    return text


def render_diarized(segments: list[dict]) -> str:
    """Render speaker-assigned segments, grouping consecutive same-speaker runs
    under a [speaker] header. Pure function."""
    lines = []
    prev_speaker = None
    for r in segments:
        if r["speaker"] != prev_speaker:
            lines.append(f"\n[{r['speaker']}]")
            prev_speaker = r["speaker"]
        lines.append(f"  [{format_time(r['start'])}] {r['text']}")
    return "\n".join(lines).strip()


def render_diarize_only(speaker_turns: list[tuple[float, float, str]]) -> str:
    """Render speaker turns as one timestamped line per turn. Pure function."""
    return "\n".join(
        f"[{format_time(s)}-{format_time(e)}] {spk}" for s, e, spk in speaker_turns
    )


@contextlib.contextmanager
def maybe_normalized(path: str, normalize: bool):
    """Yield a mono/16kHz/loudnorm-normalized wav path, or the original if unavailable."""
    if not normalize:
        yield path
        return
    if not shutil.which("ffmpeg"):
        print("    경고: ffmpeg를 찾을 수 없어 원본 파일을 사용합니다.")
        yield path
        return
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = os.path.join(tmpdir, "normalized.wav")
        try:
            subprocess.run(
                ["ffmpeg", "-y", "-i", path, "-ac", "1", "-ar", "16000", "-af", "loudnorm", out_path],
                check=True,
                capture_output=True,
            )
            print("    오디오 정규화 완료 (mono 16kHz loudnorm)")
            yield out_path
        except subprocess.CalledProcessError as e:
            msg = e.stderr.decode(errors="replace").strip()[-200:]
            print(f"    경고: 정규화 실패({msg}) — 원본 파일을 사용합니다.")
            yield path


def run_whisper(
    audio_path: str,
    model_repo: str,
    language: str,
    prompt: str | None,
    verbose: bool,
) -> dict:
    import mlx_whisper

    return mlx_whisper.transcribe(
        audio_path,
        path_or_hf_repo=model_repo,
        language=language,
        word_timestamps=True,
        initial_prompt=prompt,
        condition_on_previous_text=False,  # prevents Korean hallucination cascades
        verbose=verbose or None,
    )


def _load_pipeline(hf_token: str):
    """Load pyannote speaker-diarization-community-1 pipeline from HuggingFace."""
    from pyannote.audio import Pipeline
    return Pipeline.from_pretrained("pyannote/speaker-diarization-community-1", token=hf_token)


def _select_device(pref: str):
    """Return a torch.device based on preference: 'auto', 'mps', or 'cpu'."""
    import torch
    if pref == "cpu":
        return torch.device("cpu")
    if pref == "mps":
        return torch.device("mps")
    return torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")


@contextlib.contextmanager
def _build_hook(profile: bool):
    """Yield a pyannote hook. Uses TimingHook+ProgressHook in profile mode."""
    if profile:
        from pyannote.audio.pipelines.utils.hook import Hooks, ProgressHook, TimingHook
        with Hooks(ProgressHook(), TimingHook()) as hook:
            yield hook
    else:
        from pyannote.audio.pipelines.utils.hook import ProgressHook
        with ProgressHook() as hook:
            yield hook


def print_env_diagnostics() -> None:
    """Print torch/pyannote environment info for debugging slow runs."""
    import torch
    print("  [진단] 환경 정보")
    print(f"    platform    : {platform.machine()} / {platform.processor()}")
    print(f"    torch       : {torch.__version__}")
    print(f"    MPS avail   : {torch.backends.mps.is_available()}")
    print(f"    MPS built   : {torch.backends.mps.is_built()}")
    print(f"    MPS_FALLBACK: {os.environ.get('PYTORCH_ENABLE_MPS_FALLBACK', '(unset)')}")
    try:
        import pyannote.audio
        print(f"    pyannote    : {pyannote.audio.__version__}")
    except Exception:
        print("    pyannote    : (import 실패)")
    cache = os.path.expanduser("~/.cache/huggingface/hub/models--pyannote--speaker-diarization-community-1")
    print(f"    HF cache    : {'있음' if os.path.isdir(cache) else '없음 (첫 실행 시 다운로드)'}")


def _run_with_cpu_fallback(pipeline, device, run):
    """Move pipeline to device and run(); on MPS failure retry on CPU, else propagate."""
    import torch

    try:
        pipeline.to(device)
        return run()
    except Exception as e:
        if device.type != "mps":
            raise
        mps_env = os.environ.get("PYTORCH_ENABLE_MPS_FALLBACK", "(unset)")
        print(f"    MPS 오류 — CPU로 재시도. ({type(e).__name__}: {str(e)[:200]})")
        print(f"    PYTORCH_ENABLE_MPS_FALLBACK={mps_env}")
        with timed_step("    CPU 재시도 소요: {}"):
            pipeline.to(torch.device("cpu"))
            result = run()
        return result


def run_diarization(
    audio_path: str,
    hf_token: str,
    config: DiarizationConfig,
) -> list[tuple[float, float, str]]:
    import torch

    with timed_step("    모델 로드: {}"):
        pipeline = _load_pipeline(hf_token)

    try:
        pipeline.embedding_batch_size = config.embedding_batch_size
        pipeline.segmentation_batch_size = config.segmentation_batch_size
        print(f"    배치 크기: seg={config.segmentation_batch_size}, emb={config.embedding_batch_size}")
    except AttributeError as e:
        print(f"    경고: 배치 크기 설정 실패 ({e}) — 기본값 사용")

    device = _select_device(config.device_pref)
    print(f"    디바이스: {device}")

    kwargs: dict = {}
    if config.num_speakers is not None:
        kwargs["num_speakers"] = config.num_speakers
    else:
        if config.min_speakers is not None:
            kwargs["min_speakers"] = config.min_speakers
        if config.max_speakers is not None:
            kwargs["max_speakers"] = config.max_speakers

    # pyannote wants its input as a {"audio", "uri"} dict; that contract lives here,
    # not in callers. The hook (TimingHook in profile mode) mutates this dict in place.
    file_dict = {"audio": audio_path, "uri": os.path.basename(audio_path)}

    def run():
        with _build_hook(config.profile) as hook:
            with torch.inference_mode():
                return pipeline(file_dict, hook=hook, **kwargs)

    output = _run_with_cpu_fallback(pipeline, device, run)

    if config.profile and "timing" in file_dict:
        print("    [profile] 단계별 시간:")
        for k, v in file_dict["timing"].items():
            print(f"      {k:30s} {v:7.2f}s")

    annotation = getattr(output, "speaker_diarization", output)
    return [(t.start, t.end, spk) for t, _, spk in annotation.itertracks(yield_label=True)]


def transcribe_only(
    audio_path: str,
    model_repo: str,
    language: str,
    prompt: str | None,
    verbose: bool,
    normalize: bool,
) -> tuple[str, dict]:
    with timed_step(
        "    전사 완료 ({})",
        start=f"전사 중... ({audio_path})\n    모델: {model_repo}  언어: {language}",
    ):
        with maybe_normalized(audio_path, normalize) as work_path:
            result = run_whisper(work_path, model_repo, language, prompt, verbose)
    return result["text"], result


def transcribe_with_speakers(
    audio_path: str,
    hf_token: str,
    model_repo: str,
    language: str,
    prompt: str | None,
    verbose: bool,
    normalize: bool,
    config: DiarizationConfig,
) -> tuple[list[dict], dict]:
    with timed_step("    전체 소요: {}"):
        # Both Whisper and diarization share the same normalized wav — avoids double
        # decoding/resampling and ensures identical timestamp coordinates.
        with maybe_normalized(audio_path, normalize) as work_path:
            with timed_step(
                "    전사 완료 ({})",
                start=f"[1/3] 전사 중... ({work_path})\n    모델: {model_repo}  언어: {language}",
            ):
                result = run_whisper(work_path, model_repo, language, prompt, verbose)

            with timed_step("    화자 구분 완료 ({})", start="[2/3] 화자 구분 중..."):
                speaker_turns = run_diarization(work_path, hf_token, config)

        print("[3/3] 결과 합치는 중...")
        assigned = assign_speakers_by_word(result["segments"], speaker_turns)
    return assigned, result


def diarize_only(
    audio_path: str,
    hf_token: str,
    normalize: bool,
    config: DiarizationConfig,
) -> list[tuple[float, float, str]]:
    """Normalize then diarize, returning speaker turns. No transcription."""
    with timed_step("    완료 ({})", start=f"[화자 구분] {audio_path}"):
        with maybe_normalized(audio_path, normalize) as work_path:
            speaker_turns = run_diarization(work_path, hf_token, config)
    return speaker_turns


def resolve_hf_token(token: str | None, env: dict) -> str:
    """Return HF token from arg (preferred) or env. Exit(1) with help if missing."""
    resolved = token or env.get("HF_TOKEN")
    if not resolved:
        print("오류: HuggingFace 토큰이 필요합니다.")
        print("  --token YOUR_TOKEN 또는 HF_TOKEN 환경변수로 전달하세요.")
        print("  화자 구분 없이 전사만 하려면 --no-diarize 옵션을 사용하세요.")
        sys.exit(1)
    return resolved


def emit(output_text: str, json_payload, *, output_path: str | None, json_path: str | None) -> None:
    """Common output tail: save JSON payload (if any), then write text to file or terminal."""
    if json_path and json_payload is not None:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_payload, f, ensure_ascii=False, indent=2)
        print(f"JSON 저장: {json_path}")

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"\n저장 완료: {output_path}")
    else:
        print("\n" + "=" * 50)
        print(output_text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="음성 전사 (화자 구분 선택 가능)")
    parser.add_argument("audio", help="오디오 파일 경로 (m4a, mp3, wav 등)")
    parser.add_argument("--token", "-t", help="HuggingFace 토큰 (또는 HF_TOKEN 환경변수)")
    parser.add_argument("--language", "-l", default="ko", help="언어 코드 (기본값: ko)")
    parser.add_argument("--output", "-o", help="텍스트 출력 파일 경로 (없으면 터미널 출력)")
    parser.add_argument("--json", dest="json_output", metavar="PATH", help="JSON 출력 파일 경로")
    parser.add_argument(
        "--model", "-m",
        default="large-v3",
        choices=list(MODEL_ALIASES.keys()),
        help="Whisper 모델 (기본: large-v3 = 정확도 최우선, large-v3-turbo = 빠름)",
    )
    parser.add_argument(
        "--prompt", "-p",
        help="초기 프롬프트 (도메인 어휘/문체 힌트). 예: '회의록입니다. 참석자: 김철수, 박영희.'",
    )
    parser.add_argument("--no-diarize", action="store_true", help="화자 구분 없이 전사만 수행")
    parser.add_argument("--no-normalize", action="store_true", help="ffmpeg 오디오 정규화 건너뜀")
    parser.add_argument("--verbose", "-v", action="store_true", help="segment별 전사 중간 출력")
    parser.add_argument("--profile", action="store_true",
                        help="단계별 wall-clock 측정 (TimingHook + 환경 진단 출력)")
    parser.add_argument("--diarize-only", action="store_true",
                        help="전사 생략, 화자 구분만 실행 (--no-diarize와 상호배타)")
    parser.add_argument(
        "--device", choices=["auto", "mps", "cpu"], default="auto",
        help="diarization 디바이스 강제 선택 (기본: auto)",
    )
    parser.add_argument("--num-speakers", type=int, default=None,
                        help="화자 수가 정확히 알려진 경우 지정")
    parser.add_argument("--min-speakers", type=int, default=None, help="최소 화자 수 힌트")
    parser.add_argument("--max-speakers", type=int, default=None, help="최대 화자 수 힌트")
    parser.add_argument(
        "--embedding-batch-size", type=int, default=32,
        help="pyannote 임베딩 배치 크기 (기본 32, OOM 시 줄이세요)",
    )
    parser.add_argument(
        "--segmentation-batch-size", type=int, default=32,
        help="pyannote segmentation 배치 크기 (기본 32)",
    )
    return parser


def validate_args(args, parser: argparse.ArgumentParser) -> None:
    if args.diarize_only and args.no_diarize:
        parser.error("--diarize-only와 --no-diarize는 함께 사용할 수 없습니다.")


def main():
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)

    if not os.path.exists(args.audio):
        print(f"오류: 파일을 찾을 수 없습니다 - {args.audio}")
        sys.exit(1)

    model_repo = MODEL_ALIASES[args.model]
    prompt = args.prompt if args.prompt is not None else DEFAULT_KO_PROMPT
    normalize = not args.no_normalize

    config = DiarizationConfig(
        num_speakers=args.num_speakers,
        min_speakers=args.min_speakers,
        max_speakers=args.max_speakers,
        device_pref=args.device,
        embedding_batch_size=args.embedding_batch_size,
        segmentation_batch_size=args.segmentation_batch_size,
        profile=args.profile,
    )

    if args.profile:
        print_env_diagnostics()

    json_payload = None

    if args.no_diarize:
        text, raw = transcribe_only(args.audio, model_repo, args.language, prompt, args.verbose, normalize)
        output_text = render_plain(text)
        json_payload = raw

    elif args.diarize_only:
        hf_token = resolve_hf_token(args.token, os.environ)
        speaker_turns = diarize_only(args.audio, hf_token, normalize, config)
        output_text = render_diarize_only(speaker_turns)

    else:
        hf_token = resolve_hf_token(args.token, os.environ)
        results, raw = transcribe_with_speakers(
            args.audio, hf_token, model_repo, args.language, prompt, args.verbose, normalize, config,
        )
        output_text = render_diarized(results)
        json_payload = {"segments": results, "raw": raw}

    emit(output_text, json_payload, output_path=args.output, json_path=args.json_output)


if __name__ == "__main__":
    main()
