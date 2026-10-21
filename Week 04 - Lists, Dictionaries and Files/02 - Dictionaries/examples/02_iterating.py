"""
ITERATING OVER A DICTIONARY
=============================
Looping over keys, values, or both at once.
Run:  python 02_iterating.py
"""

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

# --- 1. .keys() - just the names --------------------------------------

for key in record.keys():
    print(key)

# for key in record:    # does the same thing - .keys() is the default
#     print(key)


# --- 2. .values() - just the values -----------------------------------

for value in record.values():
    print(value)


# --- 3. .items() - both at once, as pairs -------------------------------
# This is the one you will use most.

for key, value in record.items():
    print(f"{key}: {value}")


# --- 4. Building a report line from a dict --------------------------------

for key, value in record.items():
    print(f"  {key:<10}: {value}")


# --- 5. zip() - building a dict from two separate lists ---------------------

hostnames = ["srv-01", "srv-02", "srv-03"]
disk_used = [87, 45, 120]

usage = dict(zip(hostnames, disk_used))
print(usage)                  # {'srv-01': 87, 'srv-02': 45, 'srv-03': 120}
print(usage["srv-02"])         # 45

# WATCH OUT: different lengths - zip() stops at the shorter list, no error.
print(dict(zip(["a", "b", "c"], [1, 2])))   # {'a': 1, 'b': 2} - 'c' silently dropped


# --- TRY IT ------------------------------------------------------------------
# 1. Loop over your own dict from Topic 2's first example using .items() and
#    print "key: value" for each pair.
# 2. Predict, then check: what does list(record.keys()) give you?
# 3. Write a loop that prints only the numeric values from a dict (hint:
#    check the type of each value as you go).
