"""
.split() - DEEPER
===================
You have used this since Week 4. Here is the rest of it.
Run:  python 01_split_deeper.py
"""

# --- 1. Recap: split on a separator -------------------------------------

line = "srv-01,87,100"
print(line.split(","))     # ['srv-01', '87', '100']


# --- 2. split() with NO argument - splits on whitespace, any amount --------

messy = "srv-01    used=87   total=100"
print(messy.split())     # ['srv-01', 'used=87', 'total=100'] - handles the
                            # extra spaces automatically


# --- 3. maxsplit - stop after N splits ----------------------------------
# Everything after the Nth split stays together, unsplit.

record = "srv-01,used=87,total=100"

print(record.split(","))         # ['srv-01', 'used=87', 'total=100']
print(record.split(",", 1))       # ['srv-01', 'used=87,total=100'] - only
                                     # split once, keep the rest together


# --- 4. Why maxsplit matters - splitting a key=value pair ---------------

piece = "used=87"
key, value = piece.split("=")     # exactly 2 parts expected
print(key, value)

# piece2 = "note=server=east"
# key, value = piece2.split("=")
# ValueError: too many values to unpack (expected 2, got 3) - THREE parts, not two
# Fix: piece2.split("=", 1) -> ['note', 'server=east']


# --- TRY IT ------------------------------------------------------------------
# 1. Split "a   b    c" (uneven spacing) with no argument and see what you get.
# 2. Split "hostname:srv-01:east" so that only the first ":" is used.
# 3. Fix the commented-out ValueError example above using maxsplit.
