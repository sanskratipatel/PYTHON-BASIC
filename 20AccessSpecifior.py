# Access Specifior:- this is used to restrict the access of class members.
# Types of Access Specifior:
# 1. Public :- Members are accessible from outside the class.
# 2. Private :- Members are not accessible from outside the class.
# 3. Protected :- Members are accessible in the class and its subclasses.
# In private, members are prefixed with double underscores (__) to make them private.
# In protected, members are prefixed with a single underscore (_).
# in public, members are accessible without any prefix.


class Employee:
    def __init__(self):
        print("Default Constructor called")
        self.name = "Abhilasha"   # Public member
        self.__age = 23  # Private member
        self._country = "India"  # Protected member

a = Employee()  # Creating an object of Employee    
print(a.name)  # Output: Abhilasha  Public access    
# print(a.__age)  # Raises an AttributeError: 'Employee' object has no attribute '__age' (Private access)
print(a._Employee__age)  # Output: 23 (Accessing private member using name mangling)
print(a._country)  # Output: India (Accessing protected member)
# Name mangling (a._Employee__age):-  is a technique used to make private members accessible by changing their name to include the class name.

print(a._country)  # Output: India (Accessing protected member)

