---
name: uploading-to-clovanote
description: Use ONLY when user explicitly mentions Clova Note (클로바 노트) or Naver's STT service. Uploads audio to Naver's cloud transcription service via local CLI. For any transcription request that does NOT mention Clova Note, use transcribing-audio-locally instead.
---

# 클로바 노트 업로드

## Overview

로컬 CLI(`~/scripts/clovanote/`)를 호출해 클로바 노트 웹에 오디오 파일을 업로드한다. 브라우저 자동화(`agent-browser` + CDP)로 동작하며, 첫 1회 수동 로그인 후 세션이 영속화된다.

## When to Use

트리거 예시 (**반드시 "클로바 노트" 명시가 있어야 한다**):

- "이 m4a 클로바 노트에 올려줘"
- "음성 파일 받아쓰기 해줘 / 클로바 노트에"
- "회의 녹음 클로바 노트로 처리해줘"
- "upload this recording to Clova Note"

지원 포맷: `.m4a` `.mp3` `.aac` `.amr` `.wav`

**When NOT to use:**

- "클로바 노트" 언급 없는 일반 전사/받아쓰기 요청 → `transcribing-audio-locally` 사용
- 다른 STT(Whisper, NCloud Speech API 등) 명시 → 해당 도구 사용

## Quick Reference

**파일 경로를 아는 경우:**

```bash
cd ~/scripts/clovanote && uv run python -m clovanote_upload "<절대경로>" [--name "<제목>"] [--headed]
```

**파일을 모르는 경우 — Voice Memos 목록 조회:**

```bash
cd ~/scripts/clovanote && uv run python -m clovanote_upload --list
```

출력 예시:

```
 1. 20260507 133159.m4a  20260507 daily  (14.8 MB)
 2. 20260507 090040.m4a  oma  (28.0 MB)
 ...
```

사용자가 Voice Memos 앱에서 지정한 제목을 함께 표시한다. 목록을 사용자에게 보여주고 선택을 받은 뒤 해당 파일의 절대 경로로 업로드.

업로드 시 `--name`을 생략하면 Voice Memos DB의 사용자 지정 제목이 자동으로 노트 제목으로 사용된다.

Voice Memos 경로: `~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/`

| 옵션            | 설명                                         |
| --------------- | -------------------------------------------- |
| `<절대경로>`    | 파일의 절대 경로 (따옴표 필수, 공백 포함 시) |
| `--list`        | Voice Memos 최근 10개 나열 후 종료           |
| `--name "제목"` | 노트 제목 (생략 시 파일명 사용)              |
| `--headed`      | 헤드드 브라우저 (첫 로그인 or 세션 만료 시)  |

## First-Time Setup

첫 실행은 반드시 `--headed`로:

```bash
cd ~/scripts/clovanote && uv run python -m clovanote_upload "/path/to/file.m4a" --headed
```

헤드드 Chrome이 열리면 **사용자가 직접 네이버 로그인**. 로그인 후 세션이 `~/.clovanote/` 프로필에 저장되어 이후 헤드리스로 동작한다.

## Error Recovery

`NotLoggedInError` 발생 → 세션 만료. 사용자에게 `--headed` 재실행 안내:

```bash
cd ~/scripts/clovanote && uv run python -m clovanote_upload "<파일>" --headed
# 브라우저에서 네이버 재로그인 → 이후 헤드리스 가능
```

**자동 로그인 시도 금지** — 네이버 봇 감지/캡차 위험.

## 업로드 완료 후

CLI 출력에서 `Note URL`을 추출해 사용자에게 링크를 제공한다:

```
Uploaded: 20260511 133109.m4a
Note URL: https://clovanote.naver.com/w/.../note-detail/...
```

변환은 비동기로 처리되므로 링크를 클릭하면 상세 페이지에서 진행 상태와 완료된 transcript를 확인할 수 있다.

## Limitations

- 동시 업로드 불가 (단일 `--session-name clovanote` 세션)
- 변환은 비동기 처리 — 완료 여부는 제공된 URL에서 직접 확인
