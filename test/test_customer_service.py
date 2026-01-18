import pytest
from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO
from datetime import date

class FakeCustomerRepository:
    def create(self, customer):
        return 1


def test_create_customer_with_invalid_email():
    repository = FakeCustomerRepository()
    service = CustomerService(repository)

    dto_test = CreateCustomerDTO(
        first_name="Luis",
        last_name="Monteiro",
        birth_date=date(2004, 11, 2),
        email="luisfelipegmail.com",
        phone="(11) 99999-9999"
    )

    with pytest.raises(ValueError):
        service.create_customer(dto_test)

def test_create_customer_with_invalid_phone():
    repository = FakeCustomerRepository()
    service = CustomerService(repository)

    dto_test = CreateCustomerDTO(
        first_name="Luis",
        last_name="Monteiro",
        birth_date=date(2004, 11, 2),
        email="luisfelipe@gmail.com",
        phone="119999999"
    )
    
    with pytest.raises(ValueError):
        service.create_customer(dto_test)

def test_create_customer_with_invalid_birth_date():
    repository = FakeCustomerRepository()
    service = CustomerService(repository)

    dto_test = CreateCustomerDTO(
        first_name="Luis",
        last_name="Monteiro",
        birth_date=date(2030, 11, 2),
        email="luisfelipe@gmail.com",
        phone="(11) 99999-9999"
    )
    
    with pytest.raises(ValueError):
        service.create_customer(dto_test)

def test_create_customer_with_invalid_first_name():
    repository = FakeCustomerRepository()
    service = CustomerService(repository)

    dto_test = CreateCustomerDTO(
        first_name="",
        last_name="Monteiro",
        birth_date=date(2004, 11, 2),
        email="luisfelipe@gmail.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        service.create_customer(dto_test)

def test_create_customer_with_invalid_last_name():
    repository = FakeCustomerRepository()
    service = CustomerService(repository)

    dto_test = CreateCustomerDTO(
        first_name="Luis",
        last_name="",
        birth_date=date(2004, 11, 2),
        email="luisfelipe@gmail.com",
        phone="(11) 99999-9999"
    )   