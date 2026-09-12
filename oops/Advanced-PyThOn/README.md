<div align = "center">

# Advanced Python topics

</div>

--- 
 ## Dunder Methods
---
Dunder methods are special methods in python whose names begin and end with double underscores. Often called **magic methods**, they are not meant to be called directly.
```text
Dunder = Double Underscore
```
**Examples:**
```python
__init__()
__str__()
__len__()
__add__()
__eq__()
```
They allow us to define how our objects should behave with Python's built-in operations and syntax.
Examples:

``` python
__init__
__str__
__repr__
__eq__
__add__
```

For example:

``` python
a + b
```

can invoke:

``` python
a.__add__(b)
```

and:

``` python
len(obj)
```

can use:

``` python
obj.__len__()
```

The key idea is:

> **Dunder methods let custom objects behave naturally like Python's
> built-in objects.**

------------------------------------------------------------------------

# 1. Essential Dunder Methods

## `__init__`

Initializes an instance.

``` python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Alice", 25)
```

## `__repr__`

Provides a useful developer-oriented representation.

``` python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age})"
```

## `__eq__`

Defines equality.

``` python
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id
```

------------------------------------------------------------------------

# 2. `__str__` vs `__repr__`

``` python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ₹{self.price}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"
```

Think:

``` text
__str__  → human-friendly
__repr__ → developer/debugging-friendly
```

------------------------------------------------------------------------

# 3. Equality and Hashing

Important methods:

``` text
__eq__    → ==
__ne__    → !=
__hash__  → hash(obj)
```

Example:

``` python
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)
```

If two objects compare equal, they must have the same hash value.
Mutable state should be handled carefully when it participates in
hashing.

------------------------------------------------------------------------

# 4. Comparison Operators

``` text
<   → __lt__
>   → __gt__
<=  → __le__
>=  → __ge__
```

Example:

``` python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

print(Student(70) < Student(90))
```

These methods also support ordering operations such as sorting.

------------------------------------------------------------------------

# 5. Type Conversion and Formatting

  Operation           Special method
  ------------------- -----------------
  `str(x)`            `__str__()`
  `repr(x)`           `__repr__()`
  `bool(x)`           `__bool__()`
  `int(x)`            `__int__()`
  `float(x)`          `__float__()`
  `complex(x)`        `__complex__()`
  `bytes(x)`          `__bytes__()`
  `format(x, spec)`   `__format__()`

Example:

``` python
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return bool(self.items)
```

When `__bool__` is absent, Python can use `__len__` as a fallback for
truth-value testing.

------------------------------------------------------------------------

# 6. `__format__`

`__format__` controls formatting through `format()` and f-strings.

``` python
class Price:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, spec):
        if spec == "currency":
            return f"₹{self.amount:,.2f}"
        return format(self.amount, spec)

price = Price(12500)

print(f"{price:currency}")
```

Output:

``` text
₹12,500.00
```

------------------------------------------------------------------------

# 7. Context Managers

Objects used with `with` can implement:

``` text
__enter__
__exit__
```

Example:

``` python
class Resource:
    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")

with Resource():
    print("Working...")
```

Conceptually:

``` text
with Resource()
      ↓
__enter__()
      ↓
   work
      ↓
__exit__()
```

------------------------------------------------------------------------

# 8. Container and Collection Protocols

Important methods include:

``` text
__len__
__iter__
__next__
__getitem__
__setitem__
__delitem__
__contains__
__reversed__
__missing__
__length_hint__
```

## `__len__`

``` python
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)
```

Now:

``` python
len(team)
```

uses the object's length protocol.

## `__getitem__`

``` python
class Team:
    def __init__(self, players):
        self.players = players

    def __getitem__(self, index):
        return self.players[index]
```

This enables:

``` python
team[0]
```

## `__setitem__`

``` python
def __setitem__(self, index, value):
    self.players[index] = value
```

Enables:

``` python
team[0] = "Rahul"
```

## `__delitem__`

``` python
def __delitem__(self, index):
    del self.players[index]
```

