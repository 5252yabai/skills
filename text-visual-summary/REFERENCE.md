# Reference — Text → Visual HTML Summary

## Accuracy techniques (priority #1)

- **Quote, don't paraphrase, for claims that matter.** Preserve exact figures and direct quotes. Paraphrase only connective summary.
- **Atomic grounding.** Before drawing a chart, write the source data points as plain text and confirm each exists in the source. A chart with a fabricated value is worse than no chart.
- **No invented causation/dates/names.** If the source says "next week", don't convert to a specific date unless the date is given. If a name/abbreviation is unclear, render it as heard and add a caveat.
- **Surface uncertainty in the report.** Add a short caveat box near the top when the source is lossy:
  - STT transcripts: speaker labels may be merged/misassigned → prefer topic/decision framing over attributing quotes to named people.
  - OCR/scans: figures may be misread.
  - Abbreviations / org names: flag for user confirmation.
- **Qualitative ≠ measured.** If a radar/score chart visualizes a judgment (not a measurement), label it "정성적 도식화, 측정값 아님".
- **Don't pad (priority #2).** Cut sections with no real content. Fewer, denser, correct visuals beat many thin ones.

## Library choice

- **Chart.js** (CDN `chart.js@4`) — bar/line/doughnut/radar. Simple, light. Default.
- **ECharts** (CDN `echarts@5`) — when you need richer interactivity, sankey, treemap, graph layouts.
- **Pure CSS / inline SVG** — for lifecycles, flows, VS comparisons, timelines, metric cards. More reliable and lighter than forcing a chart lib to draw a diagram.

## Chart.js snippets

Shared defaults (match the frontend-design palette via CSS variables read in JS or hardcoded hex):

```js
Chart.defaults.font.family = "'IBM Plex Sans KR', sans-serif";
Chart.defaults.color = "#4a463d";
```

Horizontal before/after bar:

```js
new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Before", "After"],
    datasets: [
      {
        data: [44, 1.5],
        backgroundColor: ["#c1440e", "#1f6f6a"],
        borderRadius: 4,
      },
    ],
  },
  options: { indexAxis: "y", plugins: { legend: { display: false } } },
});
```

Radar (qualitative — label it):

```js
new Chart(ctx, {
  type: "radar",
  data: {
    labels: ["A", "B", "C", "D"],
    datasets: [
      {
        data: [9, 8, 9, 3],
        borderColor: "#1f6f6a",
        backgroundColor: "rgba(31,111,106,.18)",
      },
    ],
  },
  options: {
    plugins: { legend: { display: false } },
    scales: { r: { min: 0, max: 10, ticks: { display: false } } },
  },
});
```

## CSS diagram patterns

- **Lifecycle / pipeline**: a grid of `.phase` cells with a border, each holding step name + owner tag + description, joined by an absolutely-positioned `→` arrow on the right edge.
- **VS / debate**: `1fr 64px 1fr` grid — two bordered cards with `✕`/`✓` list markers and a centered "VS".
- **Flow / architecture**: flex row of bordered `.node` boxes separated by `.conn` arrows that carry an edge label.
- **Action table**: `<table>` with a dark header row and status `.pill` spans (배포 / 리뷰 / 검토 / 진행).
- **Metric cards**: dark cards with a large serif number and a small mono sublabel citing the source figure.
- **Scroll reveal**: `IntersectionObserver` adds `.in` to `.reveal` elements; CSS transitions opacity/transform.

## Self-contained HTML skeleton

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>…</title>
    <!-- fonts per frontend-design direction -->
    <link
      href="https://fonts.googleapis.com/css2?family=…&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
      :root {
        /* palette from frontend-design */
      } /* all CSS inline */
    </style>
  </head>
  <body>
    <header class="hero">…title + meta + accuracy caveat…</header>
    <section>
      …numbered sections: overview, themes, debates, metrics, actions…
    </section>
    <footer>…source + method note…</footer>
    <script>
      /* IntersectionObserver reveal + Chart.js instances with real data */
    </script>
  </body>
</html>
```

## Verify-render

`scripts/verify-render.sh <file.html> [out.png] [height]` runs headless Chrome with a virtual-time budget so CDN charts finish rendering, then writes a full-page PNG. Read the PNG and check: fonts loaded, no overflow/clipping, every chart drew (not blank), diagrams aligned. Fix and re-run until clean. If Chrome isn't found, fall back to opening the file and asking the user to confirm visually.
