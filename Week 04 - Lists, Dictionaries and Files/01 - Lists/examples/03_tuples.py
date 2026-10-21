"""
TUPLES
======
Like a list, but locked.   Run:  python 03_tuples.py
"""

# --- 1. Same brackets style, indexing and slicing work the same -------------

point = (3, 7)
print(point[0])     # 3
print(point[1])      # 7
print(point[0:1])     # (3,) - slicing a tuple gives back a tuple


# --- 2. Cannot be changed after creation ------------------------------------

# point[0] = 5
# TypeError: 'tuple' object does not support item assignment

# No .append(), no .remove() either - a tuple has no methods that change it.


# --- 3. You have already used one, without the name -------------------------
# Week 3's return sent back more than one value at once. That was a tuple.

def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent          # <- this builds a tuple: (difference, percent)

result = check_record(87, 100)
print(result)                # (-13.0, 87.0)
print(type(result))           # <class 'tuple'>

difference, percent = check_record(87, 100)   # <- this unpacks the tuple
print(difference, percent)


# --- 4. Why lock it -----------------------------------------------------
# A tuple signals intent: this collection of values belongs together and is
# not meant to change. A coordinate, an RGB colour, a fixed (label, value,
# limit) triple - all better as tuples than lists, precisely because nothing
# should accidentally mutate them later.

RED = (255, 0, 0)
# RED[0] = 200   # not allowed - and that is the point


# --- TRY IT ------------------------------------------------------------------
# 1. Create a tuple (label, value, limit) for one record. Try to change one
#    item and read the error.
# 2. Predict, then check: what does list((1, 2, 3)) give you? What about
#    tuple([1, 2, 3])?
# 3. Explain, in one sentence, why a function returning multiple values
#    naturally uses a tuple rather than a list.
