"""
*args AND **kwargs
====================
Accepting an unknown number of arguments.   Run:  python 03_args_and_kwargs.py
"""

# --- 1. *args - collects extra positional arguments into a tuple -----------

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))          # 6
print(total(10, 20, 30, 40))   # 100
print(total())                 # 0 - works with none at all


# --- 2. *args really is just a tuple - loop it, index it -------------------

def describe(*items):
    print(f"{len(items)} item(s): {items}")
    for item in items:
        print(" -", item)

describe("router", "switch", "firewall")


# --- 3. **kwargs - collects extra keyword arguments into a dict ------------

def configure(**settings):
    for key, value in settings.items():
        print(f"{key} = {value}")

configure(host="10.0.0.1", port=8080, ssl=True)


# --- 4. Mixing named parameters with *args and **kwargs ---------------------
# Order matters: normal params, then *args, then **kwargs.

def connect(host, *extra_hosts, **options):
    print("primary host:", host)
    if extra_hosts:
        print("also connecting to:", extra_hosts)
    for key, value in options.items():
        print(f"  option {key} = {value}")

connect("10.0.0.1")
connect("10.0.0.1", "10.0.0.2", "10.0.0.3", timeout=5, retries=3)


# --- WATCH OUT: *args is a tuple, not separate variables --------------------
# numbers = total(1, 2, 3)  does NOT give you numbers[0], numbers[1], numbers[2]
# as three separate variables - inside total(), *numbers IS one tuple (1, 2, 3).


# --- TRY IT ------------------------------------------------------------------
# 1. Write average(*values) that returns the mean of however many numbers it
#    gets. Call it with 3 numbers, then with 6.
# 2. Write log_event(event, **details) that prints the event name, then one
#    line per extra detail passed in as a keyword argument.
# 3. Call connect() from section 4 with a host and three keyword options of
#    your own choosing - predict the output before running it.
