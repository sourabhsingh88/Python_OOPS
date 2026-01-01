# Phase 5 – Polymorphism (OOP in Python)

## Objective
Establish a clear understanding of **polymorphism** and implement it to build flexible, scalable, and maintainable Python applications.  
This phase focuses on runtime behavior variation without changing the calling code.

---

## What Is Polymorphism?
**Polymorphism means one interface, multiple behaviors.**

In Python, the same method name can execute different logic depending on the object type at runtime.

Bottom line:  
You write generic code. Python handles the specialization.

---

## Why Polymorphism Is Non-Negotiable
From a system design perspective:
- Eliminates rigid `if-else` chains
- Improves extensibility (Open–Closed Principle)
- Reduces coupling between components
- Enables clean inheritance-based design

If your codebase lacks polymorphism, it will not scale.

---

## Types of Polymorphism in Python

---

### 1. Method Overriding (Runtime Polymorphism)
A child class provides its own implementation of a parent class method.

#### Rules
- Same method name
- Same parameters
- Decision happens at runtime

#### Example
```python
class Vehicle:
    def fuel_type(self):
        print("Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electric")

v1 = Car()
v2 = ElectricCar()

v1.fuel_type()
v2.fuel_type()
 ```
- Same method call. Different execution.
- That is polymorphism.
### 2. Operator Overloading (Compile Time Polymorphim)
- Operators can be redefined for user-defined objects using magic methods.
- Python does **NOT** support compile-time polymorphism.
## This means:
- You **cannot** create multiple functions or methods with the same name and different parameters.
- Python does **not** decide which method to call at compile time.
- The **last defined function** with a given name overwrites previous ones.
Example
```python

class Demo:
    def add(self, a, b):
        return a + b

    # This overwrites the previous method
    def add(self, a, b, c):
        return a + b + c


d = Demo()
print(d.add(1, 2, 3))   # ✅ Works
# print(d.add(1, 2))   # ❌ TypeError: missing argument



```
- Operators are just syntactic sugar for methods.
### 4. Polymorphism Using Inheritance

- Parent references can point to child objects.

Example
```python

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return "Rectangle Area"

class Circle(Shape):
    def area(self):
        return "Circle Area"

shapes = [Rectangle(), Circle()]

for shape in shapes:
    print(shape.area())


# Output
# 
# Rectangle Area
# Circle Area


```
- This is how real-world frameworks are designed.

### Key Interview Takeaways
1. Does Python support method overloading?

No.
Python does not support compile-time method overloading.
It supports runtime method overriding.

## Overloading vs Overriding

| Aspect              | Method Overloading                         | Method Overriding                          |
|---------------------|--------------------------------------------|--------------------------------------------|
| Definition          | Same method name with different parameters | Child class redefines parent class method |
| Binding Time        | Compile-time                               | Runtime                                    |
| Python Support      | ❌ Not supported natively                  | ✅ Fully supported                          |
| Inheritance Needed  | ❌ Not required                            | ✅ Mandatory                                |
| Method Signature    | Same name, different arguments             | Same name, same arguments                  |
| Polymorphism Type   | Compile-time polymorphism                  | Runtime polymorphism                       |
| Usage Scenario      | Languages like Java, C++                   | Core OOP mechanism in Python               |
| Real-world Usage    | Static method resolution                   | Dynamic behavior selection                 |


## What Is Runtime Polymorphism?

Method resolution happens during execution based on the object type, not the reference type.

## Common Anti-Patterns

- Using if-elif instead of overriding

- Not maintaining method signatures

- Mixing responsibilities in parent classes

- Calling parent logic unnecessarily

- These are design failures, not syntax issues.

### When to Use Polymorphism

- Payment gateways

- Notification systems

- Strategy-based logic

- Role-based access systems

- Shape / Vehicle / Product hierarchies

## If behavior changes but interface stays constant, polymorphism is mandatory.

### Phase 5 Summary

- Polymorphism enables dynamic behavior

- Method overriding is the core mechanism

- Reduces code duplication

- Critical for scalable and clean architecture