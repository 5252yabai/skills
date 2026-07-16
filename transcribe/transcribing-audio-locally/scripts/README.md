# scripts — transcribing-audio-locally

이 스킬이 사용하는 로컬 스크립트.

## 구성

- `transcribe/` — 로컬 음성 전사 (mlx-whisper) + 화자 구분 (speakrs, Rust/CoreML). **Apple Silicon 전용**.
- `clovanote/` — Voice Memos 목록 조회 보조 도구 (`clovanote_upload --list`). 원본은 `~/scripts/clovanote` (uploading-to-clovanote 스킬). 여기 사본은 이 스킬 자립용.

## Setup (최초 1회)

[uv](https://docs.astral.sh/uv/) 필요.

```bash
# 전사 환경
cd transcribe && uv sync

# 화자 구분 바이너리 빌드 (speakrs). rust/cargo + `brew install openblas` 필요.
cd transcribe && ./setup_speakrs.sh

# Voice Memos 목록 조회용
cd clovanote && uv sync
```

`uv sync`는 `uv.lock`에 핀된 버전으로 재현 설치한다. `setup_speakrs.sh`는 speakrs를 핀 커밋(v0.5.0)으로 클론해 `bench_turns` 예제를 빌드하고 `.speakrs/bench_turns`에 캐시한다(git 추적 제외). `SPEAKRS_BIN` 환경변수로 다른 경로의 바이너리를 지정할 수 있다.

## 실행

`SKILL.md`의 Quick Reference 참조. 핵심:

```bash
cd transcribe && uv run python transcribe.py "<오디오 절대경로>"
```

## 전제

- Apple Silicon Mac (mlx_metal / CoreML)
- 화자 구분: `./setup_speakrs.sh`로 빌드된 speakrs 바이너리 (**HF 토큰 불필요**). rust/cargo + openblas 필요
- 첫 화자 구분 실행 시 speakrs 모델 다운로드(~144MB) + CoreML 컴파일(~200초, 1회성)
- 권장: `ffmpeg` (오디오 정규화 — 화자 구분은 mono/16k/16-bit PCM 필수)

## 테스트

```bash
cd transcribe && uv run pytest
```
