class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal): # Dog class inherits from Animal class
    def bark(self):
        print("Dog is barking")

class Puppy(Dog): # Puppy class inherits from Dog class
    def play(self):
        print("Puppy is playing")

puppy_obj = Puppy() # create an Instance of Puppy class
puppy_obj.eat() # Calling method of Animal class (Grandparent class)
puppy_obj.bark() # Calling method of Dog class (Parent class)
puppy_obj.play() # Calling method of Puppy class (Child class)