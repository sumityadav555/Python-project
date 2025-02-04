class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a new bank account with a holder name and balance."""
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        """Check the account balance."""
        print(f"{self.account_holder}'s Account Balance: ${self.balance}")

# Creating a bank account
account = BankAccount("Alice", 1000)

# Performing transactions
account.deposit(500)
account.withdraw(200)
account.check_balance()

