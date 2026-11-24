class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
d1 = Dog("Buddy", 3)
d2 = Dog("Lucy", 5)
print(d1.bark())
print(d2.name, d2.age, Dog.species)