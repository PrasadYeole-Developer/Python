# Adstraction
"""
Abstract classes : where class contains one or more abstract methods
Abstract method : method is defined but not implemented in abstract class but make sure it should be implementing in subclasses
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# We cannot create object of an abstract class, we can create object of subclasses

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Duck(Animal):
    def make_sound(self):
        print("Quark!")