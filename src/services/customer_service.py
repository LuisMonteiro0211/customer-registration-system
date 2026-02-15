# TODO [X]: create_customer(dto) -> Salva o cliente e retorna o ID final
# TODO: get_customer_by_id(id) -> Chama o repositório para buscar o cliente pelo ID
# TODO: get_all_customers() -> Chama o repositório para buscar todos os clientes
# TODO: update_customer(id, dto) -> Atualiza o cliente e retorna o ID final
# TODO: delete_customer(id) -> Chama o repositório para deletar o cliente pelo ID

from datetime import date
from src.models.customer import Customer
from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import CreateCustomerDTO
import logging

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository # Recebe uma instância do repositório já pronta para uso

    def create_customer(self, customer_dto: CreateCustomerDTO) -> int:
        customer = customer_dto

        if not customer.first_name or customer.first_name.isspace():
            ## Validação do primeiro nome do cliente
            logging.warning("Nome do cliente invalido")
            raise ValueError("Nome do cliente invalido")
        
        if not customer.last_name or customer.last_name.isspace():
            ## Validação do sobrenome do cliente
            logging.warning("Sobrenome do cliente invalido")
            raise ValueError("Sobrenome do cliente invalido")
        
        if not customer.birth_date:
            ## Validação se tem valor para a data de nascimento
            logging.warning("Data de nascimento invalida")
            raise ValueError("Data de nascimento invalida")

        if customer.birth_date> date.today() or customer.birth_date < date(1900, 1, 1):
            logging.warning("Data de nascimento invalida!")
            raise ValueError("Data de nascimento invalida!")

        if not customer.email or customer.email.isspace() or "@" not in customer.email:
            ## Validação do email do cliente
            logging.warning("Email do cliente invalido")
            raise ValueError("Email do cliente invalido")
        
        if not customer.phone or customer.phone.isspace() or len(customer.phone) != 15:
            ## Validação do telefone do cliente
            logging.warning("Telefone do cliente invalido")
            raise ValueError("Telefone do cliente invalido")
        
        try:
            created = self.customer_repository.create(customer)
            logging.info(f"Cliente criado com sucesso! ID: {created}")
            return created
        except Exception as e:
            logging.error("Erro ao criar cliente!")
            raise e


    def get_customer_by_id(self, id: int) -> Customer:
        if not id or id <= 0:
            logging.warning("ID do cliente invalido")
            raise ValueError("ID do cliente invalido")

        try:
            result = self.customer_repository.get_by_id(id)
            logging.info(f"Cliente encontrado com sucesso! ID: {id}")
            return result
        except ValueError as e:
            logging.warning("Cliente não encontrado!")
            raise e
