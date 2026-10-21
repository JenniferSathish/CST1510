"""
SETS
====
Only unique values, no order, no indexing.   Run:  python 03_sets.py
"""

# --- 1. Creating a set ------------------------------------------------------

labels = ["R-001", "R-002", "R-001", "R-003", "R-002"]
unique_labels = set(labels)

print(unique_labels)          # duplicates gone - order not guaranteed
print(len(unique_labels))      # 3, not 5


# --- 2. The {} trap -----------------------------------------------------
# {} on its own is an empty DICT, not an empty set. This catches everyone once.

empty_dict = {}
empty_set = set()

print(type(empty_dict))     # <class 'dict'>
print(type(empty_set))       # <class 'set'>


# --- 3. Fast membership checks ------------------------------------------
# Checking "is this value in here" is far quicker on a set than a list, once
# there are a lot of values - worth knowing even before it matters at scale.

blocked_ips = {"10.0.0.5", "10.0.0.9", "192.168.1.1"}

print("10.0.0.5" in blocked_ips)     # True
print("10.0.0.6" in blocked_ips)      # False


# --- 4. No indexing --------------------------------------------------------
# A set has no order, so there is no "first item".

# print(unique_labels[0])
# TypeError: 'set' object is not subscriptable

for label in unique_labels:     # looping works fine - just not in a fixed order
    print(label)


# --- 5. Set operations ------------------------------------------------------
# Sets support & (intersection), | (union), - (difference) - useful for
# comparing two collections.

todays_ips = {"10.0.0.5", "10.0.0.6", "10.0.0.9"}

print(todays_ips & blocked_ips)   # {'10.0.0.5', '10.0.0.9'} - in both
print(todays_ips - blocked_ips)    # {'10.0.0.6'} - in today's, not blocked


# --- TRY IT ------------------------------------------------------------------
# 1. Given a list with some repeated values, use a set to find out how many
#    unique values it contains.
# 2. Given two lists of IPs, use sets to find which addresses appear in both.
# 3. Predict, then check: what does {1, 1, 2, 2, 3} give you when printed?
