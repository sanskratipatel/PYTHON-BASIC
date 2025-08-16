# Class :- Reeusable code that can be used to create objects
# Object :- Instance of a class 
# Self Keyword :- Used to refer to the instance of the class itself,
#  allowing access to its attributes and methods.

# Attributes :- Variables that belong to the class
# Methods :- Functions that belong to the class
class Employee:
   name ="Abhi" 
   department = "Developer"  
   age =23 
   def info(self) : 
      print(f"Name: {self.name}, Department: {self.department}, Age: {self.age}")


a =Employee()  # Creating an object of Employee  
a.name = "Katyayani"  # Accessing and modifying the attribute
print(a.name)  # Output: Katyayani
print(a.department)  # Output: Developer
print(a.age)  # Output: 23
a.info()  # Output: Name: Katyayani, Department: Developer, Age: 23


B = Employee()  # Creating another object of Employee
print(B.name)  # Output: Abhi (default value)
print(B.department)  # Output: Developer
print(B.age)  # Output: 23
B.info()  # Output: Name: Abhi, Department: Developer, Age: 23


