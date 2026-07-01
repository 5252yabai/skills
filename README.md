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
| **frontend**      | frontend-design, seo-audit, vercel-react-best-practices, webgpu-best-practices                              |
| **git-pr**        | commit, pull-request, create-github-pull-request-from-specification, code-review-excellence                                              |
| **issue**         | to-issues, to-prd                                                                                                                                       |
| **learning**      | tutor, tutor-setup                                                                                                                                      |
| **meta**          | skill-creator, write-a-skill, find-skills, setup-matt-pocock-skills                                                                                     |
| **n8n**           | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **planning**      | grill-me, grill-with-docs, handoff, prototype                                                                                                           |
| **refactor**      | improve-codebase-architecture, refactor-humble-object, refactor-name, refactor-plan, refactor-private-public, refactor-test-name                        |
| **slack**         | posting-to-slack-thread                                                                                                                                 |
| **testing**       | tdd, vitest, diagnose                                                                      |
| **transcribe**    | transcribing-audio-locally, uploading-to-clovanote                                                                                                      |
| **wiki**          | wiki-context, wiki-query, session-ingest                                                                                                                |
| **miridih**       | (비공개 서브모듈)                                                                                                                                       |

<!-- SKILL-USAGE:START -->
## 스킬 사용 통계

<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->
_총 271회 · 고유 56종 · 데이터 기준 2026-07-01 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | write-a-skill | 24 |
| 2 | transcribing-audio-locally | 19 |
| 3 | frontend-design | 17 |
| 4 | text-visual-summary | 16 |
| 5 | daily-scrum-report | 14 |
| 6 | sharing-internal-html | 13 |
| 7 | handoff | 12 |
| 8 | tdd | 10 |
| 9 | posting-service-util-daily-scrum | 9 |
| 10 | tech-interview-questions | 9 |
| 11 | miricanvas-design-system | 8 |
| 12 | agent-browser | 7 |
| 13 | aidlc:aidlc-setup | 7 |
| 14 | commit | 7 |
| 15 | posting-to-slack-thread | 7 |
| 16 | axprod-issue | 5 |
| 17 | teach | 5 |
| 18 | axprod-issue-sync | 4 |
| 19 | book-meeting-room | 4 |
| 20 | code-review-excellence | 4 |
| 21 | find-skills | 4 |
| 22 | improve-codebase-architecture | 4 |
| 23 | to-issues | 4 |
| 24 | uploading-to-clovanote | 4 |
| 25 | weekly-part-report | 4 |
| 26 | wiki-query | 4 |
| 27 | confluence-sync | 3 |
| 28 | create-service-util-issue | 3 |
| 29 | grill-me | 3 |
| 30 | open-code-review:open-code-review | 3 |
| 31 | service-util-daily-scrum-pipeline | 3 |
| 32 | superpowers:brainstorming | 3 |
| 33 | intern-interview-questions | 2 |
| 34 | open-code-review:review | 2 |
| 35 | wiki-context | 2 |
| 36 | wiki-ingest | 2 |
| 37 | datadog:ddsetup | 1 |
| 38 | deep-research | 1 |
| 39 | isolating-fragment-work | 1 |
| 40 | miricanvas-staging-deploy | 1 |
| 41 | new-post | 1 |
| 42 | prd-code-reconcile | 1 |
| 43 | pull-request | 1 |
| 44 | service-util-issue-sync | 1 |
| 45 | service-util-pr-review | 1 |
| 46 | session-ingest | 1 |
| 47 | speckit-constitution | 1 |
| 48 | speckit-implement | 1 |
| 49 | speckit-plan | 1 |
| 50 | speckit-specify | 1 |
| 51 | speckit-tasks | 1 |
| 52 | superpowers:systematic-debugging | 1 |
| 53 | superpowers:test-driven-development | 1 |
| 54 | superpowers:writing-skills | 1 |
| 55 | wiki-lint | 1 |
| 56 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
