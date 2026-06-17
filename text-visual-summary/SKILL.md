---
name: text-visual-summary
description: Analyze and summarize any source text, then turn it into a single self-contained HTML report rich with charts, diagrams, and visual elements. Use when the user wants to "시각화해줘", "요약해서 html로", "분석해서 그래프로", "visualize this text", "make a visual report/dashboard", or hands over a transcript, meeting notes, document, article, or research and asks for a visual summary. Always invokes the frontend-design skill for the aesthetics.
---

# Text → Visual HTML Summary

Convert source text into one polished, self-contained HTML report. **Accuracy is the top priority; conciseness is second.** Never sacrifice correctness for visual flair, and never pad the report.

## Non-negotiables

1. **Accuracy first.** Every number, label, quote, and claim in the HTML must trace back to the source. Do not invent data, dates, names, or causation. If the source is uncertain (e.g. STT speaker labels, OCR, ambiguous abbreviations), state the caveat in the report and avoid over-asserting. See [REFERENCE.md](REFERENCE.md) for grounding techniques.
2. **Use `frontend-design`.** Invoke the `frontend-design` skill before writing markup — it sets the aesthetic direction. This is mandatory, not optional.
3. **One self-contained file.** Output a single `.html` (inline CSS/JS). Chart/diagram libraries load via CDN; note that internet is needed to render them.
4. **Verify before claiming done.** Render headless and look at the screenshot. Never claim it works without seeing it.

## Workflow

- [ ] **1. Ingest fully.** Read the entire source (all files/segments) before summarizing. Do not work from the first page only.
- [ ] **2. Extract a grounded summary.** Break content into atomic, source-backed points. Group by theme/decision/topic — not by raw chronology unless that's the point. Capture: key topics, decisions, debates (positions + resolution), metrics/numbers, action items, timeline. Flag anything uncertain.
- [ ] **3. Plan visualizations.** Match each chunk to the right visual (see catalog below). Prefer a few high-signal visuals over many decorative ones — conciseness. Every chart needs real source data.
- [ ] **4. Invoke `frontend-design`.** Get the aesthetic direction (typography, color, layout, motion).
- [ ] **5. Build the HTML.** Single file. Sectioned report. Charts via Chart.js or ECharts (CDN); structural diagrams (flows, lifecycles, comparisons) via semantic HTML/CSS or inline SVG. Put a short accuracy/source caveat near the top.
- [ ] **6. Verify render.** `bash scripts/verify-render.sh <file.html>` → Read the PNG → fix layout/overflow/empty-chart issues. Repeat until clean.
- [ ] **7. Deliver.** `open` the file and report: output path, sections, and any accuracy caveats. Keep the source/transcript available for the user to verify.

## Visualization catalog (data → visual)

| Source content                    | Visual                                             |
| --------------------------------- | -------------------------------------------------- |
| Before/after, magnitudes, counts  | Bar chart (Chart.js)                               |
| Composition / share               | Doughnut / stacked bar                             |
| Trend over time                   | Line chart                                         |
| Multi-axis qualitative profile    | Radar (label clearly if qualitative, not measured) |
| Process / pipeline / lifecycle    | CSS or SVG step diagram with arrows                |
| Two positions / tradeoff / debate | Side-by-side VS comparison cards                   |
| Data/control flow, architecture   | Node-and-connector flow (CSS/SVG)                  |
| Action items, schedule            | Table with status pills + dates                    |
| Headline metrics                  | Large metric cards                                 |
| Key statement                     | Pull-quote strip                                   |

## Quick start

> "이 회의록 시각화해서 html로 만들어줘"

1. Read the transcript end to end. 2. Extract decisions/metrics/actions, flagging uncertain names. 3. Map to lifecycle diagram + bar charts + action table + VS cards. 4. Invoke `frontend-design`. 5. Write one HTML file. 6. `verify-render.sh` → inspect → fix. 7. Open and summarize.

See [REFERENCE.md](REFERENCE.md) for chart snippets, diagram patterns, accuracy techniques, and the self-contained HTML skeleton.
