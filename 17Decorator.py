# Decorators in Python
# A decorator is a function that takes another function
#     and extends its behavior without explicitly modifying it.
# They are often used to add functionality to existing code.


def greet(fx) : 
    def mfx(*args,**kwargs) : 
        print("Before calling the function")
        fx(*args,**kwargs)
        print("After calling the function")
    return mfx   

   
@greet
def hello() :  
    print("Hello!!!!!!!!!!!!!!!!") 

hello()  # Calling the decorated function

@greet
def add(x,y):
   print( x + y )

add(1,2) # Calling the decorated function 

