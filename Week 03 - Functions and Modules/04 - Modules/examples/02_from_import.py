"""
FROM ... IMPORT
================
Bringing in one specific name instead of the whole module.
Run:  python 02_from_import.py
"""

# --- 1. from module import name ----------------------------------------------
# No dot needed afterwards - it behaves like a function you wrote yourself.

from math import sqrt

print(sqrt(16))     # 4.0 - not math.sqrt(16)


# --- 2. You can bring in more than one -------------------------------------

from math import sqrt, ceil, floor

print(ceil(4.2))
print(floor(4.8))


# --- 3. The trade-off --------------------------------------------------------
# import math                    -> math.sqrt(16)   always clear where it came from
# from math import sqrt          -> sqrt(16)         shorter, but less obvious
#
# If a file imports from five different modules with "from ... import", a
# reader cannot tell which module a given name came from without checking
# the top of the file. Prefer "import module" once a file starts pulling in
# several things.


# --- 4. Naming collisions ----------------------------------------------------
# "from" brings the name directly into your file. If you already have a
# variable with that name, one of them silently overwrites the other.

floor = 3     # your own variable...
# from math import floor   # ...would silently replace it


# --- TRY IT ------------------------------------------------------------------
# 1. Rewrite one of Topic 4's Topic 1 lines to use "from math import" instead
#    of "import math".
# 2. Explain, in one sentence, when you would choose "import module" over
#    "from module import name".
