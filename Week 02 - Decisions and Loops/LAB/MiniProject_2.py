"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT 
Date  :

Run it:   MiniProject_2.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

count_ol = 0

while True:
    lable = input("enter hostname: ")
    
    if lable == "done":
        break
    
    used = float(input("enter used value: "))
    tot = float(input("enter total value: "))
    
    difference = tot - used
    percentage = (used / tot) * 100
    
    if percentage >= 100:
        status = "OVER LIMIT"
        count_ol += 1
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    print("="*35)
    print(f"  RECORD CHECK  -  {lable}")
    print("="*35)
    print(f"  Used        : {used:10.2f}")
    print(f"  Total       : {tot:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percentage:10.2f} %")
    print(f"  Status      : {status:>10s}")
    print("="*35)

print(f"total overlimit records: {count_ol}")