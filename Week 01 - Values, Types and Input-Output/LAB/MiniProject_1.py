"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT 
Date  : 

Run it:   MiniProject_1.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input("enter your hostname:")   
first_used = float(input("enter gb used:"))    
second_total = float(input("enter a total gb:"))    

difference_free = second_total-first_used 
percent = (first_used / second_total) * 100    

print(label)
print("=" * 50)
print(f"  RECORD CHECK  -  {label}")
print("=" * 50)

print(f"  Used     :   {first_used:10.2f}")
print(f"  Total    :   {second_total:10.2f}")
print(f"  Free     :   {difference_free:10.2f} %")
print(f"  Percent  :   {percent:10.2f} %")
print("=" * 50)

