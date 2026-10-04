"""
Experiment 8: Super Function and Cooperative Multiple Inheritance
Demonstrates:
- Using super() to delegate method calls to the next class in MRO
- Avoiding explicit hardcoding of base class names
- Cooperative multiple inheritance resolving diamond hierarchy cleanly
"""


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()


class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        super().m()


if __name__ == "__main__":
    print("--- Super() in Multiple Inheritance Demonstration ---")
    obj = Class4()
    obj.m()

    print("\nMethod Resolution Order (MRO):")
    for idx, cls in enumerate(Class4.__mro__, start=1):
        print(f"  {idx}. {cls.__name__}")
