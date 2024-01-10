import unittest
from unittest.mock import Mock

from BankingSystem.domain.entities.account import Account
from BankingSystem.usecases.making_transaction import MakeTransaction


class TestTransactionUseCase(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.transaction_use_case = MakeTransaction(self.mock_repo)
        self.account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        self.mock_repo.find_account_by_id.return_value = self.account

    def test_make_deposit(self):
        self.transaction_use_case.make_transaction(account_id=1, amount=50, transaction_type='deposit')
        self.assertEqual(self.account.get_balance(), 150)

    def test_make_withdrawal(self):
        self.transaction_use_case.make_transaction(account_id=1, amount=50, transaction_type='withdraw')
        self.assertEqual(self.account.get_balance(), 50)


if __name__ == '__main__':
    unittest.main()
