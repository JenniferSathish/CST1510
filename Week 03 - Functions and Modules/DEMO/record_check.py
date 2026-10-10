"""
RECORD CHECK  -  Week 3 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions
    Week 3   it is built from functions          <- this version
    Week 4   it reads many records from a file
    Week 5   it becomes a reusable component
    Week 6   it does the whole job in a few lines

Same program, same behaviour as last week. This time it is built from three
named, reusable pieces instead of one long block - which is what makes it
possible to keep growing it without it turning into a mess.

              get_record()
                   |
                   v
       record_id, value, limit
                   |
                   v
        check_record(value, limit)
                   |
                   v
       difference, percent, status
                   |
                   v
        print_report(record_id, value, limit,
                      difference, percent, status)

Type "quit" as the Record ID to stop.

Two lines use ideas you have not been taught yet and are marked. Trust them
for now.
"""

def get_record():
    """Ask for one record's three values. Returns None if the user is done."""
    record_id = input("Record ID (or 'quit') : ")
    if record_id == "quit":
        return None

    value = float(input("Value     : "))
    limit = float(input("Limit     : "))
    return record_id, value, limit          # <- three values, sent back at once


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


def print_report(record_id, value, limit, difference, percent, status):
    """Print one bordered report. Nothing is worked out in here - only shown."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record_id}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


while True:
    record = get_record()
    if record is None:      # <- get_record() said "no more records"
        break

    record_id, value, limit = record
    difference, percent, status = check_record(value, limit)
    print_report(record_id, value, limit, difference, percent, status)

print("Done. Checked and reported.")
