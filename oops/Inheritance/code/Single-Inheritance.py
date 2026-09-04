class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        food = "bones"
        print(f"{self.name} is eating {food}")

class Dog(Animal): # Inherit Base class Animal
    def bark(self):
        print(f"{self.name} is barking")

baseClassObj = Animal("Dog")
baseClassObj.eat()

childClassObj = Dog("Tommy")
childClassObj.bark()
childClassObj.eat()