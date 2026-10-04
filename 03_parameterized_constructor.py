"""
Experiment 3: Parameterized Constructor
Demonstrates:
- Defining a parameterized constructor (__init__) with arguments
- Passing arguments during object creation
- Assigning arguments to instance attributes
- Displaying object details using instance methods
"""


class Student:
    """Student class demonstrating a parameterized constructor."""

    # Defining a parameterized constructor having arguments
    def __init__(self, name, ids, college):
        print("This is a parameterized constructor in python")
        self.name = name
        self.ids = ids
        self.college = college

    def Display_Details(self):
        """Display student details."""
        print("Student Details")
        print("Student Name", self.name)
        print("Student ids", self.ids)
        print("Student college", self.college)


if __name__ == "__main__":
    # Here we create the objects
    student = Student("JOHN", 2023, "MIT")
    student1 = Student("rahul", 2023, "MIT")

    print()
    # Calling the instance method using the object student
    student.Display_Details()
    print()
    student1.Display_Details()
