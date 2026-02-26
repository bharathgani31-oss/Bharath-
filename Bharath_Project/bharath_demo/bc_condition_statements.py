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
'''
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
    
        
