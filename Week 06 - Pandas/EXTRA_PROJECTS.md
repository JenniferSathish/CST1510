# Week 6 — Extra Practice Projects

Optional. Beyond the lab. *100 Days of Code* doesn't cover pandas at all
(it's a fundamentals-only course through the material this is drawn
from), so there's nothing to adapt here — these three are written from
scratch, but built the same way everything else this term is: the same
report, three domains. Each is a small, guided EDA (Exploratory Data
Analysis) — nothing fancy, no new library beyond `pandas` and
`matplotlib.pyplot`, which `04 - Apply, Lambda and Finishing Up`
already used for its own chart. Every step below only needs tools this
week (or earlier) has already taught.

An EDA is just: load it, look at it, ask it a few questions, summarise
what you found. That's it — these three walk you through exactly that,
on three small, already-provided CSVs.

---

## Server Fleet Report (IT)

**Data:** `01 - Series and DataFrame/examples/servers.csv` (copy it into
your working folder, or point `pd.read_csv()` at its path) — 10 servers,
3 regions, the same file every topic this week already used.

1. **Load and look.** `pd.read_csv()` it. Print `.head()`, `.dtypes`,
   and `len()`. How many servers, how many columns, what type is each?
2. **Add a column.** `percent = (used / total) * 100` — no loop, the
   whole-column arithmetic from Topic 1.
3. **Ask a question with a filter.** How many servers are at or above
   90%? Use boolean filtering (Topic 2), not a loop.
4. **Ask a question with a group.** What's the average `percent`, per
   region? `.groupby("region")["percent"].mean()`.
5. **Sort it.** Which single server is most at risk? `.sort_values()`,
   descending, take the top row.
6. **Classify it.** Add a `status` column using `.apply()` with a
   lambda: `"OVER LIMIT"` / `"WARNING"` / `"OK"`, same thresholds as
   the walkthrough.
7. **Chart it.** A bar chart of servers per region, or per status —
   `.value_counts().plot(kind="bar")`, `plt.savefig(...)`.
8. **Save it.** Write just the `OVER LIMIT` rows to a new CSV,
   `servers_at_risk.csv`, with `.to_csv(index=False)`.
9. **Write two sentences.** In a comment at the top of your script: what
   did you actually find? (e.g. "west has the highest average usage;
   srv-03 is the single most at-risk server.") An EDA that doesn't end
   in a finding isn't finished.

---

## Survey Results Report (AI / Data Science)

**Data:** `survey_results.csv`, in this week's folder — 10 responses,
3 categories, a `score` column, and an `answered` column (`1` if they
actually answered, `0` if that row is a no-response).

1. **Load and look.** `.head()`, `.dtypes`, `len()`.
2. **Measure the gap.** What percentage of rows have `answered == 0`?
   This is Week 1's `(part / total) * 100`, just counted with a filter
   instead of typed in by hand: `len(df[df["answered"] == 0]) /
   len(df) * 100`.
3. **Filter it clean.** Build a second DataFrame containing only the
   rows where `answered == 1` — everything from here on uses that one,
   not the original.
4. **Group it.** Average `score`, per `category`, on the cleaned data.
5. **Sort it.** Which category has the strongest average score?
6. **Classify it.** Add a `result` column with `.apply()` and a lambda:
   `"Pass"` if `score >= 60`, else `"Fail"`.
7. **Chart it.** A bar chart of pass/fail counts —
   `.value_counts().plot(kind="bar")`, saved with `plt.savefig(...)`.
8. **Save it.** Write the cleaned, classified DataFrame to
   `survey_results_clean.csv`.
9. **Write two sentences.** What's the actual finding — which category
   is strongest, and what fraction of responses had to be dropped as
   unanswered?

---

## Login Attempts Report (Cyber Security)

**Data:** `login_attempts.csv`, in this week's folder — 10 login
sessions, some IPs appearing more than once, an `attempts` and a
`failed` count per row.

1. **Load and look.** `.head()`, `.dtypes`, `len()`.
2. **Ask a question with a filter.** Which rows had 3 or more failed
   attempts in a single session? Boolean filtering, same shape as
   Topic 2's `over_limit` example.
3. **Ask a question with a group.** Total `failed` attempts, per `ip` —
   remember some IPs show up in more than one row, so this is a real
   `groupby()`, not just reading one row off.
4. **Sort it.** Which single IP has the most total failed attempts
   across all its sessions?
5. **Flag it.** Add a `suspicious` column with `.apply()` and a lambda:
   `True` if that row's `failed >= 3`, else `False`.
6. **Chart it.** A bar chart of failed attempts per `ip` (group first,
   then `.plot(kind="bar")`), saved with `plt.savefig(...)`.
7. **Save it.** Write only the `suspicious == True` rows to
   `flagged_ips.csv`.
8. **Write two sentences.** Which IP would you escalate first, and why
   — total failures, or attempts in one sitting?

---

Stuck on `&`/`|` instead of `and`/`or` when combining two filters?
That's `02 - Selecting and Filtering`, section 3, in this folder. Stuck
on a chart not appearing when you run a `.py` file (instead of a
notebook)? Check you called `plt.savefig(...)`, not just built the
chart — `04 - Apply, Lambda and Finishing Up`, section 4, explains why.
