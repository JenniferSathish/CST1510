"""
APPLY AND LAMBDA
=================
A lambda is a def you don't bother naming, for a one-line function you are
only going to use once - usually right inside .apply().
Run:  python 01_apply_and_lambda.py
"""

import pandas as pd

servers = pd.read_csv("servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

# --- 1. .apply() runs a function on every value in a column -----------
# Start with a normal function, the way Week 3 taught it.

def classify(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

servers["status"] = servers["percent"].apply(classify)
print(servers)


# --- 2. lambda writes a small function inline, with no def and no name -----
# lambda parameters: expression        <- that IS the whole function.
# It can only be ONE expression - no if/elif/else statements, no loops.

double = lambda x: x * 2
print(double(21))     # 42 - exactly the same as def double(x): return x * 2


# --- 3. Chained conditional expressions - if/elif/else, as an EXPRESSION ---
# "a if cond1 else b if cond2 else c" reads top to bottom, same order as
# elif - it is just written as one line instead of a block.

servers["status"] = servers["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print(servers)

# This is exactly what classify() did in section 1. lambda only makes sense
# here because the function is small AND only used once, right where you
# need it. classify() is still the better choice if you will reuse it, or
# if the logic needs more than one expression.


# --- 4. sort_values(key=...) - another common lambda spot ------------------

print(servers.sort_values("hostname", key=lambda col: col.str.lower()))


# --- 5. Same idea, three fields ---------------------------------------------

survey_df = pd.DataFrame({"text": [" Yes ", "NO"]})
survey_df["clean_text"] = survey_df["text"].apply(lambda t: t.strip().lower())
print(survey_df)                                                    # AI / Data Science

logins_df = pd.DataFrame({"failed": [1, 5]})
logins_df["flag"] = logins_df["failed"].apply(lambda n: n >= 3)
print(logins_df)                                                    # Cyber Security

hosts_df = pd.DataFrame({"hostname": ["srv-02", "srv-01"]})
print(hosts_df.sort_values("hostname", key=lambda c: c.str.lower()))  # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Write classify as a lambda with a chained conditional, and check it
#    gives the same result as the def version for every row.
# 2. Use .apply() with a lambda to create a column "region_upper" - the
#    region column, in capitals.
# 3. Explain, in one sentence, when you would reach for classify() (a def)
#    instead of a lambda.
