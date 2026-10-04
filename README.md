# Object-Oriented Programming (OOP) in Python - Lab Experiments

This repository contains implementations and demonstrations of core Object-Oriented Programming (OOP) concepts in Python, based on **Experiment 8: OOP in Python**.

---

## 📚 Table of Contents
1. [Overview](#overview)
2. [Experiment List](#experiment-list)
   - [Exp 1: Default Constructor & Initializer](#exp-1-default-constructor--initializer)
   - [Exp 2: Class Variables vs Instance Variables](#exp-2-class-variables-vs-instance-variables)
   - [Exp 3: Parameterized Constructor](#exp-3-parameterized-constructor)
   - [Exp 4: Constructor with Default Arguments](#exp-4-constructor-with-default-arguments)
   - [Exp 5: Real-World OOP (Bank Account)](#exp-5-real-world-oop-bank-account)
   - [Exp 6: Single Inheritance](#exp-6-single-inheritance)
   - [Exp 7: Multiple Inheritance & MRO](#exp-7-multiple-inheritance--mro)
   - [Exp 8: Super Function in Multiple Inheritance](#exp-8-super-function-in-multiple-inheritance)
   - [Exp 9: Multilevel Inheritance](#exp-9-multilevel-inheritance)
   - [Exp 10: Hierarchical Inheritance](#exp-10-hierarchical-inheritance)
   - [Exp 11: Hybrid Inheritance](#exp-11-hybrid-inheritance)
   - [Exp 12: Polymorphism (Overloading & Overriding)](#exp-12-polymorphism-overloading--overriding)
3. [How to Run](#how-to-run)
4. [Output Verification](#output-verification)

---

## 🔍 Overview
Object-Oriented Programming is a paradigm based on the concept of "objects" containing data attributes and code methods. This repository covers:
- Constructors (`__init__`) and initializers
- Attribute scope (Class variables vs Instance variables)
- Inheritance patterns (Single, Multiple, Multilevel, Hierarchical, Hybrid)
- Python's Method Resolution Order (MRO) and C3 Linearization
- Cooperative multiple inheritance with `super()`
- Polymorphism (Method Overloading simulation & Method Overriding)

---

## 🧪 Experiment List

### Exp 1: Default Constructor & Initializer
- **File:** `01_default_constructor.py`
- **Concepts:** `__init__`, automatic method invocation upon instantiation (`ATM` class), instance vs local variable scope (`Addition` class).

### Exp 2: Class Variables vs Instance Variables
- **File:** `02_class_and_instance_variables.py`
- **Concepts:** Class-level attributes shared across all instances (`Demo.x`) vs instance-level attributes (`Student.name`, `Student.marks`).

### Exp 3: Parameterized Constructor
- **File:** `03_parameterized_constructor.py`
- **Concepts:** Initializing objects with specific parameters upon instantiation (`Student("JOHN", 2023, "MIT")`).

### Exp 4: Constructor with Default Arguments
- **File:** `04_constructor_default_arguments.py`
- **Concepts:** Defining optional attributes with default values (`Employee(name="Not Assigned", salary=0)`).

### Exp 5: Real-World OOP (Bank Account)
- **File:** `05_bank_account.py`
- **Concepts:** State encapsulation, deposits, withdrawals, and state reporting.

### Exp 6: Single Inheritance
- **File:** `06_single_inheritance.py`
- **Concepts:** A child class deriving from a single parent class (`Child(Parent)`).

### Exp 7: Multiple Inheritance & MRO
- **File:** `07_multiple_inheritance.py`
- **Concepts:** Deriving from two base classes (`Son(Mother, Father)`), Diamond pattern, Method Resolution Order (MRO), and explicit parent method calling.

### Exp 8: Super Function in Multiple Inheritance
- **File:** `08_super_function.py`
- **Concepts:** Using `super()` for cooperative multiple inheritance without hardcoded parent class names.

### Exp 9: Multilevel Inheritance
- **File:** `09_multilevel_inheritance.py`
- **Concepts:** Linear inheritance chain (`Grandfather` -> `Father` -> `Son`) with chained constructor calls.

### Exp 10: Hierarchical Inheritance
- **File:** `10_hierarchical_inheritance.py`
- **Concepts:** Single base class inherited by multiple derived classes (`Parent` -> `Child1`, `Child2` and `Shape` -> `Circle`, `Square`).

### Exp 11: Hybrid Inheritance
- **File:** `11_hybrid_inheritance.py`
- **Concepts:** Combining Single and Multiple inheritance (`School` -> `Student1`, `Student2` -> `Student3`).

### Exp 12: Polymorphism (Overloading & Overriding)
- **File:** `12_polymorphism_overloading_overriding.py`
- **Concepts:** Compile-time polymorphism simulation via default parameters/`*args` and run-time polymorphism via method overriding.

---

## 🚀 How to Run

### Run All Experiments
To execute all 12 experiments in sequence:
```bash
python run_all_experiments.py
```

### Run an Individual Experiment
To run any specific experiment:
```bash
python 01_default_constructor.py
python 06_single_inheritance.py
# etc.
```

---

## 📋 Requirements
- Python 3.8+ (Tested on Python 3.14)
- Standard Python libraries only (no external dependencies required)
