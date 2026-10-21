"""
LISTS AND INDEXING
===================
One variable holds one value. A list holds many, in order.
Run:  python 01_lists_and_indexing.py
"""

# --- 1. Creating a list -----------------------------------------------------

labels = ["R-001", "R-002", "R-003"]
print(labels)
print(type(labels))


# --- 2. Indexing - counting from 0, same as range() ---------------------

print(labels[0])     # R-001 - the first
print(labels[1])     # R-002
print(labels[2])     # R-003
# print(labels[3])    # IndexError - there is no fourth item


# --- 3. Negative indexing - counting from the end ---------------------------

print(labels[-1])    # R-003 - the last, without knowing how many there are
print(labels[-2])    # R-002


# --- 4. len() tells you how many ---------------------------------------------

print(len(labels))            # 3
print(labels[len(labels) - 1])  # the last item, the long way
print(labels[-1])                # the same thing, the short way


# --- 5. A list can hold anything, including mixed types ---------------------
# In practice you will keep one list's items the same type - it stays
# predictable that way.

values = [87.0, 120.0, 45.0]
mixed = ["R-001", 87.0, True]     # legal, but avoid this in real code


# --- 6. List comprehensions - building a new list in one line ---------------

doubled = []
for v in values:
    doubled.append(v * 2)
print(doubled)                       # [174.0, 240.0, 90.0]

doubled = [v * 2 for v in values]    # the same thing, one line
print(doubled)                       # [174.0, 240.0, 90.0]

big_values = [v for v in values if v >= 50]   # filter as you build
print(big_values)                    # [87.0, 120.0]

# WATCH OUT: this builds a list, it does not print one - assign it or print it.
# [print(v) for v in values]   # works, but is not what comprehensions are for


# --- 7. Same idea, three fields ---------------------------------------------

readings = [21.4, 22.0, 23.7, 21.9]          # AI / Data Science - one sensor, over a day
print(readings[0], readings[-1])

failed_ips = ["10.0.0.5", "10.0.0.9"]        # Cyber Security - failed logins in the last hour
print(len(failed_ips), "failed logins this hour")

due_tonight = ["srv-01", "srv-02", "srv-03"]  # IT - hostnames due for a check tonight
print(due_tonight[0], "is first on the list")


# --- TRY IT ------------------------------------------------------------------
# 1. Create a list of your own with 4 values. Print the first and the last
#    using indexing.
# 2. Predict, then check: what does labels[-1] give you if labels has 1 item?
# 3. Trigger an IndexError on purpose, read it, then fix it.
