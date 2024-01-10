import unittest

from BankingSystem.domain.entities.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_customer_initialization(self):
        customer = Customer(customer_id=1, name="test test", email="test123@text.com", phone_number="8888888888")
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.name, "test test")
        self.assertEqual(customer.email, "test123@text.com")
        self.assertEqual(customer.phone_number, "8888888888")

    # Additional tests can be added here for more complex validations

if __name__ == '__main__':
    unittest.main()