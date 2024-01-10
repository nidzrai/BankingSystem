from BankingSystem.domain.entities.account import Account
from BankingSystem.infrastructure import AccountRepository
from BankingSystem.usecases import GenerateAccountStatement
from BankingSystem.usecases import MakeTransaction


def main():
    # Initialize the repository
    account_repository = AccountRepository()

    # Initialize use case classes with the repository
    account_creation = Account(account_repository)
    transaction = MakeTransaction(account_repository)
    account_statement = GenerateAccountStatement(account_repository)

    # Example: Create a new account
    new_account = account_creation.create_account(customer_id=1, name="test test", email="test.test@example.com", phone_number="9199191991")
    print(f"New account created with ID: {new_account.account_id} and balance: {new_account.get_balance()}")

    # Example: Perform a deposit transaction
    transaction.make_transaction(account_id=new_account.account_id, amount=10000000000000, transaction_type='deposit')
    print(f"Account balance after deposit: {new_account.get_balance()}")

    # Example: Generate an account statement
    statement = account_statement.generate_account_statement(account_id=new_account.account_id)
    print(statement)

if __name__ == "__main__":
    main()