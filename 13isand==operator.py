# == :- use for equality comparison (example: a == b) value 
# is :- use for identity comparison (example: a is b) location in memeory

a =5 
b ="5"
print(a == b)  # Output: False (different types)
print(a is b)  # Output: False (different types)

l1 =  [1,2,3]
l2 =  [1,2,3]
print(l1 == l2)  # Output: True (same content)
print(l1 is l2)  # Output: False (different objects in memory)