Enables:

``` python
del team[0]
```

## `__contains__`

``` python
def __contains__(self, player):
    return player in self.players
```

Enables:

``` python
"Rahul" in team
```

## `__iter__`

``` python
def __iter__(self):
    return iter(self.players)
```

Enables:

``` python
for player in team:
    print(player)
```

## `__next__`

Used by iterator objects:

``` python
class Counter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        self.current += 1
        return self.current
```

------------------------------------------------------------------------

# 9. Callable Objects --- `__call__`

An object can behave like a function.

``` python
class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greeter = Greeter()

print(greeter("Alice"))
```

The call:

``` python
greeter("Alice")
```

uses:

``` python
greeter.__call__("Alice")
```

------------------------------------------------------------------------

# 10. Arithmetic Operators

  Operator   Left method      Reflected method
  ---------- ---------------- ------------------
  `+`        `__add__`        `__radd__`
  `-`        `__sub__`        `__rsub__`
  `*`        `__mul__`        `__rmul__`
  `/`        `__truediv__`    `__rtruediv__`
  `%`        `__mod__`        `__rmod__`
  `//`       `__floordiv__`   `__rfloordiv__`
  `**`       `__pow__`        `__rpow__`
  `@`        `__matmul__`     `__rmatmul__`

Example:

``` python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"Money({self.amount})"

print(Money(100) + Money(200))
```

------------------------------------------------------------------------

# 11. Reflected Operators

For:

``` python
x + y
```

Python normally gives `x` the first opportunity to handle the operation.
If appropriate, the reflected operation on `y` can be attempted.

Examples:

``` text
__radd__
__rsub__
__rmul__
__rtruediv__
__rfloordiv__
__rmod__
__rpow__
__rmatmul__
```

Returning `NotImplemented` is important when an operand type cannot
support an operation.

------------------------------------------------------------------------

# 12. Bitwise Operators

Custom objects can implement:

``` text
__and__      &
__or__       |
__xor__      ^
__lshift__   <<
__rshift__   >>
```

with reflected forms:

``` text
__rand__
__ror__
__rxor__
__rlshift__
__rrshift__
```

------------------------------------------------------------------------

# 13. Unary Operators

``` text
-x → __neg__
+x → __pos__
~x → __invert__
```

Example:

``` python
class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return Number(-self.value)

    def __repr__(self):
        return f"Number({self.value})"
```

------------------------------------------------------------------------

# 14. In-Place Operators

Augmented assignment has special methods:

``` text
+=   __iadd__
-=   __isub__
*=   __imul__
/=   __itruediv__
%=   __imod__
//=  __ifloordiv__
**=  __ipow__
@=   __imatmul__
&=   __iand__
|=   __ior__
^=   __ixor__
>>=  __irshift__
<<=  __ilshift__
```

Example:

``` python
class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount
        return self

counter = Counter(10)

counter += 5

print(counter.value)
```

Output:

``` text
15
```

For mutable objects, in-place methods commonly mutate and return the
same object.

------------------------------------------------------------------------

# 15. Math-Related Special Methods

Useful mappings include:

  Operation                   Method
  --------------------------- ----------------
  `abs(x)`                    `__abs__()`
  `divmod(x, y)`              `__divmod__()`
  `round(x)`                  `__round__()`
  `math.trunc(x)`             `__trunc__()`
  `math.floor(x)`             `__floor__()`
  `math.ceil(x)`              `__ceil__()`
  integer-required contexts   `__index__()`

`__index__` is for exact integer-like objects and is used by operations
requiring a true integer, such as certain indexing and slicing
operations.

------------------------------------------------------------------------

# 16. Attribute Access

Python provides hooks for:

``` text
__getattribute__
__getattr__
__setattr__
__delattr__
__dir__
```

### `__getattribute__`

Called for attribute access:

``` python
class Demo:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return object.__getattribute__(self, name)
```

Use carefully because incorrect implementations can recurse
indefinitely.

### `__getattr__`

Called when normal lookup fails:

