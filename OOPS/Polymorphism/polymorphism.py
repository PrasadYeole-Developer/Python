# Polymorphism
"""
In Python, traditional method overloading (same method name with different
number or type of parameters as in Java/C++) is not supported.

However, similar behavior can be achieved using default arguments,
*args, and **kwargs.

Polymorphism in Python is mainly achieved through method overriding
and duck typing.
"""

# Method overriding 
class Parent:
    def sound(self):
        print("parent sound!")

class Child(Parent):
    def sound(self):
        print("child sound!")

obj = Child()
obj.sound() # the child overrides the parent's method

# Duck typing
"""
Python doesn't care what an object is it only cares what the object can do that is duck typing
"""

class Human:
    def talk(self):
        print("Speaks")

class Duck:
    def talk(self):
        print("Quacks")

# We don't care if it is human or duck we only care does the object have talk method

# OR 

class Dog:
    def speak(self):
        print("Bark")

class Human:
    def speak(self):
        print("Hello")

def talk(obj):
    obj.speak()

talk(Dog())
talk(Human()) # Similarly here as well


