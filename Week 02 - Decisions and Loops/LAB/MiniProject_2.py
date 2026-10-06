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
    lable = input("Enter hostname: ").strip()
    
    if lable == "quit":
        break
    
    used = float(input("Enter Used value: "))
    tot = float(input("Enter Total value: "))
    
    difference = tot - used
    percentage = (used / tot) * 100
    
    if percentage >= 100:
        status = "OVER LIMIT"
        count_ol += 1
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    print("\n==================================")
    print(f"  RECORD CHECK  -  {lable}")
    print("==================================")
    print(f"  Used        : {used:10.2f}")
    print(f"  Total       : {tot:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percentage:10.2f} %")
    print(f"  Status      : {status:>10s}")
    print("==================================")

print(f"total overlimit records: {count_ol}")