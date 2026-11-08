"""
GROUPBY AND AGGREGATING
==========================
Answering "one number per group" questions without writing the loop yourself.
Run:  python 01_groupby_and_agg.py
"""

import pandas as pd

servers = pd.read_csv("servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

# --- 1. groupby splits the rows into groups ---------------------------

grouped = servers.groupby("region")
print(grouped)     # a groupby object - nothing happens until you ask for something


# --- 2. Then you ask for a number per group -----------------------------

print(grouped["percent"].mean())     # average percent, per region
print(grouped["percent"].max())       # highest percent, per region
print(grouped.size())                  # how many rows in each group


# --- 3. .agg() - more than one summary at once -----------------------------

print(grouped["percent"].agg(["mean", "max", "min"]))


# --- 4. value_counts() - counting a categorical column directly ------------
# A shortcut for groupby(...).size() on a single column.

print(servers["region"].value_counts())


# --- 5. Same idea, three fields ---------------------------------------------

scores = pd.DataFrame({"class": ["A", "A", "B"], "score": [80, 90, 70]})
print(scores.groupby("class")["score"].mean())                       # AI / Data Science

attempts = pd.DataFrame({"ip": ["10.0.0.5", "10.0.0.5", "10.0.0.9"], "failed": [1, 1, 1]})
print(attempts.groupby("ip")["failed"].count())                      # Cyber Security

disks = pd.DataFrame({"region": ["east", "east", "west"], "used_pct": [90, 80, 40]})
print(disks.groupby("region")["used_pct"].mean())                    # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Group by "region" and print the total "used" per region.
# 2. Use .agg() to get both the mean and the count of "percent" per region,
#    in one call.
# 3. Predict, then check: does value_counts() sort the results, and in
#    which order?
