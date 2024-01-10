import unittest
from unittest.mock import Mock

from BankingSystem.domain.entities.account import Account
from BankingSystem.usecases.create_account import CreateAccount

class TestAccountCreationUseCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.account_creation_use_case = CreateAccount(self.mock_repo)

    def test_create_account(self):
        self.mock_repo.save_account.return_value = None
        account = self.account_creation_use_case.create_account(customer_id=1, name="test test", email="test123@text.com", phone_number="8888888888")
        self.assertIsInstance(account, Account)

    # Additional tests can be added here to test for exceptions or invalid inputs

if __name__ == '__main__':
    unittest.main()