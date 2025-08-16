# Constructor :- A special method used to initialize objects 
# It is called when an object is created from a class and allows the class to initialize the attributes of the class.
# Types of Constructor:
# 1. Default Constructor: No parameters are passed.
# 2. Parameterized Constructor: Parameters are passed to initialize the attributes with specific values.

class Employee:
    name = "Abhilasha" 
    age = 23 
    country = "India"  
    # def __init__(self) :
    #     print("Default Constructor called")
    

    def __init__(self, n,a) :
        print("parameterized Constructor called")
        self.name = n
        self.age =  a
        print(f"Constructor called with name: {self.name} with age: {self.age}")
       

    def info(self):
        print(f"Name :{self.name} age : {self.age} and Country :- {self.country}"  )

# print("Default Constructor")
a = Employee("abhi" ,23)  # Creating an object of Employee 
b = Employee("Katyayani", 22)  # Creating another object of Employee

