"""
THE __main__ GUARD
====================
Making a file behave differently depending on whether it's run directly or
imported. Run this file, then also run checker.py on its own and compare.
Run:  python 03_main_guard.py
Then:  python checker.py
"""

# --- 1. Importing checker.py - its __main__ block does NOT run from here ----

print("--- importing checker ---")
import checker
print("--- back in 03_main_guard.py ---")

# checker's function is still perfectly usable, even though its test prints
# (inside ITS OWN __main__ guard) never ran when we just imported it.
print(checker.is_over_limit(87))     # False
print(checker.is_over_limit(120))    # True


# --- 2. Your own file can do the same thing ----------------------------------

def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

if __name__ == "__main__":
    print(area_of_circle(5))    # only prints when THIS file is run directly


# --- TRY IT ------------------------------------------------------------------
# 1. Run this file (python 03_main_guard.py). Confirm checker.py's own guarded
#    prints ("checker.py is running directly...") never appear - only this
#    file's own output does.
# 2. Now run checker.py on its own (python checker.py). Its guarded prints DO
#    appear this time - same file, different behaviour, depending on how it
#    was started.
# 3. Add a print() inside checker.py, OUTSIDE its __main__ guard. Run this
#    file again - does that new print appear now? Why?
