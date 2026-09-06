---
name: meeting-pipeline
description: 회의 녹음 하나를 전사→회의록→시각 HTML→(선택)업로드·슬랙 게시까지 처리하는 범용 파이프라인. 팀 전용 스크럼 스킬이 없는 회의에 사용. "이 회의 녹음 전사해서 정리해줘", "회의록 만들어서 시각화해줘" 류 요청, 또는 팀 전용 파이프라인 스킬이 프리셋 베이스로 참조할 때.
---

# 회의 파이프라인 (범용)

녹음 하나 → **전사 → 회의록 → 시각 HTML → (슬롯 있으면) 업로드 → 슬랙 게시**.
고정값 0개. 맥락은 전부 **슬롯으로 주입**받는다. 슬롯 비면 그 단계 스킵.

## 로컬 보관

작성 전에 `~/texts_wiki/AGENTS.md`의 "업무 산출물 저장 규칙"을 읽고 완료 기준까지 적용한다.

`~/texts_wiki/2.Wiki/deliverables/{조직·프로젝트}/{회의종류}/`에 날짜·주제별 회의록 md와 HTML을 보존한다. 조직·회의종류는 입력 맥락으로 정하고 불명확하면 사용자에게 확인한다.

## 슬롯

| 슬롯             | 필수 | 없으면                                                                  |
| ---------------- | ---- | ----------------------------------------------------------------------- |
| 오디오 경로      | ✔    | Voice Memos 최신 목록 보여주고 사용자 확인                              |
| 회의명·날짜      | ✔    | 오디오 제목·녹음 시각에서 추정, 사용자에게 한 줄 확인                   |
| 참석자           |      | 사용자가 명단 직접 주거나, 캘린더 이벤트 지정 시 참가자 추출. 추측 금지 |
| 화자 단서·용어집 |      | 매핑 불확실 → 회의록에 caveat 표시                                      |
| 업로드 경로      |      | 업로드 스킵                                                             |
| 슬랙 채널·멘션   |      | 슬랙 게시 스킵                                                          |

팀 전용 프리셋 스킬이 이 슬롯들을 채워서 호출해도 된다 (예: 서비스유틸 = service-util-daily-scrum-pipeline).

## 단계 위임

| 단계      | 위임 스킬                                    | 비고                                   |
| --------- | -------------------------------------------- | -------------------------------------- |
| 전사      | `transcribing-audio-locally`                 | `--no-diarize`, 백그라운드             |
| 회의록    | (이 스킬)                                    | 아래 형식                              |
| 시각화    | `text-visual-summary`                        | 회의록 md → 단일 HTML                  |
| 업로드    | `sharing-internal-html`                      | `<업로드 경로>/<회의날짜>.html`        |
| 슬랙 게시 | `posting-to-slack-thread`                    | 주입받은 채널·멘션 사용                |
| 이슈 후보 | `axprod-issue` / `create-service-util-issue` | AXProduction 업무 / 파트 업무로 라우팅 |

## Workflow

- [ ] **1. 슬롯 채우기** — 위 표 순서로 확인. 필수 둘 확정, 선택 슬롯은 있는 것만. 참석자를 캘린더에서 뽑을 땐 사용자가 지정한 이벤트만 조회.
  ```bash
  # 오디오 목록 (경로 없을 때)
  builtin cd ~/.claude/skills/transcribing-audio-locally/scripts/clovanote && uv run python -m clovanote_upload --list
  ```
- [ ] **2. 전사** — 백그라운드 실행, JSON+TXT 저장 완료까지.
  ```bash
  builtin cd ~/.claude/skills/transcribing-audio-locally/scripts/transcribe && \
    uv run python transcribe.py "<오디오 절대경로>" --no-diarize -o <out.txt> --json <out.json>
  ```
- [ ] **3. 회의록** — 전사문 전체 읽고 인물별 markdown. 화자 매핑은 내용 단서 + 참석자 슬롯으로. 불확실한 매핑·인물명·약어는 본문에 caveat로 남긴다. 수치·결정·미해결 항목 누락 없이.
- [ ] **4. 시각화** — `text-visual-summary`로 단일 HTML 생성, `verify-render.sh` 통과까지.
- [ ] **5. 업로드** _(슬롯 있을 때)_ — `sharing-internal-html`로 업로드, 사내 URL 확보.
- [ ] **6. 슬랙 게시 (유일한 승인 게이트)** _(슬롯 있을 때)_ — `posting-to-slack-thread` 패턴으로 톱+댓글 초안 작성, **사용자 승인 후** 게시. HTML URL 있으면 톱 제목 끝 `(<URL|시각요약>)`.
- [ ] **7. 이슈 후보 제안** _(액션 아이템 있을 때)_ — 업무 소속으로 라우팅: AXProduction 업무 → `axprod-issue`, 파트 업무 → `create-service-util-issue`. 각 스킬의 중복 검사 절차를 따라 후보별 제목/타입/담당자/중복 여부 표로 제시. **텍스트 제안만** — 생성은 사용자가 명시할 때. 기존 이슈와 중복이면 "기존 이슈에 귀속"으로 표시.

## 회의록 형식

```
<회의명> 회의록 (YYYY-MM-DD)
참석자: <주입받은 명단>

## <이름> — <주제>
- 불릿 요약 (간결체, 수치·결정·미해결 보존)

## 공통 논의 — <주제>
- 입장 + 결론
```

## 주의

- `cd` 실패(zoxide) → `builtin cd` 또는 절대경로.
- 전사 오류 잦음: 인물명·약어·제품명 의심되면 caveat. 화자가 쓴 용어 그대로 유지.
- 동일 HTML 재업로드는 기존 URL 반환(정상).
