#  Lambda functions :-  are anonymous functions defined with the lambda keyword. 
# They can have any number of arguments but only one expression.
# The expression is evaluated and returned. 
 
def add(x): 
    return x + 10

print(add(5))  # Output: 15 


# Lambda function equivalent
add_lambda = lambda x :x+10  
print(add_lambda(5))  # Output: 15 

cube_lamda = lambda z:z**3  
print("cube =========",cube_lamda(3))  # Output: 27

two_args = lambda x,y,z :(x+y+z)/3

print("Average of 3 numbers:", two_args(10, 20, 30))  # Output: 20.0 

def cube(x):
    return x**3 

def app(fx, value) : 
    return 10+fx(value) 

# Normal function
val = app(cube,3)
print("Using normal function:" ,val)  # Output: 37 

# Using lambda function 
val2 = app(lambda x: x**3, 3)
print("Using lambda function:", val2)  # Output: 37