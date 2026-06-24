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
_총 221회 · 고유 54종 · 데이터 기준 2026-06-24 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | transcribing-audio-locally | 17 |
| 2 | write-a-skill | 16 |
| 3 | frontend-design | 13 |
| 4 | text-visual-summary | 12 |
| 5 | daily-scrum-report | 10 |
| 6 | tdd | 10 |
| 7 | sharing-internal-html | 9 |
| 8 | handoff | 8 |
| 9 | miricanvas-design-system | 8 |
| 10 | posting-service-util-daily-scrum | 8 |
| 11 | tech-interview-questions | 8 |
| 12 | agent-browser | 7 |
| 13 | aidlc:aidlc-setup | 7 |
| 14 | commit | 7 |
| 15 | posting-to-slack-thread | 7 |
| 16 | teach | 5 |
| 17 | improve-codebase-architecture | 4 |
| 18 | to-issues | 4 |
| 19 | uploading-to-clovanote | 4 |
| 20 | axprod-issue | 3 |
| 21 | confluence-sync | 3 |
| 22 | find-skills | 3 |
| 23 | grill-me | 3 |
| 24 | superpowers:brainstorming | 3 |
| 25 | weekly-part-report | 3 |
| 26 | wiki-query | 3 |
| 27 | axprod-issue-sync | 2 |
| 28 | book-meeting-room | 2 |
| 29 | create-service-util-issue | 2 |
| 30 | intern-interview-questions | 2 |
| 31 | open-code-review:open-code-review | 2 |
| 32 | open-code-review:review | 2 |
| 33 | wiki-context | 2 |
| 34 | wiki-ingest | 2 |
| 35 | code-review-excellence | 1 |
| 36 | datadog:ddsetup | 1 |
| 37 | deep-research | 1 |
| 38 | isolating-fragment-work | 1 |
| 39 | miricanvas-staging-deploy | 1 |
| 40 | new-post | 1 |
| 41 | prd-code-reconcile | 1 |
| 42 | pull-request | 1 |
| 43 | service-util-daily-scrum-pipeline | 1 |
| 44 | session-ingest | 1 |
| 45 | speckit-constitution | 1 |
| 46 | speckit-implement | 1 |
| 47 | speckit-plan | 1 |
| 48 | speckit-specify | 1 |
| 49 | speckit-tasks | 1 |
| 50 | superpowers:systematic-debugging | 1 |
| 51 | superpowers:test-driven-development | 1 |
| 52 | superpowers:writing-skills | 1 |
| 53 | wiki-lint | 1 |
| 54 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
