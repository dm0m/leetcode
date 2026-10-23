#!/usr/bin/env python3
"""Regenerate README stats + problem table from each problem's NOTES.md frontmatter
and the solution files present. No external dependencies required."""
import os
import re
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBLEMS = os.path.join(ROOT, "problems")
README = os.path.join(ROOT, "README.md")

DIFF_EMOJI = {"Easy": "\U0001F7E2", "Medium": "\U0001F7E1", "Hard": "\U0001F534"}
EXT_LANG = {
    ".py": "Py", ".java": "Java", ".cs": "C#", ".cpp": "C++", ".c": "C",
    ".js": "JS", ".ts": "TS", ".go": "Go", ".rs": "Rust", ".kt": "Kt", ".rb": "Rb",
}
LANG_ORDER = ["Py", "Java", "C#", "C++", "C", "JS", "TS", "Go", "Rust", "Kt", "Rb"]


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip() if key == "title" else val.split("#", 1)[0].strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
        else:
            fm[key] = val.strip("'\"")
    return fm


def langs_in(dir_path):
    found = []
    for fn in sorted(os.listdir(dir_path)):
        label = EXT_LANG.get(os.path.splitext(fn)[1])
        if label and label not in found:
            found.append(label)
    return sorted(found, key=lambda l: LANG_ORDER.index(l) if l in LANG_ORDER else 99)


def collect():
    probs = []
    if not os.path.isdir(PROBLEMS):
        return probs
    for name in sorted(os.listdir(PROBLEMS)):
        d = os.path.join(PROBLEMS, name)
        notes = os.path.join(d, "NOTES.md")
        if not os.path.isdir(d) or not os.path.isfile(notes):
            continue
        with open(notes, encoding="utf-8") as f:
            fm = parse_frontmatter(f.read())
        if fm:
            fm["_dir"] = "problems/" + name
            fm["_langs"] = langs_in(d)
            probs.append(fm)
    return probs


def to_int(x, default=10 ** 9):
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def current_streak(dates):
    ds = sorted(set(dates))
    if not ds:
        return 0, None
    last, dset = ds[-1], set(ds)
    streak, cur = 1, ds[-1]
    while (cur - timedelta(days=1)) in dset:
        cur -= timedelta(days=1)
        streak += 1
    return streak, last


def replace_between(content, tag, new):
    start, end = "<!-- %s:START -->" % tag, "<!-- %s:END -->" % tag
    block = "%s\n%s\n%s" % (start, new, end)
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pat.sub(lambda _: block, content) if pat.search(content) else content + "\n\n" + block + "\n"


def main():
    probs = collect()
    total = len(probs)
    by_diff = {"Easy": 0, "Medium": 0, "Hard": 0}
    by_status, topics, lang_count, dates = {}, {}, {}, []
    for p in probs:
        d = p.get("difficulty", "")
        by_diff[d] = by_diff.get(d, 0) + 1
        st = p.get("status", "")
        if st:
            by_status[st] = by_status.get(st, 0) + 1
        for t in p.get("topics", []) or []:
            topics[t] = topics.get(t, 0) + 1
        for lg in p.get("_langs", []) or []:
            lang_count[lg] = lang_count.get(lg, 0) + 1
        try:
            dates.append(datetime.strptime(p.get("date", ""), "%Y-%m-%d").date())
        except (TypeError, ValueError):
            pass

    streak, last = current_streak(dates)

    stats = ["**Total solved:** %d  " % total,
             "\U0001F7E2 Easy: %d \u00b7 \U0001F7E1 Medium: %d \u00b7 \U0001F534 Hard: %d  "
             % (by_diff.get("Easy", 0), by_diff.get("Medium", 0), by_diff.get("Hard", 0))]
    if streak:
        stats.append("\U0001F525 **Current streak:** %d day(s) \u2014 last solved %s  " % (streak, last.isoformat()))
    if lang_count:
        ordered = sorted(lang_count.items(),
                         key=lambda kv: LANG_ORDER.index(kv[0]) if kv[0] in LANG_ORDER else 99)
        stats.append("**Languages:** " + ", ".join("%s (%d)" % (k, v) for k, v in ordered) + "  ")
    if by_status:
        stats.append("**By status:** " + ", ".join("%s: %d" % (k, v) for k, v in sorted(by_status.items())) + "  ")
    if topics:
        top = sorted(topics.items(), key=lambda kv: (-kv[1], kv[0]))[:8]
        stats.append("**Top topics:** " + ", ".join("%s (%d)" % (k, v) for k, v in top) + "  ")
    stats_md = "\n".join(stats) if total else "_No problems solved yet._"

    rows = ["| # | Problem | Difficulty | Topics | Solutions | Status | Date |",
            "|---|---------|------------|--------|-----------|--------|------|"]
    for p in sorted(probs, key=lambda p: to_int(p.get("number"))):
        de = DIFF_EMOJI.get(p.get("difficulty", ""), "")
        rows.append("| %s | [%s](%s) | %s %s | %s | %s | %s | %s |" % (
            p.get("number", ""), p.get("title", "(untitled)"), p.get("_dir", ""),
            de, p.get("difficulty", ""), ", ".join(p.get("topics", []) or []),
            " ".join(p.get("_langs", []) or []), p.get("status", ""), p.get("date", "")))
    table_md = "\n".join(rows) if total else "_No problems yet. Run `./scripts/new.sh` to add one._"

    with open(README, encoding="utf-8") as f:
        content = f.read()
    content = replace_between(content, "STATS", stats_md)
    content = replace_between(content, "TABLE", table_md)
    with open(README, "w", encoding="utf-8") as f:
        f.write(content)
    print("README updated: %d problem(s)." % total)


if __name__ == "__main__":
    main()
