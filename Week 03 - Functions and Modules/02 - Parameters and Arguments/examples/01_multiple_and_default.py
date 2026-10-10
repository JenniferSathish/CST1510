"""
MULTIPLE PARAMETERS AND DEFAULTS
=================================
More than one input, and inputs that don't always need to be given.
Run:  python 01_multiple_and_default.py
"""

# --- 1. Multiple parameters, matched by position -----------------------------

def within_limit(value, limit):
    return value <= limit

print(within_limit(87, 100))    # value=87, limit=100 - matched by position
print(within_limit(100, 87))    # swapped - a completely different answer


# --- 2. A default value is a fallback -----------------------------------------
# Give a parameter = something in the def line, and callers can leave it out.

def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95))              # warning_at not given - uses the default, 90
print(status_of(95, 96))          # warning_at given - overrides the default


# --- 3. Defaults must come after non-defaults ---------------------------------
# This is not a style choice - Python enforces it.

# def broken(warning_at=90, percent):   # SyntaxError: non-default argument
#     ...                                # follows default argument


# --- 4. Same idea, three fields ---------------------------------------------
# A default is a sensible fallback the caller can still override.

def load(path, header=True):                                # AI / Data Science
    return f"loading {path} (header={header})"

def scan(target, timeout=5):                                 # Cyber Security
    return f"scanning {target} (timeout={timeout}s)"

def backup(source, destination="/backups"):                  # IT
    return f"backing up {source} to {destination}"

print(load("survey_2026.csv"))
print(scan("10.0.0.5"))
print(backup("srv-01", destination="/mnt/backups"))


# --- TRY IT ------------------------------------------------------------------
# 1. Write report_line(label, value, width=10) that returns label followed by
#    value right-aligned in width characters. Call it once using the default
#    width and once overriding it.
# 2. Predict, then check: status_of(89) and status_of(89, 85)
