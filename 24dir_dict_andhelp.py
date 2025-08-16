# dir ():- this methosd is used to get the list of attributes and methods of an object
# __dict__() :- this method is used to get the dictionary representation of an object
# help() :- this method is used to get the documentation of an object

x= [1,2,3,4] 
print(dir(x))  # Output: List of attributes and methods of the list object
print(x.__add__) 

y = "Hello"
print(dir(y))  # Output: List of attributes and methods of the string object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}") 

p = Student("Katyayani", 22)

print(p.__dict__)  # Output: Dictionary representation of the Student object 

print(help(Student))  # Output: Documentation of the Student object
print(help(y))