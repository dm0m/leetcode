#!/usr/bin/env bash
set -euo pipefail

# Scaffold a new problem.
# Usage: ./scripts/new.sh [-l lang[,lang...]] <number> <slug> <difficulty> [topic ...]
# Examples:
#   ./scripts/new.sh 1 two-sum easy Array "Hash Table"          # Python only (default)
#   ./scripts/new.sh -l py,java,csharp 1 two-sum easy Array     # three languages
# Default language: Python (override with -l, or env LC_LEETCODE_LANG).

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
. "$ROOT/scripts/lib/langs.sh"

DEFAULT_LANG="${LC_LEETCODE_LANG:-python}"

usage() {
  echo "Usage: $0 [-l lang[,lang...]] <number> <slug> <difficulty> [topic ...]" >&2
  echo "Languages: python java csharp cpp c javascript typescript go rust kotlin ruby" >&2
}

langs_csv=""
positional=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    -l|--lang|--langs)       langs_csv="${2:-}"; shift 2;;
    -l=*|--lang=*|--langs=*)  langs_csv="${1#*=}"; shift;;
    -h|--help)                usage; exit 0;;
    --)                       shift; while [ "$#" -gt 0 ]; do positional+=("$1"); shift; done;;
    -*)                       echo "Unknown option: $1" >&2; usage; exit 1;;
    *)                        positional+=("$1"); shift;;
  esac
done
set -- "${positional[@]:-}"

if [ "$#" -lt 3 ]; then usage; exit 1; fi

number="$1"; slug="$2"; difficulty_raw="$3"; shift 3
topics=("$@")

printf -v padded "%04d" "$number" 2>/dev/null || padded="$number"

case "$(printf '%s' "$difficulty_raw" | tr '[:upper:]' '[:lower:]')" in
  easy)        difficulty="Easy";;
  medium|med)  difficulty="Medium";;
  hard)        difficulty="Hard";;
  *)           difficulty="$difficulty_raw";;
esac

title="$(printf '%s' "$slug" | tr '-' ' ' \
  | awk '{for(i=1;i<=NF;i++){$i=toupper(substr($i,1,1)) substr($i,2)}; print}')"

dir="$ROOT/problems/${padded}-${slug}"
if [ -d "$dir" ]; then
  echo "Already exists: $dir" >&2
  echo "Add a language to it with: ./scripts/add-lang.sh $number <lang>" >&2
  exit 1
fi
mkdir -p "$dir"

if [ "${#topics[@]}" -gt 0 ] && [ -n "${topics[0]}" ]; then
  joined=""
  for t in "${topics[@]}"; do [ -z "$joined" ] && joined="$t" || joined="$joined, $t"; done
  topics_str="[$joined]"
else
  topics_str="[]"
fi

today="$(date +%Y-%m-%d)"

cat > "$dir/NOTES.md" <<NOTES
---
number: ${number}
title: ${title}
difficulty: ${difficulty}
topics: ${topics_str}
date: ${today}
status: solved-independently
---

## Intuition
The one-sentence key insight.

## Approach
The algorithm in plain words.

## Complexity
- Time:
- Space:

## Gotchas
Edge cases, mistakes, alternatives worth remembering.
NOTES

[ -z "$langs_csv" ] && langs_csv="$DEFAULT_LANG"
created=()
IFS=',' read -ra _langs <<< "$langs_csv"
for raw in "${_langs[@]}"; do
  raw="$(printf '%s' "$raw" | tr -d '[:space:]')"
  [ -z "$raw" ] && continue
  key="$(normalize_lang "$raw")"
  if [ -z "$key" ]; then echo "Skipping unknown language: $raw" >&2; continue; fi
  created+=("$(write_stub "$key" "$dir" "$number" "$title" "$difficulty" "$slug")")
done

if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/scripts/gen_readme.py" >/dev/null 2>&1 && echo "README refreshed."
fi

echo "Created: $dir"
echo "  NOTES.md"
for f in "${created[@]}"; do echo "  $f"; done
