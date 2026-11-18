"""
CASE METHODS
=============
Normalizing text so comparisons actually work.   Run:  python 01_case_methods.py
"""

# --- 1. The problem case creates ---------------------------------------

hostname_a = "SRV-01"
hostname_b = "srv-01"

print(hostname_a == hostname_b)   # False - same server, different text


# --- 2. .lower() and .upper() -----------------------------------------

print(hostname_a.lower())     # srv-01
print(hostname_b.upper())      # SRV-01
print(hostname_a.lower() == hostname_b.lower())   # True - now they match


# --- 3. .title() - capitalise each word --------------------------------

name = "record check console"
print(name.title())     # Record Check Console


# --- 4. These return a NEW string - they do not change the original -----
# Same rule as every string method: strings are locked (Week 4).

original = "SRV-01"
lowered = original.lower()

print(original)    # still SRV-01
print(lowered)       # srv-01


# --- TRY IT ------------------------------------------------------------------
# 1. Given ids = ["R-001", "r-002", "R-003"], print all three in lowercase.
# 2. Predict, then check: does "Hello".lower() == "hello".lower() give True?
# 3. Explain why original was unchanged in section 4.
