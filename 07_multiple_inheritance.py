"""
Experiment 7: Multiple Inheritance & Method Resolution Order (MRO)
Demonstrates:
- Inheriting from multiple parent classes (Mother, Father -> Son)
- Method overriding across multiple base classes (Diamond Problem)
- Python's C3 Linearization (Method Resolution Order - MRO)
- Explicit invocation of parent class methods using ClassName.method(self)
"""


# --- Example 1: Basic Multiple Inheritance ---
class Mother:
    """Base class 1: Mother"""

    mothername = ""

    def mother(self):
        print("Mother's Name:", self.mothername)


class Father:
    """Base class 2: Father"""

    fathername = ""

    def father(self):
        print("Father's Name:", self.fathername)


class Son(Mother, Father):
    """Derived class inheriting from both Mother and Father."""

    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


# --- Example 2: Method Overriding in Multiple Inheritance (MRO) ---
class BaseA:
    def m(self):
        print("In BaseA")


class SubB(BaseA):
    def m(self):
        print("In SubB (overriding BaseA)")


class SubC(BaseA):
    def m(self):
        print("In SubC (overriding BaseA)")


class DiamondClass(SubB, SubC):
    """Inherits from SubB and SubC; MRO determines which m() executes."""
    pass


# --- Example 3: Explicit Parent Method Calling ---
class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)


class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)


if __name__ == "__main__":
    print("--- Example 1: Mother, Father, Son ---")
    s1 = Son()
    s1.fathername = "RAM"
    s1.mothername = "SITA"
    s1.parents()

    print("\n--- Example 2: MRO Resolution in Diamond Inheritance ---")
    obj_diamond = DiamondClass()
    obj_diamond.m()
    print("MRO:", [cls.__name__ for cls in DiamondClass.__mro__])

    print("\n--- Example 3: Explicitly Calling Parent Class Methods ---")
    obj4 = Class4()
    obj4.m()
