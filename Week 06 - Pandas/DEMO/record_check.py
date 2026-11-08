"""
RECORD CHECK  -  Week 6 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions
    Week 3   it is built from functions
    Week 4   it reads many records from a file
    Week 5   it becomes a reusable component
    Week 6   it does the whole job in a few lines      <- this version

Every week so far has hand-built the same three things: read the records,
work out a status for each, report a summary. This is the exact same job as
Week 5's RecordChecker class - reading, deciding, reporting, counting - done
with pandas instead of your own loop and your own class.

One line uses an idea from Topic 4 (a lambda) and is marked.
"""

import pandas as pd

df = pd.read_csv("records.csv")

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(                                   # <- Topic 4
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print(df)

over_limit = df[df["status"] == "OVER LIMIT"]
print(f"\nChecked {len(df)} records. {len(over_limit)} were over limit.")

print("\nBy status:")
print(df["status"].value_counts())

df.to_csv("report.csv", index=False)
print("\nSaved report.csv")
