# Phase 02: Abstraction in Python

## Objective
This phase focuses on **Abstraction**, one of the core pillars of Object-Oriented Programming (OOP).

The objective is to understand **how Python enforces contracts**, hides implementation details, and ensures that derived classes follow a predefined structure using **Abstract Base Classes (ABC)**.

Abstraction is critical for building **scalable, maintainable, and reliable systems**.

---

## What is Abstraction?

**Abstraction means exposing only what is necessary and hiding how it is implemented.**
**Hiding implementation details of a class and only showing the essential features to the user.**
In simple terms:
- You define **what a class must do**
- You do NOT define **how it must do it**

Python achieves abstraction using:
- `abc` module
- `ABC` base class
- `@abstractmethod` decorator

---

## Example: Car Abstraction in Python

### Concept
In real life, a user knows **what a car can do** (start, stop), but does not need to know **how the engine or motor works internally**.

This is **Abstraction**.

The abstract class defines the required behavior, and concrete classes provide the implementation.

---

### Code Example

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete Implementation
class PetrolCar(Car):

    def start(self):
        print("Petrol car engine started")

    def stop(self):
        print("Petrol car engine stopped")


class ElectricCar(Car):

    def start(self):
        print("Electric car motor started")

    def stop(self):
        print("Electric car motor stopped")


if __name__ == "__main__":
    car1 = PetrolCar()
    car1.start()
    car1.stop()

    car2 = ElectricCar()
    car2.start()
    car2.stop()

## Why Abstraction Matters

- Enforces consistent class behavior
- Prevents incomplete implementations
- Reduces tight coupling
- Improves code readability and reliability
- Makes large systems easier to maintain

Without abstraction, large codebases become fragile and error-prone.

---

## Concepts Covered

### 1. Abstract Base Classes (ABC)
- Creating abstract classes using `ABC`
- Role of abstract classes as contracts
- Why abstract classes cannot be instantiated

### 2. Abstract Methods
- Defining methods using `@abstractmethod`
- Mandatory implementation in child classes
- Compile-time–like enforcement in Python

### 3. Partial vs Complete Implementation
- Abstract classes can have:
  - Abstract methods
  - Concrete (implemented) methods
- Child classes must implement all abstract methods

### 4. Abstraction vs Interface (Python Context)
- How Python simulates interfaces using ABC
- Difference between abstraction and encapsulation
- When to use abstraction instead of inheritance alone

---

## Files in This Phase

| File Name | Purpose |
|---------|--------|
| `base.py` | Demonstrates basic abstraction using ABC |
| `abs_methods.py` | Shows mandatory method enforcement |
| `interface_like_abs.py` | Interface-style abstraction in Python |
| `exam_abs.py` | Practical abstraction use case |

---

## Key Takeaways

- Abstract classes **define rules**, not behavior
- You cannot create objects of abstract classes
- Child classes must implement all abstract methods
- Abstraction focuses on **what**, not **how**
- It is essential for large-scale system design

---

## Execution

Each file can be run independently:

```bash
python <filename>.py
