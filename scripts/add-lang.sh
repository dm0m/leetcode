#!/usr/bin/env bash
set -euo pipefail

# Add one or more language solution stubs to an EXISTING problem.
# Usage: ./scripts/add-lang.sh <number|problem-dir> <lang> [lang ...]
# Examples:
#   ./scripts/add-lang.sh 1 java
#   ./scripts/add-lang.sh 0001-two-sum csharp cpp

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
. "$ROOT/scripts/lib/langs.sh"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <number|problem-dir> <lang> [lang ...]" >&2
  echo "Languages: python java csharp cpp c javascript typescript go rust kotlin ruby" >&2
  exit 1
fi

target="$1"; shift

dir=""
if [ -d "$ROOT/problems/$target" ]; then
  dir="$ROOT/problems/$target"
elif [ -d "$target" ]; then
  dir="$target"
else
  printf -v padded "%04d" "$target" 2>/dev/null || padded="$target"
  for m in "$ROOT"/problems/${padded}-*; do
    [ -d "$m" ] && { dir="$m"; break; }
  done
fi

if [ -z "$dir" ] || [ ! -d "$dir" ]; then
  echo "Problem not found for: $target" >&2
  exit 1
fi

notes="$dir/NOTES.md"
get_fm() { grep -m1 "^$1:" "$notes" 2>/dev/null | sed "s/^$1:[[:space:]]*//; s/[[:space:]]*#.*$//"; }
number="$(get_fm number)";     number="${number:-0}"
title="$(get_fm title)";       title="${title:-$(basename "$dir")}"
difficulty="$(get_fm difficulty)"; difficulty="${difficulty:-}"
slug="$(basename "$dir" | sed 's/^[0-9]*-//')"

echo "Target: $dir"
for raw in "$@"; do
  key="$(normalize_lang "$raw")"
  if [ -z "$key" ]; then echo "Skipping unknown language: $raw" >&2; continue; fi
  echo "  $(write_stub "$key" "$dir" "$number" "$title" "$difficulty" "$slug")"
done

if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/scripts/gen_readme.py" >/dev/null 2>&1 && echo "README refreshed."
fi
