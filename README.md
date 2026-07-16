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
_총 581회 · 고유 75종 · 데이터 기준 2026-07-16 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 56 |
| 2 | transcribing-audio-locally | 36 |
| 3 | write-a-skill | 33 |
| 4 | wayfinder | 32 |
| 5 | frontend-design | 27 |
| 6 | agent-browser | 26 |
| 7 | daily-scrum-report | 25 |
| 8 | text-visual-summary | 25 |
| 9 | sharing-internal-html | 22 |
| 10 | tdd | 22 |
| 11 | web2-architecture-map | 22 |
| 12 | posting-service-util-daily-scrum | 17 |
| 13 | posting-to-slack-thread | 15 |
| 14 | commit | 14 |
| 15 | service-util-daily-scrum-pipeline | 11 |
| 16 | service-util-pr-review | 11 |
| 17 | isolating-fragment-work | 10 |
| 18 | tech-interview-questions | 9 |
| 19 | miricanvas-design-system | 8 |
| 20 | aidlc:aidlc-setup | 7 |
| 21 | axprod-issue-sync | 7 |
| 22 | book-meeting-room | 7 |
| 23 | grill-me | 7 |
| 24 | weekly-part-report | 7 |
| 25 | axprod-issue | 6 |
| 26 | find-skills | 6 |
| 27 | grilling | 6 |
| 28 | superpowers:brainstorming | 6 |
| 29 | wiki-ingest | 6 |
| 30 | create-service-util-issue | 5 |
| 31 | teach | 5 |
| 32 | code-review-excellence | 4 |
| 33 | improve-codebase-architecture | 4 |
| 34 | pull-request | 4 |
| 35 | superpowers:subagent-driven-development | 4 |
| 36 | to-issues | 4 |
| 37 | uploading-to-clovanote | 4 |
| 38 | wiki-query | 4 |
| 39 | code-review | 3 |
| 40 | confluence-sync | 3 |
| 41 | n8n-mcp-tools-expert | 3 |
| 42 | open-code-review:open-code-review | 3 |
| 43 | refactor-private-public | 3 |
| 44 | wiki-context | 3 |
| 45 | deep-research | 2 |
| 46 | intern-interview-questions | 2 |
| 47 | open-code-review:review | 2 |
| 48 | persona-builder | 2 |
| 49 | pr-create | 2 |
| 50 | schedule | 2 |
| 51 | session-ingest | 2 |
| 52 | superpowers:test-driven-development | 2 |
| 53 | artifact-design | 1 |
| 54 | claude-md-improver | 1 |
| 55 | datadog:ddsetup | 1 |
| 56 | domain-modeling | 1 |
| 57 | grill-with-docs | 1 |
| 58 | loop | 1 |
| 59 | miricanvas-staging-deploy | 1 |
| 60 | new-post | 1 |
| 61 | prd-code-reconcile | 1 |
| 62 | review | 1 |
| 63 | service-util-issue-sync | 1 |
| 64 | speckit-constitution | 1 |
| 65 | speckit-implement | 1 |
| 66 | speckit-plan | 1 |
| 67 | speckit-specify | 1 |
| 68 | speckit-tasks | 1 |
| 69 | superpowers:systematic-debugging | 1 |
| 70 | superpowers:writing-plans | 1 |
| 71 | superpowers:writing-skills | 1 |
| 72 | update-config | 1 |
| 73 | wiki-lint | 1 |
| 74 | write-spec | 1 |
| 75 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
