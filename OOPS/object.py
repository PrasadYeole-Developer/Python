class Developer:
    name="Prasad Yeole"
    age=21
    bio="Full Stack Developer"
    def about(self, name="Unknown"):
        print(f"Hello there! I'm {name} and I'm a full stack developer")


obj = Developer()
print(obj.name, obj.age, obj.bio)
obj.about("Prasad")