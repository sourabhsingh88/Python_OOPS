# 🛡️ Phase 03: Encapsulation in Python

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