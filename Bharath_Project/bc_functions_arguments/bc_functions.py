'''
Created on 23 Mar 2026

@author: Bharath.c

a = 10
b = 20
print(a+b)

c = 10
d = 20
print(c+d)
def add(a, b):
    print(f"sum of {a} and {b}:", a+b)

add(4, 7)
add(5, 9)
def start_msg():
    print("wecome to iquest")
    print("lets start programming")
start_msg()

g = add
print(g(10, 20))

def first_fun():
    def sec_fun():
        print("This is sec function")
    return sec_fun
h = first_fun()
h()

num = 1
n = 4
for i in range(1 , n+1):
    num = num * i
print(num)

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result
print(factorial(4))

a = 10
b = 15
c = 25
if a > b:
    print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater", c)

'''
def greater(a, b, c):
    if a>b and a > c:
        return("a is grater", a)
    elif b > a and b > c:
        return("b is greater", b)
    else:
        print("c is greater", c)
print(greater(10, 20, 50))
    
    
    
    
    
