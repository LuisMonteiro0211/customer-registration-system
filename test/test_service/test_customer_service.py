import pytest
from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO
from datetime import date, timedelta
from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import UpdateCustomerDTO
from src.repositories.interfaces.interface_repository import IRepository
from src.models.customer import Customer
from typing import List

class FakeCustomerRepository(IRepository):
    """Fake repository configurável para testes"""
    
    def __init__(self):
        # Flags de configuração para diferentes cenários de teste
        self.should_fail_create = False
        self.should_fail_update = False
        self.should_fail_delete = False
        self.flag_email_exists = False #Caso seja necessário validar se o email já existe | Caso não seja necessário, retorna False
        self.flag_phone_exists = False
        self.return_none_on_get = False #Caso seja necessário retornar None | Caso não seja necessário, retorna False
        self.flag_birth_date_past = False #Caso seja necessário validar se a data de nascimento é anterior a data atual | Caso não seja necessário, retorna False
        self.return_none_on_get_all = False #Caso seja necessário retornar None | Caso não seja necessário, retorna False
        self.customer_id_to_return = None #Caso seja necessário retornar um ID específico | Caso não seja necessário, retorna None
        
    def create(self, customer) -> int:
        if self.should_fail_create:
            return 0
        return 1
    
    def get_by_id(self, id: int):
        if self.return_none_on_get:
            raise ValueError(f"Cliente com ID 1 não encontrado")
        
        return Customer(
            id=1, 
            first_name="João", 
            last_name="Silva", 
            birth_date=date(1990, 1, 1), 
            email="joao.silva@example.com", 
            phone="(11) 99999-9999"
        )

    def get_all(self) -> List[Customer]:
        if self.return_none_on_get_all:
            raise ValueError("Sem clientes cadastrados")
        return [Customer(
            id=1, 
            first_name="João", 
            last_name="Silva", 
            birth_date=date(1990, 1, 1), 
            email="joao.silva@example.com", 
            phone="(11) 99999-9999"
        )]

    def update(self, list_fields: List[tuple[str, str]]) -> int:
        if self.should_fail_update:
            return 0
        return 1
    
    def delete(self, id: int) -> int:
        if self.should_fail_delete:
            return 0
        return 1

    def exists_by_email(self, email: str) -> bool:
        return self.flag_email_exists

    def exists_by_phone(self, phone: str) -> bool:
        return self.flag_phone_exists

@pytest.fixture
def service():
    return CustomerService(FakeCustomerRepository())

@pytest.fixture
def dto_valido():
    return CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )

@pytest.fixture
def dto_invalid_email():
    return CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva.example.com",
        phone="(11) 99999-9999"
    )

@pytest.fixture
def dto_invalid_phone():
    return CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1990, 1, 1),
        email="joao.silva@example.com",
        phone="+55(11) 99999-9999"
    )

@pytest.fixture
def dto_invalid_birth_date_past():
    return CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date(1800, 1, 1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )

@pytest.fixture
def dto_invalid_birth_date_future():
    return CreateCustomerDTO(
        first_name="João",
        last_name="Silva",
        birth_date=date.today() + timedelta(days=1),
        email="joao.silva@example.com",
        phone="(11) 99999-9999"
    )

def test_create_customer_success(service, dto_valido):
    """Testa se o método create_customer cria um cliente com sucesso"""
    customer_created = service.create_customer(dto_valido)
    assert customer_created > 0

def test_create_customer_invalid_email(service, dto_invalid_email):
    """Testa se o método create_customer retorna um erro se o email já existe"""
    service.customer_repository.flag_email_exists = True

    with pytest.raises(ValueError, match="Email já cadastrado"):
        service.create_customer(dto_invalid_email)

def test_create_customer_invalid_phone(service, dto_invalid_phone):
    """Testa se o método create_customer retorna um erro se o telefone já existe"""
    service.customer_repository.flag_phone_exists = True

    with pytest.raises(ValueError, match="Telefone já cadastrado"):
        service.create_customer(dto_invalid_phone)

def test_create_customer_invalid_birth_date_past(service, dto_invalid_birth_date_past):
    """Testa se o método create_customer retorna um erro se a data de nascimento é anterior a data atual"""
    with pytest.raises(ValueError, match="Data de nascimento inválida"):
        service.create_customer(dto_invalid_birth_date_past)

def test_create_customer_invalid_birth_date_future(service, dto_invalid_birth_date_future):
    """Testa se o método create_customer retorna um erro se a data de nascimento é futura"""
    with pytest.raises(ValueError, match="Data de nascimento inválida"):
        service.create_customer(dto_invalid_birth_date_future)
#####################################################################################################

#####################################################################################################
# Testes para o método get_customer_by_id
#####################################################################################################

def test_get_customer_by_id_success(service, dto_valido):
    """Testa se o método get_customer_by_id retorna um cliente com sucesso"""
    customer_id = 1
    customer = service.get_customer_by_id(customer_id)
    assert customer.id == customer_id

def test_get_customer_by_id_not_found(service, dto_valido):
    """Testa se o método get_customer_by_id retorna um erro se o cliente não for encontrado"""
    service.customer_repository.return_none_on_get = True
    with pytest.raises(ValueError, match="Cliente com ID 1 não encontrado"):
        service.get_customer_by_id(1)

def test_get_customer_by_id_invalid_id(service, dto_valido):
    """Testa se o método get_customer_by_id retorna um erro se o ID não for um número inteiro"""
    with pytest.raises(ValueError, match="Valor deve ser um número"):
        service.get_customer_by_id("1")

#####################################################################################################
# Testes para o método get_all_customers
#####################################################################################################

def test_get_all_customers_success(service, dto_valido):
    """Testa se o método get_all_customers retorna todos os clientes com sucesso"""
    customers = service.get_all_customers()
    assert len(customers) > 0

def test_get_all_customers_no_customers(service, dto_valido):
    """Testa se o método get_all_customers retorna um erro se não houver clientes cadastrados"""
    service.customer_repository.return_none_on_get_all = True
    with pytest.raises(ValueError, match="Sem clientes cadastrados"):
        service.get_all_customers()