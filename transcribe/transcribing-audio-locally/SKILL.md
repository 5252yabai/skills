---
name: transcribing-audio-locally
description: Use for any audio transcription request (받아쓰기/전사/transcribe, m4a/mp3/wav/aac/flac) that does NOT explicitly mention Clova Note. Default local transcription tool using mlx-whisper + speakrs at scripts/transcribe/transcribe.py (within this skill). When run inside a wiki vault (cwd has 1.Raw/ and 2.Wiki/), also saves the transcript to 1.Raw and chains wiki-ingest to summarize into 2.Wiki. Only use uploading-to-clovanote when user says "클로바 노트".
---

# 로컬 음성 전사 (transcribe.py)

## Overview

`~/.agents/skills/transcribing-audio-locally/scripts/transcribe/transcribe.py`로 호출. mlx-whisper(전사) + speakrs(화자 구분, Rust/CoreML), 모두 로컬·온디바이스. 클라우드 업로드 없음 — 프라이버시 보호. 화자 구분은 speakrs 공개 모델(hf-hub 자동 다운로드)을 쓰므로 **HF 토큰 불필요**하고, pyannote 대비 ~17배 빠르다(43분 오디오 diarize ~10초).

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
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오 절대경로>"
```

전사만 (더 빠름):

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" --no-diarize
```

