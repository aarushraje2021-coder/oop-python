"""
Experiment 9: Multilevel Inheritance
Demonstrates:
- Multilevel inheritance hierarchy (Grandfather -> Father -> Son)
- Chained constructor initialization across levels of inheritance
- Accessing attributes inherited across multiple generations of classes
"""


# Base class
class Grandfather:
    """Base class at the top of the multilevel hierarchy."""

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# Intermediate class
class Father(Grandfather):
    """Intermediate class inheriting from Grandfather."""

    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)


# Derived class
class Son(Father):
    """Derived class inheriting from Father and indirectly Grandfather."""

    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        """Print names from all three generations."""
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)


if __name__ == "__main__":
    print("--- Multilevel Inheritance Demonstration ---")
    # Driver code
    s1 = Son('ABC', 'MUKESH', 'DHIRUBHAI')
    print("Accessing direct attribute:", s1.grandfathername)
    print("\nCalling print_name() method:")
    s1.print_name()
