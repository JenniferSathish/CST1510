"""
SORTING
========
Ordering rows by one or more columns.   Run:  python 02_sorting.py
"""

import pandas as pd

servers = pd.read_csv("servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

# --- 1. sort_values - smallest to largest by default -----------------

print(servers.sort_values("percent"))


# --- 2. Largest first -----------------------------------------------------

print(servers.sort_values("percent", ascending=False))


# --- 3. Sorting by more than one column --------------------------------
# Sorts by the first column, then breaks ties using the second.

print(servers.sort_values(["region", "percent"]))


# --- 4. Sorting does not change the row labels ---------------------------
# Notice the index column on the left - it stays with its row, even after
# sorting. reset_index(drop=True) renumbers it if you want that instead.

sorted_servers = servers.sort_values("percent").reset_index(drop=True)
print(sorted_servers)


# --- TRY IT ------------------------------------------------------------------
# 1. Sort servers by "used", largest first.
# 2. Sort by "region", then by "used" within each region, smallest first.
# 3. Find the single highest-percent row using sort_values and .iloc[0] -
#    or look up whether pandas has a more direct way to ask "which row is
#    the maximum".
