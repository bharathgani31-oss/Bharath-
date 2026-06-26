'''
Created on 12 May 2026

@author: Bharath.c

class GrandFather:
    def gf_method(self):
        print("This is grandfather class")
class Father(GrandFather):
    def f_method(self):
        print("This is father method")
        

print("=======Grand father method==========")
ajja = GrandFather()
ajja.gf_method()

print("=======father method==========")
appa = Father()
appa.f_method()
print("=======Grand father method==========")
appa.gf_method()
print("=======father method==========")
appa.f_method()
'''
num = enter a number:
a = 5
b = 6
c = a+b        