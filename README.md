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
_총 247회 · 고유 55종 · 데이터 기준 2026-06-26 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | write-a-skill | 22 |
| 2 | transcribing-audio-locally | 17 |
| 3 | frontend-design | 14 |
| 4 | text-visual-summary | 13 |
| 5 | daily-scrum-report | 12 |
| 6 | handoff | 12 |
| 7 | sharing-internal-html | 10 |
| 8 | tdd | 10 |
| 9 | tech-interview-questions | 9 |
| 10 | miricanvas-design-system | 8 |
| 11 | posting-service-util-daily-scrum | 8 |
| 12 | agent-browser | 7 |
| 13 | aidlc:aidlc-setup | 7 |
| 14 | commit | 7 |
| 15 | posting-to-slack-thread | 7 |
| 16 | teach | 5 |
| 17 | axprod-issue | 4 |
| 18 | axprod-issue-sync | 4 |
| 19 | find-skills | 4 |
| 20 | improve-codebase-architecture | 4 |
| 21 | to-issues | 4 |
| 22 | uploading-to-clovanote | 4 |
| 23 | wiki-query | 4 |
| 24 | book-meeting-room | 3 |
| 25 | code-review-excellence | 3 |
| 26 | confluence-sync | 3 |
| 27 | grill-me | 3 |
| 28 | open-code-review:open-code-review | 3 |
| 29 | superpowers:brainstorming | 3 |
| 30 | weekly-part-report | 3 |
| 31 | create-service-util-issue | 2 |
| 32 | intern-interview-questions | 2 |
| 33 | open-code-review:review | 2 |
| 34 | wiki-context | 2 |
| 35 | wiki-ingest | 2 |
| 36 | datadog:ddsetup | 1 |
| 37 | deep-research | 1 |
| 38 | isolating-fragment-work | 1 |
| 39 | miricanvas-staging-deploy | 1 |
| 40 | new-post | 1 |
| 41 | prd-code-reconcile | 1 |
| 42 | pull-request | 1 |
| 43 | service-util-daily-scrum-pipeline | 1 |
| 44 | service-util-issue-sync | 1 |
| 45 | session-ingest | 1 |
| 46 | speckit-constitution | 1 |
| 47 | speckit-implement | 1 |
| 48 | speckit-plan | 1 |
| 49 | speckit-specify | 1 |
| 50 | speckit-tasks | 1 |
| 51 | superpowers:systematic-debugging | 1 |
| 52 | superpowers:test-driven-development | 1 |
| 53 | superpowers:writing-skills | 1 |
| 54 | wiki-lint | 1 |
| 55 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
