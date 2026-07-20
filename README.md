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
_총 765회 · 고유 78종 · 데이터 기준 2026-07-20 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | handoff | 106 |
| 2 | agent-browser | 65 |
| 3 | wayfinder | 62 |
| 4 | transcribing-audio-locally | 36 |
| 5 | write-a-skill | 36 |
| 6 | figma-mockup | 28 |
| 7 | frontend-design | 28 |
| 8 | daily-scrum-report | 27 |
| 9 | text-visual-summary | 25 |
| 10 | sharing-internal-html | 22 |
| 11 | tdd | 22 |
| 12 | web2-architecture-map | 22 |
| 13 | page-spec | 17 |
| 14 | posting-service-util-daily-scrum | 17 |
| 15 | posting-to-slack-thread | 15 |
| 16 | commit | 14 |
| 17 | grilling | 12 |
| 18 | service-util-daily-scrum-pipeline | 11 |
| 19 | service-util-pr-review | 11 |
| 20 | isolating-fragment-work | 10 |
| 21 | tech-interview-questions | 9 |
| 22 | miricanvas-design-system | 8 |
| 23 | aidlc:aidlc-setup | 7 |
| 24 | axprod-issue-sync | 7 |
| 25 | book-meeting-room | 7 |
| 26 | grill-me | 7 |
| 27 | weekly-part-report | 7 |
| 28 | axprod-issue | 6 |
| 29 | find-skills | 6 |
| 30 | superpowers:brainstorming | 6 |
| 31 | wiki-ingest | 6 |
| 32 | create-service-util-issue | 5 |
| 33 | pull-request | 5 |
| 34 | teach | 5 |
| 35 | code-review-excellence | 4 |
| 36 | improve-codebase-architecture | 4 |
| 37 | n8n-mcp-tools-expert | 4 |
| 38 | superpowers:subagent-driven-development | 4 |
| 39 | to-issues | 4 |
| 40 | uploading-to-clovanote | 4 |
| 41 | wiki-query | 4 |
| 42 | code-review | 3 |
| 43 | confluence-sync | 3 |
| 44 | domain-modeling | 3 |
| 45 | grill-with-docs | 3 |
| 46 | open-code-review:open-code-review | 3 |
| 47 | refactor-private-public | 3 |
| 48 | schedule | 3 |
| 49 | wiki-context | 3 |
| 50 | deep-research | 2 |
| 51 | intern-interview-questions | 2 |
| 52 | open-code-review:review | 2 |
| 53 | persona-builder | 2 |
| 54 | pr-create | 2 |
| 55 | session-ingest | 2 |
| 56 | superpowers:test-driven-development | 2 |
| 57 | artifact-design | 1 |
| 58 | claude-md-improver | 1 |
| 59 | datadog:ddsetup | 1 |
| 60 | diagnose | 1 |
| 61 | loop | 1 |
| 62 | miricanvas-staging-deploy | 1 |
| 63 | new-post | 1 |
| 64 | prd-code-reconcile | 1 |
| 65 | review | 1 |
| 66 | service-util-issue-sync | 1 |
| 67 | speckit-constitution | 1 |
| 68 | speckit-implement | 1 |
| 69 | speckit-plan | 1 |
| 70 | speckit-specify | 1 |
| 71 | speckit-tasks | 1 |
| 72 | superpowers:systematic-debugging | 1 |
| 73 | superpowers:writing-plans | 1 |
| 74 | superpowers:writing-skills | 1 |
| 75 | update-config | 1 |
| 76 | wiki-lint | 1 |
| 77 | write-spec | 1 |
| 78 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
