import unittest
from unittest.mock import Mock

from BankingSystem.domain.entities.account import Account
from BankingSystem.usecases.generate_statment import GenerateAccountStatement


class TestAccountStatementUseCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.account_statement_use_case = GenerateAccountStatement(self.mock_repo)
        self.mock_repo.find_account_by_id.return_value = Account(account_id=1, customer_id=1, account_number="123456",
                                                                 balance=100)

    def test_generate_statement(self):
        statement = self.account_statement_use_case.generate_account_statement(account_id=1)
        self.assertIn("Account ID 1", statement)
    # Test cases...


if __name__ == '__main__':
    unittest.main()
