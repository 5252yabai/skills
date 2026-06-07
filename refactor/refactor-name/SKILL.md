---
name: refactor-name
description: 이름을 리팩토링 할때 사용합니다.
---

이름은 맥락이 모자란 부분만 채워주고, 연산의 결과가 무엇인지까지만 짚어주면 충분하다.

좋은 이름은 많은 걸 담는 이름이 아니다. 현재 위치에서 필요한 만큼만 담는 이름이다. 그래서 잘 읽히는 코드의 핵심은 "설명을 많이 붙이기"보다, "주변 코드가 이미 어디까지 설명하고 있는지 판단하기"에 더 가깝다.

## 예시 1

`const userListFilteredByActive = users.filter((user) => user.isActive)`
이 코드가 틀린 건 아니지만 읽는 사람 입장에서는 피곤하다. 우리는 이미 users.filter를 보고 있고, 조건이 user.isActive라는 것도 보고 있다. 즉, 이름이 구현을 다시 길게 설명할 필요는 없다.

이럴 때는 동작을 설명하는 이름보다, 결과가 바로 떠오르는 이름이 더 읽기 좋다.

`const activeUsers = users.filter((user) => user.isActive)`

## 예시 2

```tsx
<Dialog
  isDialogOpen={isDialogOpen}
  onDialogClose={handleDialogClose}
/>
```

Dialog라는 컴포넌트 이름이 이미 "이건 열려 있는 상태와 닫기 핸들러다"라는 걸 말해주고 있다.
Dialog라는 맥락 안에서는 보통 이쪽이 더 빨리 읽힌다.

<Dialog
  isOpen={isDialogOpen}
  onClose={handleDialogClose}
/>
바깥 코드에서는 isDialogOpen처럼 길어도 괜찮다. 어떤 대상을 열고 닫는지까지 구분해야 할 수 있기 때문이다.

## 예시 3

```tsx
// apps/workspace/src/router/pathname.ts
type parseWorkspaceRoutePathname = (pathname: string): => string 
```

워크스페이스 url을 파싱하는 함수라서, workspace라는 접두사를 붙였다.
코드뿐 아니라 파일, 폴더 경로도 맥락이다. workspace라는 정보는 이미 파일에 포함되어 있어서 생략하는게 좋다.

```tsx
type parseRoutePathname = (pathname: string): => string 
```
