"""
A LIST OF DICTS
================
This week's three tools combine into the shape almost every real program
uses: a list of records, each record a dict.
Run:  python 01_list_of_dicts.py
"""

# --- 1. Build one by hand first, before loading anything -------------------

records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0},
]

print(type(records))         # list
print(type(records[0]))       # dict - each ITEM of the list is a dict
print(records[0]["label"])     # R-001 - index into the list, then key into the dict


# --- 2. Looping over it - one dict per pass ---------------------------------

for record in records:
    print(record["label"], record["value"], record["limit"])


# --- 3. Using .items() inside the loop, if you want every field ------------

for record in records:
    for key, value in record.items():
        print(f"  {key}: {value}")
    print()


# --- 4. How many records? --------------------------------------------------

print(len(records))     # 3 - the number of dicts in the list


# --- 5. Same idea, three fields ---------------------------------------------

survey_rows = [                                              # AI / Data Science
    {"answer": "yes", "age": 21},
    {"answer": "no", "age": 34},
]
for row in survey_rows:
    print(row["answer"], row["age"])

log_lines = [                                                 # Cyber Security
    {"ip": "10.0.0.5", "time": "09:01", "result": "FAILED"},
    {"ip": "10.0.0.9", "time": "09:02", "result": "OK"},
]
for entry in log_lines:
    print(entry["ip"], entry["result"])

server_rows = [                                               # IT
    {"hostname": "srv-01", "used": 87, "total": 120},
    {"hostname": "srv-02", "used": 45, "total": 100},
]
for server in server_rows:
    print(server["hostname"], server["used"], "/", server["total"])


# --- TRY IT ------------------------------------------------------------------
# 1. Build a list of 2 dicts by hand, each with label, value and limit.
#    Loop over it and print just the label from each.
# 2. Add a "status" key to each dict in your list, inside the loop, based
#    on whether value is over limit.
