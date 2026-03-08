'''
Created on 4 Mar 2026

@author: Bharath.c


a = []
print(a)
print(type(a))

b = [1, 2, 3, 4]
print(b)
print(type(b))

c = [1,2,3,'bharath']
print(c)
print(type(c))

d = tuple(range(10))
print("d:", d)

c = [1,2,3,4,5]

index = 0
while index < len(c):
    print(c[index])
    index += 1

b = [1,2,3,4,5]
c = [6,7,8,9,10]
a = b + c
print(a)

index = 6
b = [1,2,3,4,5]
c = [6,7,8,9,10]
for i in c:
    b.insert(index,i)
    index=index+1
print(b) 
'''
f = [2,3,4,5,6,7,8,9,3,4,6,9] 
print(f)
a = int(input(f'enter a number inside:' ))
print(a)
c=f.count(a)
print(c)
pos = 0
for i in range(c):
    j = f.index(a,pos)
    pos = j+1
    print(j)
       
    
    
     

