# Class and Object Practice
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")


# Create instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access class attributes and call methods
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()

print(f"{dog2.name} is {dog2.age} years old.")
dog2.bark()

# Have the dogs celebrate their birthdays
dog1.birthday()
dog2.birthday()
