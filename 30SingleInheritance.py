class Parent: 
    def __init__(self ,name,age) :
        self.name = name 
        self.age = age 

    def belling(self):
        print("This is belling") 
    
    def intro(self): 
        print(f"My name is {self.name} and age {self.age}") 

class Child(Parent):
    def __init__(self,name,age,country): 
        self.country = country
        super().__init__(name,age)
    
    def chilling(self):
        print("We are chilling") 


a1 = Parent("abhi",12)
a1.intro()
a1.belling()
a2 = Child("abhiiiiiiiiiiiiii",100002,"India") 
a2.intro() 
a2.belling() 

