"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish 
Lane  : IT
Date  : 10/18/2026

Run it:   miniproject4.py

"""

"""
## What to build
**Excellent.** Also **write the results out to a new file** — one line per record,
`label,status` — as well as printing them. Keep a running count of how many were
`OVER LIMIT` and print that once, after the loop ends. Wrap the call to
`load_records` in a `try`/`except` so a missing file prints a clear message and
starts with an empty list, instead of crashing (Topic 4).
"""

#no need to make many funtion blocks for this project. ill use only one funtion def from the week04.05 walkthrough since most of the code req. has already been written
#all counting rec?overlimit recs. and caluclations + storing in list as dictionary will be done in one funtion block 
#output for the records will be printed as a dictionary  


def load_records(path):
    """this funct. will read the label, value, limit lines from a file inserted by the user + counts overlimit records + returns a list of dicts."""
    records = []                      #making an empty list
    tot_rec = 0                       #setting count to count total records inserted by user annd how many recs were over limit
    ol_count = 0

    try:                                        #try except block to check if file exists and proceed without any error
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:                                                     #removing white spaces and splitting the values wherever there is a comma ,
                        a_list = [l.strip() for l in line.split(",")]                
                        if len(a_list) == 3:                                  #assigning the values inside the file by indexing to varibales using a condiontional stat. if the list has 3 values inserted 
                            label = a_list[0]
                            value = float(a_list[1])
                            limit = float(a_list[2])
                            tot_rec += 1
                            
                                                                                # Calculate percentage to check if it's over limit and storing the n.o of overlimit in ol_count
                            if limit > 0:                                               
                                percent = (value / limit) * 100
                                if percent > 100:
                                    ol_count += 1

                                                                                                             # Append values to list as a dictionary
                            records.append({"label": label, "value": value, "limit": limit})

                    except ValueError:
                        continue
                        
                                                                                                     # Printing the count
        print(f"\n{ol_count} out of {tot_rec} records were over limit")

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        
    return records


with open ("gb_rec.txt", "w") as f:                                       #using a while loop to get multiple user inputs to store and write into a file 
        while True:
            label = input("enter hostname/label: ")
            value = input("enter value: ")
            limit = input("enter limit: ")
            
            f.write(f"{label}, {value}, {limit}\n")
            
            again = input("add another? (y/n): ")
            if again != "y":
                break


result= (load_records("gb_rec.txt"))                                    #storeint whats returned in result
print("\nrecords entered:")                                             #loop through each record thats stored ina  dictionary in the list to print it line by line as a dictionary only 
for record in result:
    print(record) 