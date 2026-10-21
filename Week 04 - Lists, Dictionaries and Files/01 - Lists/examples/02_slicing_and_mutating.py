"""
SLICING AND MUTATING
=====================
Taking a piece of a list, and changing one in place.
Run:  python 02_slicing_and_mutating.py
"""

# --- 1. Slicing - same rule as range(): stop is never included --------------

values = [10, 20, 30, 40, 50]

print(values[1:3])     # [20, 30]     - index 1 up to (not including) 3
print(values[:2])       # [10, 20]     - from the start
print(values[2:])       # [30, 40, 50] - to the end
print(values[:])         # [10, 20, 30, 40, 50] - a full copy


# --- 2. Lists are mutable - strings are not -----------------------------
# You can change an item in place, by index.

values[0] = 99
print(values)     # [99, 20, 30, 40, 50]

# name = "abc"
# name[0] = "z"      # TypeError - strings cannot be changed this way


# --- 3. append adds one item to the end ---------------------------------

labels = ["R-001", "R-002"]
labels.append("R-003")
print(labels)     # ['R-001', 'R-002', 'R-003']


# --- 4. remove takes one item out, by value -----------------------------

labels.remove("R-001")
print(labels)     # ['R-002', 'R-003']

# labels.remove("R-999")   # ValueError - it is not in the list


# --- 5. in checks whether a value is present -----------------------------

print("R-002" in labels)     # True
print("R-999" in labels)     # False


# --- TRY IT ------------------------------------------------------------------
# 1. Given values = [5, 10, 15, 20, 25], slice out just the middle three.
# 2. Append a value to a list, then remove a different one. Print the result
#    after each step.
# 3. Predict, then check: what happens if you remove() a value that appears
#    twice in the list?
