---
name: refactor-humble-object
description: 테스트코드를 작성하기 쉬운 구조로 코드를 리팩토링 할때 사용합니다.
---

테스트하기 쉬운 구조로 코드를 변경해주세요. 

모킹이 없고 SOLID한 코드가 테스트하기 쉬운 코드입니다.

험블 객체 패턴을 이용해주세요. 객체가 자신의 역할을 넘어 다른 객체의 세부사항을 알게 하는 일 없이 인터페이스에 의존하게 해주세요.

## 예시 1: `localStorage` 직접 호출 분리

문제: 비즈니스 로직이 브라우저 저장소를 직접 알면 테스트에서 global mock이 필요합니다.

```ts
class UserPreferenceService {
  saveTheme(userId: string, theme: "light" | "dark") {
    const payload = JSON.stringify({ userId, theme });
    window.localStorage.setItem("theme", payload);
  }
}
```

개선: 저장 행위를 작은 인터페이스 뒤로 밀어 넣고, 실제 `localStorage` 접근은 humble object가 담당합니다.

```ts
interface PreferenceWriter {
  save(value: string): void;
}

class LocalStoragePreferenceWriter implements PreferenceWriter {
  save(value: string) {
    window.localStorage.setItem("theme", value);
  }
}

class UserPreferenceService {
  constructor(private readonly writer: PreferenceWriter) {}

  saveTheme(userId: string, theme: "light" | "dark") {
    this.writer.save(JSON.stringify({ userId, theme }));
  }
}
```

테스트는 global mock 없이 stub만 사용합니다.

```ts
it("theme을 저장하면 writer에 사용자 preference payload를 전달한다", () => {
  const saved: string[] = [];
  const service = new UserPreferenceService({
    save: value => saved.push(value),
  });

  service.saveTheme("user-1", "dark");

  expect(saved).toEqual([JSON.stringify({ userId: "user-1", theme: "dark" })]);
});
```

## 예시 2: 인터페이스를 호출자 기준으로 작게 분리

문제: 하나의 repository 인터페이스에 메서드를 계속 추가하면, 기존 테스트 stub이 쓰지도 않는 메서드까지 구현해야 합니다.

```ts
interface PreferenceRepository {
  save(value: string): void;
  load(): string | null;
  remove(): void;
}

class SavePreferenceUseCase {
  constructor(private readonly repository: PreferenceRepository) {}

  execute(theme: "light" | "dark") {
    this.repository.save(JSON.stringify({ theme }));
  }
}
```

개선: 각 유스케이스가 실제로 사용하는 행위만 인터페이스로 둡니다.

```ts
interface PreferenceWriter {
  save(value: string): void;
}

interface PreferenceReader {
  load(): string | null;
}

class BrowserPreferenceRepository implements PreferenceWriter, PreferenceReader {
  save(value: string) {
    window.localStorage.setItem("theme", value);
  }

  load() {
    return window.localStorage.getItem("theme");
  }
}

class SavePreferenceUseCase {
  constructor(private readonly writer: PreferenceWriter) {}

  execute(theme: "light" | "dark") {
    this.writer.save(JSON.stringify({ theme }));
  }
}
```

테스트 stub은 필요한 메서드 하나만 구현합니다.

```ts
it("theme 저장을 실행하면 writer에 theme payload를 전달한다", () => {
  const saved: string[] = [];
  const useCase = new SavePreferenceUseCase({
    save: value => saved.push(value),
  });

  useCase.execute("light");

  expect(saved).toEqual([JSON.stringify({ theme: "light" })]);
});
```

## 예시 3: React hook의 외부 의존성 분리

문제: hook 내부에서 `fetch`, `localStorage`, `window.location`을 직접 사용하면 hook 테스트가 브라우저/API mock에 묶입니다.

```tsx
function useUserPreference(userId: string) {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  useEffect(() => {
    fetch(`/api/users/${userId}/preference`)
      .then(response => response.json())
      .then(data => {
        setTheme(data.theme);
        window.localStorage.setItem("theme", data.theme);
      });
  }, [userId]);

  return theme;
}
```

개선: hook은 port에 의존하고, browser/API 접근은 humble adapter로 분리합니다.

```tsx
interface PreferencePort {
  load(userId: string): Promise<"light" | "dark">;
  remember(theme: "light" | "dark"): void;
}

class BrowserPreferencePort implements PreferencePort {
  async load(userId: string) {
    const response = await fetch(`/api/users/${userId}/preference`);
    const data = await response.json();
    return data.theme;
  }

  remember(theme: "light" | "dark") {
    window.localStorage.setItem("theme", theme);
  }
}

function useUserPreference(userId: string, port: PreferencePort) {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  useEffect(() => {
    let ignore = false;

    port.load(userId).then(nextTheme => {
      if (ignore) return;
      setTheme(nextTheme);
      port.remember(nextTheme);
    });

    return () => {
      ignore = true;
    };
  }, [userId, port]);

  return theme;
}
```

hook 테스트는 async stub port로 로직만 검증합니다.

```tsx
it("preference를 로드하면 theme 상태를 갱신하고 기억한다", async () => {
  const remembered: string[] = [];
  const port: PreferencePort = {
    load: async () => "dark",
    remember: theme => remembered.push(theme),
  };

  const { result } = renderHook(() => useUserPreference("user-1", port));

  await waitFor(() => expect(result.current).toBe("dark"));
  expect(remembered).toEqual(["dark"]);
});
```
