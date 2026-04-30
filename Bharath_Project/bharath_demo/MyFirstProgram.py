'''
Created on 16 Feb 2026

@author: Bharath.c

print("My First Python Program On Eclipse")
'''
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


