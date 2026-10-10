"""
RECORD CHECK  -  my version
===========================

Name  : Jennifer Preethi Sathish
Lane  : IT
Date  : 10/10/2026

Run it:   miniproject3.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns a message based on the percent"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:                                #funtion block to check the value of percentage givin and display the output based on the limit
        return "OK"

def check(value, limit):
    """Returns the difference and value"""
    difference = limit - value
    percent = (value/limit)*100            #a funtion block to calculate the difference and percentage from the value and limit enetered by the user 
    return difference, percent             #then itt returns the values in 2 other variables

def print_report(label, value, limit, difference, percent, status):
    """Printing the report format"""
    print("="*35)
    print(f"RECORD CHECK --- {label}")
    print("="*35)
    print(f"Used    : {value:.2f}")
    print(f"Total   : {limit:.2f}")               #the overall format and displaying of the input in the funtion block
    print(f"Status  : {status}")
    print(f"Free    : {difference:.2f}")
    print(f"Percent : {percent:.2f}%")
    print("="*35)

def entering():
        label= input("enter hostname:")                  #since im looping the code, all the inputs will be in this funtion block separatly
        value= float(input("enter a value:"))            #its easier for me to have this in a def block than using it inside the while loop
        limit= float(input("enter the limit:"))

        difference, percent= check(value, limit)
        status= status_of(percent)

        print_report(label, value, limit, difference, percent, status)



while True:                      #while True loop function added so users can enter many records until they type "n" to stop the loop
    entering()
    again = input("enter another record? y/n:")

    if again == "y":
        entering()
    else:
        break
