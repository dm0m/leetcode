# LeetCode

One problem a day — solutions and notes.

Primary language: **Python**. Select problems are also solved in Java, C#, and
others. Following: [NeetCode 150](https://neetcode.io/practice) /
[Grind 75](https://www.techinterviewhandbook.org/grind75).

## Progress

<!-- STATS:START -->
**Total solved:** 5  
🟢 Easy: 4 · 🟡 Medium: 1 · 🔴 Hard: 0  
🔥 **Current streak:** 1 day(s) — last solved 2026-10-28  
**Languages:** Py (5)  
**By status:** solved-independently: 5  
**Top topics:** Array (2), Linked List (2), Recursion (2), Dynamic Programming (1), Hash Table (1), Math (1), Stack (1), String (1)  
<!-- STATS:END -->

## Problems

<!-- TABLE:START -->
| # | Problem | Difficulty | Topics | Solutions | Status | Date |
|---|---------|------------|--------|-----------|--------|------|
| 1 | [Two Sum](problems/0001-two-sum) | 🟢 Easy | Array, Hash Table | Py | solved-independently | 2026-10-23 |
| 2 | [Add Two Numbers](problems/0002-add-two-numbers) | 🟡 Medium | Linked List, Math, Recursion | Py | solved-independently | 2026-10-23 |
| 20 | [Valid Parentheses](problems/0020-valid-parentheses) | 🟢 Easy | Stack, String | Py | solved-independently | 2026-10-25 |
| 21 | [Merge Two Sorted Lists](problems/0021-merge-two-sorted-lists) | 🟢 Easy | Linked List, Recursion | Py | solved-independently | 2026-10-26 |
| 121 | [Best Time To Buy And Sell Stock](problems/0121-best-time-to-buy-and-sell-stock) | 🟢 Easy | Array, Dynamic Programming | Py | solved-independently | 2026-10-28 |
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
