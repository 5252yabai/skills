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
_총 999회 · 고유 93종 · 데이터 기준 2026-07-30 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 123 |
| 2 | agent-browser | 102 |
| 3 | wayfinder | 91 |
| 4 | figma-mockup | 45 |
| 5 | transcribing-audio-locally | 39 |
| 6 | daily-scrum-report | 38 |
| 7 | frontend-design | 37 |
| 8 | write-a-skill | 36 |
| 9 | tdd | 31 |
| 10 | text-visual-summary | 31 |
| 11 | sharing-internal-html | 25 |
| 12 | grilling | 23 |
| 13 | web2-architecture-map | 23 |
| 14 | commit | 20 |
| 15 | posting-service-util-daily-scrum | 19 |
| 16 | page-spec | 17 |
| 17 | service-util-daily-scrum-pipeline | 16 |
| 18 | posting-to-slack-thread | 15 |
| 19 | hunk-review | 13 |
| 20 | isolating-fragment-work | 13 |
| 21 | service-util-pr-review | 11 |
| 22 | superpowers:brainstorming | 10 |
| 23 | tech-interview-questions | 10 |
| 24 | weekly-part-report | 9 |
| 25 | miricanvas-design-system | 8 |
| 26 | prototype | 8 |
| 27 | aidlc:aidlc-setup | 7 |
| 28 | axprod-issue-sync | 7 |
| 29 | book-meeting-room | 7 |
| 30 | grill-me | 7 |
| 31 | wiki-ingest | 7 |
| 32 | axprod-issue | 6 |
| 33 | emil-design-eng | 6 |
| 34 | find-skills | 6 |
| 35 | create-service-util-issue | 5 |
| 36 | domain-modeling | 5 |
| 37 | pr-create | 5 |
| 38 | pull-request | 5 |
| 39 | teach | 5 |
| 40 | to-issues | 5 |
| 41 | wiki-query | 5 |
| 42 | code-review-excellence | 4 |
| 43 | grill-with-docs | 4 |
| 44 | improve-codebase-architecture | 4 |
| 45 | n8n-mcp-tools-expert | 4 |
| 46 | superpowers:subagent-driven-development | 4 |
| 47 | superpowers:test-driven-development | 4 |
| 48 | uploading-to-clovanote | 4 |
| 49 | code-review | 3 |
| 50 | confluence-sync | 3 |
| 51 | open-code-review:open-code-review | 3 |
| 52 | refactor-private-public | 3 |
| 53 | schedule | 3 |
| 54 | wiki-context | 3 |
| 55 | dataviz | 2 |
| 56 | deep-research | 2 |
| 57 | intern-interview-questions | 2 |
| 58 | miricanvas-production-deploy | 2 |
| 59 | miricanvas-staging-deploy | 2 |
| 60 | modern-css | 2 |
| 61 | open-code-review:review | 2 |
| 62 | persona-builder | 2 |
| 63 | resolving-merge-conflicts | 2 |
| 64 | session-ingest | 2 |
| 65 | superpowers:systematic-debugging | 2 |
| 66 | superpowers:writing-plans | 2 |
| 67 | update-config | 2 |
| 68 | apple-design | 1 |
| 69 | artifact-design | 1 |
| 70 | axprod-meeting-minutes | 1 |
| 71 | axprod-weekly-meeting | 1 |
| 72 | buzz-cli | 1 |
| 73 | claude-md-improver | 1 |
| 74 | create-storybook-story | 1 |
| 75 | datadog:ddsetup | 1 |
| 76 | diagnose | 1 |
| 77 | doctori-book-pick | 1 |
| 78 | loop | 1 |
| 79 | new-post | 1 |
| 80 | prd-code-reconcile | 1 |
| 81 | research | 1 |
| 82 | review | 1 |
| 83 | service-util-issue-sync | 1 |
| 84 | speckit-constitution | 1 |
| 85 | speckit-implement | 1 |
| 86 | speckit-plan | 1 |
| 87 | speckit-specify | 1 |
| 88 | speckit-tasks | 1 |
| 89 | superpowers:writing-skills | 1 |
| 90 | to-prd | 1 |
| 91 | wiki-lint | 1 |
| 92 | write-spec | 1 |
| 93 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
