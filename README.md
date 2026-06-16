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
_총 102회 · 고유 36종 · 데이터 기준 2026-06-15 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | tdd | 8 |
| 2 | handoff | 7 |
| 3 | miricanvas-design-system | 7 |
| 4 | tech-interview-questions | 7 |
| 5 | write-a-skill | 7 |
| 6 | transcribing-audio-locally | 6 |
| 7 | agent-browser | 4 |
| 8 | commit | 4 |
| 9 | improve-codebase-architecture | 4 |
| 10 | teach | 4 |
| 11 | to-issues | 4 |
| 12 | uploading-to-clovanote | 4 |
| 13 | confluence-sync | 3 |
| 14 | daily-scrum-report | 3 |
| 15 | posting-service-util-daily-scrum | 3 |
| 16 | posting-to-slack-thread | 3 |
| 17 | grill-me | 2 |
| 18 | intern-interview-questions | 2 |
| 19 | wiki-ingest | 2 |
| 20 | wiki-query | 2 |
| 21 | find-skills | 1 |
| 22 | miricanvas-staging-deploy | 1 |
| 23 | new-post | 1 |
| 24 | prd-code-reconcile | 1 |
| 25 | pull-request | 1 |
| 26 | session-ingest | 1 |
| 27 | speckit-constitution | 1 |
| 28 | speckit-implement | 1 |
| 29 | speckit-plan | 1 |
| 30 | speckit-specify | 1 |
| 31 | speckit-tasks | 1 |
| 32 | superpowers:brainstorming | 1 |
| 33 | superpowers:systematic-debugging | 1 |
| 34 | superpowers:writing-skills | 1 |
| 35 | wiki-lint | 1 |
| 36 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
