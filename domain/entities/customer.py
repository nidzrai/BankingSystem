"""Customer entity class"""
import re
import uuid
from BankingSystem.domain import InvalidPhoneNumberException


class Customer:

    def __init__(self, name, email, phone_number):
        # Basic validation of input types
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string")
        if not isinstance(phone_number, str) or not phone_number:
            raise ValueError("Phone number must be a non-empty string")

        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone_number = self.phone_validation(phone_number)

    @staticmethod
    def phone_validation(v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        return v

    #Email Validator
    def Email_validator(self):
        pass
