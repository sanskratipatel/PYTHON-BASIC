# Class Method :- A method that is bound to the class and not the instance of the class.
# It can be called on the class itself, without creating an instance.
# Class methods are defined using the @classmethod decorator.

class Employee:
    company = "KSOLVES" 
    def show(self):
        print(f"Company: {self.company} and name: {self.name}")
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company 



e1 =Employee()  # Creating an instance of Employee
e1.name = "Katyayani"  # Setting the name attribute for the instance
e1.show()  # Output: Company: KSOLVES and name: Katyayani
e1.change_company("New Company")  # Changing the class variable company
e1.show()  # Output: Company: New Company and name: Katyayani
print(Employee.company)  # Output: New Company (class variable accessed through class)

e1.change_company("Another Company")  # Changing the class variable again
e1.show()  # Output: Company: Another Company and name: Katyayani
print(Employee.company)  # Output: Another Company (class variable accessed through class)


