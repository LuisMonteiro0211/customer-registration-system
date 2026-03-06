from src.controllers.customer_controller import CustomerController
from src.services.customer_service import CustomerService
from src.repositories.interfaces.interface_customer import ICustomerRepository 
from src.models.customer import Customer
from typing import List, Dict
from src.dtos.customer_dto import CreateCustomerDTO
from datetime import date

class FakeCustomerService():

    def create_customer(self, entity) -> int:
        return 1

    def get_customer_by_id(self, id: int):
        return None

    def get_all_customers(self) -> List[Customer]:
        return []

    def update_customer(self, entity) -> int:
        return 1

    def delete_customer(self, id: int) -> int:
        return 1

    def exists_by_email(self, email: str) -> bool:
        return False

    def exists_by_phone(self, phone: str) -> bool:
        return False

customer_service = FakeCustomerService()
customer_controller = CustomerController(customer_service)

def test_create_customer_success():
    customer_info: Dict[str, str] = {
        "first_name": "João",
        "last_name": "Silva",
        "birth_date": "01/01/1990",
        "email": "joao.silva@example.com",
        "phone": "16992949652"
    }
    customer_created = customer_controller.create_customer(customer_info)
    assert customer_created > 0