화자 구분만:

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" --diarize-only
```

파일로 저장 (TXT + JSON):

```bash
cd ~/.agents/skills/transcribing-audio-locally/scripts/transcribe && uv run python transcribe.py "<오디오>" -o out.txt --json out.json
```

## Options

| 옵션                  | 기본값                      | 설명                                        |
| --------------------- | --------------------------- | ------------------------------------------- |
| `--language`, `-l`    | `ko`                        | 언어 코드                                   |
| `--model`, `-m`       | `large-v3`                  | `large-v3`(정확도) / `large-v3-turbo`(속도) |
| `--prompt`, `-p`      | "다음은 한국어 음성입니다." | 도메인 어휘·참석자 힌트                     |
| `--no-diarize`        | off                         | 화자 구분 생략 (전사만)                     |
| `--diarize-only`      | off                         | 전사 생략 (화자 구분만)                     |
| `--output`, `-o` PATH | stdout                      | TXT 출력 경로                               |
| `--json` PATH         | (없음)                      | JSON 출력 경로                              |
| `--verbose`, `-v`     | off                         | segment별 중간 출력                         |
| `--no-normalize`      | off                         | ffmpeg 정규화 건너뜀 (화자 구분 시 비권장)  |

> speakrs는 cosine-threshold 클러스터링이라 화자 수(`--num-speakers` 등)·디바이스·배치 옵션을 받지 않는다. 화자 수는 자동 추정된다.

## Decision Logic

사용자 요청에서 아래를 추출해 옵션을 결정한다.

1. **화자 구분 필요한가?**
   - 단일 화자 / 받아쓰기만 → `--no-diarize` (더 빠름)
   - 다중 화자 회의·인터뷰 → 기본(diarization 포함). 화자 수는 speakrs가 자동 추정

2. **도메인 힌트가 있는가?**
   - 회의 주제·참석자 이름·전문 용어 → `--prompt "회의록입니다. 참석자: A, B. 주요 용어: X, Y."`

3. **출력 형식**
   - 슬랙 게시 등 후속 처리 → `--json out.json` 함께 지정
   - 텍스트만 → `-o out.txt`

## Workflow

1. 오디오 파일의 **절대경로** 확보.
   - 경로가 주어진 경우: 그대로 사용
   - 경로가 없는 경우: `cd ~/.agents/skills/transcribing-audio-locally/scripts/clovanote && uv run python -m clovanote_upload --list`로 Voice Memos 최근 목록을 조회해 사용자에게 보여준 뒤 선택을 받는다. 선택된 파일의 경로는 `~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/<파일명>` 형식이다.
2. Decision Logic으로 옵션 결정
3. (화자 구분 시) speakrs 바이너리 확인 — 없으면 스크립트가 `./setup_speakrs.sh` 안내 후 종료. 최초 1회 빌드 필요
4. 명령 실행 → 진행 로그(한국어)가 stdout으로 출력됨
5. 출력 파일 경로 또는 stdout 결과를 사용자에게 전달
6. **위키 vault면 위키 통합 수행** (아래) — cwd에 `1.Raw/`와 `2.Wiki/`가 모두 있으면 실행

## 위키 통합 (vault 자동감지)

cwd에 `1.Raw/`와 `2.Wiki/`가 **둘 다** 있을 때만 수행한다. 없으면 이 섹션 전체를 건너뛴다(일반 전사만).

감지:

```bash
[ -d 1.Raw ] && [ -d 2.Wiki ] && echo "vault"
```

`vault`가 출력되면 다음을 이어서 한다.

1. **전사 원본을 1.Raw에 저장** — 4단계 전사 결과를 `1.Raw/{YYYY-MM}/audio/` 아래 md로 저장한다. `{YYYY-MM}`는 오늘 날짜 기준. 폴더가 없으면 만든다. 파일명은 원본 오디오명 slug 또는 `transcript-{YYYY-MM-DD}-{짧은설명}.md`.
   - frontmatter는 `created`(YYYY-MM-DD), `source: audio-transcript` **두 필드만** 둔다. 그 외 필드 금지.
   - 본문은 전사 전문(화자 라벨 포함)을 **가공 없이** 그대로 넣는다. 이 파일은 이후 읽기 전용이다.
2. **wiki-ingest 체이닝** — 방금 저장한 `1.Raw/{YYYY-MM}/audio/<파일>`을 대상으로 `wiki-ingest` 스킬을 호출해 `2.Wiki/`를 갱신한다. 요약·핵심 통찰은 wiki-ingest 절차대로 `2.Wiki/analyses/`(및 필요 시 entities/themes)에 반영된다.
   - 오디오 전사 요약은 원칙적으로 **Analysis 페이지**로 남긴다: 회의·대화의 핵심 결정·논점·액션을 정리. entity/theme 갱신이 자연스러우면 함께 처리한다.
3. 사용자에게 저장된 1.Raw 경로와 생성/갱신된 2.Wiki 페이지 목록을 함께 보고한다.

주의:

- `1.Raw/`는 저장 후 절대 수정하지 않는다(읽기 전용).
- 화자 매핑이 불확실하면 전사 원본은 라벨 그대로 저장하되, 요약(2.Wiki)에는 확인 전까지 실명 단정을 피한다.

## Prerequisites

- Apple Silicon Mac — mlx(전사)·speakrs CoreML(화자 구분) 모두 Apple Silicon 전용
- 전사 의존성: `scripts/transcribe/`에서 `uv sync` (최초 1회). `mlx-whisper` 설치. 자세한 setup은 `scripts/README.md`
- 화자 구분: 최초 1회 `cd scripts/transcribe && ./setup_speakrs.sh` — speakrs(Rust/CoreML) 바이너리 빌드. `rust/cargo`와 `brew install openblas` 필요. **HF 토큰 불필요**
- 권장: `ffmpeg` (오디오 정규화 — 화자 구분은 mono/16k/16-bit PCM 필수라 정규화 권장)
- 첫 화자 구분 실행 시 speakrs 모델 다운로드(~144MB) + CoreML 컴파일(~200초, 1회성)

## Common Mistakes

- speakrs 바이너리 미빌드 상태로 화자 구분 → `./setup_speakrs.sh` 안내 또는 `--no-diarize`
- `--no-normalize` + 화자 구분 → speakrs는 mono/16k/16-bit PCM만 받으므로 정규화 없이 임의 포맷 입력 시 실패. 화자 구분 땐 정규화 유지
- 긴 오디오를 `--verbose`로 실행 → 출력 폭주
- 상대경로 입력 → 항상 절대경로 + 따옴표 사용
- 클로바 노트 요청을 이 스킬로 처리 → `uploading-to-clovanote` 사용
- **동일 `SPEAKER_XX` 라벨에 다중 화자 가능**: speakrs도 비슷한 톤·거리의 화자를 한 라벨로 묶을 수 있다. 자기소개 발화 1개로 라벨 전체를 한 사람으로 단정 금지. 같은 라벨 내 발화 스타일·역할·다른 참석자의 호칭 패턴이 일관되는지 교차 검증. 불확실하면 사용자에게 화자 매핑을 명시적으로 확인.
- **약어·조직명 정확도 의심**: 한국어 STT는 1~3음절 약어(TX/DX, CP1, AX 등)와 조직명에서 오류 빈도가 높다. 회의 내 소속 언급 구간의 약어가 맞는지 사용자에게 확인하거나 채널 과거 게시물에서 검증한다.
