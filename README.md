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
_총 130회 · 고유 45종 · 데이터 기준 2026-06-17 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | tdd | 10 |
| 2 | transcribing-audio-locally | 9 |
| 3 | write-a-skill | 9 |
| 4 | handoff | 7 |
| 5 | miricanvas-design-system | 7 |
| 6 | tech-interview-questions | 7 |
| 7 | commit | 6 |
| 8 | daily-scrum-report | 5 |
| 9 | posting-service-util-daily-scrum | 5 |
| 10 | teach | 5 |
| 11 | agent-browser | 4 |
| 12 | improve-codebase-architecture | 4 |
| 13 | to-issues | 4 |
| 14 | uploading-to-clovanote | 4 |
| 15 | confluence-sync | 3 |
| 16 | find-skills | 3 |
| 17 | posting-to-slack-thread | 3 |
| 18 | aidlc:aidlc-setup | 2 |
| 19 | frontend-design | 2 |
| 20 | grill-me | 2 |
| 21 | intern-interview-questions | 2 |
| 22 | wiki-context | 2 |
| 23 | wiki-ingest | 2 |
| 24 | wiki-query | 2 |
| 25 | code-review-excellence | 1 |
| 26 | deep-research | 1 |
| 27 | isolating-fragment-work | 1 |
| 28 | miricanvas-staging-deploy | 1 |
| 29 | new-post | 1 |
| 30 | prd-code-reconcile | 1 |
| 31 | pull-request | 1 |
| 32 | session-ingest | 1 |
| 33 | speckit-constitution | 1 |
| 34 | speckit-implement | 1 |
| 35 | speckit-plan | 1 |
| 36 | speckit-specify | 1 |
| 37 | speckit-tasks | 1 |
| 38 | superpowers:brainstorming | 1 |
| 39 | superpowers:systematic-debugging | 1 |
| 40 | superpowers:test-driven-development | 1 |
| 41 | superpowers:writing-skills | 1 |
| 42 | text-visual-summary | 1 |
| 43 | weekly-part-report | 1 |
| 44 | wiki-lint | 1 |
| 45 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
