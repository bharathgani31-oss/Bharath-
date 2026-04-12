'''
Created on 23 Feb 2026

@author: Bharath.c

Conditional Statements: Statements based on condition from which flow of program execution will be decided

We define condition Using if statement

Syntax: 

If <condition>
    code
Indentation: Leading spaces<spaces given at the begenning statements)
age = int(input("please enter your age:"))
if age>=18:
    print("Adult")
    else

age = int(input("please enter your age:"))
if age > 0:
    if age<=3:
        print("you are an infant")
        
    elif age<=12:
        print("You are a child")
        
    elif age<=18:
        print("You are a teen")
    
    elif age<=60:
        print("you are an adult")
    
    else:
        print("you are old")
else:
    print("enter a valid integer greater than zero")       

age = int(input("What is your age: "))
if age >= 18:
    print("The person is 18 and above is eligible to vote")
else:
    print("The person is below age 18 and not eligible to vote") 

age = int(input("Is the age above 18 : "))
weight = int(input("is weight is above 50: "))
if age >18 and weight > 50:
    print("You are in the position to donate the blood")
else:
    print("You are under weight and age to donate the blood")
weight = int(input("is weight is above 50: "))
print("Thank you")

balance = float(input("Enter amount to withdraw: "))
if balance >= 3000:
    print("Withdraw your money")
else:
    print("Maintain your balance of 3000")

age = int(input("Person age: "))
if age < 5:
    print("Free Ticket")
elif age>18:
    print("Full ticket")
else:
    print("Half ticket")

bill = int(input ("Enter your power unit: "))
if bill == 100:
    print("Rs 5/Unit")
elif bill >200:
    print("Rs 10/unit")
else:
    print("Rs 7/unit")

Num1 = float(input("Enter Num 1:"))
Num2 = float(input("Enter Num 2:"))
 c = Num1 + Num2:
print(f'The sum of {Num1} and {Num2} is : ', c )
c = Num1 * Num2
print(f'The Mul of {Num1} and {Num2} is : ', c )
c = Num1 - Num2
print(f'The Sub of {Num1} and {Num2} is : ', c )
c = Num1 / Num2
print(f'The div of {Num1} and {Num2} is : ', c )
'''
marks = int(input("Enter the Marks: "))
if marks in range(95,100):
    print("Grade A+")
elif marks in range(80,90):
    print("Grade A")
elif marks in range(75,79):
    print("Grade B")
elif marks in range(65,74):
    print("Grade c")
elif marks in range(50,64):
    print("Grade D")
elif marks in range(40,49):
    print("Just Pass")
else:
    print("Fail")

