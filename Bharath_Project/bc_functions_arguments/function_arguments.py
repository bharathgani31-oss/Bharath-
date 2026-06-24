'''
Created on 31 Mar 2026

@author: Bharath.c

s = 0
a = (10,24,45,50)
for i in a:
    s = s + i
print(s)



def add(*a):
    s = 0
    for i in a:
        s = s + i
    print(s)
#add(1,4,6,4)
'''
addition = lambda a,b : a+b
print("addition",addition(3,9))

def add(a=0,b=0):
    c = a+b
    return c
print(add())
print(add())
