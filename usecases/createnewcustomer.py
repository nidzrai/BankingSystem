class CreateCustomer:
    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def create_customer(self, name, email, phone):
        return self.customer_repository.create_customer(name, email, phone)