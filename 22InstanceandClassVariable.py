# Instance and Class Variables
# -> Instance Variable: A variable that is defined inside a method and is specific to an instance of a class.
# -> Class Variable: A variable that is shared among all instances of a class.
#  It is defined within the class but outside any method.


class Employee: 
    name = "Abhi"   # Class Variable 

    def __init__(self,age):
        self.age = age  # Instance Variable 
        self.country = "India"

    def info(self):
        print(f"Name: {self.name}, Age: {self.age} , Country: {self.country}")


em = Employee(23)  # Creating an instance of Employee with age 23
em.country = "USA"  # Modifying the instance variable
em.info()  # Output: Name: Abhi, Age: 23

em1 = Employee(22)  # Creating another instance of Employee with age 22 
em1.name = "Katyayani"  # Modifying the class variable for this instance
em1.info()  # Output: Name: Abhi, Age: 22 , Country: India

