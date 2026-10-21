"""
WRITING AND READING FILES
============================
Everything so far disappears when the program ends. A file does not.
Run:  python 01_writing_and_reading.py
"""

# --- 1. Writing - "w" mode ------------------------------------------------
# with...as automatically closes the file for you, even if something goes
# wrong partway through. Always use it.

with open("output.txt", "w") as f:
    f.write("R-001\n")
    f.write("R-002\n")
    f.write("R-003\n")

# the file is closed here - as soon as the indented block ends


# --- 2. "w" mode overwrites - every time -----------------------------------
# Run this file twice. output.txt still only has 3 lines, not 6.
# "w" starts the file empty each time you open it this way.


# --- 3. Reading the whole file at once --------------------------------------

with open("output.txt") as f:      # no mode given - "r" (read) is the default
    text = f.read()

print(text)
print(type(text))     # str - the whole file, as one string


# --- 4. "a" mode appends instead of overwriting -----------------------------

with open("output.txt", "a") as f:
    f.write("R-004\n")

with open("output.txt") as f:
    print(f.read())     # now 4 lines


# --- 5. Same idea, three fields ---------------------------------------------

with open("readings.csv", "w") as f:                    # AI / Data Science
    f.write("21.4\n22.0\n23.7\n")
with open("readings.csv") as f:
    print("readings loaded:", f.read().split())

with open("access.log", "w") as f:                       # Cyber Security
    f.write("ok\nok\nFAILED 10.0.0.5\n")
with open("access.log") as f:
    for line in f:
        print(line.strip())

with open("hosts.txt", "w") as f:                        # IT
    f.write("srv-01\nsrv-02\nsrv-03\n")
with open("hosts.txt") as f:
    print("hostnames:", f.read().split())


# --- TRY IT ------------------------------------------------------------------
# 1. Write 3 lines of your own to a new file called my_notes.txt.
# 2. Read my_notes.txt back and print it.
# 3. Predict, then check: what happens if you open a file with "w" that
#    already has content in it?
