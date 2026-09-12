<div align="center">

# Abstraction in Python

</div>

---
Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user. It's used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

**Real Life Example:** In a graphics software, multiple shapes are available such as Circle, Rectangle and Triangle. All shapes share common data and support the same set of actions, but the internal details are hidden:

- **Common data:** name, color, border thickness, fill style.
- **Common actions:** draw(), resize(), getArea().
- Each shape implements these actions differently Circle uses radius, Rectangle uses length and width and Triangle uses base and height.

The software only knows that a shape can be drawn and its area can be calculated. How the shape is drawn or how the area is calculated is hidden.

# Abstract Base Class
**Abstract Base Class (ABC)** is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes. Abstract classes are created using `abc` module and `@abstractmethod` decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.
```python
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
```