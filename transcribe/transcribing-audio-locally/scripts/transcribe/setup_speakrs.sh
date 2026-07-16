#!/usr/bin/env bash
# 최초 1회: speakrs(Rust/CoreML) 화자 구분 바이너리를 빌드해 .speakrs/bench_turns 에 캐시한다.
# 재실행하면 바이너리가 이미 있을 때 건너뛴다 (--force 로 재빌드).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="$SCRIPT_DIR/.speakrs"
DEST_BIN="$DEST_DIR/bench_turns"
SRC_DIR="$DEST_DIR/speakrs-src"

SPEAKRS_REPO="https://github.com/avencera/speakrs"
SPEAKRS_PIN="b9f9a62ede6feb15fc9881c3aa23ea443c2e709f"  # v0.5.0
OPENBLAS_PREFIX="/opt/homebrew/opt/openblas"

FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

if [ -x "$DEST_BIN" ] && [ "$FORCE" -eq 0 ]; then
  echo "이미 빌드됨: $DEST_BIN (재빌드하려면 --force)"
  exit 0
fi

# 선결 조건 -------------------------------------------------------------
[ "$(uname -s)" = "Darwin" ] || { echo "오류: macOS(Apple Silicon) 전용입니다."; exit 1; }
command -v cargo >/dev/null || { echo "오류: rust/cargo 필요 — https://rustup.rs"; exit 1; }
if [ ! -d "$OPENBLAS_PREFIX" ]; then
  echo "오류: openblas 필요 (speakrs가 동적 링크). 설치: brew install openblas"
  exit 1
fi

mkdir -p "$DEST_DIR"

# speakrs 소스 (핀 커밋) -----------------------------------------------
if [ ! -d "$SRC_DIR/.git" ]; then
  echo "speakrs 클론 중 ($SPEAKRS_PIN)..."
  git clone --filter=blob:none "$SPEAKRS_REPO" "$SRC_DIR"
fi
git -C "$SRC_DIR" fetch --depth 1 origin "$SPEAKRS_PIN" 2>/dev/null || git -C "$SRC_DIR" fetch origin
git -C "$SRC_DIR" checkout -q "$SPEAKRS_PIN"

# 우리가 만든 예제(bench_turns: turns를 TSV로 stdout 출력) 주입 ---------
cp "$SCRIPT_DIR/bench_turns.rs" "$SRC_DIR/examples/bench_turns.rs"

# 빌드 (openblas-system, coreml) --------------------------------------
echo "빌드 중... (최초 빌드는 수 분 소요)"
export LDFLAGS="-L$OPENBLAS_PREFIX/lib"
export CPPFLAGS="-I$OPENBLAS_PREFIX/include"
export PKG_CONFIG_PATH="$OPENBLAS_PREFIX/lib/pkgconfig:${PKG_CONFIG_PATH:-}"
(
  cd "$SRC_DIR"
  cargo build --release --example bench_turns \
    --no-default-features --features online,coreml,openblas-system
)

cp "$SRC_DIR/target/release/examples/bench_turns" "$DEST_BIN"
chmod +x "$DEST_BIN"
echo "완료: $DEST_BIN"
echo "첫 화자 구분 실행 시 CoreML 모델 컴파일(~200초, 1회성)이 발생합니다."
