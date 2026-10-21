"""
CREATING AND ACCESSING DICTIONARIES
=====================================
A list finds things by position. A dictionary finds things by name.
Run:  python 01_creating_and_accessing.py
"""

# --- 1. Creating a dictionary -------------------------------------------

record = {
    "label": "R-001",
    "value": 87.0,
    "limit": 100.0,
}

print(record)
print(type(record))


# --- 2. Accessing by key, not position ------------------------------------

print(record["label"])     # R-001
print(record["value"])      # 87.0

# print(record["status"])    # KeyError: 'status' - that key does not exist


# --- 3. Adding or updating a key ---------------------------------------
# The same line does both. If the key exists, it updates. If not, it adds.

record["status"] = "OK"       # new key - added
record["value"] = 90.0         # existing key - updated

print(record)


# --- 4. .get() - a safer way to ask for a key that might not exist -----

print(record.get("status"))            # OK
print(record.get("missing"))            # None - no KeyError
print(record.get("missing", "n/a"))      # n/a - your own fallback


# --- 5. Same idea, three fields ---------------------------------------------

dataset = {"rows": 1200, "missing": 13, "source": "survey_2026"}   # AI / Data Science
print(dataset["rows"], "rows,", dataset["missing"], "missing")

incident = {"ip": "10.0.0.5", "failed": 12, "locked": True}         # Cyber Security
print(incident["ip"], "->", incident["failed"], "failed attempts")

server = {"hostname": "srv-01", "used_gb": 87, "total_gb": 120}     # IT
print(server["hostname"], server["used_gb"], "/", server["total_gb"], "GB")


# --- TRY IT ------------------------------------------------------------------
# 1. Create a dict for one record with label, value and limit. Print two of
#    its values.
# 2. Add a fourth key to your dict, then update one of the original three.
# 3. Use .get() to safely check for a key you know does not exist, with a
#    default of your choosing.
