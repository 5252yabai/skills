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
_총 1367회 · 고유 114종 · 데이터 기준 2026-08-13 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | agent-browser | 126 |
| 2 | handoff | 125 |
| 3 | wayfinder | 91 |
| 4 | frontend-design | 59 |
| 5 | mattpocock-skills:wayfinder | 50 |
| 6 | text-visual-summary | 50 |
| 7 | daily-scrum-report | 48 |
| 8 | hunk-review | 47 |
| 9 | figma-mockup | 45 |
| 10 | sharing-internal-html | 41 |
| 11 | transcribing-audio-locally | 40 |
| 12 | write-a-skill | 36 |
| 13 | mattpocock-skills:handoff | 35 |
| 14 | tdd | 34 |
| 15 | service-util-daily-scrum-pipeline | 32 |
| 16 | commit | 28 |
| 17 | grilling | 23 |
| 18 | web2-architecture-map | 23 |
| 19 | mattpocock-skills:tdd | 20 |
| 20 | posting-service-util-daily-scrum | 20 |
| 21 | emil-design-eng | 17 |
| 22 | page-spec | 17 |
| 23 | posting-to-slack-thread | 17 |
| 24 | isolating-fragment-work | 14 |
| 25 | mattpocock-skills:writing-great-skills | 12 |
| 26 | mattpocock-skills:grilling | 11 |
| 27 | pr-create | 11 |
| 28 | service-util-pr-review | 11 |
| 29 | weekly-part-report | 11 |
| 30 | create-service-util-issue | 10 |
| 31 | prototype | 10 |
| 32 | superpowers:brainstorming | 10 |
| 33 | tech-interview-questions | 10 |
| 34 | book-meeting-room | 8 |
| 35 | hallmark | 8 |
| 36 | miricanvas-design-system | 8 |
| 37 | aidlc:aidlc-setup | 7 |
| 38 | axprod-issue | 7 |
| 39 | axprod-issue-sync | 7 |
| 40 | grill-me | 7 |
| 41 | wiki-ingest | 7 |
| 42 | find-skills | 6 |
| 43 | grill-with-docs | 6 |
| 44 | wiki-query | 6 |
| 45 | domain-modeling | 5 |
| 46 | mattpocock-skills:prototype | 5 |
| 47 | mattpocock-skills:wait-what | 5 |
| 48 | n8n-mcp-tools-expert | 5 |
| 49 | pull-request | 5 |
| 50 | teach | 5 |
| 51 | to-issues | 5 |
| 52 | code-review-excellence | 4 |
| 53 | improve-codebase-architecture | 4 |
| 54 | modern-css | 4 |
| 55 | superpowers:subagent-driven-development | 4 |
| 56 | superpowers:test-driven-development | 4 |
| 57 | uploading-to-clovanote | 4 |
| 58 | artifact-design | 3 |
| 59 | axprod-meeting-minutes | 3 |
| 60 | code-review | 3 |
| 61 | confluence-sync | 3 |
| 62 | dataviz | 3 |
| 63 | meeting-pipeline | 3 |
| 64 | modularization-review-pipeline | 3 |
| 65 | open-code-review:open-code-review | 3 |
| 66 | refactor-private-public | 3 |
| 67 | schedule | 3 |
| 68 | session-ingest | 3 |
| 69 | update-config | 3 |
| 70 | wiki-context | 3 |
| 71 | apple-design | 2 |
| 72 | axprod-weekly-meeting | 2 |
| 73 | deep-research | 2 |
| 74 | intern-interview-questions | 2 |
| 75 | mattpocock-skills:domain-modeling | 2 |
| 76 | mattpocock-skills:grill-with-docs | 2 |
| 77 | mattpocock-skills:to-spec | 2 |
| 78 | miricanvas-production-deploy | 2 |
| 79 | miricanvas-staging-deploy | 2 |
| 80 | open-code-review:review | 2 |
| 81 | persona-builder | 2 |
| 82 | resolving-merge-conflicts | 2 |
| 83 | superpowers:systematic-debugging | 2 |
| 84 | superpowers:writing-plans | 2 |
| 85 | buzz-cli | 1 |
| 86 | claude-md-improver | 1 |
| 87 | create-storybook-story | 1 |
| 88 | datadog:ddsetup | 1 |
| 89 | ddd-study-pipeline | 1 |
| 90 | diagnose | 1 |
| 91 | doctori-book-pick | 1 |
| 92 | frontend-lead-weekly-pipeline | 1 |
| 93 | loop | 1 |
| 94 | mattpocock-skills:to-tickets | 1 |
| 95 | mattpocock-skills:writing-for-agents | 1 |
| 96 | new-post | 1 |
| 97 | ponytail:ponytail | 1 |
| 98 | prd-code-reconcile | 1 |
| 99 | research | 1 |
| 100 | review | 1 |
| 101 | service-util-issue-sync | 1 |
| 102 | share | 1 |
| 103 | skill-creator | 1 |
| 104 | speckit-constitution | 1 |
| 105 | speckit-implement | 1 |
| 106 | speckit-plan | 1 |
| 107 | speckit-specify | 1 |
| 108 | speckit-tasks | 1 |
| 109 | superpowers:writing-skills | 1 |
| 110 | to-prd | 1 |
| 111 | vitest | 1 |
| 112 | wiki-lint | 1 |
| 113 | write-spec | 1 |
| 114 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
