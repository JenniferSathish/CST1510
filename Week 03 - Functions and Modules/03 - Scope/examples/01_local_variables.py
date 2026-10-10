"""
LOCAL VARIABLES
===============
A variable created inside a function only exists inside it.
Run:  python 01_local_variables.py
"""

# --- 1. Local means local -----------------------------------------------

def check():
    result = "OK"
    print(result)     # fine - result exists here

check()

# print(result)        # NameError: name 'result' is not defined
                        # result never existed outside check()


# --- 2. Parameters are local too ------------------------------------------

def double(n):
    n = n * 2
    return n

number = 21
print(double(number))   # 42
print(number)            # still 21 - the n inside double is its own copy


# --- 3. Each call gets its own fresh locals --------------------------------

def add_one(n):
    n = n + 1
    return n

print(add_one(5))    # 6
print(add_one(5))    # 6 again - nothing carried over from the last call


# --- 4. Reading an outer variable is fine ------------------------------
# A function CAN read a variable defined outside it, as long as it is not
# also a parameter or created inside the function.

WARNING_AT = 90

def status_of(percent):
    if percent >= WARNING_AT:     # reading WARNING_AT from outside - allowed
        return "WARNING"
    return "OK"

print(status_of(92))


# --- 5. Same idea, three fields ---------------------------------------------
# The wall protects the caller's original value from the function's own work.

def clean_reading(reading):                          # AI / Data Science
    reading = reading.strip().lower()      # only changes the LOCAL copy
    return reading

raw_reading = " Missing "
print(clean_reading(raw_reading))
print(raw_reading)                          # unchanged - the original dataset is safe

def scan_result(status):                              # Cyber Security
    status = "flagged: " + status
    return status

live_status = "clean"
print(scan_result(live_status))
print(live_status)                          # unchanged - the system being checked is untouched

def checked_disk(percent):                            # IT
    percent = min(percent, 100)
    return percent

server_disk = 87
print(checked_disk(server_disk))
print(server_disk)                          # unchanged - the server's own value is untouched


# --- TRY IT ------------------------------------------------------------------
# 1. Uncomment the print(result) line in section 1, run it, read the error.
# 2. Predict, then check: after double(number), is number 42 or still 21?
# 3. Write a function that reads a variable defined above it in the file,
#    without passing it in as a parameter.
