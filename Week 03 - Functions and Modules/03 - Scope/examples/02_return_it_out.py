"""
GETTING A CHANGE BACK OUT
===========================
A function cannot reach out and change your variable for you.
It can only hand you back a new value - you decide what to do with it.
Run:  python 02_return_it_out.py
"""

# --- 1. This looks like it should work. It does not. -----------------------

def add_tax(price):
    price = price * 1.2      # this only changes the LOCAL copy of price
    # no return - nothing comes back

total = 100
add_tax(total)
print(total)                  # still 100 - add_tax's change never left add_tax


# --- 2. The fix: return the new value, and catch it -------------------------

def add_tax(price):
    price = price * 1.2
    return price               # now it comes back out

total = 100
total = add_tax(total)         # catch it and reassign total
print(total)                    # 120.0


# --- 3. Same idea, three values at once -------------------------------------
# You met this in the Week 3 demo. Return more than one value, and unpack
# them into names on the way back out.

def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

difference, percent = check_record(87, 100)
print(difference, percent)


# --- 4. The wall is the whole point -----------------------------------------
# Because check_record cannot reach outside itself, calling it can never
# accidentally break something unrelated elsewhere in the program. That is
# not a limitation - it is what makes a function safe to call from anywhere.


# --- TRY IT ------------------------------------------------------------------
# 1. Write increment(count) that returns count + 1. Use it to increase a
#    variable called total_checked by 1, three times in a row.
# 2. In section 1, the change to price is silently lost - there is no error.
#    Explain why that is more dangerous than an error would be.
