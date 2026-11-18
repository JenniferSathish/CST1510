"""
OPS CONSOLE  -  a preview
================================
Run it with:    python ops_console.py

This is a taste of what your own project becomes next week. From Week 8 you
start one project of your own and grow it for the rest of term - the
record-check idea, grown up, on real data. This week is just the first tool
it will need: cleaning and parsing real, messy text.

Once your project starts, expect roughly this shape as it grows:

    Week 8    it pulls real data - an API, Kaggle, or your own repository
    Week 9    it has a login, with hashed passwords
    Week 10   it stores everything in a real database
    Week 11   it has a real dashboard
    Week 12   it (optionally) gets an AI-assisted feature, and is deployed

Real status readings rarely arrive as tidy comma-separated numbers. These four
lines look like they came from an actual monitoring tool - inconsistent
spacing, inconsistent case, key=value pairs. This version turns them into the
same clean shape Weeks 4 and 5 already know how to work with.
"""

def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"],
    }


def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


raw_lines = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,used=120,total=100",
    "  srv-03,used=45 ,total=100",
    "Srv-04 , used = 93 , total=100",
]

print(f"{'HOST':<8} {'USED/TOTAL':<14} STATUS")
print("-" * 34)

for raw_line in raw_lines:
    record = parse_line(raw_line)
    status = status_of(record["used"], record["total"])
    usage = f"{record['used']:.1f}/{record['total']:.1f}"
    print(f"{record['hostname']:<8} {usage:<14} {status}")
