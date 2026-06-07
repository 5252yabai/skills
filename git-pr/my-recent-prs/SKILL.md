---
name: my-recent-prs
description: 현재 작업과 관련된 나의 최근 GitHub PR들을 탐색하여 맥락을 파악하는 스킬. 버그 수정, 기능 개발 등 작업 시작 시 관련 PR의 변경사항과 패턴을 자동으로 찾아 제공한다. '/my-recent-prs'로 호출하거나, 사용자가 이슈 해결/기능 개발을 요청하면서 "최근 PR 확인해줘", "내가 올린 PR 봐줘", "관련 PR 찾아줘" 등을 언급할 때 사용한다.
---

# 나의 최근 PR 탐색

현재 레포지토리에서 내가 올린 최근 PR들 중 현재 작업과 관련된 것들을 찾아 맥락을 제공한다.

## 실행 절차

### 1. 현재 컨텍스트 파악

```bash
# GitHub 사용자명
gh api user --jq '.login'

# 현재 브랜치에서 이슈 번호/키워드 추출
git branch --show-current
```

브랜치명에서 이슈 번호(예: PROJ-1234, ABC-567)나 기능 키워드를 추출한다.

### 2. 최근 PR 목록 조회

```bash
gh pr list --author <username> --state all --limit 15 \
  --json number,title,state,url,createdAt,headRefName \
  --jq '.[] | "\(.number) [\(.state)] \(.title) (\(.headRefName))"'
```

사용자가 검색 키워드를 지정한 경우 `--search` 옵션을 활용한다:

```bash
gh pr list --author <username> --state all --limit 15 --search "<키워드>"
```

### 3. 관련 PR 필터링

다음 기준으로 관련성을 판단:

- **이슈 번호 일치**: 브랜치명이나 PR 제목에 동일/유사 이슈 번호 포함
- **키워드 유사성**: PR 제목에 현재 작업과 관련된 키워드 (같은 기능, 컴포넌트, 실험 등)
- **브랜치명 패턴**: 유사한 접두사나 기능명을 가진 브랜치

### 4. 관련 PR 상세 분석

관련 PR이 발견되면:

```bash
# 변경된 파일 목록
gh pr diff <PR번호> --name-only

# 실제 diff (필요시)
gh pr diff <PR번호>
```

### 5. 맥락 요약

- 관련 PR 목록 (번호, 제목, 상태)
- 각 PR에서 변경된 주요 파일과 패턴
- 현재 작업에 재사용할 수 있는 함수, 패턴, 접근 방식
- 주의할 점 (이미 적용된 수정, 누락된 부분 등)
