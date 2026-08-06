# skills

코딩 에이전트 [Skills](https://agentskills.my/specification/) 모음. 의미 그룹별 폴더로 정리되어 있다.

## 사용법

```bash
git clone --recurse-submodules https://github.com/5252yabai/skills.git
```

각 스킬은 `SKILL.md`를 가진 폴더다. 코딩 에이전트의 스킬 디렉토리(`~/.claude/skills` 등)로 심볼릭 링크해 사용한다. `link-skill.sh`가 링크를 돕는다 (그룹 단위 지원).

> `miridih/`는 비공개 서브모듈(회사 전용 스킬)이라 권한이 없으면 빈 폴더로 보인다. 나머지는 모두 공개 범용 스킬이다.

> Matt Pocock 스킬(grilling, tdd, handoff, wayfinder, to-spec, code-review 등)은 여기서 관리하지 않는다. `mattpocock-skills` 플러그인(마켓플레이스 `mattpocock/skills`)을 쓴다.

### description은 상시 비용이다

링크된 스킬의 `description`은 매 세션 컨텍스트에 실린다(본문은 호출될 때만). 한 주제에 스킬을 여러 개 두면 그만큼 고정 지출이 늘어난다. **관련 스킬은 진입점 하나 + `references/` 구조로 묶는다** — `n8n/`이 그 예다(7종 통합, 1,475 → 147 토큰).

사용 실적은 아래 통계표와 `~/.rig/usage.jsonl`로 확인한다. 안 쓰는 스킬은 링크를 끊거나 삭제한다.

## 그룹

| 그룹              | 스킬                                                                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **agent-browser** | 브라우저 자동화 에이전트                                                                                                                      |
| **frontend**      | frontend-design, seo-audit, vercel-react-best-practices, webgpu-best-practices                                                                |
| **git-pr**        | commit, pull-request                                                                                                                          |
| **learning**      | tutor, tutor-setup                                                                                                                            |
| **meta**          | skill-creator, find-skills                                                                                                                    |
| **n8n**           | 단일 스킬 + `references/` 7종 (mcp-tools, workflow-patterns, node-configuration, expression-syntax, code-javascript, code-python, validation) |
| **slack**         | posting-to-slack-thread                                                                                                                       |
| **testing**       | vitest                                                                                                                                        |
| **transcribe**    | transcribing-audio-locally                                                                                                                    |
| **wiki**          | wiki-context, wiki-query, session-ingest                                                                                                      |
| **miridih**       | (비공개 서브모듈)                                                                                                                             |

<!-- SKILL-USAGE:START -->
## 스킬 사용 통계

<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->
_총 1189회 · 고유 107종 · 데이터 기준 2026-08-05 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 124 |
| 2 | agent-browser | 121 |
| 3 | wayfinder | 91 |
| 4 | frontend-design | 46 |
| 5 | figma-mockup | 45 |
| 6 | daily-scrum-report | 42 |
| 7 | transcribing-audio-locally | 40 |
| 8 | text-visual-summary | 37 |
| 9 | write-a-skill | 36 |
| 10 | hunk-review | 34 |
| 11 | tdd | 32 |
| 12 | sharing-internal-html | 31 |
| 13 | commit | 27 |
| 14 | mattpocock-skills:wayfinder | 24 |
| 15 | grilling | 23 |
| 16 | service-util-daily-scrum-pipeline | 23 |
| 17 | web2-architecture-map | 23 |
| 18 | posting-service-util-daily-scrum | 19 |
| 19 | page-spec | 17 |
| 20 | emil-design-eng | 16 |
| 21 | mattpocock-skills:handoff | 16 |
| 22 | posting-to-slack-thread | 15 |
| 23 | isolating-fragment-work | 13 |
| 24 | mattpocock-skills:tdd | 12 |
| 25 | service-util-pr-review | 11 |
| 26 | create-service-util-issue | 10 |
| 27 | superpowers:brainstorming | 10 |
| 28 | tech-interview-questions | 10 |
| 29 | weekly-part-report | 10 |
| 30 | pr-create | 9 |
| 31 | miricanvas-design-system | 8 |
| 32 | prototype | 8 |
| 33 | aidlc:aidlc-setup | 7 |
| 34 | axprod-issue-sync | 7 |
| 35 | book-meeting-room | 7 |
| 36 | grill-me | 7 |
| 37 | mattpocock-skills:grilling | 7 |
| 38 | mattpocock-skills:writing-great-skills | 7 |
| 39 | wiki-ingest | 7 |
| 40 | axprod-issue | 6 |
| 41 | find-skills | 6 |
| 42 | wiki-query | 6 |
| 43 | domain-modeling | 5 |
| 44 | grill-with-docs | 5 |
| 45 | n8n-mcp-tools-expert | 5 |
| 46 | pull-request | 5 |
| 47 | teach | 5 |
| 48 | to-issues | 5 |
| 49 | code-review-excellence | 4 |
| 50 | improve-codebase-architecture | 4 |
| 51 | mattpocock-skills:prototype | 4 |
| 52 | superpowers:subagent-driven-development | 4 |
| 53 | superpowers:test-driven-development | 4 |
| 54 | uploading-to-clovanote | 4 |
| 55 | artifact-design | 3 |
| 56 | code-review | 3 |
| 57 | confluence-sync | 3 |
| 58 | open-code-review:open-code-review | 3 |
| 59 | refactor-private-public | 3 |
| 60 | schedule | 3 |
| 61 | session-ingest | 3 |
| 62 | update-config | 3 |
| 63 | wiki-context | 3 |
| 64 | apple-design | 2 |
| 65 | axprod-meeting-minutes | 2 |
| 66 | dataviz | 2 |
| 67 | deep-research | 2 |
| 68 | intern-interview-questions | 2 |
| 69 | mattpocock-skills:to-spec | 2 |
| 70 | miricanvas-production-deploy | 2 |
| 71 | miricanvas-staging-deploy | 2 |
| 72 | modern-css | 2 |
| 73 | open-code-review:review | 2 |
| 74 | persona-builder | 2 |
| 75 | resolving-merge-conflicts | 2 |
| 76 | superpowers:systematic-debugging | 2 |
| 77 | superpowers:writing-plans | 2 |
| 78 | axprod-weekly-meeting | 1 |
| 79 | buzz-cli | 1 |
| 80 | claude-md-improver | 1 |
| 81 | create-storybook-story | 1 |
| 82 | datadog:ddsetup | 1 |
| 83 | diagnose | 1 |
| 84 | doctori-book-pick | 1 |
| 85 | loop | 1 |
| 86 | mattpocock-skills:domain-modeling | 1 |
| 87 | mattpocock-skills:grill-with-docs | 1 |
| 88 | mattpocock-skills:to-tickets | 1 |
| 89 | new-post | 1 |
| 90 | ponytail:ponytail | 1 |
| 91 | prd-code-reconcile | 1 |
| 92 | research | 1 |
| 93 | review | 1 |
| 94 | service-util-issue-sync | 1 |
| 95 | share | 1 |
| 96 | skill-creator | 1 |
| 97 | speckit-constitution | 1 |
| 98 | speckit-implement | 1 |
| 99 | speckit-plan | 1 |
| 100 | speckit-specify | 1 |
| 101 | speckit-tasks | 1 |
| 102 | superpowers:writing-skills | 1 |
| 103 | to-prd | 1 |
| 104 | vitest | 1 |
| 105 | wiki-lint | 1 |
| 106 | write-spec | 1 |
| 107 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
