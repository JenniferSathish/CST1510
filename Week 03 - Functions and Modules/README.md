# Week 3 — Functions and Modules

**Box we build this week:** `the wiring` — see `../system_diagram.md`

---

## By the end of this week you can

1. Define a function and call it, with and without parameters
2. Explain the difference between `print`ing a value and `return`ing one
3. Give a parameter a default value, and call a function using keyword arguments
4. Write a function that accepts an unknown number of arguments, with `*args` and `**kwargs`
5. Explain why a variable created inside a function cannot be seen outside it
6. Get a value out of a function properly, using `return`, instead of expecting it to change something outside on its own
7. Import and use a function from a module you did not write
8. Document what a function does with a one-line docstring
9. Make a file behave differently when run directly versus imported, with `if __name__ == "__main__":`

---

## Workshop — 2 hours

| Time | | Open |
|------|---|---|
| 0:00 | **Run the demo** — same problem, now built from three named pieces | `DEMO/record_check.py` |
| 0:10 | **The system diagram** — this week's box is `the wiring` | `../system_diagram.md` |
| 0:20 | Topic 1 — Defining and Calling Functions | `01 - .../W03T01_walkthrough.ipynb` |
| 0:40 | Topic 2 — Parameters and Arguments | `02 - .../W03T02_walkthrough.ipynb` |
| 1:00 | **Break** | |
| 1:10 | Topic 3 — Scope | `03 - .../W03T03_walkthrough.ipynb` |
| 1:30 | Topic 4 — Modules | `04 - .../W03T04_walkthrough.ipynb` |
| 1:50 | **Brief the mini-project** — built in the lab | `LAB/W03_Lab.ipynb` |

Each topic runs **teach 10 / do 10**. Every walkthrough has a *Your turn* cell after
each idea and a challenge at the end for students who are ahead.

## Lab — 3 hours

Everything is in **`LAB/W03_Lab.ipynb`** — it runs the whole session in order.

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
| `DEMO/record_check.py` | the finished program, now built from functions | workshop 0:00 |
| `01 - Defining and Calling Functions/` | walkthrough + 2 examples | workshop / revision |
| `02 - Parameters and Arguments/` | walkthrough + 3 examples (incl. `*args`/`**kwargs`) | workshop / revision |
| `03 - Scope/` | walkthrough + 2 examples | workshop / revision |
| `04 - Modules/` | walkthrough + 4 examples (incl. the `__main__` guard + its helper module) | workshop / revision |
| `LAB/W03_Lab.ipynb` | warm-up, drills, mini-project, cheat sheet, git | lab |
| `LAB/template.py` | the mini-project scaffold | lab |
| `LAB/warmup/` | 3 deliberately broken files | lab 0:00 |

**Most topic folders = 3 files** — the walkthrough plus two `examples/` files, each an
~40-line runnable reference that goes deeper than the session does. Topics 2 and 4 carry
an extra example each (`*args`/`**kwargs`, and the `__main__` guard with its own tiny
helper module) — short additions, not full extra topics.

---

## Threaded skills this week

| Thread | This week | Where |
|--------|-----------|-------|
| Git | third commit and push | `LAB/W03_Lab.ipynb` — Wrap-up |
| Cheat sheet | this week's notes, photographed and pasted into the notebook | `LAB/W03_Lab.ipynb` — Wrap-up |
| Revision questions *(not submitted)* | optional, on paper | `LAB/W03_Lab.ipynb` — Optional revision |
| Debugging | `TypeError` (missing argument), `NameError` (scope), `ModuleNotFoundError` | `LAB/` — Warm-up |
| Domains | *Same idea, three fields* in every walkthrough | all four topics |

## Assessment

Nothing is marked this week. Everything is kept — see the CW1 specification for what accumulates and when it is submitted.

| Tier | Standard | Indicative |
|------|----------|------------|
| Threshold | drills D1–D3 + Threshold mini-project | pass |
| Typical | + drills D4–D6 + Typical mini-project | mid |
| Excellent | + drill D7 + Excellent mini-project | high |
