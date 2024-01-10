import unittest

from BankingSystem.domain.entities.account import Account

class TestAccount(unittest.TestCase):

    def test_account_initialization(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        self.assertEqual(account.balance, 100)
        self.assertEqual(account.account_id, 1)
        self.assertEqual(account.customer_id, 1)
        self.assertEqual(account.account_number, "123456")

    def test_deposit_positive_amount(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_deposit_negative_amount(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw_valid_amount(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_excessive_amount(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_withdraw_negative_amount(self):
        account = Account(account_id=1, customer_id=1, account_number="123456", balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)


if __name__ == '__main__':
    unittest.main()