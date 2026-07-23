# skills

코딩 에이전트 [Skills](https://agentskills.my/specification/) 모음. 의미 그룹별 폴더로 정리되어 있다.

## 사용법

```bash
git clone --recurse-submodules https://github.com/5252yabai/skills.git
```

각 스킬은 `SKILL.md`를 가진 폴더다. 코딩 에이전트의 스킬 디렉토리(`~/.claude/skills` 등)로 심볼릭 링크해 사용한다. `link-skill.sh`가 링크를 돕는다 (그룹 단위 지원).

> `miridih/`는 비공개 서브모듈(회사 전용 스킬)이라 권한이 없으면 빈 폴더로 보인다. 나머지는 모두 공개 범용 스킬이다.

## 그룹

| 그룹              | 스킬                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **agent-browser** | 브라우저 자동화 에이전트                                                                                                                                |
| **frontend**      | frontend-design, seo-audit, vercel-react-best-practices, webgpu-best-practices                                                                          |
| **git-pr**        | commit, pull-request, create-github-pull-request-from-specification, code-review-2axis, resolving-merge-conflicts                                       |
| **issue**         | to-issues, to-prd, triage                                                                                                                               |
| **learning**      | tutor, tutor-setup                                                                                                                                      |
| **meta**          | skill-creator, write-a-skill, find-skills, setup-matt-pocock-skills                                                                                     |
| **n8n**           | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **planning**      | grill-me, grill-with-docs, grilling, domain-modeling, handoff, prototype, implement, research                                                           |
| **refactor**      | improve-codebase-architecture, codebase-design, refactor-humble-object, refactor-name, refactor-private-public, refactor-test-name                      |
| **slack**         | posting-to-slack-thread                                                                                                                                 |
| **testing**       | tdd, vitest, diagnose                                                                                                                                   |
| **transcribe**    | transcribing-audio-locally, uploading-to-clovanote                                                                                                      |
| **wiki**          | wiki-context, wiki-query, session-ingest, persona-builder                                                                                               |
| **miridih**       | (비공개 서브모듈)                                                                                                                                       |

<!-- SKILL-USAGE:START -->
## 스킬 사용 통계

<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->
_총 850회 · 고유 84종 · 데이터 기준 2026-07-23 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 115 |
| 2 | agent-browser | 77 |
| 3 | wayfinder | 72 |
| 4 | transcribing-audio-locally | 37 |
| 5 | figma-mockup | 36 |
| 6 | write-a-skill | 36 |
| 7 | daily-scrum-report | 30 |
| 8 | frontend-design | 30 |
| 9 | text-visual-summary | 27 |
| 10 | sharing-internal-html | 24 |
| 11 | web2-architecture-map | 23 |
| 12 | tdd | 22 |
| 13 | grilling | 20 |
| 14 | posting-service-util-daily-scrum | 19 |
| 15 | page-spec | 17 |
| 16 | commit | 16 |
| 17 | posting-to-slack-thread | 15 |
| 18 | service-util-daily-scrum-pipeline | 13 |
| 19 | service-util-pr-review | 11 |
| 20 | isolating-fragment-work | 10 |
| 21 | tech-interview-questions | 10 |
| 22 | miricanvas-design-system | 8 |
| 23 | superpowers:brainstorming | 8 |
| 24 | weekly-part-report | 8 |
| 25 | aidlc:aidlc-setup | 7 |
| 26 | axprod-issue-sync | 7 |
| 27 | book-meeting-room | 7 |
| 28 | grill-me | 7 |
| 29 | wiki-ingest | 7 |
| 30 | axprod-issue | 6 |
| 31 | find-skills | 6 |
| 32 | create-service-util-issue | 5 |
| 33 | pull-request | 5 |
| 34 | teach | 5 |
| 35 | wiki-query | 5 |
| 36 | code-review-excellence | 4 |
| 37 | domain-modeling | 4 |
| 38 | grill-with-docs | 4 |
| 39 | improve-codebase-architecture | 4 |
| 40 | n8n-mcp-tools-expert | 4 |
| 41 | superpowers:subagent-driven-development | 4 |
| 42 | to-issues | 4 |
| 43 | uploading-to-clovanote | 4 |
| 44 | code-review | 3 |
| 45 | confluence-sync | 3 |
| 46 | open-code-review:open-code-review | 3 |
| 47 | pr-create | 3 |
| 48 | prototype | 3 |
| 49 | refactor-private-public | 3 |
| 50 | schedule | 3 |
| 51 | superpowers:test-driven-development | 3 |
| 52 | wiki-context | 3 |
| 53 | deep-research | 2 |
| 54 | intern-interview-questions | 2 |
| 55 | miricanvas-production-deploy | 2 |
| 56 | miricanvas-staging-deploy | 2 |
| 57 | open-code-review:review | 2 |
| 58 | persona-builder | 2 |
| 59 | resolving-merge-conflicts | 2 |
| 60 | session-ingest | 2 |
| 61 | artifact-design | 1 |
| 62 | buzz-cli | 1 |
| 63 | claude-md-improver | 1 |
| 64 | datadog:ddsetup | 1 |
| 65 | diagnose | 1 |
| 66 | doctori-book-pick | 1 |
| 67 | loop | 1 |
| 68 | new-post | 1 |
| 69 | prd-code-reconcile | 1 |
| 70 | review | 1 |
| 71 | service-util-issue-sync | 1 |
| 72 | speckit-constitution | 1 |
| 73 | speckit-implement | 1 |
| 74 | speckit-plan | 1 |
| 75 | speckit-specify | 1 |
| 76 | speckit-tasks | 1 |
| 77 | superpowers:systematic-debugging | 1 |
| 78 | superpowers:writing-plans | 1 |
| 79 | superpowers:writing-skills | 1 |
| 80 | to-prd | 1 |
| 81 | update-config | 1 |
| 82 | wiki-lint | 1 |
| 83 | write-spec | 1 |
| 84 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
