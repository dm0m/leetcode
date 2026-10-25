# LeetCode

One problem a day — solutions and notes.

Primary language: **Python**. Select problems are also solved in Java, C#, and
others. Following: [NeetCode 150](https://neetcode.io/practice) /
[Grind 75](https://www.techinterviewhandbook.org/grind75).

## Progress

<!-- STATS:START -->
**Total solved:** 2  
🟢 Easy: 1 · 🟡 Medium: 1 · 🔴 Hard: 0  
🔥 **Current streak:** 1 day(s) — last solved 2026-10-23  
**Languages:** Py (2)  
**By status:** solved-independently: 2  
**Top topics:** Array (1), Hash Table (1), Linked List (1), Math (1), Recursion (1)  
<!-- STATS:END -->

## Problems

<!-- TABLE:START -->
| # | Problem | Difficulty | Topics | Solutions | Status | Date |
|---|---------|------------|--------|-----------|--------|------|
| 1 | [Two Sum](problems/0001-two-sum) | 🟢 Easy | Array, Hash Table | Py | solved-independently | 2026-10-23 |
| 2 | [Add Two Numbers](problems/0002-add-two-numbers) | 🟡 Medium | Linked List, Math, Recursion | Py | solved-independently | 2026-10-23 |
<!-- TABLE:END -->

## Usage

Add a new problem (Python by default):

```bash
./scripts/new.sh <number> <slug> <difficulty> [topics...]
# e.g.
./scripts/new.sh 1 two-sum easy Array "Hash Table"
```

Start it in several languages at once:

```bash
./scripts/new.sh -l py,java,csharp 1 two-sum easy Array "Hash Table"
```

Add another language to a problem you've already started:

```bash
./scripts/add-lang.sh 1 java
./scripts/add-lang.sh 0001-two-sum csharp cpp
```

Supported: `python java csharp cpp c javascript typescript go rust kotlin ruby`
(aliases like `py`, `js`, `c#` work). Change the default with the
`LC_LEETCODE_LANG` env var.

Then fill in `NOTES.md` and commit:

```bash
git add problems/0001-two-sum
git commit -m "solve: 0001 Two Sum (easy)"
```

`README.md` regenerates automatically. The source of truth is each problem's
`NOTES.md` frontmatter plus the solution files present — never edit the tables
between the `STATS`/`TABLE` markers by hand.
