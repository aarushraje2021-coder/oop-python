"""
Experiment 6: Single Inheritance
Demonstrates:
- Base class (Parent) and Derived class (Child)
- Inheriting methods from a single parent class
- Reusability of code through inheritance
"""


# Base class
class Parent:
    """Parent class defining base functionality."""

    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):
    """Child class inheriting from Parent class."""

    def func2(self):
        print("This function is in child class.")


if __name__ == "__main__":
    print("--- Single Inheritance Demonstration ---")
    # Driver code
    obj = Child()
    obj.func1()  # Inherited from Parent
    obj.func2()  # Defined in Child
