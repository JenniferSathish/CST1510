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
        percentage = (self.gb_used/self.gb_total)*100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


def w_file(path):
     """ writing data into another txt file due to some path errors"""
     datas = "srv-01,87,120\nsrv-02,112,110\nsrv-03,45,100\nsrv-04,95,100\n"
     with open(path, "w") as file:
               file.write(datas) 
     

def load_recs(path):
    """reads recs from the text file and returns it as a list of record objects"""
    records = []
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                hostname, used, total = parts
                records.append(Record(hostname, used, total))
    return records


def format(record):
    """printing a formatted report of the data returned"""
    status = record.status()
    
    print("="*30)
    print(f"Hostname: {record.hostname}")
    print(f"Used    : {record.gb_used} GB")
    print(f"Total   : {record.gb_total} GB")
    print(f"Status  : {status}")
    print("="*30)


#assign the txt file into a variable which will be used to call function w_file to write the data into this txt file
file_path = w_file("data.txt")
#after writing, this line will load and read the records/data we wrote into the txt file and append it into a list as record objects from our class variables
records = load_recs(file_path)

#counting number of times a rec is overlimit
over_limit_count = 0
for record in records:
    format(record)        #print the formatted data first
    
    if record.status() == "OVER LIMIT":     #then we count the n.o of limes overlimit rec has appeared
        over_limit_count += 1

print(f"\nnumber of records that are OVER LIMIT: {over_limit_count}")


#to check if r1 and r2 are independent instances
print("\nto check the independent instances of r1 and r2 -->\n")
if len(records) >= 2:    #check if the list has more than 2 elements 
    r1 = records[0]      #index the records for r1 and r2
    r2 = records[1]
    
    print(f"before changing value:-\nr1: {r1.hostname}, {r1.gb_used}\nr2: {r2.hostname}, {r2.gb_used}\n")
    r1.gb_used = 9999    #change by assigning a value to r1
    print(f"after changing value r1:-\nr1: {r1.hostname}, {r1.gb_used}\nr2: {r2.hostname}, {r2.gb_used} -> not changed")

    #from the output its clearr that r1 and r2 are independent instances 