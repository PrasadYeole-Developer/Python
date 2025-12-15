# Access modifires
"""
Public attrs and methds : every function and variable we have created till now are public
Protected : the variable and function that we would be creating with single underscore (_) will be protected but still they can be accessed outside the class in python (python doesn't give protected access like other languages) it just a naming convention here to tell developers
Private : cannot accessed from outside only within a class where it is defined
"""

class Demo:
    def __init__(self):
        self.name = "Prasad"
        self._age = 23
        self.__salary = 80000

    def show(self):
        print("Inside the class: ")
        print(f"Public: {self.name}")
        print(f"Protected: {self._age}")
        print(f"Private: {self.__salary}")
        
obj = Demo()

obj.show()

print(obj.name)
print(obj._age)
print(obj.__salary) # will give error while accessing private variable directly