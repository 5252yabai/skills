#!/usr/bin/env node
// ~/.rig/usage.jsonl 의 스킬 사용 기록을 집계해 README.md 의 마커 구간을 갱신한다.
// .githooks/pre-commit 이 호출하지만, 수동 실행도 가능하다.
//   node scripts/update-skill-usage.mjs
// 로그 경로는 RIG_USAGE_LOG_PATH 로 덮어쓸 수 있다.
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const expand = (p) =>
  p.startsWith("~/") ? resolve(homedir(), p.slice(2)) : resolve(p);

const LOG = expand(process.env.RIG_USAGE_LOG_PATH || "~/.rig/usage.jsonl");
const README = resolve(
  dirname(fileURLToPath(import.meta.url)),
  "..",
  "README.md",
);
const START = "<!-- SKILL-USAGE:START -->";
const END = "<!-- SKILL-USAGE:END -->";

if (!existsSync(LOG)) {
  console.error(`[skill-usage] 로그 없음(${LOG}) — README 갱신 건너뜀`);
  process.exit(0);
}

const rows = readFileSync(LOG, "utf8")
  .split("\n")
  .filter(Boolean)
  .map((l) => {
    try {
      return JSON.parse(l);
    } catch {
      return null;
    }
  })
  .filter((r) => r && r.skillName);

if (rows.length === 0) {
  console.error("[skill-usage] 기록 없음 — README 갱신 건너뜀");
  process.exit(0);
}

const counts = new Map();
for (const r of rows)
  counts.set(r.skillName, (counts.get(r.skillName) || 0) + 1);
const sorted = [...counts].sort(
  (a, b) => b[1] - a[1] || a[0].localeCompare(b[0]),
);
const total = rows.length;
const lastUsed =
  rows
    .map((r) => r.usedAt)
    .filter(Boolean)
    .sort()
    .at(-1)
    ?.slice(0, 10) ?? "";

const block = [
  START,
  "## 스킬 사용 통계",
  "",
  "<!-- 이 구간은 .githooks/pre-commit 이 자동 생성한다. 직접 수정 금지. -->",
  `_총 ${total}회 · 고유 ${sorted.length}종 · 데이터 기준 ${lastUsed} (출처: \`~/.rig/usage.jsonl\`)_`,
  "",
  "| 순위 | 스킬 | 사용 |",
  "| ---- | ---- | ---- |",
  ...sorted.map(([skill, n], i) => `| ${i + 1} | ${skill} | ${n} |`),
  END,
].join("\n");

let md = readFileSync(README, "utf8");
const s = md.indexOf(START);
const e = md.indexOf(END);
if (s !== -1 && e !== -1) {
  md = md.slice(0, s) + block + md.slice(e + END.length);
} else {
  md = `${md.trimEnd()}\n\n${block}\n`;
}
writeFileSync(README, md);
console.error(
  `[skill-usage] README 갱신: ${total}회 / ${sorted.length}종 (기준 ${lastUsed})`,
);
