# Week 6 — Pandas

**Box we build this week:** `STORE + PROCESS, upgraded` — see `../system_diagram.md`

One more week of toolkit-building after this — Week 7 — before the format
changes and one continuous project starts.

---

## By the end of this week you can

1. Create a Series and a DataFrame, and read a whole file into one with `pd.read_csv()`
2. Add a new column from existing ones, without writing a loop
3. Select rows and columns with `loc`/`iloc`, and filter rows with a boolean condition
4. Group rows and calculate a summary per group with `groupby()` and `.agg()`
5. Sort a DataFrame by one or more columns
6. Write a `lambda`, and explain when it is the right choice over a named function
7. Use `.apply()` with a lambda to build a column from another one
8. Summarise a DataFrame, save it to a file, and produce a first chart directly from it

---

## Workshop — 2 hours

| Time | | Open |
|------|---|---|
| 0:00 | **Run the demo** — same problem, now about ten lines | `DEMO/record_check.py` |
| 0:10 | **The system diagram** — this week's box is `STORE + PROCESS`, upgraded | `../system_diagram.md` |
| 0:20 | Topic 1 — Series and DataFrame | `01 - .../W06T01_walkthrough.ipynb` |
| 0:40 | Topic 2 — Selecting and Filtering | `02 - .../W06T02_walkthrough.ipynb` |
| 1:00 | **Break** | |
| 1:10 | Topic 3 — Grouping, Sorting and Aggregating | `03 - .../W06T03_walkthrough.ipynb` |
| 1:30 | Topic 4 — Apply, Lambda and Finishing Up | `04 - .../W06T04_walkthrough.ipynb` |
| 1:50 | **Brief the mini-project** — built in the lab | `LAB/W06_Lab.ipynb` |

Each topic runs **teach 10 / do 10**. Every walkthrough has a *Your turn* cell after
each idea and a challenge at the end for students who are ahead.

## Lab — 3 hours

Everything is in **`LAB/W06_Lab.ipynb`** — it runs the whole session in order.

| Time | Part |
|------|------|
| 0:00 | Warm-up — fix 3 broken files in `LAB/warmup/` |
| 0:15 | Drills — short tasks on every topic this week, plus two challenges |
| 1:15 | Break |
| 1:25 | Mini-project — `LAB/template.py`, three lanes, three tiers |
| 2:45 | Wrap-up — this week's cheat sheet notes, photographed into the notebook · commit and push |

---

## Contents — 28 files

| | What | Used |
|---|---|---|
| `README.md` | this file | you |
| `EXTRA_PROJECTS.md` | optional extra EDA practice projects, beyond the lab | if you want more reps |
| `survey_results.csv` + `login_attempts.csv` | data for the extra EDA projects | if you want more reps |
| `DEMO/record_check.py` + `DEMO/records.csv` | the finished program, now ~10 lines | workshop 0:00 |
| `01 - Series and DataFrame/` | walkthrough + 2 examples + shared `servers.csv` | workshop / revision |
| `02 - Selecting and Filtering/` | walkthrough + 2 examples + `servers.csv` | workshop / revision |
| `03 - Grouping, Sorting and Aggregating/` | walkthrough + 2 examples + `servers.csv` | workshop / revision |
| `04 - Apply, Lambda and Finishing Up/` | walkthrough + 2 examples + `servers.csv` | workshop / revision |
| `LAB/W06_Lab.ipynb` | warm-up, drills, mini-project, cheat sheet, git | lab |
| `LAB/template.py` | the mini-project scaffold | lab |
| `LAB/records_sample.csv` | sample data for the drills | lab |
| `LAB/warmup/` | 3 deliberately broken files | lab 0:00 |

**All four topics share one `servers.csv`** (10 servers, 3 regions) so filtering,
grouping and sorting all work on data that's actually worth grouping — the record-check
theme continues in the DEMO and mini-project, where it matters most.

---

## Threaded skills this week

| Thread | This week | Where |
|--------|-----------|-------|
| Git | sixth commit and push | `LAB/W06_Lab.ipynb` — Wrap-up |
| Cheat sheet | this week's notes, photographed and pasted into the notebook | `LAB/W06_Lab.ipynb` — Wrap-up |
| Revision questions *(not submitted)* | optional, on paper | `LAB/W06_Lab.ipynb` — Optional revision |
| Debugging | `KeyError` (bad column name), `ValueError` (`and`/`or` on a Series), `TypeError` (arithmetic on text) | `LAB/` — Warm-up |
| Domains | *Same idea, three fields* in every walkthrough | all four topics |

## Assessment

Nothing is marked this week. Everything is kept — see the CW1 specification for
what accumulates and when it is submitted.

| Tier | Standard | Indicative |
|------|----------|------------|
| Threshold | drills D1–D3 + Threshold mini-project | pass |
| Typical | + drills D4–D6 + Typical mini-project | mid |
| Excellent | + drill D7 + Excellent mini-project | high |
