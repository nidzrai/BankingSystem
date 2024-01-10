import pytest

from BankingSystem.domain import Customer
from BankingSystem.domain import InvalidPhoneNumberException


def test_customer_create():
    customer = Customer(
        name="test",
        email="test@testdom.com",
        phone="+1234567890"
    )
    assert customer
    assert customer.name == "test"
    assert customer.email == "test@testdom.com"
    assert customer.phone == "+1234567890"


def test_customer_create_throws_invalid_email_exception():
    with pytest.raises(InvalidPhoneNumberException) as exc:
        Customer(
            name="test",
            email="test@testdom.com",
            phone="+12345678eqweqweqweqweqw90"
        )
    assert isinstance(exc.value, InvalidPhoneNumberException)
