from unittest.mock import patch
from src.controllers.customer_controller import CustomerController
from src.models.customer import Customer
from typing import List
from src.dtos.customer_dto import CreateCustomerDTO

class FakeService:
    def create_customer(self, customer_dto: CreateCustomerDTO):
        return 1
    
    def get_all_customers(self):
        lista: List[Customer] = []
        return lista

    def get_customer_by_id(self):
        return Customer

    def delete_customer(self):
        return 1

fake_customer_service = FakeService()
customer_controller = CustomerController(fake_customer_service)

def test_create_customer_success():
    with patch("src.view.customer_view.create_customer_form") as mock_view:
        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }
        result = customer_controller._create_customer()

    assert result == 1

def test_create_customer_invalid_name():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }
        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_create_customer_invalid_last_name():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "",
            "birth_date": "02/01/2004",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_create_customer_invalid_birth_date():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "2004/01/02",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_invalid_birth_date_str_eua():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "2004-01-02",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_invalid_birth_date_number_join():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "20040102",
            "email": "john.doe@example.com",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_create_customer_invalid_email():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "john.doe.example.com",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once() 
        assert result == None

def test_create_customer_invalid_phone():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "john.doe@example.com",
            "phone": "+55(16)992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_create_customer_invalid_email():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "",
            "phone": "16992949652"
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None

def test_create_customer_invalid_phone_empty():
    with patch("src.view.customer_view.create_customer_form") as mock_view, \
         patch("src.controllers.customer_controller.show_error") as mock_error:

        mock_view.return_value = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "02/01/2004",
            "email": "john.doe@example.com",
            "phone": ""
        }

        result = customer_controller._create_customer()
        mock_error.assert_called_once()
        assert result == None