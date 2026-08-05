# skills

코딩 에이전트 [Skills](https://agentskills.my/specification/) 모음. 의미 그룹별 폴더로 정리되어 있다.

## 사용법

```bash
git clone --recurse-submodules https://github.com/5252yabai/skills.git
```

각 스킬은 `SKILL.md`를 가진 폴더다. 코딩 에이전트의 스킬 디렉토리(`~/.claude/skills` 등)로 심볼릭 링크해 사용한다. `link-skill.sh`가 링크를 돕는다 (그룹 단위 지원).

> `miridih/`는 비공개 서브모듈(회사 전용 스킬)이라 권한이 없으면 빈 폴더로 보인다. 나머지는 모두 공개 범용 스킬이다.

> Matt Pocock 스킬(grilling, tdd, handoff, wayfinder, to-spec, code-review 등)은 여기서 관리하지 않는다. `mattpocock-skills` 플러그인(마켓플레이스 `mattpocock/skills`)을 쓴다.

## 그룹

| 그룹              | 스킬                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **agent-browser** | 브라우저 자동화 에이전트                                                                                                                                |
| **frontend**      | frontend-design, seo-audit, vercel-react-best-practices, webgpu-best-practices                                                                          |
| **git-pr**        | commit, pull-request, create-github-pull-request-from-specification                                                                                     |
| **learning**      | tutor, tutor-setup                                                                                                                                      |
| **meta**          | skill-creator, find-skills                                                                                                                              |
| **n8n**           | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **planning**      | orchestrate                                                                                                                                             |
| **refactor**      | refactor-humble-object, refactor-name, refactor-private-public, refactor-test-name                                                                      |
| **slack**         | posting-to-slack-thread                                                                                                                                 |
| **testing**       | vitest                                                                                                                                                  |
| **transcribe**    | transcribing-audio-locally, uploading-to-clovanote                                                                                                      |
| **wiki**          | wiki-context, wiki-query, session-ingest, persona-builder                                                                                               |
| **miridih**       | (비공개 서브모듈)                                                                                                                                       |

<!-- SKILL-USAGE:START -->
## 스킬 사용 통계

<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->
_총 1136회 · 고유 103종 · 데이터 기준 2026-08-05 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 124 |
| 2 | agent-browser | 114 |
| 3 | wayfinder | 91 |
| 4 | figma-mockup | 45 |
| 5 | frontend-design | 45 |
| 6 | daily-scrum-report | 41 |
| 7 | transcribing-audio-locally | 40 |
| 8 | text-visual-summary | 36 |
| 9 | write-a-skill | 36 |
| 10 | tdd | 32 |
| 11 | sharing-internal-html | 31 |
| 12 | hunk-review | 29 |
| 13 | commit | 23 |
| 14 | grilling | 23 |
| 15 | web2-architecture-map | 23 |
| 16 | service-util-daily-scrum-pipeline | 21 |
| 17 | mattpocock-skills:wayfinder | 20 |
| 18 | posting-service-util-daily-scrum | 19 |
| 19 | page-spec | 17 |
| 20 | posting-to-slack-thread | 15 |
| 21 | emil-design-eng | 13 |
| 22 | isolating-fragment-work | 13 |
| 23 | service-util-pr-review | 11 |
| 24 | mattpocock-skills:handoff | 10 |
| 25 | superpowers:brainstorming | 10 |
| 26 | tech-interview-questions | 10 |
| 27 | weekly-part-report | 10 |
| 28 | mattpocock-skills:tdd | 9 |
| 29 | miricanvas-design-system | 8 |
| 30 | pr-create | 8 |
| 31 | prototype | 8 |
| 32 | aidlc:aidlc-setup | 7 |
| 33 | axprod-issue-sync | 7 |
| 34 | book-meeting-room | 7 |
| 35 | create-service-util-issue | 7 |
| 36 | grill-me | 7 |
| 37 | wiki-ingest | 7 |
| 38 | axprod-issue | 6 |
| 39 | find-skills | 6 |
| 40 | wiki-query | 6 |
| 41 | domain-modeling | 5 |
| 42 | mattpocock-skills:grilling | 5 |
| 43 | mattpocock-skills:writing-great-skills | 5 |
| 44 | n8n-mcp-tools-expert | 5 |
| 45 | pull-request | 5 |
| 46 | teach | 5 |
| 47 | to-issues | 5 |
| 48 | code-review-excellence | 4 |
| 49 | grill-with-docs | 4 |
| 50 | improve-codebase-architecture | 4 |
| 51 | mattpocock-skills:prototype | 4 |
| 52 | superpowers:subagent-driven-development | 4 |
| 53 | superpowers:test-driven-development | 4 |
| 54 | uploading-to-clovanote | 4 |
| 55 | code-review | 3 |
| 56 | confluence-sync | 3 |
| 57 | open-code-review:open-code-review | 3 |
| 58 | refactor-private-public | 3 |
| 59 | schedule | 3 |
| 60 | session-ingest | 3 |
| 61 | wiki-context | 3 |
| 62 | apple-design | 2 |
| 63 | artifact-design | 2 |
| 64 | axprod-meeting-minutes | 2 |
| 65 | dataviz | 2 |
| 66 | deep-research | 2 |
| 67 | intern-interview-questions | 2 |
| 68 | miricanvas-production-deploy | 2 |
| 69 | miricanvas-staging-deploy | 2 |
| 70 | modern-css | 2 |
| 71 | open-code-review:review | 2 |
| 72 | persona-builder | 2 |
| 73 | resolving-merge-conflicts | 2 |
| 74 | superpowers:systematic-debugging | 2 |
| 75 | superpowers:writing-plans | 2 |
| 76 | update-config | 2 |
| 77 | axprod-weekly-meeting | 1 |
| 78 | buzz-cli | 1 |
| 79 | claude-md-improver | 1 |
| 80 | create-storybook-story | 1 |
| 81 | datadog:ddsetup | 1 |
| 82 | diagnose | 1 |
| 83 | doctori-book-pick | 1 |
| 84 | loop | 1 |
| 85 | new-post | 1 |
| 86 | ponytail:ponytail | 1 |
| 87 | prd-code-reconcile | 1 |
| 88 | research | 1 |
| 89 | review | 1 |
| 90 | service-util-issue-sync | 1 |
| 91 | share | 1 |
| 92 | skill-creator | 1 |
| 93 | speckit-constitution | 1 |
| 94 | speckit-implement | 1 |
| 95 | speckit-plan | 1 |
| 96 | speckit-specify | 1 |
| 97 | speckit-tasks | 1 |
| 98 | superpowers:writing-skills | 1 |
| 99 | to-prd | 1 |
| 100 | vitest | 1 |
| 101 | wiki-lint | 1 |
| 102 | write-spec | 1 |
| 103 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
