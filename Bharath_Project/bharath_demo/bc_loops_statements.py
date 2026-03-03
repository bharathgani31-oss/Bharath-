'''
Created on 25 Feb 2026

@author: Bharath.c

looping statements:

A loop will be executed repeatedly until a condition is fulfilled
count = 5
while count > 0:
    print("My name is bharath")
    count = count - 1


count = 5
while count > 0:
    print("My name is bharath")
    # count = count + 1 # Increment
    count = count - 1


count = 0
while count <= 100:
    print(count)
    count = count + 1

num = int(input("enter a number"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")


n = 0
while n <= 100:
    n = n+1
    if n % 2 == 0:
        print(n)
        

for i in range(5):
    print("* * * * *")

for i in range(5*5):
    print("*", end = " ")

for j in range(5):
    for i in range(5):
        print("*", end =" ")
    print()

for j in range(1, 6):
    for i in range(j):
        print("*", end=" ")
    print()

for j in range(1, 6):
    for i in range(j):
        print("*", end=" ")
    print()

for j in range(1, 6): # No. of lines
    for i in range(j): # No. of stars
        print("*", end=" ")    
    print()
'''
for j in range(0, 5):
    for i in range (5-j):
        print("*",end=" ")
    print()
    
