"""
RECORD CHECK  -  Week 4 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions
    Week 3   it is built from functions
    Week 4   it reads many records from a file      <- this version
    Week 5   it becomes a reusable component
    Week 6   it does the whole job in a few lines

No more typing records in one at a time. This version reads every record from
records.txt in one go, keeps them as a list of dictionaries, then checks and
reports on each one.

records.txt holds one record per line:   label,value,limit
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


def check_record(value, limit, warning_at=90):
    """Work out the difference, percentage and status for one record."""
    difference = value - limit
    percent    = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= warning_at:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered report. Nothing is worked out in here - only shown."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


records = load_records("records.txt")

over_limit_count = 0

for record in records:                      # <- a dict, one per record, from the list
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"Checked {len(records)} records. {over_limit_count} were over limit.")
