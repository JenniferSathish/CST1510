"""
KEYWORD ARGUMENTS
=================
Naming which parameter you are filling in.   Run:  python 02_keyword_arguments.py
"""

# --- 1. Positional - order decides everything --------------------------------

def status_of(percent, warning_at):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95, 90))            # percent=95, warning_at=90


# --- 2. Keyword - name decides, order stops mattering --------------------

print(status_of(percent=95, warning_at=90))
print(status_of(warning_at=90, percent=95))    # same result, reordered


# --- 3. Mixing positional and keyword ------------------------------------
# Positional arguments must come first, then keyword.

print(status_of(95, warning_at=90))    # fine
# print(status_of(percent=95, 90))     # SyntaxError - keyword before positional


# --- 4. Why bother -------------------------------------------------------
# Once a function has three or more parameters, the call site alone does
# not tell you what each value means. Keywords make it readable again.

def check(value, limit, warning_at):
    pass

# check(87, 100, 90)                      -- what is 90?
# check(87, 100, warning_at=90)           -- immediately clear


# --- TRY IT ------------------------------------------------------------------
# 1. Call status_of using keyword arguments, in the opposite order to how
#    they were defined.
# 2. Write connect(host, port=443, timeout=30) and call it three ways:
#    all positional, all keyword, and mixed.
