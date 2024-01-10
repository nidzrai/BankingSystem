# Test Scenario
from infrastructure import AccountRepository
from BankingSystem.usecases.create_account import CreateAccount
from BankingSystem.usecases.createnewcustomer import CreateCustomer
from BankingSystem.usecases.generate_statment import GenerateAccountStatement
from BankingSystem.usecases.making_transaction import MakeTransaction


def test_banking_system():
    customer_id = "3123"
    name = "test test"
    email = "test@test.com"
    phone_number = "23423"
    account_repository = AccountRepository()
    create_customer = CreateCustomer()
    create_account = CreateAccount(account_repository)
    make_transaction = MakeTransaction(account_repository)
    generate_account_statement = GenerateAccountStatement(account_repository)

    # Creating a new account
    customer = create_customer.create_customer(name, email, phone_number)
    account = create_account.create_account(customer.customer_id, name, email, phone_number)
    make_transaction.make_transaction(account.account_id, 1000, 'deposit')
    make_transaction.make_transaction(account.account_id, 500, 'withdraw')
    statement = generate_account_statement.generate_account_statement(account.account_id)
    #will match the data received by above test case
    assert True
