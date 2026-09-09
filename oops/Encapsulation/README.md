# Encapsulation in Python

## Introduction

**Encapsulation** is one of the four fundamental concepts of
Object-Oriented Programming (OOP).

It means **bundling data (attributes) and the methods that operate on
that data inside a class**, while controlling how that data can be
accessed or modified.

In simple words:

> **Encapsulation = Data + Methods + Controlled Access**

The main goal is to protect an object's internal state from unwanted or
invalid changes.

------------------------------------------------------------------------

## Simple Example

Consider a bank account:

``` python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
```

Here, the `balance` and the methods that modify it are bundled inside
`BankAccount`.

------------------------------------------------------------------------

# Access Modifiers in Python

Python commonly uses naming conventions to indicate different levels of
access:

  -----------------------------------------------------------------------
  Type                    Syntax                  Meaning
  ----------------------- ----------------------- -----------------------
  Public                  `name`                  Can be accessed
                                                  directly

  Protected               `_name`                 Intended for the class
                                                  and subclasses

  Private                 `__name`                Name-mangled to
                                                  discourage direct
                                                  external access
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 1. Public Members

Public members can be accessed directly from outside the class.

``` python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Rahul")

print(student.name)
```

Output:

``` text
Rahul
```

`name` is a **public attribute**.

---

## 2. Protected Members

A single underscore `_` indicates that a member is intended for internal
use or use by subclasses.

``` python
class Student:

    def __init__(self, name):
        self._name = name


student = Student("Rahul")

print(student._name)
```

Python still allows access to `_name`, because `_` is mainly a
**convention**, not strict access control.

``` text
_name
  ↓
"Please treat this as internal"
```

------------------------------------------------------------------------

## 3. Private Members

A double underscore `__` triggers **name mangling**.

``` python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(5000)

# print(account.__balance)  # AttributeError
```

The attribute cannot normally be accessed using:

``` python
account.__balance
```

Python internally changes its name approximately to:

``` text
_BankAccount__balance
```

This is called **name mangling**.

> Python's private members are not absolutely private; name mangling
> mainly prevents accidental access and name conflicts.

------------------------------------------------------------------------

# Encapsulation Using Methods

Instead of allowing users to modify important data directly, we can
provide controlled methods.

``` python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance
```

Usage:

``` python
account = BankAccount(5000)

account.deposit(1000)
account.withdraw(200)

print(account.get_balance())
```

Output:

``` text
5800
```

The user does not directly modify:

``` python
__balance
```

Instead, they use:

``` text
deposit()
withdraw()
get_balance()
```

This provides **controlled access** to the data.

------------------------------------------------------------------------

# Encapsulation with `@property`

Python provides `@property` for creating controlled access to
attributes.

``` python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")
```

Usage:

``` python
account = BankAccount(5000)

print(account.balance)

account.balance = 8000
print(account.balance)

account.balance = -100
```

Output:

``` text
5000
8000
Balance cannot be negative
```

The property allows us to **control how a value is read and changed**.

------------------------------------------------------------------------

# ❌ Example Without Proper Encapsulation

``` python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account = BankAccount(5000)

account.balance = -100000
```

There is no validation.

The object's state can become invalid.

------------------------------------------------------------------------

# ✅ Example With Encapsulation

``` python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance
```

Now the balance can only be changed through controlled operations.

``` text
              BankAccount
                   |
          ┌────────┴────────┐
          ↓                 ↓
      __balance          Methods
                            |
                  ┌─────────┼─────────┐
                  ↓         ↓         ↓
               deposit   withdraw  get_balance
```

------------------------------------------------------------------------

# Why Do We Need Encapsulation?

### 1. Data Protection

Important data can be protected from accidental modification.

### 2. Validation

We can validate data before changing the object's state.

``` python
if amount > 0:
    self.__balance += amount
```

### 3. Controlled Access

Users interact with an object through defined methods instead of
directly changing internal data.

### 4. Maintainability

Internal implementation can change without changing how other parts of
the program use the class.

### 5. Reduced Coupling

Other parts of the application don't need to know the internal details
of a class.

------------------------------------------------------------------------

# Encapsulation vs Abstraction

These concepts are often confused.

### Encapsulation

Focuses on:

> **How do we bundle and control access to data and behavior?**

``` text
Data + Methods
      ↓
   Class
      ↓
Controlled Access
```

### Abstraction

Focuses on:

> **What should the user see, while hiding unnecessary implementation
> details?**

``` text
Complex Implementation
        ↓
    Simple Interface
```

### Easy Difference

``` text
Encapsulation → Protect / control data

Abstraction   → Hide complexity
```

------------------------------------------------------------------------

# Real-World Example

Think about an ATM.

You interact with:

``` text
Withdraw Money
Deposit Money
Check Balance
```

But you don't directly manipulate the bank's internal database.

``` text
             ATM
              |
       ┌──────┼──────┐
       ↓      ↓      ↓
   Withdraw Deposit Balance
       |
       ↓
   Controlled access
       |
       ↓
   Internal account data
```

The internal account data is protected, and operations are provided
through controlled interfaces.

------------------------------------------------------------------------

# Interview-Friendly Definition

If an interviewer asks:

### "What is Encapsulation?"

A good answer is:

> **Encapsulation is the OOP principle of bundling data and the methods
> that operate on that data inside a class while controlling access to
> the internal state. In Python, it is commonly implemented using
> public, protected, and private naming conventions, along with
> properties and methods for controlled access.**

## One-Line Memory Trick

``` text
ENCAPSULATION
      =
DATA + METHODS
      +
CONTROLLED ACCESS
```

------------------------------------------------------------------------

## Key Takeaways

-   Encapsulation bundles **data and behavior** inside a class.
-   It helps protect an object's internal state.
-   Python uses `_` and `__` naming conventions for protected/private
    members.
-   `__name` uses **name mangling**.
-   Use methods or `@property` when you need controlled access or
    validation.
-   Encapsulation improves **maintainability, safety, and control**.
