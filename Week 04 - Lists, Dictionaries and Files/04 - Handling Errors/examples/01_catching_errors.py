"""
CATCHING ERRORS
================
try/except - stopping a specific failure from crashing everything.
Run:  python 01_catching_errors.py
"""

# --- 1. try / except - the basic shape --------------------------------------

try:
    value = int("abc")
except ValueError:
    print("not a whole number - using 0 instead")
    value = 0

print(value)     # 0 - the program kept going


# --- 2. A file that might not exist ------------------------------------------

try:
    with open("missing.txt") as f:
        text = f.read()
except FileNotFoundError:
    print("missing.txt not found - using an empty report instead")
    text = ""

print(repr(text))     # ''


# --- 3. Multiple except blocks - checked in order, first match wins ----------

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("can't divide by zero")
        return None
    except TypeError:
        print("both values need to be numbers")
        return None

print(safe_divide(10, 2))       # 5.0
print(safe_divide(10, 0))       # can't divide by zero -> None
print(safe_divide(10, "two"))   # both values need to be numbers -> None


# --- 4. WATCH OUT: a bare except hides real bugs -----------------------------
# try:
#     result = 10 / 0
# except:                  # catches EVERYTHING - including typos you made
#     print("something went wrong")   # you'll never know what


# --- 5. as e - seeing the actual error message --------------------------------

try:
    int("abc")
except ValueError as e:
    print("caught it:", e)     # caught it: invalid literal for int() with base 10: 'abc'


# --- TRY IT ------------------------------------------------------------------
# 1. Write a function that asks for a number with input() and int(), catching
#    ValueError and asking again if it fails. (Hint: wrap it in a while loop.)
# 2. Trigger a FileNotFoundError on purpose, on a file you know doesn't exist.
#    Read the traceback - which line does Python say the error happened on?
# 3. Add a second except block to section 2 that also catches PermissionError.
