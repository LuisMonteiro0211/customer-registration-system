import pytest
from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO
from datetime import date
from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import UpdateCustomerDTO
class FakeCustomerRepository:
    # Criado para não precisar de conexão com o banco de dados
    # Simula o método create do repositório
    def create(self, customer) -> int:
        return 1

    def update(self, customer) -> int:
        return 1

    def delete(self, id: int) -> int:
        return 1

customer_service = CustomerService(FakeCustomerRepository())

def test_create_customer_success():
    dto_success = CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    customer_created = customer_service.create_customer(dto_success)
    assert customer_created > 0

def test_create_customer_invalid_name():
    dto_invalid_name = CreateCustomerDTO(
        first_name="",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        customer_service.create_customer(dto_invalid_name)

def test_create_customer_invalid_email():
    dto_invalid_email = CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva.example.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        customer_service.create_customer(dto_invalid_email)

def test_create_customer_invalid_phone():
    dto_invalid_phone = CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="11999999999"
    )
    with pytest.raises(ValueError):
        customer_service.create_customer(dto_invalid_phone)

def test_create_customer_invalid_birth_date():
    dto_invalid_birth_date = CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1899, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        customer_service.create_customer(dto_invalid_birth_date)

def test_create_customer_invalid_birth_date_future():
    dto_invalid_birth_date_future = CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(2026, 12, 31),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        customer_service.create_customer(dto_invalid_birth_date_future)

def test_update_customer_success():
    dto_success = UpdateCustomerDTO(
        id=1,
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    customer_updated = customer_service.update_customer(dto_success)
    assert customer_updated > 0

def test_update_customer_invalid_id():
    dto_invalid_id = UpdateCustomerDTO(
        id=0,
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )
    with pytest.raises(ValueError):
        customer_service.update_customer(dto_invalid_id)

def test_delete_customer_success():
    id = 1
    deleted = customer_service.delete_customer(id)
    assert deleted > 0

def test_delete_customer_invalid_id():
    id = 0
    with pytest.raises(ValueError):
        customer_service.delete_customer(id)