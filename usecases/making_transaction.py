"""Make transaction use case"""

class MakeTransaction:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_repository, account_id, amount, transaction_type):
        # Validate inputs and retrieve account
        if not account_repository:
            raise ValueError("Repository is required")

        try:
            account = account_repository.find_account_by_id(account_id)
            if not account:
                raise ValueError("Account not found!, Invalid account ID")
            if transaction_type == 'withdraw':
                return account.withdraw(amount)
            elif transaction_type == 'deposit':
                return account.deposit(amount)
            else:
                raise ValueError("Invalid transaction type")
        except ValueError as e:
            # Log the error or handle it as required
            raise
