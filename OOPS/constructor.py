class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

s1 = Student()
s2 = Student("Prasad", 21)
print(s1.name, s1.age)
print(s2.name, s2.age)