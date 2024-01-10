"""Account Entity CLass"""


class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0):
        # Validate input types and values
        # Initial balance must not be negative

        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Check if the amount is valid for deposit
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number")
        self.balance += amount
        return True

    def withdraw(self, amount):
        # Check if the amount is valid and available for withdrawal
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number")
        if amount > self.balance:
            raise ValueError("Insufficient Money in your account")
        self.balance -= amount
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("less balance")
        self.balance = self.balance-amount

    def get_balance(self):
        return self.balance

