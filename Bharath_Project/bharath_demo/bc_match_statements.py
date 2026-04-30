'''
Created on 3 Mar 2026

@author: Bharath.c
'''

day_number = int(input("enter the number to know the date:"))
match day_number:
    case 1:
        print("Sunday")
    
    case 2:
        print("Monday")
        
    case 3:
        print("Tuesday")
    
    case 4:
        print("Wednesday")
    
    case 5:
        print("Thursday")
    
    case 6:
        print("Friday")
    
    case 7:
        print("Saturday")
    
    case _:
        print("Please enter the correct number 1-7")

