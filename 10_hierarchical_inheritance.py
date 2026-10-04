"""
Experiment 10: Hierarchical Inheritance
Demonstrates:
- Multiple derived classes inheriting from a single base class
- Method sharing and attribute reuse across child classes
- Shape hierarchy (Shape -> Circle, Square) with method overriding and super()
"""


# --- Example 1: Basic Hierarchical Inheritance ---
# Base class
class Parent:
    """Base class for child classes."""

    def func1(self):
        print("This function is in parent class.")


# Derived class 1
class Child1(Parent):
    """Child class 1 inheriting from Parent."""

    def func2(self):
        print("This function is in child 1.")


# Derived class 2
class Child2(Parent):
    """Child class 2 inheriting from Parent."""

    def func3(self):
        print("This function is in child 2.")


# --- Example 2: Shape Hierarchy with super() and Polymorphism ---
class Shape:
    """Base Shape class."""

    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    """Circle inheriting from Shape."""

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    """Square inheriting from Shape."""

    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length**2


if __name__ == "__main__":
    print("--- Example 1: Parent and Child Classes ---")
    object1 = Child1()
    object2 = Child2()

    print("Child 1 calls:")
    object1.func1()
    object1.func2()

    print("\nChild 2 calls:")
    object2.func1()
    object2.func3()

    print("\n--- Example 2: Shape, Circle, and Square ---")
    circle = Circle("Red", 5)
    square = Square("Blue", 4)

    print(f"Circle color: {circle.color}, Area: {circle.area()}")
    print(f"Square color: {square.color}, Area: {square.area()}")
