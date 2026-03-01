import pytest
from src.services.address_service import AddressService
from src.dtos.address_dto import CreateAddressDTO, UpdateAddressDTO
from src.repositories.interfaces.interface_repository import IRepository
from src.models.address import Address
from typing import List

class FakeAddressRepository(IRepository):
    def create(self, address) -> int:
        return 1
    
    def get_by_id(self, id: int):
        return Address(id=1, street="Rua das Flores", number="123", neighborhood="Centro", cep="01001-000", customer_id=1)

    def get_all(self) -> List[Address]:
        return [Address(id=1, street="Rua das Flores", number="123", neighborhood="Centro", cep="01001-000", customer_id=1)]

    def update(self, address) -> int:
        return 1

    def delete(self, id: int) -> int:
        return 1

address_service = AddressService(FakeAddressRepository())

def test_create_address_success():
    dto_success = CreateAddressDTO(
        street="Rua das Flores",
        number="123",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=1
    )
    address_created = address_service.create_address(dto_success)
    assert address_created > 0

def test_create_address_invalid_street():
    dto_invalid = CreateAddressDTO(
        street="",
        number="123",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=1
    )
    with pytest.raises(ValueError):
        address_service.create_address(dto_invalid)

def test_create_address_invalid_number():
    dto_invalid = CreateAddressDTO(
        street="Rua das Flores",
        number="",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=1
    )
    with pytest.raises(ValueError):
        address_service.create_address(dto_invalid)

def test_create_address_invalid_neighborhood():
    dto_invalid = CreateAddressDTO(
        street="Rua das Flores",
        number="123",
        neighborhood="",
        cep="01001-000",
        customer_id=1
    )
    with pytest.raises(ValueError):
        address_service.create_address(dto_invalid)

def test_create_address_invalid_cep():
    dto_invalid = CreateAddressDTO(
        street="Rua das Flores",
        number="123",
        neighborhood="Centro",
        cep="",
        customer_id=1
    )
    with pytest.raises(ValueError):
        address_service.create_address(dto_invalid)

def test_create_address_invalid_customer_id():
    dto_invalid = CreateAddressDTO(
        street="Rua das Flores",
        number="123",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=0
    )
    with pytest.raises(ValueError):
        address_service.create_address(dto_invalid)

def test_update_address_success():
    dto_success = UpdateAddressDTO(
        id=1,
        street="Rua das Flores",
        number="456",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=1
    )
    address_updated = address_service.update_address(dto_success)
    assert address_updated > 0

def test_update_address_invalid_id():
    dto_invalid = UpdateAddressDTO(
        id=0,
        street="Rua das Flores",
        number="456",
        neighborhood="Centro",
        cep="01001-000",
        customer_id=1
    )
    with pytest.raises(ValueError):
        address_service.update_address(dto_invalid)

def test_delete_address_success():
    deleted = address_service.delete_address(1)
    assert deleted > 0

def test_delete_address_invalid_id():
    with pytest.raises(ValueError):
        address_service.delete_address(0)
