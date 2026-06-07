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
| **frontend**      | frontend-design, seo-audit, storybook, vercel-react-best-practices, web-design-guidelines, web-perf, webgpu-best-practices                              |
| **git-pr**        | commit, pull-request, create-github-pull-request-from-specification, my-recent-prs, code-review-excellence                                              |
| **issue**         | to-issues, to-prd, triage                                                                                                                               |
| **learning**      | tutor, tutor-setup                                                                                                                                      |
| **meta**          | skill-creator, write-a-skill, find-skills, setup-matt-pocock-skills                                                                                     |
| **n8n**           | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **pdf**           | PDF 생성·편집·폼 처리                                                                                                                                   |
| **planning**      | grill-me, grill-with-docs, handoff, prototype                                                                                                           |
| **refactor**      | improve-codebase-architecture, refactor-humble-object, refactor-name, refactor-plan, refactor-private-public, refactor-test-name                        |
| **slack**         | posting-to-slack-thread                                                                                                                                 |
| **testing**       | tdd, test-driven-development, testing-strategies, vitest, webapp-testing, diagnose                                                                      |
| **transcribe**    | transcribing-audio-locally, uploading-to-clovanote                                                                                                      |
| **wiki**          | wiki-context, wiki-query, session-ingest                                                                                                                |
| **zoom-out**      | 큰 그림 재정렬                                                                                                                                          |
| **miridih**       | (비공개 서브모듈)                                                                                                                                       |
