"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT   
Date  : 11/8/2026

Run it:  miniproject.py

"""
import os #importing this mod. to fix path errors

#pipelining to clean and make the records in the txt file uniformed
def parse_line(raw_line):
    parts = [part.strip() for part in raw_line.strip().split(",")]  #for each part in the rec. strip whitespaces and split the parts where commas are
    record = {"server": parts[0].upper()}      #capitalize srv located at index 0
    for i in parts[1:]:                         #same procedure for the other parts (used and total where they have = sign) and then add them into a dic.
        key, value = i.split("=")
        record[key.strip().lower()] = int(value.strip())
    return record

#check the status of each rec. using conditionals 
def status(record):
    percent = (record["used"] / record["total"]) * 100
    if percent >= 90:
        return "OVER LIMIT"
    elif percent >= 75:
        return "WARNING"
    return "OK"


#fixing path so the txt file is created inside the lab folder 
base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "messy_lines.txt")
output_path = os.path.join(base_dir, "cleaned_lines.txt")

#open the messy_lines file in read mode and remove white spaces in each linetehn append it into a list
raw_records = []
with open(input_path, "r") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)

#creating counters and a clean_lines empty list
tot_count = 0
flag_count = 0
clean_lines = []

#formatting the results by calling the funct.in stored variables 
for records in raw_records:
    cleaned = parse_line(records)
    rec_status = status(cleaned)
    tot_count += 1
    if rec_status != "OK":
        flag_count += 1
    output= f"{cleaned} this record status is: {rec_status}"
    print(output)
    clean_lines.append(output)

#creating a new txt file to write the output into
with open(output_path, "w") as file:
    file.writelines(clean_lines)

print("\n------------------------------------------------------------------------------>")
#printing the counters as a summary
print(f"\nsummary: {tot_count} records processed, {flag_count} flagged.")
