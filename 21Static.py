# Static methods are defined using the @staticmethod decorator.
# They do not require an instance of the class to be called.

# Static methods can be called on the class itself, without creating an instance.
# They are used when the method does not need to access or modify the instance or class state 
# We remove self and add @staticmethod decorator to the method definition.

# @staticmethod
# def addtonum(n):
#     return self.num + n
class Math:

    def __init__(self,num):
        self.num = num
    
    def addtonum(self,n):
        self.num = self.num +n 

    @staticmethod
    def add(a,b):
        return a + b


a = Math(10) 
print(a.num)
a.addtonum(5)  # Adding 5 to the instance's num attribute
print(a.num)  # Output: 15 

print(Math.add(10,20))
# Output: 30 (Calling static method without creating an instance)