class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("name is "+self.name+" age is ", self.age)

person = Person("Anil", 40);
person.myFunction()