``` python
class User:
    def __getattr__(self, name):
        return f"{name} is unavailable"
```

### `__setattr__`

Controls assignment:

``` python
class User:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        object.__setattr__(self, name, value)
```

### `__delattr__`

Controls deletion:

``` python
class User:
    def __delattr__(self, name):
        print(f"Deleting {name}")
        object.__delattr__(self, name)
```

### `__dir__`

Controls the result of `dir(obj)`.

------------------------------------------------------------------------

# 17. Metaprogramming

Advanced methods include:

``` text
__prepare__
__instancecheck__
__subclasscheck__
__init_subclass__
__subclasses__
__mro_entries__
__class_getitem__
```

## `__init_subclass__`

``` python
class Plugin:
    def __init_subclass__(cls):
        print(f"New plugin: {cls.__name__}")

class EmailPlugin(Plugin):
    pass
```

This lets a base class react when subclasses are defined.

## `__class_getitem__`

This enables subscription syntax on classes and is important for generic
type syntax.

``` python
class Box:
    @classmethod
    def __class_getitem__(cls, item):
        return (cls, item)

print(Box[int])
```

------------------------------------------------------------------------

# 18. Descriptors

Descriptors customize attribute access.

Important methods:

``` text
__set_name__
__get__
__set__
__delete__
```

Example:

``` python
class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
```

Descriptors are fundamental to mechanisms such as `property` and are
heavily used by frameworks.

------------------------------------------------------------------------

# 19. Buffer Protocol

Modern Python includes special methods associated with the buffer
protocol:

``` text
__buffer__
__release_buffer__
```

These are specialized, low-level hooks for objects exposing memory
buffers.

------------------------------------------------------------------------

# 20. Asynchronous Protocols

Async context managers:

``` text
__aenter__
__aexit__
```

Async iteration:

``` text
__aiter__
__anext__
```

Awaitable objects:

``` text
__await__
```

Example:

``` python
class AsyncResource:
    async def __aenter__(self):
        print("Opening")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Closing")
```

These participate in:

``` python
async with ...
async for ...
await ...
```

------------------------------------------------------------------------

# 21. Object Creation and Finalization

Important methods:

``` text
__new__
__init__
__del__
```

Conceptually:

``` text
Class(...)
   ↓
__new__()
   ↓
instance created
   ↓
__init__()
   ↓
instance initialized
```

### `__new__`

Participates in creating and returning the instance:

``` python
class Demo:
    def __new__(cls):
        print("Creating")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing")
```

For normal classes, prefer `__init__` unless you specifically need to
control object creation.

### `__del__`

A finalization hook:

``` python
class Resource:
    def __del__(self):
        print("Finalizing")
```

For deterministic cleanup of files, locks, database connections, etc.,
context managers are generally preferable.

------------------------------------------------------------------------

# 22. Standard-Library-Specific Dunder Methods

Some methods are associated with particular standard-library protocols:

``` text
__post_init__       → dataclasses
__subclasshook__    → ABC machinery
__fspath__          → path-like objects
__copy__            → shallow copy
__deepcopy__        → deep copy
__replace__         → replacement protocols
__getstate__        → serialization state
__setstate__        → restoring state
__reduce__          → pickling
__reduce_ex__       → pickling
__sizeof__          → object size
```

Example:

``` python
import os

class MyPath:
    def __init__(self, path):
        self.path = path

    def __fspath__(self):
        return self.path

path = MyPath("/tmp/example.txt")

print(os.fspath(path))
```

------------------------------------------------------------------------

# 23. Common Dunder Attributes

Dunder attributes are different from dunder methods.

Common examples:

``` text
__name__
__module__
__doc__
__class__
__dict__
__slots__
__mro__
__bases__
__file__
__wrapped__
__version__
__all__
```

Example:

``` python
class Student:
    """Represents a student."""

student = Student()

print(Student.__name__)
print(Student.__doc__)
print(student.__class__)
```

### `__dict__`

``` python
class User:
    def __init__(self):
        self.name = "Alice"
        self.age = 25

user = User()

print(user.__dict__)
```

