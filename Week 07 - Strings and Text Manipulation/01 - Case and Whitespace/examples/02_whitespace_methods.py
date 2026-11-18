"""
WHITESPACE METHODS
====================
The single most important cleaning step for real text.
Run:  python 02_whitespace_methods.py
"""

# --- 1. Real text arrives with stray whitespace ------------------------

raw = "  srv-01  "
print(f"[{raw}]")            # [  srv-01  ] - spaces you cannot see in print()


# --- 2. .strip() removes it from both ends ------------------------------

clean = raw.strip()
print(f"[{clean}]")          # [srv-01]


# --- 3. .lstrip() and .rstrip() - one side only -------------------------

print(f"[{raw.lstrip()}]")     # [srv-01  ] - left only
print(f"[{raw.rstrip()}]")      # [  srv-01] - right only


# --- 4. .strip() can remove specific characters, not just spaces -----------

messy = "***srv-01***"
print(messy.strip("*"))     # srv-01 - strips "*" from both ends only


# --- 5. Chaining - strip then lower, in one line --------------------------

field = "  SRV-01  "
print(field.strip().lower())     # srv-01


# --- 6. Why this matters for comparisons ------------------------------

user_input = "  srv-01  "
known_hosts = ["srv-01", "srv-02"]

print(user_input in known_hosts)              # False - the spaces break it
print(user_input.strip() in known_hosts)       # True


# --- 7. Same idea, three fields ---------------------------------------------

answer = "  Yes  "
print(answer.strip().lower() == "yes")                 # AI / Data Science

blocklist = ["10.0.0.5"]
raw_ip = " 10.0.0.5 "
print(raw_ip.strip() in blocklist)                      # Cyber Security

known_hostnames = ["srv-01"]
raw_hostname = " SRV-01 "
print(raw_hostname.strip().lower() in known_hostnames)  # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Given "   R-004   ", print it with the whitespace removed.
# 2. Given "///R-004///", strip just the "/" characters.
# 3. Chain .strip() and .upper() in one line on a value of your choosing.
