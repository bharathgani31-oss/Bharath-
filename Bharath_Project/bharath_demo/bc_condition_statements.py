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

marks = int(input("Enter the Marks: "))
if marks in range(90,100):
    print("Grade A+")
elif marks in range(80,90):
    print("Grade A")
elif marks in range(70,80):
    print("Grade B")
elif marks in range(60,70):
    print("Grade c")
elif marks in range(50,60):
    print("Grade D")
elif marks in range(40,50):
    print("Just Pass")
else:
    print("Fail")
    

num = int(input("enter a number: "))
if num > 0:
    print(f'{num} is a positive Number')
elif num < 0:
    print(f'{num} is negitive number')
else:
    print(f'{num} is equal to Zero')


num1 = int(input("Enter num1: "))
num2 = int(input ("Enter num2: ")) 
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
c=list1 + list2
print(c)

operator = input("Enter an operator (+ - * /): ")
Num1 = float(input("Enter Num1 :"))
Num2 = float(input("Enter Num2 :"))
if operator == "+":
    operator = Num1 + Num2
    print(operator)
elif operator == "-":
    operator = Num1 - Num2
    print(operator)
elif operator == "*":
    operator = Num1 * Num2
    print(operator)
elif operator == "/":
    operator = Num1 / Num2
    print(operator)
else:
    print("Wrong choice")

a = "Bharath"
print(a.isalpha())
print(a.isdigit())
'''