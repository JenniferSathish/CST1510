"""
loc AND iloc
=============
Selecting rows and columns by label, or by position.
Run:  python 01_loc_and_iloc.py
"""

import pandas as pd

servers = pd.read_csv("servers.csv")

# --- 1. iloc - by position, like list indexing ---------------------------

print(servers.iloc[0])          # the first row
print(servers.iloc[0:3])         # the first 3 rows - same slicing rule as a list


# --- 2. loc - by label ---------------------------------------------------
# With the default index (0, 1, 2, ...) loc looks the same as iloc, but it
# is asking a different question: "give me the row labelled 0", not
# "give me the row in position 0". This matters once you set your own index.

print(servers.loc[0])
print(servers.loc[0, "hostname"])     # one row, one column


# --- 3. Selecting columns -------------------------------------------------

print(servers["hostname"])                 # one column - a Series
print(servers[["hostname", "region"]])       # more than one - a DataFrame


# --- 4. A custom index --------------------------------------------------

by_hostname = servers.set_index("hostname")
print(by_hostname.loc["srv-03"])     # now loc looks up by hostname, not position


# --- TRY IT ------------------------------------------------------------------
# 1. Print rows 2 to 4 (inclusive) using iloc.
# 2. Print just the "region" and "used" columns, for every row.
# 3. Set the index to "hostname" and use loc to look up "srv-07" directly.
