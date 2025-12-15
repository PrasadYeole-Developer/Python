class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent: {name}")    

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"Child: {age}")

Child("Prasad", 21)

# Constructor inheritance // the constructor in parent class can be accessed(called) in child class in the child class's constructor with the help of super() function

"""
| Scenario                               | Result                 |
| -------------------------------------- | ---------------------- |
| Child has no `__init__`                | Parent `__init__` runs |
| Child has `__init__` without `super()` | Parent ignored         |
| Child has `super()`                    | Parent + Child run     |
"""


