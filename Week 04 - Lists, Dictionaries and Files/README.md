# Week 4 — Lists, Dictionaries and Files

**Box we build this week:** `STORE` — see `../system_diagram.md`

---

## By the end of this week you can

1. Create a list, index into it, slice it, and change it in place
2. Loop over a list directly, without counting
3. Build a new list from an old one in one line, with a list comprehension
4. Create a tuple, and explain why it cannot be changed once made
5. Create a dictionary and access, add and update its values by key
6. Loop over a dictionary's keys, values, or both at once
7. Build a dictionary from two separate lists, with `zip()`
8. Create a set, and use it to find unique values or check membership quickly
9. Read from and write to a file safely, using `with`
10. Read a file line by line and turn each line into a record
11. Catch a specific error with `try`/`except` instead of letting it crash the program
12. Combine everything into the shape most real data comes in: a list of dicts, loaded safely from a file

---

## Workshop — 2 hours

| Time | | Open |
|------|---|---|
| 0:00 | **Run the demo** — same problem, now reading many records from a file | `DEMO/record_check.py` |
| 0:10 | **The system diagram** — this week's box is `STORE` | `../system_diagram.md` |
| 0:20 | Topic 1 — Lists | `01 - Lists/W04T01_walkthrough.ipynb` |
| 0:36 | Topic 2 — Dictionaries | `02 - Dictionaries/W04T02_walkthrough.ipynb` |
| 0:52 | **Break** | |
| 1:02 | Topic 3 — Files | `03 - Files/W04T03_walkthrough.ipynb` |
| 1:18 | Topic 4 — Handling Errors | `04 - .../W04T04_walkthrough.ipynb` |
| 1:34 | Topic 5 — Putting It Together | `05 - .../W04T05_walkthrough.ipynb` |
| 1:50 | **Brief the mini-project** — built in the lab | `LAB/W04_Lab.ipynb` |

Five topics this week, not four — each now runs **~16 min** instead of 20 (teach
10 / do 6), to fit the new Handling Errors topic into the same 2-hour workshop
without extending it. Every walkthrough still has a *Your turn* cell after each
idea and a challenge at the end for students who are ahead.

## Lab — 3 hours

Everything is in **`LAB/W04_Lab.ipynb`** — it runs the whole session in order.

| Time | Part |
|------|------|
| 0:00 | Warm-up — fix 3 broken files in `LAB/warmup/` |
| 0:15 | Drills — short tasks on every topic this week, plus two challenges |
| 1:15 | Break |
| 1:25 | Mini-project — `LAB/template.py`, three lanes, three tiers |
| 2:45 | Wrap-up — this week's cheat sheet notes, photographed into the notebook · commit and push |

---

## Contents — 29 files

| | What | Used |
|---|---|---|
| `README.md` | this file | you |
| `EXTRA_PROJECTS.md` | optional extra practice projects, beyond the lab | if you want more reps |
| `DEMO/record_check.py` + `DEMO/records.txt` | the finished program, now reading from a file | workshop 0:00 |
| `01 - Lists/` | walkthrough + 3 examples (lists, slicing, tuples) | workshop / revision |
| `02 - Dictionaries/` | walkthrough + 3 examples (dicts, iterating, sets) | workshop / revision |
| `03 - Files/` | walkthrough + 2 examples + sample data | workshop / revision |
| `04 - Handling Errors/` | walkthrough + 2 examples | workshop / revision |
| `05 - Putting It Together/` | walkthrough + 2 examples + sample data | workshop / revision |
| `LAB/W04_Lab.ipynb` | warm-up, drills, mini-project, cheat sheet, git | lab |
| `LAB/template.py` | the mini-project scaffold | lab |
| `LAB/records_sample.txt` | sample data for the drills | lab |
| `LAB/warmup/` | 3 deliberately broken files | lab 0:00 |

**Lists and Dictionaries carry a third example each** — tuples and sets are taught as
short extensions of those two topics (same session, no extra time slot) rather than
full topics of their own, so the week covers all four core Python data structures
without needing their own topic slots. **Handling Errors is new** — it earns its own
slot because it is a real skill in its own right, not just an extension of Files.

---

## Threaded skills this week

| Thread | This week | Where |
|--------|-----------|-------|
| Git | fourth commit and push | `LAB/W04_Lab.ipynb` — Wrap-up |
| Cheat sheet | this week's notes, photographed and pasted into the notebook | `LAB/W04_Lab.ipynb` — Wrap-up |
| Revision questions *(not submitted)* | optional, on paper | `LAB/W04_Lab.ipynb` — Optional revision |
| Debugging | `IndexError`, `KeyError`, `FileNotFoundError` — and now how to catch one | `LAB/` — Warm-up, Topic 4 |
| Domains | *Same idea, three fields* in every walkthrough | all five topics |

## Assessment

Nothing is marked this week. Everything is kept — see the CW1 specification for what accumulates and when it is submitted.

| Tier | Standard | Indicative |
|------|----------|------------|
| Threshold | drills D1–D3 + Threshold mini-project | pass |
| Typical | + drills D4–D6 + Typical mini-project | mid |
| Excellent | + drill D7 + Excellent mini-project | high |
