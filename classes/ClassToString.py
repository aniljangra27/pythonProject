# like toSting method in Java we have __str__ in python to print the object values
class ClassToString:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("Name is " + self.name)

    def __str__(self):
        return f"{self.name}({self.age})"

# initialise the object
cts = ClassToString("one", 12)
print(cts)
