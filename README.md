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
_총 1503회 · 고유 116종 · 데이터 기준 2026-08-18 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | agent-browser | 169 |
| 2 | handoff | 125 |
| 3 | wayfinder | 91 |
| 4 | frontend-design | 64 |
| 5 | mattpocock-skills:wayfinder | 55 |
| 6 | text-visual-summary | 55 |
| 7 | daily-scrum-report | 50 |
| 8 | hunk-review | 47 |
| 9 | figma-mockup | 45 |
| 10 | sharing-internal-html | 45 |
| 11 | mattpocock-skills:tdd | 42 |
| 12 | transcribing-audio-locally | 40 |
| 13 | mattpocock-skills:handoff | 38 |
| 14 | write-a-skill | 36 |
| 15 | service-util-daily-scrum-pipeline | 35 |
| 16 | tdd | 34 |
| 17 | commit | 29 |
| 18 | grilling | 23 |
| 19 | web2-architecture-map | 23 |
| 20 | posting-service-util-daily-scrum | 20 |
| 21 | emil-design-eng | 17 |
| 22 | page-spec | 17 |
| 23 | posting-to-slack-thread | 17 |
| 24 | hallmark | 15 |
| 25 | isolating-fragment-work | 14 |
| 26 | mattpocock-skills:grilling | 13 |
| 27 | mattpocock-skills:wait-what | 13 |
| 28 | mattpocock-skills:writing-great-skills | 12 |
| 29 | pr-create | 11 |
| 30 | service-util-pr-review | 11 |
| 31 | weekly-part-report | 11 |
| 32 | create-service-util-issue | 10 |
| 33 | prototype | 10 |
| 34 | superpowers:brainstorming | 10 |
| 35 | tech-interview-questions | 10 |
| 36 | book-meeting-room | 8 |
| 37 | meeting-pipeline | 8 |
| 38 | miricanvas-design-system | 8 |
| 39 | aidlc:aidlc-setup | 7 |
| 40 | axprod-issue | 7 |
| 41 | axprod-issue-sync | 7 |
| 42 | grill-me | 7 |
| 43 | grill-with-docs | 7 |
| 44 | wiki-ingest | 7 |
| 45 | axprod-weekly-meeting | 6 |
| 46 | find-skills | 6 |
| 47 | modern-css | 6 |
| 48 | wiki-query | 6 |
| 49 | acc | 5 |
| 50 | artifact-design | 5 |
| 51 | domain-modeling | 5 |
| 52 | mattpocock-skills:prototype | 5 |
| 53 | n8n-mcp-tools-expert | 5 |
| 54 | pull-request | 5 |
| 55 | teach | 5 |
| 56 | to-issues | 5 |
| 57 | axprod-meeting-minutes | 4 |
| 58 | code-review-excellence | 4 |
| 59 | dataviz | 4 |
| 60 | improve-codebase-architecture | 4 |
| 61 | mattpocock-skills:domain-modeling | 4 |
| 62 | superpowers:subagent-driven-development | 4 |
| 63 | superpowers:test-driven-development | 4 |
| 64 | uploading-to-clovanote | 4 |
| 65 | code-review | 3 |
| 66 | confluence-sync | 3 |
| 67 | mattpocock-skills:writing-for-agents | 3 |
| 68 | modularization-review-pipeline | 3 |
| 69 | open-code-review:open-code-review | 3 |
| 70 | refactor-private-public | 3 |
| 71 | schedule | 3 |
| 72 | session-ingest | 3 |
| 73 | update-config | 3 |
| 74 | wiki-context | 3 |
| 75 | apple-design | 2 |
| 76 | deep-research | 2 |
| 77 | intern-interview-questions | 2 |
| 78 | mattpocock-skills:grill-with-docs | 2 |
| 79 | mattpocock-skills:to-spec | 2 |
| 80 | miricanvas-production-deploy | 2 |
| 81 | miricanvas-staging-deploy | 2 |
| 82 | open-code-review:review | 2 |
| 83 | persona-builder | 2 |
| 84 | resolving-merge-conflicts | 2 |
| 85 | superpowers:systematic-debugging | 2 |
| 86 | superpowers:writing-plans | 2 |
| 87 | buzz-cli | 1 |
| 88 | claude-md-improver | 1 |
| 89 | create-storybook-story | 1 |
| 90 | datadog:ddsetup | 1 |
| 91 | ddd-study-pipeline | 1 |
| 92 | diagnose | 1 |
| 93 | doctori-book-pick | 1 |
| 94 | fix-pnpm-lockfile | 1 |
| 95 | frontend-lead-weekly-pipeline | 1 |
| 96 | loop | 1 |
| 97 | mattpocock-skills:to-tickets | 1 |
| 98 | new-post | 1 |
| 99 | ponytail:ponytail | 1 |
| 100 | prd-code-reconcile | 1 |
| 101 | research | 1 |
| 102 | review | 1 |
| 103 | service-util-issue-sync | 1 |
| 104 | share | 1 |
| 105 | skill-creator | 1 |
| 106 | speckit-constitution | 1 |
| 107 | speckit-implement | 1 |
| 108 | speckit-plan | 1 |
| 109 | speckit-specify | 1 |
| 110 | speckit-tasks | 1 |
| 111 | superpowers:writing-skills | 1 |
| 112 | to-prd | 1 |
| 113 | vitest | 1 |
| 114 | wiki-lint | 1 |
| 115 | write-spec | 1 |
| 116 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
