#!/bin/bash
# 자체완결 HTML 리포트를 헤드리스 크롬으로 렌더해 전체 페이지 PNG로 저장한다.
# CDN 차트(Chart.js/ECharts)가 그려질 시간을 virtual-time-budget으로 확보한다.
# 사용법: verify-render.sh <file.html> [out.png] [height]
set -e

html="$1"
out="${2:-/tmp/tvs-render.png}"
height="${3:-6000}"

[ -z "$html" ] && { echo "사용법: verify-render.sh <file.html> [out.png] [height]"; exit 1; }
[ -f "$html" ] || { echo "파일 없음: $html"; exit 1; }

# 절대경로 file:// URL
abs="$(cd "$(dirname "$html")" && pwd)/$(basename "$html")"
url="file://$abs"

# 크롬 실행 파일 탐색 (macOS / Linux)
CHROME=""
for c in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
  "$(command -v google-chrome 2>/dev/null)" \
  "$(command -v chromium 2>/dev/null)" \
  "$(command -v chromium-browser 2>/dev/null)"; do
  [ -n "$c" ] && [ -x "$c" ] && { CHROME="$c"; break; }
done

if [ -z "$CHROME" ]; then
  echo "크롬 계열 브라우저를 못 찾음 — 수동 확인 필요: open \"$abs\""
  exit 2
fi

"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1100,"$height" --virtual-time-budget=5000 \
  --screenshot="$out" "$url" 2>/dev/null

if [ -f "$out" ]; then
  echo "렌더 완료: $out ($(wc -c < "$out") bytes)"
  echo "→ 이 PNG를 Read로 열어 폰트 로드·오버플로·빈 차트 여부를 확인하세요."
else
  echo "스크린샷 실패 — 수동 확인: open \"$abs\""
  exit 3
fi
