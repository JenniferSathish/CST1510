# Week 7 — Strings and Text Manipulation

**Box we build this week:** `INPUT, deepened` — see `../system_diagram.md`

The last week of CW1's toolkit-building — from Week 8 the format changes: one
project, started in the lab, grown for the rest of term. See
**`../RESOURCES/cw2-project-brief.md`** to preview what's coming, but nothing
here needs to be kept or set up specially — this week works exactly like
Weeks 1–6.

---

## By the end of this week you can

1. Normalise text with `.lower()`, `.upper()` and `.title()`
2. Remove stray whitespace with `.strip()`, `.lstrip()` and `.rstrip()`
3. Check for and locate substrings with `in` and `.find()`
4. Swap text with `.replace()`, and check edges with `.startswith()`/`.endswith()`
5. Split text properly — with no separator, a separator, and a `maxsplit` limit
6. Rebuild text with `.join()` and f-strings
7. Parse one raw, messy real-world line into a clean dict — and know which
   error means what when a line does not parse

---

## Workshop — 2 hours

| Time | | Open |
|------|---|---|
| 0:00 | **Run the demo** — a preview of next week's real project: cleaning messy text | `DEMO/ops_console.py` |
| 0:10 | **The system diagram** — INPUT, deepened; a look ahead to Week 8 | `../system_diagram.md` |
| 0:20 | Topic 1 — Case and Whitespace | `01 - .../W07T01_walkthrough.ipynb` |
| 0:40 | Topic 2 — Searching and Replacing | `02 - .../W07T02_walkthrough.ipynb` |
| 1:00 | **Break** | |
| 1:10 | Topic 3 — Splitting, Joining and Building Strings | `03 - .../W07T03_walkthrough.ipynb` |
| 1:30 | Topic 4 — Parsing Real Text | `04 - .../W07T04_walkthrough.ipynb` |
| 1:50 | **Brief the mini-project** — built in the lab | `LAB/W07_Lab.ipynb` |

Each topic runs **teach 10 / do 10**. Every walkthrough has a *Your turn* cell after
each idea and a challenge at the end for students who are ahead.

## Lab — 3 hours

Everything is in **`LAB/W07_Lab.ipynb`** — it runs the whole session in order.

| Time | Part |
|------|------|
| 0:00 | Warm-up — fix 3 broken files in `LAB/warmup/` |
| 0:15 | Drills — short tasks on every topic this week, plus two challenges |
| 1:15 | Break |
| 1:25 | Mini-project — `LAB/template.py`, three lanes, three tiers |
| 2:45 | Wrap-up — this week's cheat sheet notes, photographed into the notebook · commit and push |

---

## Contents — 23 files

| | What | Used |
|---|---|---|
| `README.md` | this file | you |
| `EXTRA_PROJECTS.md` | optional extra practice projects, beyond the lab | if you want more reps |
| `DEMO/ops_console.py` | a preview of Week 8's real project, this week's tools only | workshop 0:00 |
| `01 - Case and Whitespace/` | walkthrough + 2 examples | workshop / revision |
| `02 - Searching and Replacing/` | walkthrough + 2 examples | workshop / revision |
| `03 - Splitting, Joining and Building Strings/` | walkthrough + 2 examples | workshop / revision |
| `04 - Parsing Real Text/` | walkthrough + 3 examples + sample data | workshop / revision |
| `LAB/W07_Lab.ipynb` | warm-up, drills, mini-project, cheat sheet, git | lab |
| `LAB/template.py` | the mini-project scaffold | lab |
| `LAB/messy_lines.txt` | sample messy data for the drills | lab |
| `LAB/warmup/` | 3 deliberately broken files | lab 0:00 |

---

## Threaded skills this week

| Thread | This week | Where |
|--------|-----------|-------|
| Git | seventh commit and push | `LAB/W07_Lab.ipynb` — Wrap-up |
| Cheat sheet | this week's notes, photographed and pasted into the notebook | `LAB/W07_Lab.ipynb` — Wrap-up |
| Revision questions *(not submitted)* | optional, on paper | `LAB/W07_Lab.ipynb` — Optional revision |
| Debugging | `ValueError` (unpack, and float conversion), `AttributeError` (method on the wrong type) | `LAB/` — Warm-up |
| Domains | *Same idea, three fields* in every walkthrough | all four topics |

## Assessment

Nothing is marked this week. Everything is kept — see the CW1 specification for
what accumulates and when it is submitted.

| Tier | Standard | Indicative |
|------|----------|------------|
| Threshold | drills D1–D3 + Threshold mini-project | pass |
| Typical | + drills D4–D6 + Typical mini-project | mid |
| Excellent | + drill D7 + Excellent mini-project | high |
