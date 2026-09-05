class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal): # Dog class inherits from Animal class
    def bark(self):
        print("Dog is barking")

class Cat(Animal): # Cat class inherits from Animal class
    def meow(self):
        print("Cat is meowing")

dog_obj = Dog() # create an Instance of Dog class
dog_obj.eat() # Calling method of Animal class (Parent class)
dog_obj.bark() # Calling method of Dog class (Child class)
cat_obj = Cat() # create an Instance of Cat class
cat_obj.eat() # Calling method of Animal class (Parent class)
cat_obj.meow() # Calling method of Cat class (Child class)
