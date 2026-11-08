"""
BOOLEAN FILTERING
===================
This replaces every if statement you have written inside a loop since
Week 2 - one line, no loop.
Run:  python 02_boolean_filtering.py
"""

import pandas as pd

servers = pd.read_csv("servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

# --- 1. A comparison on a column gives back a Series of True/False --------

print(servers["percent"] >= 100)


# --- 2. Putting that Series in [] filters the rows -------------------------
# Compare to Week 4/5: "for record in records: if record.status() ==
# 'OVER LIMIT':". This is the same idea, no loop.

over_limit = servers[servers["percent"] >= 100]
print(over_limit)


# --- 3. Combining conditions - & and |, NOT and/or --------------------------
# Each comparison needs its own brackets.

east_over = servers[(servers["region"] == "east") & (servers["percent"] >= 90)]
print(east_over)

# servers[servers["region"] == "east" and servers["percent"] >= 90]
# ValueError: The truth value of a Series is ambiguous.
# "and" does not work element-by-element on a Series - use &.


# --- 4. isin() - checking against several values at once --------------------

target_regions = servers[servers["region"].isin(["east", "north"])]
print(target_regions)


# --- 5. Same idea, three fields ---------------------------------------------

survey_df = pd.DataFrame({"row": [1, 2, 3], "missing": [0, 2, 0]})
print(survey_df[survey_df["missing"] > 0])                          # AI / Data Science

logins_df = pd.DataFrame({"ip": ["10.0.0.5", "10.0.0.9"], "failed_logins": [5, 1]})
print(logins_df[logins_df["failed_logins"] >= 3])                   # Cyber Security

disk_df = pd.DataFrame({"hostname": ["srv-01", "srv-02"], "used_pct": [92, 40]})
print(disk_df[disk_df["used_pct"] >= 90])                           # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Filter servers to just the rows where region is "west".
# 2. Filter to rows where percent is between 90 and 100, using & and brackets
#    around each comparison.
# 3. Predict, then check: what does servers[servers["region"] == "south"]
#    give you, given there is no "south" in the data?
