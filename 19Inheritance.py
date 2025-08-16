# Inheritance:-
# This file demonstrates the concept of inheritance in Python. 

# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). 
# type of inheritance: 
# 1. Single Inheritance: A child class inherits from one parent class.
# 2. Multiple Inheritance: A child class inherits from multiple parent classes. 
# 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Parent:   
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def sing(self) : 
        print(f"{self.name} is singing") 
    def bell(self) :
        print(f"{self.name} is ringing the bell")
    def info(self):
        print(f"Name :{self.name} and age :- {self.age}")




a =Parent("Abhi",23) 
a.info() 
a.sing()
a.bell() 


# Child class inheriting from Parent class 

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing") 

E = Child("Katyayani", 22)  
E.play() 
E.info() 
E.sing()
E.bell()   


