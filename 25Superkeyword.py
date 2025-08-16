# Super Keyword in Python
# The `super()` function in Python is used to call methods from a parent class.
# It allows you to access inherited methods that have been overridden in a child class.

class Parent:  
   

    def parent_method(self):
        print("This is a method from the Parent class") 
 

class Chlid(Parent): 
    def parent_method(self):
        print("This is an overridden method from the Child class")
    def child_method(self):
        print("This is a method from the Child class") 

        super().parent_method()  # Calling the parent class method using super() 


child = Chlid() 
 # Creating an instance of the Child class
child.child_method()  # Output: This is a method from the Child class
child.parent_method()  # Output: This is an overridden method from the Child class
         

class Parent2:  
    def __init__(self,name, age):
        self.name = name
        self.age = age
        print("Parent class constructor called")  

class Child2(Parent2): 
    def __init__(self, name, age, city):
        self.city = city
        super().__init__(name, age)  # Calling the parent class constructor using super(

a = Child2("Katyayani", 22, "Delhi") 
print(f"Child class constructor called with name: {a.name}, age: {a.age}, city: {a.city}")
b = Parent2("Abhilasha", 23) 
# Output: Parent class constructor called
print(f"Parent class constructor called with name: {b.name}, age: {b.age}")