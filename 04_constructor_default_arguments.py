"""
Experiment 4: Constructor with Default Arguments
Demonstrates:
- Defining default parameter values in __init__
- Instantiating objects with and without arguments
- Handling optional attributes gracefully in classes
"""


class Employee:
    """Employee class demonstrating default values in constructor arguments."""

    def __init__(self, name="Not Assigned", salary=0):
        self.name = name
        self.salary = salary

    def display(self):
        """Display employee name and salary."""
        print(self.name, self.salary)


if __name__ == "__main__":
    print("--- Constructor with Default Arguments ---")
    # Instantiation without arguments uses default values
    e1 = Employee()

    # Instantiation with arguments overrides defaults
    e2 = Employee("Amit", 40000)

    e1.display()
    e2.display()
