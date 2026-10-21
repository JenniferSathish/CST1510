"""
LOAD AND PROCESS
=================
The full shape: read a file, build a list of dicts, process each one.
This is exactly what this week's DEMO does.
Run:  python 02_load_and_process.py
(needs sample_records.txt in the same folder)
"""

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


# --- 1. Loading turns a file into a list of dicts ---------------------------

records = load_records("sample_records.txt")
print(records)
print(len(records), "records loaded")


# --- 2. Processing each one --------------------------------------------------

for record in records:
    percent = (record["value"] / record["limit"]) * 100
    status = "OVER LIMIT" if percent >= 100 else "OK"
    print(f"{record['label']}: {status}")


# --- 3. Building a summary as you go -----------------------------------------

over_limit_count = 0

for record in records:
    percent = (record["value"] / record["limit"]) * 100
    if percent >= 100:
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} were over limit")


# --- TRY IT ------------------------------------------------------------------
# 1. Add a WARNING tier (90% or more) to the loop in section 2.
# 2. Write your own load_records-style function for a file with a different
#    number of fields per line.
# 3. Change the loop in section 3 to also count how many were exactly OK.
