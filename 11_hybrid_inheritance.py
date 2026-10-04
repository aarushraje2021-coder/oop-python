"""
Experiment 11: Hybrid Inheritance
Demonstrates:
- Combining multiple inheritance types (Single + Multiple Inheritance)
- Base class: School
- Single Inheritance: Student1 and Student2 inherit from School
- Multiple Inheritance: Student3 inherits from Student1 and School
- Resolving methods through the inheritance tree
"""


# Base class
class School:
    """Base class School."""

    def func1(self):
        print("This function is in school.")


# Derived class 1 (Single Inheritance)
class Student1(School):
    """Derived class 1 inheriting from School."""

    def func2(self):
        print("This function is in student 1.")


# Derived class 2 (Another Single Inheritance)
class Student2(School):
    """Derived class 2 inheriting from School."""

    def func3(self):
        print("This function is in student 2.")


# Derived class 3 (Multiple Inheritance combining Student1 and School)
class Student3(Student1, School):
    """Derived class 3 combining Student1 and School."""

    def func4(self):
        print("This function is in student 3.")


if __name__ == "__main__":
    print("--- Hybrid Inheritance Demonstration ---")
    # Driver code
    obj = Student3()
    obj.func1()  # From School (inherited via Student1 or School)
    obj.func2()  # From Student1
    obj.func4()  # From Student3

    print("\nMethod Resolution Order (MRO) for Student3:")
    for idx, cls in enumerate(Student3.__mro__, start=1):
        print(f"  {idx}. {cls.__name__}")
