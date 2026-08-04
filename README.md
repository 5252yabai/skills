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
_총 1078회 · 고유 102종 · 데이터 기준 2026-08-04 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 124 |
| 2 | agent-browser | 107 |
| 3 | wayfinder | 91 |
| 4 | figma-mockup | 45 |
| 5 | frontend-design | 42 |
| 6 | daily-scrum-report | 41 |
| 7 | transcribing-audio-locally | 40 |
| 8 | text-visual-summary | 36 |
| 9 | write-a-skill | 36 |
| 10 | tdd | 32 |
| 11 | sharing-internal-html | 31 |
| 12 | hunk-review | 26 |
| 13 | grilling | 23 |
| 14 | web2-architecture-map | 23 |
| 15 | commit | 21 |
| 16 | service-util-daily-scrum-pipeline | 21 |
| 17 | posting-service-util-daily-scrum | 19 |
| 18 | page-spec | 17 |
| 19 | posting-to-slack-thread | 15 |
| 20 | isolating-fragment-work | 13 |
| 21 | service-util-pr-review | 11 |
| 22 | superpowers:brainstorming | 10 |
| 23 | tech-interview-questions | 10 |
| 24 | emil-design-eng | 9 |
| 25 | weekly-part-report | 9 |
| 26 | mattpocock-skills:wayfinder | 8 |
| 27 | miricanvas-design-system | 8 |
| 28 | prototype | 8 |
| 29 | aidlc:aidlc-setup | 7 |
| 30 | axprod-issue-sync | 7 |
| 31 | book-meeting-room | 7 |
| 32 | grill-me | 7 |
| 33 | wiki-ingest | 7 |
| 34 | axprod-issue | 6 |
| 35 | create-service-util-issue | 6 |
| 36 | find-skills | 6 |
| 37 | pr-create | 6 |
| 38 | wiki-query | 6 |
| 39 | domain-modeling | 5 |
| 40 | mattpocock-skills:tdd | 5 |
| 41 | n8n-mcp-tools-expert | 5 |
| 42 | pull-request | 5 |
| 43 | teach | 5 |
| 44 | to-issues | 5 |
| 45 | code-review-excellence | 4 |
| 46 | grill-with-docs | 4 |
| 47 | improve-codebase-architecture | 4 |
| 48 | superpowers:subagent-driven-development | 4 |
| 49 | superpowers:test-driven-development | 4 |
| 50 | uploading-to-clovanote | 4 |
| 51 | code-review | 3 |
| 52 | confluence-sync | 3 |
| 53 | mattpocock-skills:writing-great-skills | 3 |
| 54 | open-code-review:open-code-review | 3 |
| 55 | refactor-private-public | 3 |
| 56 | schedule | 3 |
| 57 | session-ingest | 3 |
| 58 | wiki-context | 3 |
| 59 | artifact-design | 2 |
| 60 | axprod-meeting-minutes | 2 |
| 61 | dataviz | 2 |
| 62 | deep-research | 2 |
| 63 | intern-interview-questions | 2 |
| 64 | mattpocock-skills:handoff | 2 |
| 65 | miricanvas-production-deploy | 2 |
| 66 | miricanvas-staging-deploy | 2 |
| 67 | modern-css | 2 |
| 68 | open-code-review:review | 2 |
| 69 | persona-builder | 2 |
| 70 | resolving-merge-conflicts | 2 |
| 71 | superpowers:systematic-debugging | 2 |
| 72 | superpowers:writing-plans | 2 |
| 73 | update-config | 2 |
| 74 | apple-design | 1 |
| 75 | axprod-weekly-meeting | 1 |
| 76 | buzz-cli | 1 |
| 77 | claude-md-improver | 1 |
| 78 | create-storybook-story | 1 |
| 79 | datadog:ddsetup | 1 |
| 80 | diagnose | 1 |
| 81 | doctori-book-pick | 1 |
| 82 | loop | 1 |
| 83 | mattpocock-skills:grilling | 1 |
| 84 | mattpocock-skills:prototype | 1 |
| 85 | new-post | 1 |
| 86 | prd-code-reconcile | 1 |
| 87 | research | 1 |
| 88 | review | 1 |
| 89 | service-util-issue-sync | 1 |
| 90 | share | 1 |
| 91 | skill-creator | 1 |
| 92 | speckit-constitution | 1 |
| 93 | speckit-implement | 1 |
| 94 | speckit-plan | 1 |
| 95 | speckit-specify | 1 |
| 96 | speckit-tasks | 1 |
| 97 | superpowers:writing-skills | 1 |
| 98 | to-prd | 1 |
| 99 | vitest | 1 |
| 100 | wiki-lint | 1 |
| 101 | write-spec | 1 |
| 102 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
