'''
Created on 22 Feb 2026

@author: Bharath.c

operators:
'''
a = 20
b = 23
c = (a+b)
print(f'sum of {a} and {b} is', c)
c = (a-b)
print(f'sub of {a} and {b} is', c)
c = (a*b)
print(f'Mul of {a} and {b} is', c)
c = (a/b)
print(f'div of {a} and {b} is', c)
c = (a%b)
print(f'mod of {a} and {b} is', c)
c = (a**b)
print(f' of {a} and {b} is', c)
c = (a//b)
print(f'int of {a} and {b} is', c)
c = (a>b)
print(f'greater of {a} and {b} is', c)
c = (a<b)
print(f'greater of {a} and {b} is', c)
c = (a==b)
print(f' Is {a} and {b} is equal', c)
c = (a<=b)
print(f'Is lesser or equal of {a} and {b} is', c)
c = (a>=b)
print(f'greater or equal of {a} and {b} is', c)
c = (a!=b)
print(f'not equal of {a} and {b} is', c)
c = (a & b)
print(f' {a} and {b} is', c)
a = False
b = True
g = not(a and b)
print(g)
c = (a | b)
print(c)

a = 'i'
b = 'bharath'
print('i' in 'bharath')
print('b' in 'bharath')

a = b = 10
print(a is b)