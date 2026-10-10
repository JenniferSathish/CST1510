"""
IMPORT
======
Using functions someone else already wrote.   Run:  python 01_import.py
"""

# --- 1. import brings in a whole module -------------------------------------
# Access what is inside it with a dot.

import math

print(math.sqrt(16))     # 4.0
print(math.pi)            # 3.141592653589793
print(math.ceil(4.2))     # 5 - rounds up
print(math.floor(4.8))    # 4 - rounds down


# --- 2. random - another module in the standard library ---------------------

import random

print(random.randint(1, 6))     # a whole number, 1 to 6 inclusive
print(random.choice(["OK", "WARNING", "OVER LIMIT"]))


# --- 3. Modules are just files of functions ----------------------------------
# math and random ship with Python - the "standard library". Nothing to
# install. pandas, which you will meet soon, does not - that has to be
# installed first with pip. Same import keyword either way.


# --- 4. Same idea, three fields ---------------------------------------------
# Same keyword, three modules from the standard library.

import statistics                                              # AI / Data Science
readings = [23.7, 21.0, 24.5, 22.1]
print(statistics.mean(readings), statistics.median(readings))

import hashlib                                                  # Cyber Security
print(hashlib.sha256(b"password123").hexdigest())

import datetime                                                 # IT
print(datetime.datetime.now().isoformat())


# --- TRY IT ------------------------------------------------------------------
# 1. Use math to calculate the area of a circle with radius 5 (area = pi * r ** 2).
# 2. Use random.randint to simulate rolling two dice and print their total.
# 3. Look up one more function in the math module you have not used before
#    and try it.
