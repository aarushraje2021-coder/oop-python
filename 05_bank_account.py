"""
Experiment 5: Real-World OOP Application - Bank Account Management
Demonstrates:
- Encapsulation of state (balance, account holder name)
- Methods to modify internal state (deposit, withdraw)
- Displaying updated object state
"""


class BankAccount:
    """Bank account class encapsulating balance and transaction methods."""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit an amount into the account."""
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        """Withdraw an amount from the account."""
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def display(self):
        """Display current account information."""
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


if __name__ == "__main__":
    print("--- Bank Account Demonstration ---")
    acc = BankAccount("Sneha", 10000)
    acc.display()

    print("\nPerforming Transactions:")
    acc.deposit(2000)
    acc.withdraw(1500)

    print("\nUpdated Account Details:")
    acc.display()
