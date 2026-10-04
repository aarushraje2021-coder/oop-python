"""
Experiment 2: Class Variables vs Instance Variables
Demonstrates:
- Defining and accessing class variables (shared across all instances)
- Defining and accessing instance variables (unique to each object instance)
- Scope and behavior when modifying class vs instance attributes
"""


class Demo:
    """Demo class showing class variable shared across instances."""

    x = 100  # CLASS variable (belongs to the class, shared by all instances)


class Student:
    """Student class illustrating instance variables."""

    def __init__(self, name, marks):
        self.name = name        # INSTANCE variable
        self.marks = marks      # INSTANCE variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


if __name__ == "__main__":
    print("--- Class Variable Demonstration ---")
    a = Demo()
    b = Demo()
    print("Value of a.x:", a.x)  # 100
    print("Value of b.x:", b.x)  # 100

    print("\n--- Modifying Class Variable ---")
    Demo.x = 200
    print("After Demo.x = 200:")
    print("Value of a.x:", a.x)  # 200
    print("Value of b.x:", b.x)  # 200

    print("\n--- Instance Variable Demonstration ---")
    s1 = Student("Rahul", 85)
    s2 = Student("Priya", 92)
    s1.display()
    s2.display()
