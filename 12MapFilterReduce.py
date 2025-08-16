# Map : -  Map is used to apply a function to all items in an input list (or any iterable).
# Filter : -  Filter is used to create a list of elements for which a function returns true.
# Reduce : -  Reduce is used to apply a rolling computation to sequential pairs of values in a list.  


def square(x):
    return x**2 

li = [1,2,3,4,5,6,7] 

new1 =[] 
for i in range(0,len(li)):
    new1.append(square(li[i])) 
print(new1)  # Output: [1, 4, 9, 16, 25, 36, 49] 

# Using map function 
new2 = list(map(square,li))
print(new2)  # Output: [1, 4, 9, 16, 25, 36, 49] 

# with lambda function
new3 = list(map(lambda x:x**2 , li)) 
print(new3)  # Output: [1, 4, 9, 16, 25, 36, 49] 


# Filter function example 

def fi(a): 
    return a%2 == 0
l2 =[1,2,3,4,5,6] 
new4 = list(filter(fi,l2))
print(new4)  # Output: [2, 4, 6] 

new5 = list(filter(lambda x: x%2==0, l2))
print(new5)  # Output: [2, 4, 6]  


# Reduce function example
from functools import reduce

 
def sum3 (x,y):
    return x+y 
sum1 = 0
for i in range(0,len(l2)-1): 
   sum1 = sum3(l2[i],l2[i+1])

print(sum1)  # Output: 21 (1+2+3+4+5+6)


sum4 = reduce(sum3 ,l2) 
print(sum4)  # Output: 21 (1+2+3+4+5+6)