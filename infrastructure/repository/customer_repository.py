from BankingSystem.domain.entities.account import Account
from BankingSystem.domain.entities.customer import Customer


class CustomerRepository:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_customer(self, first_name, last_name, email, phone):
        customer = Customer(first_name, last_name, email, phone)
        customer.account = Account(customer.customer_id)
        return customer