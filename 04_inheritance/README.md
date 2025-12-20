# Phase 4 – Inheritance (Python OOP)

## Overview

Inheritance is a core Object-Oriented Programming (OOP) concept that allows a class
(child / subclass) to reuse and extend the behavior of another class
(parent / superclass).

It establishes an **IS-A relationship** between classes and enables:
- Code reuse
- Logical hierarchy
- Method overriding
- Polymorphism

---

## Key Terminology

| Term        | Meaning |
|-------------|--------|
| Parent Class | The class being inherited from |
| Child Class  | The class that inherits |
| `super()`    | Used to access parent class methods/constructor |
| IS-A         | Relationship created by inheritance |

Example:
- `Car` → Parent
- `Fortuner` → Child  
- `Fortuner IS A Car`

---

## Basic Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

### Real-World Example

```python
# Parent Class: Car
class Car:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print(self.fuel_type, "car started")

    def stop(self):
        print(self.fuel_type, "car stopped")

# Child Class: Fortuner
class Fortuner(Car):
    def __init__(self, model, fuel_type):
        super().__init__(fuel_type)   # initialize parent
        self.model = model
        self.start()                  # inherited method

    def offroad(self):
        print(self.model, "model", self.fuel_type, "car on off-road")

# Object Creation
c1 = Fortuner(2018, "Petrol")
c1.offroad()

# Output
# Petrol car started
# 2018 model Petrol car on off-road
```

### super() Keyword

## super() is used to:

- Call parent class constructor

- call parent class methods

- Without super(), parent initialization will not occur.
```python
super().__init__("FuelType - not in a string")
super().start()
```

Types of Inheritance in Python
1. Single Inheritance
```python

class A:
    pass

class B(A):
    pass

```

2. Multilevel Inheritance
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

3. Multiple Inheritance
```python

class A:
    pass

class B:
    pass

class C(A, B):
    pass

```

### Method Overriding (Polymorphism)

- Child class can redefine parent behavior.

```python

class Car:
    def start(self):
        print("Car started")

class ElectricCar(Car):
    def start(self):
        print("Electric car started silently")

```