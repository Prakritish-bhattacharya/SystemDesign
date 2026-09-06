The word `polymorphism` means `having many forms`. In programming, polymorphism means the **same function name** (but different signatures) being **used for different types**. The key difference is the data types and number of arguments used in a function.
User-defined polymorphic functions allow you to write functions that can handle multiple types of data. Here’s a simple example in Python using a function that works with different types:

> One method name === Different Behaviour

**Example:**
```python
class Dog:
    def sound(self):
        print("Dog Barks")

class Cat:
    def sound(self):
        print("Cat Meows")

dogObj = Dog()
catObj = Cat()

dogObj.sound()
catObj.sound()
```

## Polymorphism with Method Overriding

One of the most common forms of polymorphism in Python is method overriding. A parent class defines a method, and different child classes provide their own implementation.

**Example:**
```python
class Animal:

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):

    def speak(self):
        print("Dog says Woof")

class Cat(Animal):

    def speak(self):
        print("Cat says Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```
## Polymorphism with a Common Function
Polymorphism becomes even more useful when we don't need to know the exact class of an object.
```python
def make_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
```
## Polymorphism Through Duck Typing
Python heavily relies on duck typing. If an object behaves like the required type, Python can use it.

The object does not necessarily need to inherit from the same parent class.

**Example:**
```python
class Dog:

    def speak(self):
        print("Dog says Woof")

class Robot:

    def speak(self):
        print("Robot says Hello")

def make_sound(obj):
    obj.speak()

dog = Dog()
robot = Robot()

make_sound(dog)
make_sound(robot)
```
## Polymorphism with Different Classes
Polymorphism isn't restricted to inheritance.

**Example:**
```python
class Car:

    def move(self):
        print("Car is driving")

class Boat:

    def move(self):
        print("Boat is sailing")

class Airplane:

    def move(self):
        print("Airplane is flying")

def start(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
airplane = Airplane()

start(car)
start(boat)
start(airplane)
```

## Method Overloading
Method overloading means using the same method name with different numbers or types of arguments.

Python does not support traditional method overloading like Java or C++. Instead, we usually achieve similar behavior using default arguments or *args.

**Example:**
```python
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))
```
You cannot define multiple methods with the same name like this:
```python
class Calculator:

    def add(self, a, b):
        pass

    def add(self, a, b, c):
        pass
```
The second add() replaces the first one.

So in Python, method overloading is generally implemented using techniques such as:
***As:***
```python
def add(self, a, b=0, c=0):
```
***Or:***
```python
def add(self, *args):
```
## Method Overriding
Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

**Example:**
```python
class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def speak(self):
        print("Dog says Woof")


class Cat(Animal):

    def speak(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```
| Method Overloading                                         | Method Overriding                          |
| ---------------------------------------------------------- | ------------------------------------------ |
| Same class                                                 | Parent and child classes                   |
| Same method name                                           | Same method name                           |
| Different arguments                                        | Same method signature/compatible signature |
| Usually associated with compile-time polymorphism          | Runtime polymorphism                       |
| Python simulates it using default arguments, `*args`, etc. | Directly supported through inheritance     |

---

When asked **“Does Python support method overloading?”**, say:

Python does not support traditional method overloading by defining multiple methods with the same name. The latest definition replaces the previous one. However, similar behavior can be achieved using default arguments, *args, or **kwargs.

**And for overriding:**

Method overriding occurs when a subclass provides a new implementation of a method inherited from its parent class.

👉&nbsp;&nbsp;&nbsp;&nbsp;[Polymorphism](../Polymorphism/code/polymorphism.py)[![Open Editor](https://img.shields.io/badge/>Open%20Editor-F9AB00?logo=googlecolab&logoColor=white)](../Polymorphism/code/polymorphism.py)