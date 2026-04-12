'''
Created on 8 Mar 2026

@author: Bharath.c
Tuple:

Creation:

    1. An empty tuple can be created
    2. List with data elements
        a. Homogeneous tuple can be created
        b. Heterogeneous tuple can be created
        c. Tuple can have duplicate elements
    3. Tuple can be created using built-in  function
    
Accessing:
       1.

a = ()
print(a)
print(type(a))

b = (1, 2, 3, 4, 5)
print("b:", b)
print(type(b))

c = (3, 4.5, 3, 3,'bharath', 6+7j, True, None)
print("c:", c)
print(type(c))

d = tuple(range(10))
print("d:", d)

e = (1, 2, 3, 4, 5)
for i in e:
    print(i)

index = 0
f = (1, 2, 3, 4, 6)
while index < len(f):
    print(f[index])
    index += 1
    
g = (1,2,3,4,5)
print("g:", g[1])
print("g:", g[-1])

print("=================Slicing Operator=============")
f = (1,2,3,4,5)
print("f:", f)
print("f(::)", f[::])
print("f(::):", f[1:4:1])
print("f(::):", f[-1:-3:-1])
print("f(::):", f[-3:-1:1])
h = (1, 2, 3, 4, 5, 6)
h[2] = 4
print(h)


a = {}
print(a)
print(type(a))

b = {1, 2, 3}
print(b)
print(type(b))

c = {1, 1.2, 'bharath', 6+7j, True, None}
print("c:", c)
print(type(c))

d = set(range(10))
print("d:", d)

e = {1, 2, 3, 4, 5}
for i in e:
    print(i)

index = 0
f = {1, 2, 3}
while index < len(f):
    print(f[index])
    index+=1

g = {1,2,3,4,5}// TypeError: 'set' object is not subscriptable
print("g:", g[1])
print("g:", g[-1])

print("=================Slicing Operator=============")


index = 0/// TypeError: 'set' object is not subscriptable
f = {1, 2, 3}
while index < len(f):
    print(f[index])
    index+=1

print("=================Slicing Operator=============")
f = {1, 2, 3, 4, 5}
print("f:", f)
print("f(::)", f[::])
print("f(::)", f[0:3:1])
print("f(::)", f[-1:-7:1])

h = {1, 2, 3, 4, 5, 6}
h[2] = 4
print(h)

f = {1, 2, 3, 4, 5}
print("f:", f)
print("f(::)", list(f)[::])



e = {1, 2, 3, 4, 5}
for i in e:
    print(i)
    
b = {9,8,6,1, 2, 3,99,0}
print("b:", b)
print(type(b))

c = {1, 1.2, 'bharath', 6+7j, False , None, 0,True}
print("c:", c)
print(type(c))


d = set(range(10))
print("d:", d)
d.add(99)
print("d:", d)
print(d.difference(b))
#print(d.difference_update(b))
#print(d)
d.discard(99)
print("d:", d)

d.discard(99)
print("d:", d)

#d.remove(99) KeyError: 99
#print("d:", d)

print(d.intersection(b))


print("d.pop",d.pop())
print(d)
print("d.remove:",d.remove(7))
print(d)


#print("d.union:",d.union(b))

print("d.update(b):",d.update(b))
print(d)


x = 123# // IT will be  0  so the 123 is not displayed
x = 43# // New value will be displayed
print(x)
'''
a = 12
b = 12
a == b
print(b)
print(id(a))
print(id(b))

s = 1, 3
print(s)
print(type(s))







