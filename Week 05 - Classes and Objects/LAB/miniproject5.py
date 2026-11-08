"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT
Date  : 10/25/2026

Run it:   miniproject5.py
"""


class Record:
    def __init__(self, hostname, gb_used, gb_total):
        """initialize a rec with a hostname, used gb and total gb"""
        self.hostname = hostname
        self.gb_used = int(gb_used)
        self.gb_total = int(gb_total)

    def status(self):
        """returns status after checking the percentage"""
        percentage = (self.gb_used / self.gb_total) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


def load_recs(path):
    """reads recs from the sample text file and returns it as a list of record objects"""
    records = []
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:                  #make sures that the number of elements in the line that was parted is 3 before adding it into a list
                hostname, used, total = parts
                records.append(Record(hostname, used, total))
    return records


def format(record):
    """printing a formatted report of the data returned"""
    status = record.status()
    print("=" * 30)
    print(f"Hostname: {record.hostname}")
    print(f"Used    : {record.gb_used} GB")
    print(f"Total   : {record.gb_total} GB")
    print(f"Status  : {status}")
    print("=" * 30)



import os   #importing os due to path errors, this was able to resolve the exact folder path error
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "records_sample.txt")

#reads records 
records = load_recs(file_path)

#counting number of times a rec is overlimit
over_limit_count = 0
for record in records:
    format(record)
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(f"\nnumber of records that are OVER LIMIT: {over_limit_count}")


#to check if r1 and r2 are independent instances
print("\nto check the independent instances of r1 and r2 -->\n")
if len(records) >= 2:
    r1 = records[0]
    r2 = records[1]
    
    print(f"before changing value:-\nr1: {r1.hostname}, {r1.gb_used}\nr2: {r2.hostname}, {r2.gb_used}\n")
    r1.gb_used = 9999
    print(f"after changing value r1:-\nr1: {r1.hostname}, {r1.gb_used}\nr2: {r2.hostname}, {r2.gb_used} -> not changed")
    
    #from the output its clearr that r1 and r2 are independent instances 