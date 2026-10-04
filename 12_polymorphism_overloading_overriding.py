"""
Experiment 12: Polymorphism - Method Overloading and Method Overriding
Demonstrates:
- Compile-time Polymorphism: Method Overloading
  (Python does not support traditional method overloading; implemented using default arguments and *args)
- Run-time Polymorphism: Method Overriding
  (A child class provides a specific implementation of a method already defined in its parent class)
"""


# --- Part 1: Method Overloading (Compile-Time Polymorphism Simulation) ---
class Calculator:
    """Demonstrates Method Overloading using default parameters and variable arguments."""

    # Overloading using default arguments
    def add(self, a=None, b=None, c=None):
        """Add two or three numbers based on provided arguments."""
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        return 0

    # Overloading using variable-length arguments (*args)
    def sum_all(self, *args):
        """Sum any number of arguments."""
        return sum(args)


# --- Part 2: Method Overriding (Run-Time Polymorphism) ---
class Animal:
    """Base class defining generic behavior."""

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    """Child class overriding speak() method."""

    def speak(self):
        print("The dog barks: Woof! Woof!")


class Cat(Animal):
    """Child class overriding speak() method."""

    def speak(self):
        print("The cat meows: Meow! Meow!")


if __name__ == "__main__":
    print("=== Method Overloading Demonstration ===")
    calc = Calculator()
    print("Add with 1 arg (5):", calc.add(5))
    print("Add with 2 args (5, 10):", calc.add(5, 10))
    print("Add with 3 args (5, 10, 15):", calc.add(5, 10, 15))
    print("Sum with variable args (1, 2, 3, 4, 5):", calc.sum_all(1, 2, 3, 4, 5))

    print("\n=== Method Overriding Demonstration ===")
    generic_animal = Animal()
    dog = Dog()
    cat = Cat()

    print("Animal:")
    generic_animal.speak()

    print("\nDog (Overridden):")
    dog.speak()

    print("\nCat (Overridden):")
    cat.speak()
