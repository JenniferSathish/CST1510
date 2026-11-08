"""
SUMMARIZING, SAVING AND A FIRST CHART
========================================
Finishing the job: a quick overview, writing the result out, and a first look
at plotting straight from a DataFrame.
Run:  python 02_summarizing_saving_and_charting.py
"""

import pandas as pd
import matplotlib.pyplot as plt

servers = pd.read_csv("servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100
servers["status"] = servers["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# --- 1. describe() - a quick statistical overview of the numeric columns ---

print(servers.describe())


# --- 2. value_counts() - how many of each status ---------------------------

print(servers["status"].value_counts())


# --- 3. Saving the result -----------------------------------------------

servers.to_csv("servers_report.csv", index=False)
print("saved servers_report.csv")


# --- 4. A first chart, straight off a DataFrame ------------------------
# In a notebook, this line alone shows the chart. In a plain script you need
# to save or show it explicitly - see below.

servers["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig("status_counts.png")     # in a notebook: plt.show() instead
print("saved status_counts.png")


# --- TRY IT ------------------------------------------------------------------
# 1. Use describe() on just the "percent" column on its own.
# 2. Make a bar chart of servers per region instead of per status.
# 3. Save a second CSV containing only the OVER LIMIT rows.
