#!/bin/bash
# 새 스킬을 ~/.agents/skills/[<group>/]<name>에서 claude·pi·opencode로 심링크한다.
# 사용법: bash ~/.agents/skills/link-skill.sh <skill-name> [group]
#   group 생략 시 루트의 스킬을 찾고, 없으면 그룹 폴더에서 자동 탐색한다.
# 멱등: 이미 링크가 있으면 건너뛴다. (dest의 링크는 항상 평면 <name>)
set -e
name="$1"
group="$2"
[ -z "$name" ] && { echo "사용법: link-skill.sh <skill-name> [group]"; exit 1; }
AG="$HOME/.agents/skills"

# 원본 경로 결정: 명시 group > 루트 > 그룹 자동탐색
if [ -n "$group" ]; then
  relsrc="$group/$name"
elif [ -d "$AG/$name" ]; then
  relsrc="$name"
else
  relsrc="$(cd "$AG" && find . -maxdepth 2 -mindepth 2 -type d -name "$name" | head -1 | sed 's|^\./||')"
fi
[ -n "$relsrc" ] && [ -d "$AG/$relsrc" ] || { echo "원본 없음: $AG/$name"; exit 1; }

# dest_root:rel_prefix (rel_prefix는 dest/<name>에서 ~/.agents/skills까지의 상대경로)
for entry in \
  "$HOME/.claude/skills:../../.agents/skills" \
  "$HOME/.pi/agent/skills:../../../.agents/skills" \
  "$HOME/.config/opencode/skills:../../../.agents/skills"; do
  dir="${entry%%:*}"
  rel="${entry#*:}"
  [ -d "$dir" ] || { echo "skip(디렉토리 없음): $dir"; continue; }
  if [ -e "$dir/$name" ] || [ -L "$dir/$name" ]; then
    echo "skip(이미 존재): $dir/$name"
  else
    ln -s "$rel/$relsrc" "$dir/$name"
    echo "링크: $dir/$name -> $rel/$relsrc"
  fi
done
