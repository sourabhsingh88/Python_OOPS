# Python OOP Journey 🚀

This repository documents my end-to-end learning journey of Object-Oriented Programming (OOP) in Python.

## What this repo covers
- Core OOP concepts (classes, objects, methods)
- Encapsulation, Inheritance, Polymorphism, Abstraction
- Static methods vs Class methods
- Advanced Python OOP features
- Design patterns
- Mini real-world projects

## Why this repo exists
- To build strong OOP fundamentals
- To create interview-ready examples
- To demonstrate structured Python knowledge on GitHub

## How to use
Each folder represents a focused OOP concept with clean, runnable examples.

## Tech Stack
- Python 3.x

## Status
🚧 Actively maintained and updated


S## Repository Structure

```text
python-oops-journey/
├── 01_basics/
├── 02_encapsulation/
├── 03_abstraction/
├── 04_inheritance/
├── 05_polymorphism/
├── 06_advanced_oop/
├── 07_design_patterns/
├── 08_mini_projects/
└── README.md
```

# Phase 01: OOP Basics in Python

## Objective
This phase establishes the foundational building blocks of Object-Oriented Programming (OOP) in Python. The goal is to understand how Python models real-world entities using classes and objects, and how behavior and state are encapsulated within them.

This phase is non-negotiable. Every advanced OOP concept depends on mastery of what is covered here.

---

## Concepts Covered

### 1. Classes and Objects
- Definition and purpose of a class
- Creating objects (instances)
- Relationship between class blueprint and object state

### 2. Constructors (`__init__`)
- Role of the constructor in object initialization
- Using `self` to bind instance data
- Difference between constructor parameters and instance variables

### 3. Instance vs Class Variables
- Instance variables: object-specific state
- Class variables: shared state across instances
- When to use each and why misuse causes bugs

### 4. Method Types (Intro)
- Instance methods
- Static methods (utility behavior)
- High-level distinction from class methods (deep dive later)

---

## Files in This Phase

| File Name | Purpose |
|---------|--------|
| `classes_and_objects.py` | Demonstrates basic class structure and object creation |
| `constructors.py` | Covers object initialization and constructor behavior |
| `instance_vs_class_variables.py` | Explains data ownership and scope |
| `methods_types.py` | Introduces instance and static methods |

---

## Key Takeaways
- `self` is a reference to the current object, not a keyword
- Objects store state; classes define structure and behavior
- Poor understanding of basics leads to fragile designs later
- Static methods do not operate on object or class state

---

## Execution
Each file is independently executable.

```bash
python <filename>.py
```
#### Phase 02: Abstraction in Python

## Objective
This phase focuses on **Abstraction**, one of the core pillars of Object-Oriented Programming (OOP).

The objective is to understand **how Python enforces contracts**, hides implementation details, and ensures that derived classes follow a predefined structure using **Abstract Base Classes (ABC)**.

Abstraction is critical for building **scalable, maintainable, and reliable systems**.

---

## What is Abstraction?

**Abstraction means exposing only what is necessary and hiding how it is implemented.**

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
```

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
- Interface = abstract class with only abstract methods
- Abstract class = abstract + concrete methods
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
```

### 🛡️ Phase 03: Encapsulation in Python

## 🎯 Objective
This phase focuses on **Encapsulation**, a core pillar of Object-Oriented Programming (OOP). You will learn how Python protects internal object states, controls data access, and enforces business rules to ensure objects remain robust and cannot be misused by external code.

> **Note:** Encapsulation is mandatory for building stable, maintainable, and production-ready systems.

---

## 🧩 What is Encapsulation?

Encapsulation is the process of **bundling data and methods** together while **restricting direct access** to the internal state of an object.



### In Practical Terms:
* **Hidden Data:** Internal variables are shielded from the outside world.
* **Controlled Access:** Interacting with data is only possible through defined interfaces.
* **Integrity Enforcement:** Invalid state changes (e.g., setting a negative balance) are blocked at the source.

### simple words
- Controls access → prevents direct, uncontrolled modification
- Adds validation → ensures only valid data enters the object
- Maintains data integrity → object never enters an invalid state
---

## 🐍 Encapsulation in Python: The Reality

Unlike languages like Java or C++, Python does **not** strictly enforce access modifiers. There is no true "hard" `private` keyword. Instead, Python relies on:

1.  **Naming Conventions:** Using underscores to signal intent.
2.  **Developer Discipline:** Respecting the "consenting adults" philosophy.

---

## 🚦 Access Levels in Python (By Convention)

| Level | Syntax | Meaning |
| :--- | :--- | :--- |
| **Public** | `variable` | Free access from anywhere. (Avoid for mutable data). |
| **Protected** | `_variable` | Internal or subclass use only. |
| **Private** | `__variable` | Class-private; triggers **Name Mangling**. |

---

## ❌ Example 1: No Encapsulation (The Anti-Pattern)

```python
class Account:
    def __init__(self, balance):
        self.balance = balance  # Public attribute
```

## What’s Wrong Here?

- Direct Modification: Anyone can set acc.balance = -99999.

- No Validation: There is no logic to check if the change is legal.

- Fragile State: The object is a "weak container" rather than a smart entity.

## 🔒 Example 2: Using Private Attributes

```Python

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
```
- Internal Magic: Python rewrites __balance as _Account__balance. This process,
- called Name Mangling, prevents accidental external access.

## ✨ Example 3: The Pythonic Way (@property)
- This is the standard practice for modern Python development.

```Python

class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        """The Getter: Controls read access."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """The Setter: Validates data before changing state."""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
```

## 🛠️ Example 4: Behavior-Based Encapsulation (Best Practice)
- Top-tier developers stop exposing "setters" and instead expose Intent-Based Actions.

```Python

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance
```

## Why this is superior:
- State Integrity: You cannot "glitch" the balance; you must follow the deposit or withdraw rules.

- Encapsulated Logic: The math happens inside the class, not in the main script.

## ⚖️ Encapsulation vs Abstraction

| Concept | Purpose | Question It Answers |
|--------|--------|---------------------|
| Encapsulation | Protects internal state | How is the data protected? |
| Abstraction | Hides complexity | What does this object do? |


### ⚠️ Common Pitfalls to Avoid

✅
```md
1. **The Public Trap** – Making all attributes public by default  
2. **Useless Setters** – Setters without validation  
3. **Bypassing Mangling** – Accessing `_Class__var` externally  
4. **Struct Thinking** – Treating classes as data containers  
```

### 🚀 Key Takeaways
**Public mutable data is a liability.** Always protect data that shouldn't be changed arbitrarily.

**Validation belongs inside the class.**

**Expose behavior, not state.** Give your objects "verbs" (methods) rather than just "nouns" (attributes).

**Python trusts you.** The language gives you the tools, but it won't stop you from breaking your own rules.

## Execution

Each file can be run independently:

```bash
python <filename>.py
```