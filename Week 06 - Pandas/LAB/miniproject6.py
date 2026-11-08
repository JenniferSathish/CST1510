"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT  
Date  : 11/8/2026

Run it:   miniproject6.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading data from record_sample.csv
df = pd.read_csv("Week 06 - Pandas/LAB/records_sample.csv")

# adding and calc. percent column and status column using .apply() with a lambda instead of def block
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")

# printing the dataframe
print(df)

#filtereing to display rows that are not OK status using boolean indexing
print("\n---------------- status that are not OK -----------------------\n")
print(df[df["status"] != "OK"])

#grouping by status and printing counts per group
print("\n------------ group by status and print count per group --------------\n") 
print([df.groupby("status").size()])

#saving the dataframe to a new CSV
df.to_csv("Week 06 - Pandas/LAB/servers_new.csv", index=False)

#saving one bar chart of the counts per status
df["status"].value_counts().plot(kind="bar", title="server count by status")
plt.show()
