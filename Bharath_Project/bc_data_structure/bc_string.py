'''
Created on 14 Mar 2026

@author: Bharath.c

Strings: 
' '
" "
""" """
''' '''

name1 = 'bharath'
name2 = "Manju"
address = """c/o iQuest,
             near Infosys
             Mysuru"""
name3 = ""
print("name3:", name3)
print(type(name3))
print("name1:", name1)
print("name2:", name2)
print("address:", address)

print(name1[2])

name = 'bharath'
for i in name:
    print("i:", i)
    

name = 'bharath'
index = 0
while index <= 6:
    print("i:", name[index])
    index += 1

name = "bharath"
name[2] = r
print(name)

b = "bharath"

print("b:", b)    
print("b:", b[::])   
print("b:", b[0:3:1])   
print("b:", b[-1:-3:-1])
print(b.capitalize() )
print(b.casefold())
print(b.count(b))
print(b.isalpha())
print(b.isalnum())
print(b.isupper())

for j in range(5):
    for i in range(5):
        print("*", end =" ")
    print()

num = 1
for j in range(1, 5):
    for i in range(j):
        print(num, end=" ")
        num+=1
    print()



for j in range(1, 6):
    for i in range(j):
        print(i+1, end=" ")
    print()
    

for j in range(1, 6):
    for i in range(j):
        print(i+1, end=" ")
    print()

print('He said,"yes!!"')
'''
for j in range(1, 6):
    for i in range(j):
        print(i+1, end=" ")
    print()

