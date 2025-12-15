class Parent:
    def speak(self):
        print("Hey, I can speak!")

class Child(Parent):
    pass

obj = Child()

obj.speak() # This is how inheritance works in python

