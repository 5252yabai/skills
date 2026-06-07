---
name: transcribing-audio-locally
description: Use for any audio transcription request (받아쓰기/전사/transcribe, m4a/mp3/wav/aac/flac) that does NOT explicitly mention Clova Note. Default local transcription tool using mlx-whisper + pyannote at scripts/transcribe/transcribe.py (within this skill). Only use uploading-to-clovanote when user says "클로바 노트".
---

# 로컬 음성 전사 (transcribe.py)

## Overview

`~/.agents/skills/transcribing-audio-locally/scripts/transcribe/transcribe.py`로 호출. mlx-whisper(전사) + pyannote(화자 구분), 모두 로컬·온디바이스. 클라우드 업로드 없음 — 프라이버시 보호.

## When to Use

트리거 예시:

- "이 m4a 받아쓰기 해줘"
- "회의 녹음 전사 + 화자 구분 해줘"
- "Whisper로 이 음성 받아쓰기"
- "transcribe this recording"

지원 포맷: `.m4a` `.mp3` `.wav` `.aac` `.flac` 등 ffmpeg 지원 포맷

**When NOT to use:**

- 사용자가 **클로바 노트(Clova Note)**를 명시 → `uploading-to-clovanote` 사용
- 사용자가 OpenAI Whisper API / 다른 클라우드 STT를 명시 → 해당 도구
- Apple Silicon이 아닌 환경 (MLX/MPS 의존)

## Quick Reference

**파일 경로가 없을 때 — Voice Memos 목록 조회:**

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/clovanote && uv run python -m clovanote_upload --list
```

출력 예시:

```
 1. 20260507 133159.m4a  20260507 daily  (14.8 MB)
 2. 20260507 090040.m4a  회의  (28.0 MB)
```

목록을 사용자에게 보여주고 선택을 받은 뒤, 아래 파일 경로로 실행한다:

`~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/<파일명>`

---

기본 (화자 구분 + 전사, 한국어):

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오 절대경로>" --token "$HF_TOKEN"
```

전사만 (HF 토큰 불필요, 더 빠름):

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" --no-diarize
```

화자 구분만:

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" --token "$HF_TOKEN" --diarize-only
```

파일로 저장 (TXT + JSON):

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" --token "$HF_TOKEN" -o out.txt --json out.json
```

## Options

| 옵션                                                   | 기본값                      | 설명                                        |
| ------------------------------------------------------ | --------------------------- | ------------------------------------------- |
| `--token`, `-t`                                        | `$HF_TOKEN`                 | HuggingFace 토큰. 화자 구분 시 필수         |
| `--language`, `-l`                                     | `ko`                        | 언어 코드                                   |
| `--model`, `-m`                                        | `large-v3`                  | `large-v3`(정확도) / `large-v3-turbo`(속도) |
| `--prompt`, `-p`                                       | "다음은 한국어 음성입니다." | 도메인 어휘·참석자 힌트                     |
| `--no-diarize`                                         | off                         | 화자 구분 생략                              |
| `--diarize-only`                                       | off                         | 전사 생략                                   |
| `--num-speakers N`                                     | auto                        | 정확히 N명 화자                             |
| `--min-speakers` / `--max-speakers`                    | auto                        | 화자 수 범위 힌트                           |
| `--output`, `-o` PATH                                  | stdout                      | TXT 출력 경로                               |
| `--json` PATH                                          | (없음)                      | JSON 출력 경로                              |
| `--verbose`, `-v`                                      | off                         | segment별 중간 출력                         |
| `--profile`                                            | off                         | 단계별 시간 측정 + 환경 진단                |
| `--device`                                             | `auto`                      | `auto` / `mps` / `cpu`                      |
| `--no-normalize`                                       | off                         | ffmpeg 정규화 건너뜀                        |
| `--embedding-batch-size` / `--segmentation-batch-size` | 32                          | OOM 시 줄임                                 |

## Decision Logic

사용자 요청에서 아래를 추출해 옵션을 결정한다.

1. **화자 구분 필요한가?**
   - 단일 화자 / 받아쓰기만 → `--no-diarize` (HF 토큰 불필요)
   - 다중 화자 회의·인터뷰 → 기본(diarization 포함). HF 토큰 확인

2. **화자 수를 아는가?**
   - 정확히 안다 → `--num-speakers N`
   - 대략 안다 → `--min-speakers` / `--max-speakers`
   - 모름 → 생략(자동 추정). **가능하면 사용자에게 화자 수 확인**

3. **도메인 힌트가 있는가?**
   - 회의 주제·참석자 이름·전문 용어 → `--prompt "회의록입니다. 참석자: A, B. 주요 용어: X, Y."`

4. **출력 형식**
   - 슬랙 게시 등 후속 처리 → `--json out.json` 함께 지정
   - 텍스트만 → `-o out.txt`

## Workflow

1. 오디오 파일의 **절대경로** 확보.
   - 경로가 주어진 경우: 그대로 사용
   - 경로가 없는 경우: `cd ~/.agents/skills/transcribing-audio-locally/scripts/clovanote && uv run python -m clovanote_upload --list`로 Voice Memos 최근 목록을 조회해 사용자에게 보여준 뒤 선택을 받는다. 선택된 파일의 경로는 `~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/<파일명>` 형식이다.
2. Decision Logic으로 옵션 결정
3. HF_TOKEN 확인 (`echo "${HF_TOKEN:+set}"` — 값 노출 없이 확인). 없고 화자 구분 필요하면 `--no-diarize` 제안
4. 명령 실행 → 진행 로그(한국어)가 stdout으로 출력됨
5. 출력 파일 경로 또는 stdout 결과를 사용자에게 전달

## Prerequisites

- Apple Silicon Mac (MPS) — mlx는 Apple Silicon 전용
- 의존성: `scripts/transcribe/`에서 `uv sync` (최초 1회). `mlx-whisper`, `pyannote.audio`, `torch` 설치. 자세한 setup은 `scripts/README.md`
- 화자 구분 시: `HF_TOKEN` 환경변수 또는 `--token`
- 권장: `ffmpeg` (오디오 정규화)
- 첫 실행 시 HuggingFace 캐시 다운로드 (~150MB pyannote 모델)

## Common Mistakes

- HF 토큰 없이 화자 구분 시도 → `--no-diarize` 안내 또는 토큰 요청
- 긴 오디오를 `--verbose`로 실행 → 출력 폭주. `--profile` 사용
- 상대경로 입력 → 항상 절대경로 + 따옴표 사용
- 화자 수 추측 후 `--num-speakers` 입력 → 모르면 생략하거나 사용자에게 확인
- 클로바 노트 요청을 이 스킬로 처리 → `uploading-to-clovanote` 사용
- **동일 `SPEAKER_XX` 라벨에 다중 화자 가능**: pyannote는 비슷한 톤·거리의 화자를 한 라벨로 묶을 수 있다. 자기소개 발화 1개로 라벨 전체를 한 사람으로 단정 금지. 같은 라벨 내 발화 스타일·역할·다른 참석자의 호칭 패턴이 일관되는지 교차 검증. 불확실하면 사용자에게 화자 매핑을 명시적으로 확인.
- **약어·조직명 정확도 의심**: 한국어 STT는 1~3음절 약어(TX/DX, CP1, AX 등)와 조직명에서 오류 빈도가 높다. 회의 내 소속 언급 구간의 약어가 맞는지 사용자에게 확인하거나 채널 과거 게시물에서 검증한다.
