"""
in AND .find()
================
Checking whether text contains something, and where.
Run:  python 01_in_and_find.py
"""

# --- 1. `in` - does this substring appear? ------------------------------

line = "2026-09-08 ERROR failed to connect to srv-01"

print("ERROR" in line)      # True
print("WARNING" in line)     # False


# --- 2. Case matters, same as any comparison ---------------------------

print("error" in line)                # False - different case
print("error" in line.lower())         # True - normalise first


# --- 3. .find() - WHERE it appears, not just whether -----------------------

position = line.find("ERROR")
print(position)     # 11 - the index where "ERROR" starts

missing = line.find("WARNING")
print(missing)        # -1 - not found. NOT an error, NOT None. Check for -1.


# --- 4. `in` for a yes/no answer, .find() when you need the position -------

if "ERROR" in line:
    print("This line has an error.")

position = line.find("srv-")
if position != -1:
    print(f"Hostname starts at position {position}")


# --- TRY IT ------------------------------------------------------------------
# 1. Given log = "2026-09-08 WARNING disk 90% full", check whether it
#    contains "WARNING", case-insensitively.
# 2. Use .find() to locate where "disk" starts in that same string.
# 3. Predict, then check: what does "".find("x") give you?
