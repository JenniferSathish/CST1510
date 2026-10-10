"""
A small module that 03_main_guard.py imports, to prove the __main__ guard
actually changes what runs. Not meant to be studied on its own - see
03_main_guard.py first.
"""

def is_over_limit(value, limit=100):
    return value >= limit


# This block only runs when checker.py is launched directly with
# `python checker.py` - NOT when another file imports it.
if __name__ == "__main__":
    print("checker.py is running directly - this line only appears here")
    print(is_over_limit(87))    # False
    print(is_over_limit(120))   # True
