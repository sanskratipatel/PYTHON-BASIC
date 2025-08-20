class Parent1:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def intro(self):
        print(f"This iis me {self.name} and my age {self.age} ") 
    def drum(self) :
        print("this is parent1")

    def one(self , country): 
        self.country = country
        
        print(f"This iis me {self.name} and my age {self.age} and country {self.country} ") 

class Parent2:
    def __init__(self,car):
        self.car = car
    
    def drum(self) :
        print("this is parent2")


    def two(self , number) :  
        self.number = number
        print("WEare from second class") 

    
class Child(Parent2, Parent1):
    def __init__(self, name, age ,new,car):
        self.new = new 
        self.car =car
        # super().__init__(name, age)  
        Parent1.__init__(self,name,age)
        Parent2.__init__(self,car)

    def intro(self) : 
        Parent1.intro(self)  
        print(f"my name {self.name} age {self.age} and new = {self.new} my car is {self.car}")
    
   
a3 = Child("abhi",133,"gdd","Tata")  
a3.intro()
a3.drum()