# Dunder Methods In Python (__init_, __str__, __len__, etc.)
# Dunder methods, also known as magic methods or special methods, are predefined methods in Python
# that start and end with double underscores (hence "dunder"). They allow you to define the behavior of your objects
# for built-in operations like addition, subtraction, string representation,
# and more. These methods enable you to customize how your objects interact with Python's built-in


class Point:
    name = "Abhi" 
    def __len__(self):
        l =0
        for i in range(0 ,len(self.name)):
            l = l+1
            return l
            


a = Point()  # Creating an instance of Point class
print(a.name)  # Output: Abhi (default value)
print(len(a))  # Output: 4 (Length of the string "Abhi" using the __len__ method)

