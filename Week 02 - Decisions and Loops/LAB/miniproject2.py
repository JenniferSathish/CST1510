"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT
Date  : 10/3/2026

Run it:  miniproject2.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

count_ol = 0                                     #setting a count function

while True:
    lable = input("enter hostname: ")
    
    if lable == "done":                         #when user enters done, the loop breaks 
        break
    
    used = float(input("enter used value: "))
    tot = float(input("enter total value: "))
    
    difference = tot - used
    percentage = (used / tot) * 100
    
    if percentage >= 100:
        status = "OVER LIMIT"
        count_ol += 1                         #using the count function to count n.o of  OVERLIMIT records only
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    print("="*35)                                    #formatting 
    print(f"  RECORD CHECK  -  {lable}")
    print("="*35)
    print(f"  Used        : {used:10.2f}")
    print(f"  Total       : {tot:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percentage:10.2f} %")
    print(f"  Status      : {status:>10s}")
    print("="*35)

print(f"total overlimit records: {count_ol}")              #when the loop breaks after user enters done, this line will print the total n.o of records that are OVER LIMIT


