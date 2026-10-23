#!/usr/bin/env bash
# Language registry: canonical keys, solution filenames, and stubs.
# Add a language by extending all three functions below.

normalize_lang() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    py|python|python3) echo python;;
    java)              echo java;;
    cs|csharp|c#|dotnet) echo csharp;;
    cpp|c++|cplusplus|cc) echo cpp;;
    c)                 echo c;;
    js|javascript|node) echo javascript;;
    ts|typescript)     echo typescript;;
    go|golang)         echo go;;
    rs|rust)           echo rust;;
    kt|kotlin)         echo kotlin;;
    rb|ruby)           echo ruby;;
    *)                 echo "";;
  esac
}

lang_filename() {
  case "$1" in
    python)     echo solution.py;;
    java)       echo Solution.java;;
    csharp)     echo Solution.cs;;
    cpp)        echo solution.cpp;;
    c)          echo solution.c;;
    javascript) echo solution.js;;
    typescript) echo solution.ts;;
    go)         echo solution.go;;
    rust)       echo solution.rs;;
    kotlin)     echo Solution.kt;;
    ruby)       echo solution.rb;;
    *)          echo "";;
  esac
}

# write_stub <lang> <dir> <number> <title> <difficulty> <slug>
# Prints the filename it created (or "<name> (exists)" if already present).
write_stub() {
  local lang="$1" dir="$2" number="$3" title="$4" difficulty="$5" slug="$6"
  local fname; fname="$(lang_filename "$lang")"
  [ -z "$fname" ] && return 1
  local path="$dir/$fname"
  if [ -f "$path" ]; then echo "$fname (exists)"; return 0; fi
  local url="https://leetcode.com/problems/${slug}/"
  local hdr="${number}. ${title}  (${difficulty})"
  case "$lang" in
    python)
cat > "$path" <<PYSTUB
# ${hdr}
# ${url}

class Solution:
    pass
PYSTUB
      ;;
    java)
cat > "$path" <<JAVASTUB
// ${hdr}
// ${url}
class Solution {

}
JAVASTUB
      ;;
    csharp)
cat > "$path" <<CSSTUB
// ${hdr}
// ${url}
public class Solution {

}
CSSTUB
      ;;
    cpp)
cat > "$path" <<CPPSTUB
// ${hdr}
// ${url}
#include <vector>
using namespace std;

class Solution {
public:

};
CPPSTUB
      ;;
    c)
cat > "$path" <<CSTUB
// ${hdr}
// ${url}
CSTUB
      ;;
    javascript)
cat > "$path" <<JSSTUB
// ${hdr}
// ${url}
JSSTUB
      ;;
    typescript)
cat > "$path" <<TSSTUB
// ${hdr}
// ${url}
export {};
TSSTUB
      ;;
    go)
cat > "$path" <<GOSTUB
// ${hdr}
// ${url}
package main
GOSTUB
      ;;
    rust)
cat > "$path" <<RSSTUB
// ${hdr}
// ${url}
struct Solution;

impl Solution {}
RSSTUB
      ;;
    kotlin)
cat > "$path" <<KTSTUB
// ${hdr}
// ${url}
class Solution {

}
KTSTUB
      ;;
    ruby)
cat > "$path" <<RBSTUB
# ${hdr}
# ${url}
RBSTUB
      ;;
  esac
  echo "$fname"
}
