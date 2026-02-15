# TODO [X]: create_customer(dto) -> Salva o cliente e retorna o ID final
# TODO: get_customer_by_id(id) -> Chama o repositório para buscar o cliente pelo ID
# TODO: get_all_customers() -> Chama o repositório para buscar todos os clientes
# TODO: update_customer(id, dto) -> Atualiza o cliente e retorna o ID final
# TODO: delete_customer(id) -> Chama o repositório para deletar o cliente pelo ID

from datetime import date
from src.models.customer import Customer
from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import CreateCustomerDTO, UpdateCustomerDTO
from typing import List
from src.utils.validators import validate_id, validate_name, validate_email, validate_phone, validate_birth_date
import logging

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        """
        Serviço de clientes
        Atributos:
            - customer_repository: CustomerRepository: Repositório de clientes (Instância do repositório já pronta para uso - Injeção de Dependência)
        Métodos:
            - create_customer(customer_dto: CreateCustomerDTO) -> int: Cria um novo cliente
            - get_customer_by_id(id: int) -> Customer: Retorna um cliente pelo ID
            - get_all_customers() -> List[Customer]: Retorna todos os clientes
            - update_customer(id: int, customer_dto: UpdateCustomerDTO) -> int: Atualiza um cliente
            - delete_customer(id: int) -> int: Deleta um cliente pelo ID
        """
        self.customer_repository = customer_repository # Recebe uma instância do repositório já pronta para uso
        
    def create_customer(self, customer_dto: CreateCustomerDTO) -> int:
        """
        Cria um novo cliente
        Args:
            customer_dto: CreateCustomerDTO: DTO de criação de cliente
        Returns:
            int: ID do cliente criado
        """
        validate_name(customer_dto.first_name)
        validate_name(customer_dto.last_name)
        validate_birth_date(customer_dto.birth_date)
        validate_email(customer_dto.email)
        validate_phone(customer_dto.phone)

        try:
            created = self.customer_repository.create(customer_dto)
            logging.info(f"Cliente criado com sucesso! ID: {created}")
            return created
        except Exception as e:
            logging.error("Erro ao criar cliente!")
            raise e


    def get_customer_by_id(self, id: int) -> Customer:
        """
        Retorna um cliente pelo ID

        Args:
            id: int: ID do cliente a ser retornado
        Returns:
            Customer: Cliente encontrado
        """
        validate_id(id)

        try:
            result = self.customer_repository.get_by_id(id)
            logging.info(f"Cliente encontrado com sucesso! ID: {id}")
            return result
        except ValueError as e:
            logging.warning("Cliente não encontrado!")
            raise e

    def get_all_customers(self) -> List[Customer]:
        """
        Retorna todos os clientes

        Args:
            Nenhum
        Returns:
            List[Customer]: Lista com todos os clientes
        """
        try:
            result = self.customer_repository.get_all()
            logging.info(f"{len(result)} Clientes encontrados com sucesso!")
            return result
        except Exception as e:
            logging.error("Erro ao buscar clientes!")
            raise e

    def update_customer(self,customer_update_dto: UpdateCustomerDTO) -> int:
        """
        Atualiza um cliente
        Args:
            customer_update_dto: UpdateCustomerDTO: DTO de atualização de cliente
        Returns:
            int: ID do cliente atualizado
        """
        validate_id(customer_update_dto.id)
        validate_name(customer_update_dto.first_name)
        validate_name(customer_update_dto.last_name)
        validate_birth_date(customer_update_dto.birth_date)
        validate_email(customer_update_dto.email)
        validate_phone(customer_update_dto.phone)

        try:
            updated = self.customer_repository.update(customer_update_dto)
            logging.info(f"Cliente atualizado com sucesso! ID: {updated}")
            return updated
        except Exception as e:
            logging.error("Erro ao atualizar cliente!")
            raise e
    
    def delete_customer(self, id: int) -> int:
        """
        Deleta um cliente pelo ID
        Args:
            id: int: ID do cliente a ser deletado
        Returns:
            int: Número de linhas deletadas
        """
        validate_id(id)

        try:
            deleted = self.customer_repository.delete(id)
            logging.info(f"Cliente deletado com sucesso! ID: {id}")
            return deleted
        except Exception as e:
            logging.error("Erro ao deletar cliente!")
            raise e