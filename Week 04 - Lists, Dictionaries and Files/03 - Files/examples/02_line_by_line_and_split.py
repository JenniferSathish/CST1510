"""
LINE BY LINE, AND SPLITTING A LINE
=====================================
The way you will actually process a file of records.
Run:  python 02_line_by_line_and_split.py
(needs sample_records.txt in the same folder)
"""

# --- 1. Looping over a file gives you one line at a time --------------------

with open("sample_records.txt") as f:
    for line in f:
        print(line)

# Notice the blank-looking extra line between each - every line from a file
# still has its "\n" on the end. print() then adds another.


# --- 2. .strip() removes it -----------------------------------------------

with open("sample_records.txt") as f:
    for line in f:
        print(line.strip())     # no more gaps


# --- 3. .split(",") turns one line into several values ----------------------

line = "R-001,87,100"
parts = line.split(",")
print(parts)                # ['R-001', '87', '100']
print(type(parts))           # list

label, value, limit = parts   # unpacking, same idea as Week 3's return values
print(label, value, limit)


# --- 4. Everything from split() is still text - convert what needs it -------

value = float(value)
limit = float(limit)
print(value + limit)    # works now - these are numbers


# --- 5. Putting 1-4 together: one line, fully parsed -------------------------

with open("sample_records.txt") as f:
    for line in f:
        label, value, limit = line.strip().split(",")
        value = float(value)
        limit = float(limit)
        print(label, value, limit)


# --- TRY IT ------------------------------------------------------------------
# 1. Read sample_records.txt and print just the label from each line.
# 2. Read it again, and print the value converted to float, for each line.
# 3. Predict, then check: what does "a,b,c".split(",") give you?