### `__mro__`

``` python
class Animal:
    pass

class Dog(Animal):
    pass

print(Dog.__mro__)
```

Conceptually:

``` text
Dog
 ↓
Animal
 ↓
object
```

`__mro__` is especially important with multiple inheritance.

------------------------------------------------------------------------

# 24. Dunder Methods as Python Protocols

Think of dunder methods as **hooks into Python protocols**:

``` text
                    Python Protocols
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   Object Protocol    Container Protocol   Numeric Protocol
        │                  │                  │
    __repr__           __len__            __add__
    __str__            __iter__           __sub__
    __eq__             __getitem__        __mul__
```

Other protocol families include:

``` text
Context manager
    ↓
__enter__
__exit__

Async
    ↓
__aenter__
__aexit__
__aiter__
__anext__
__await__

Descriptor
    ↓
__get__
__set__
__delete__
```

------------------------------------------------------------------------

# 25. Complete Practical Example

``` python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"Money({self.amount})"

    def __str__(self):
        return f"₹{self.amount}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount < other.amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)


a = Money(100)
b = Money(200)

print(a)          # __str__
print(repr(a))    # __repr__
print(a == b)     # __eq__
print(a < b)      # __lt__
print(a + b)      # __add__
```

This makes the custom class work naturally with Python syntax.

------------------------------------------------------------------------

# 26. Interview Cheat Sheet

  Python syntax          Typical special method
  ---------------------- ----------------------------
  `Class(...)`           `__new__`, then `__init__`
  `str(obj)`             `__str__`
  `repr(obj)`            `__repr__`
  `obj == other`         `__eq__`
  `obj != other`         `__ne__`
  `obj < other`          `__lt__`
  `obj > other`          `__gt__`
  `len(obj)`             `__len__`
  `obj[i]`               `__getitem__`
  `obj[i] = value`       `__setitem__`
  `del obj[i]`           `__delitem__`
  `item in obj`          `__contains__`
  `for x in obj`         `__iter__`
  `next(obj)`            `__next__`
  `obj()`                `__call__`
  `a + b`                `__add__`
  `a - b`                `__sub__`
  `a * b`                `__mul__`
  `a / b`                `__truediv__`
  `with obj`             `__enter__`, `__exit__`
  `async with obj`       `__aenter__`, `__aexit__`
  `async for x in obj`   `__aiter__`, `__anext__`

------------------------------------------------------------------------

# 27. What to Learn First

Do not try to memorize every special method at once.

## Level 1 --- OOP and Interviews

``` text
__init__
__str__
__repr__
__eq__
__len__
__iter__
__getitem__
__call__
```

## Level 2 --- Operator Overloading

``` text
__add__
__sub__
__mul__
__truediv__
__lt__
__gt__
__le__
__ge__
```

## Level 3 --- Advanced Python

``` text
__new__
__getattr__
__getattribute__
__setattr__
__enter__
__exit__
__next__
```

## Level 4 --- Advanced Internals

``` text
__init_subclass__
__class_getitem__
__mro_entries__
__prepare__
__instancecheck__
__subclasscheck__
```

Then explore:

``` text
Descriptors
Metaclasses
Async protocols
Buffer protocol
Serialization
```

------------------------------------------------------------------------

# 28. Final Mental Model

``` text
                 YOUR CUSTOM CLASS
                        │
                        ↓
                 DUNDER METHODS
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
    Operators       Built-ins        Syntax
        │               │                │
        ↓               ↓                ↓
      + - *           len()             with
      == < >          bool()            for
      []              repr()            obj()
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                 Natural Python
                    behavior
```

### Key takeaway

> **Dunder methods allow custom objects to integrate with Python's
> built-in operations, syntax, and protocols.**

------------------------------------------------------------------------

## Source

Topic coverage was informed by:

**Python Morsels --- Every dunder method in Python**\
https://www.pythonmorsels.com/every-dunder-method/

For exact language semantics and version-specific behavior, consult the
official Python documentation.
