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


## Repository Structure

```text
python-oops-journey/
├── 01_basics/
├── 02_encapsulation/
├── 03_inheritance/
├── 04_polymorphism/
├── 05_abstraction/
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
