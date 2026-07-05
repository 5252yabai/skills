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
| **wiki**          | wiki-context, wiki-query, session-ingest                                                                                                                |
| **miridih**       | (비공개 서브모듈)                                                                                                                                       |

<!-- SKILL-USAGE:START -->
## 스킬 사용 통계

<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->
_총 345회 · 고유 64종 · 데이터 기준 2026-07-05 (출처: `~/.rig/usage.jsonl`)_

| 순위 | 스킬 | 사용 |
| ---- | ---- | ---- |
| 1 | write-a-skill | 28 |
| 2 | transcribing-audio-locally | 22 |
| 3 | frontend-design | 20 |
| 4 | handoff | 20 |
| 5 | text-visual-summary | 19 |
| 6 | daily-scrum-report | 16 |
| 7 | sharing-internal-html | 16 |
| 8 | tdd | 16 |
| 9 | posting-service-util-daily-scrum | 13 |
| 10 | agent-browser | 10 |
| 11 | tech-interview-questions | 9 |
| 12 | commit | 8 |
| 13 | miricanvas-design-system | 8 |
| 14 | aidlc:aidlc-setup | 7 |
| 15 | posting-to-slack-thread | 7 |
| 16 | service-util-pr-review | 7 |
| 17 | axprod-issue-sync | 6 |
| 18 | book-meeting-room | 6 |
| 19 | service-util-daily-scrum-pipeline | 6 |
| 20 | axprod-issue | 5 |
| 21 | superpowers:brainstorming | 5 |
| 22 | teach | 5 |
| 23 | code-review-excellence | 4 |
| 24 | create-service-util-issue | 4 |
| 25 | find-skills | 4 |
| 26 | grill-me | 4 |
| 27 | improve-codebase-architecture | 4 |
| 28 | to-issues | 4 |
| 29 | uploading-to-clovanote | 4 |
| 30 | weekly-part-report | 4 |
| 31 | wiki-query | 4 |
| 32 | code-review | 3 |
| 33 | confluence-sync | 3 |
| 34 | n8n-mcp-tools-expert | 3 |
| 35 | open-code-review:open-code-review | 3 |
| 36 | pull-request | 3 |
| 37 | web2-architecture-map | 3 |
| 38 | intern-interview-questions | 2 |
| 39 | open-code-review:review | 2 |
| 40 | superpowers:test-driven-development | 2 |
| 41 | wiki-context | 2 |
| 42 | wiki-ingest | 2 |
| 43 | datadog:ddsetup | 1 |
| 44 | deep-research | 1 |
| 45 | isolating-fragment-work | 1 |
| 46 | miricanvas-staging-deploy | 1 |
| 47 | new-post | 1 |
| 48 | persona-builder | 1 |
| 49 | prd-code-reconcile | 1 |
| 50 | schedule | 1 |
| 51 | service-util-issue-sync | 1 |
| 52 | session-ingest | 1 |
| 53 | speckit-constitution | 1 |
| 54 | speckit-implement | 1 |
| 55 | speckit-plan | 1 |
| 56 | speckit-specify | 1 |
| 57 | speckit-tasks | 1 |
| 58 | superpowers:subagent-driven-development | 1 |
| 59 | superpowers:systematic-debugging | 1 |
| 60 | superpowers:writing-plans | 1 |
| 61 | superpowers:writing-skills | 1 |
| 62 | update-config | 1 |
| 63 | wiki-lint | 1 |
| 64 | writing-sync | 1 |
<!-- SKILL-USAGE:END -->
