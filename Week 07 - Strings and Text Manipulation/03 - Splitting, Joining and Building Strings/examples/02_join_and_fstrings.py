"""
.join() AND BUILDING STRINGS
===============================
The reverse of split, and putting a clean line back together.
Run:  python 02_join_and_fstrings.py
"""

# --- 1. .join() - a list of strings, glued with a separator -----------

parts = ["srv-01", "87", "100"]
print(",".join(parts))     # srv-01,87,100


# --- 2. The separator can be anything ------------------------------

print(" | ".join(parts))     # srv-01 | 87 | 100
print("".join(parts))          # srv-018 7100 - no separator at all


# --- 3. join() only works on a list of STRINGS ---------------------------

numbers = [87, 100]
# ",".join(numbers)
# TypeError: sequence item 0: expected str instance, int found

print(",".join(str(n) for n in numbers))     # convert first: 87,100


# --- 4. split() then join() - round-tripping ----------------------------

original = "srv-01,used=87,total=100"
pieces = original.split(",")
rebuilt = ",".join(pieces)

print(original == rebuilt)     # True - split and join undo each other


# --- 5. f-strings for building a clean line, review + more -------------

hostname, used, total = "srv-01", 87.0, 100.0

print(f"{hostname:<10} {used:>6.1f}/{total:<6.1f}")     # padded, aligned
print(f"{hostname.upper()}: {used/total*100:.1f}% used")   # a calculation inline


# --- 6. Same idea, three fields ---------------------------------------------

survey_row = "21,yes,london"
age, answer, city = survey_row.split(",")             # AI / Data Science
print(f"{age} year old from {city} answered {answer}")

ip, port = "10.0.0.5:443".split(":")                   # Cyber Security
print(f"host {ip} on port {port}")

key, value = "used=87".split("=")                       # IT
print(f"{key} is {value}")


# --- TRY IT ------------------------------------------------------------------
# 1. Join ["R-001", "R-002", "R-003"] into one line separated by " | ".
# 2. Given percentages = [87.0, 120.0, 45.0], build one comma-separated
#    string of them formatted to 1 decimal place each.
# 3. Explain why ",".join(numbers) fails when numbers is a list of ints.
