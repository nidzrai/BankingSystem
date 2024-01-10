"""Implement a Use Case class for creating a new account. It should have a method named
create_account() that takes customer_id, name, email, and phone_number as input and
returns an Account object."""

import uuid

from BankingSystem.domain.entities.account import Account
from BankingSystem.domain.entities.customer import Customer


def _generate_account_id():
    # Generate a unique account ID
    # for now we are using uuid.uuid4()
    return uuid.uuid4()


def _generate_account_number():
    # Generate a unique account number
    # for now we are using uuid.uuid4()
    return uuid.uuid4()


class CreateAccount:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self,  account_repository, customer_id, name, email, phone_number):
        # Basic input validation
        if not account_repository:
            raise ValueError("account_repository is required")

        # Create account and save to repository
        account = Account(account_id=_generate_account_id, customer_id=customer_id, account_number=_generate_account_number)
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        self.account_repository.save_account(account)
        return account

