'''
Created on 9 Apr 2026

@author: Bharath.c

class CarClass:
    def __init__(self, name, color, model):
        print(f"A car of {color} of {name} is created in the year {model}")
        self.name = name
        self.color = color
        self.model = model
    def start(self):
        print(f"{self.name} is started")
        
    def move_forward(self):
        print("car is moving forward")
    
    def move_backward(self):
        print(f"{self.name} car is moving backward")
        
    def stop(self):
        print("car stopped")    
car1 = CarClass("swift","red",2026)   
car1.start()
print(type(car1))

car2 = CarClass("Thar", "black", 2026)
car2.start()

car1.move_backward()
print("car1.name:", car1.name)

class CarClass:
    def __init__(self,name,color,model):
        print(f"A {name} car of {color} color is created in the year {model}")
car1 = CarClass("Thar", "red","2026")
'''
class Animal:
    def __init__(self):
        print("Constructor is being called")
animal1 = Animal()# constructor can be called implecitely if required
animal1.__init__()# constructor can called explicitely if required

car1.start()