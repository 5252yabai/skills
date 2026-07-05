---
name: orchestrate
description: 메인 세션을 오케스트레이터로 유지하며 goal을 달성하는 프로세스. 모든 실행과 검증을 분리된 subagent에 위임하고, 결과는 handoff 문서로만 전달받아 메인 컨텍스트를 보호한다. 사용자가 '/orchestrate', '오케스트레이터로 진행해줘', 'subagent에 위임해서 해줘'라고 하거나, goal 기반 장시간·밤샘 자율 실행에서 컨텍스트 소모 없이 작업할 때 사용한다.
argument-hint: "달성할 goal"
---

# Orchestrate

메인 세션은 지휘만 한다. 구현도 검증도 직접 하지 않는다.

## 오케스트레이터 규칙

1. **직접 작업 금지**: 파일 수정, 코드 작성, 대량 파일 읽기를 하지 않는다. 탐색이 필요하면 Explore subagent에 위임한다.
2. **실행과 검증은 반드시 별도 subagent**: 실행자에게 검증을 맡기지 않는다. 검증자는 매번 fresh하게 스폰한다 — 실행자의 추론 과정을 모르는 상태가 검증의 독립성을 보장한다.
3. **완료 기준은 실행 전에 확정**: 각 작업의 acceptance criteria를 PLAN.md에 먼저 쓴다. 검증자는 이 기준으로만 판정한다. 실행 후 기준을 바꾸지 않는다.
4. **상태는 전부 파일에**: 메인 컨텍스트가 압축돼도 `PLAN.md` + `handoffs/`만으로 전체 상태를 복원할 수 있어야 한다.

## 프로세스

### 1. 계획

- `.orchestrator/PLAN.md` 생성 (git 레포면 `.orchestrator/`를 `.gitignore`에 추가할지 확인).
- goal을 독립적으로 검증 가능한 작업 단위로 분해하고, 작업마다 완료 기준을 명시한다:

```md
## Goal
<goal 원문>

## Tasks
- [ ] 01 <작업명>
  - 기준: <검증자가 기계적으로 판정할 수 있는 조건들>
- [ ] 02 ...
```

### 2. 작업 루프 (작업당 반복)

**a. 실행 subagent 스폰** (Agent tool, general-purpose):

> `.orchestrator/PLAN.md`의 작업 NN을 수행하라. 완료 후:
> - 변경사항을 커밋하라.
> - `.orchestrator/handoffs/NN-exec.md`에 handoff를 작성하라: 변경 파일 목록 / 한 것과 의도적으로 안 한 것 / 검증 방법 / 남은 이슈.
> - 최종 메시지는 한 줄 요약만 반환하라. 상세 내용은 handoff 파일에만 쓴다.

**b. 검증 subagent 스폰** (별도 Agent 호출, fresh):

> `.orchestrator/PLAN.md`의 작업 NN 완료 기준과 `handoffs/NN-exec.md`를 읽어라.
> handoff의 주장을 믿지 말고 산출물을 직접 확인하라 (파일 열기, 테스트·빌드 실행, 링크 확인).
> `handoffs/NN-verify.md`에 기준별 PASS/FAIL과 확인한 증거를 기록하라.
> 최종 메시지는 `PASS` 또는 `FAIL: <한 줄 사유>`만 반환하라.

**c. 판정 처리**:
- PASS → PLAN.md 체크, 다음 작업.
- FAIL → 실패 사유와 `NN-verify.md` 경로를 포함해 **새** 실행 subagent를 스폰한다 (a로 복귀). 같은 작업 3회 FAIL 시 PLAN.md에 `blocked: <사유>`로 표시하고 다음 작업으로 넘어간다.

의존성 없는 작업들은 실행-검증 쌍 단위로 병렬 스폰해도 된다. 쌍 내부는 항상 순차다.

### 3. 종료

- 전체 작업 완료(또는 blocked만 남음) 시 PLAN.md 기준 최종 요약을 보고한다: 완료 목록, blocked 목록과 사유.

## 재개

세션이 압축·중단됐다면 `.orchestrator/PLAN.md`를 읽고 체크되지 않은 첫 작업부터 루프를 계속한다. handoff 파일들이 이력의 원천이므로 대화 기록에 의존하지 않는다.
