"""
Experiment 1: Default Constructor and Initializer
Demonstrates:
- Default constructor (__init__)
- Initializing instance variables
- Calling methods from the constructor
- Difference between instance variables and local variables
"""


class ATM:
    """ATM class demonstrating default constructor and automatic method invocation."""

    def __init__(self):  # DEFAULT CONSTRUCTOR OR INITIALIZER
        self.pin = None
        self.balance = 0
        print("ATM system initialized!")
        self.menu()  # Automatically call menu

    def menu(self):
        print("Hello! How can I help you?")
        print("1. Set PIN")
        print("2. Change PIN")
        print("3. Check Balance")
        print("4. Withdraw Cash")


class Addition:
    """Addition class demonstrating instance variables vs local variables."""

    # INITIALIZER
    def __init__(self):
        # Initializing INSTANCE variables
        self.num1 = 1000
        self.num2 = 2000
        self.num3 = 3000

    def result(self):
        X = 10  # LOCAL variable
        self.num = self.num1 + self.num2 + self.num3 + X
        print("Output", self.num)


if __name__ == "__main__":
    print("--- ATM Demonstration ---")
    atm1 = ATM()

    print("\n--- Addition Demonstration ---")
    Sum = Addition()
    # Calling the instance method using the object Sum
    Sum.result()
