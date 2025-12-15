# Single inheritance is everything we have seen till now

# Multiple inheritance 
"""
In this the child class will inherit attrs and methds of more that one parent classes but call only first parent's constructor will be called with super() function
"""
class Father:
    def skills(self):
        print("can Drive")

class Mother:
    def skills(self):
        print("can Cook")

class Child(Father, Mother):
    def show(self):
        print("have multiple skills")

obj = Child()

obj.skills()
obj.show()

# OR
print("class separation!")

class Father2:
    def skills(self):
        print("can Drive")

class Mother2:
    def skills(self):
        print("can Cook")

class Child2(Father2, Mother2):
    def show(self):
        super().skills()
        Mother2.skills(self)
        print("have multiple skills")

obj2 = Child2()

obj2.show()

# Multilevel inheritance
"""
This works like a class inherits from a class which is already inheriting a class
"""
print("class separation!")

class Grandfather:
    def house(self):
        print("Has a house")

class Father(Grandfather):
    def car(self):
        print("Has a car")

class Child(Father):
    def bike(self):
        print("Has a bike")

c = Child()
c.house()
c.car()
c.bike()
