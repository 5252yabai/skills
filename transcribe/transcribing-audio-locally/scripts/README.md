# scripts — transcribing-audio-locally

이 스킬이 사용하는 로컬 스크립트.

## 구성

- `transcribe/` — 로컬 음성 전사 (mlx-whisper) + 화자 구분 (pyannote). **Apple Silicon 전용**.
- `clovanote/` — Voice Memos 목록 조회 보조 도구 (`clovanote_upload --list`). 원본은 `~/scripts/clovanote` (uploading-to-clovanote 스킬). 여기 사본은 이 스킬 자립용.

## Setup (최초 1회)

[uv](https://docs.astral.sh/uv/) 필요.

```bash
# 전사 환경
cd transcribe && uv sync

# Voice Memos 목록 조회용
cd clovanote && uv sync
```

`uv sync`는 `uv.lock`에 핀된 버전으로 재현 설치한다. `pyproject.toml`의 의존성 핀은 느슨(`>=`)하므로 머신/OS에 따라 해석이 달라질 수 있으나, `uv.lock`이 동일 환경 재현을 보장한다.

## 실행

`SKILL.md`의 Quick Reference 참조. 핵심:

```bash
cd transcribe && uv run python transcribe.py "<오디오 절대경로>" --token "$HF_TOKEN"
```

## 전제

- Apple Silicon Mac (MPS / mlx_metal)
- 화자 구분 시 `HF_TOKEN` 환경변수 또는 `--token`
- 첫 실행 시 HuggingFace pyannote 모델 캐시 다운로드 (~150MB)
- 권장: `ffmpeg` (오디오 정규화)

## 테스트

```bash
cd transcribe && uv run pytest
```
