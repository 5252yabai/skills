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
_총 494회 · 고유 72종 · 데이터 기준 2026-07-15 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | transcribing-audio-locally | 36 |
| 2 | write-a-skill | 33 |
| 3 | handoff | 31 |
| 4 | frontend-design | 26 |
| 5 | daily-scrum-report | 25 |
| 6 | text-visual-summary | 24 |
| 7 | sharing-internal-html | 21 |
| 8 | web2-architecture-map | 21 |
| 9 | tdd | 19 |
| 10 | posting-service-util-daily-scrum | 16 |
| 11 | posting-to-slack-thread | 15 |
| 12 | agent-browser | 14 |
| 13 | commit | 12 |
| 14 | service-util-pr-review | 11 |
| 15 | isolating-fragment-work | 10 |
| 16 | service-util-daily-scrum-pipeline | 10 |
| 17 | tech-interview-questions | 9 |
| 18 | miricanvas-design-system | 8 |
| 19 | aidlc:aidlc-setup | 7 |
| 20 | axprod-issue-sync | 7 |
| 21 | book-meeting-room | 7 |
| 22 | grill-me | 7 |
| 23 | weekly-part-report | 7 |
| 24 | axprod-issue | 6 |
| 25 | superpowers:brainstorming | 6 |
| 26 | wiki-ingest | 6 |
| 27 | find-skills | 5 |
| 28 | teach | 5 |
| 29 | code-review-excellence | 4 |
| 30 | create-service-util-issue | 4 |
| 31 | grilling | 4 |
| 32 | improve-codebase-architecture | 4 |
| 33 | pull-request | 4 |
| 34 | superpowers:subagent-driven-development | 4 |
| 35 | to-issues | 4 |
| 36 | uploading-to-clovanote | 4 |
| 37 | wiki-query | 4 |
| 38 | code-review | 3 |
| 39 | confluence-sync | 3 |
| 40 | n8n-mcp-tools-expert | 3 |
| 41 | open-code-review:open-code-review | 3 |
| 42 | refactor-private-public | 3 |
| 43 | wiki-context | 3 |
| 44 | intern-interview-questions | 2 |
| 45 | open-code-review:review | 2 |
| 46 | persona-builder | 2 |
| 47 | schedule | 2 |
| 48 | session-ingest | 2 |
| 49 | superpowers:test-driven-development | 2 |
| 50 | wayfinder | 2 |
| 51 | datadog:ddsetup | 1 |
| 52 | deep-research | 1 |
| 53 | domain-modeling | 1 |
| 54 | grill-with-docs | 1 |
| 55 | loop | 1 |
| 56 | miricanvas-staging-deploy | 1 |
| 57 | new-post | 1 |
| 58 | prd-code-reconcile | 1 |
| 59 | review | 1 |
| 60 | service-util-issue-sync | 1 |
| 61 | speckit-constitution | 1 |
| 62 | speckit-implement | 1 |
| 63 | speckit-plan | 1 |
| 64 | speckit-specify | 1 |
| 65 | speckit-tasks | 1 |
| 66 | superpowers:systematic-debugging | 1 |
| 67 | superpowers:writing-plans | 1 |
| 68 | superpowers:writing-skills | 1 |
| 69 | update-config | 1 |
| 70 | wiki-lint | 1 |
| 71 | write-spec | 1 |
| 72 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
