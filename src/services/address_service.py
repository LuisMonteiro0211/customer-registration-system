from src.repositories.address_repository import AddressRepository
from src.dtos.address_dto import CreateAddressDTO, UpdateAddressDTO
from src.utils.validators import validate_is_integer, validate_filled_string
from src.models.address import Address
import logging
from typing import List

class AddressService:
    def __init__(self, address_repository: AddressRepository):
        self.address_repository = address_repository # Recebe uma instância do repositório já pronta para uso

    def create_address(self, address_dto: CreateAddressDTO) -> int:
        """
        Cria um novo endereço

        Args:
            address_dto: CreateAddressDTO: DTO de criação de endereço
        Returns:
            int: ID do endereço criado
        """
        validate_filled_string(address_dto.street)
        validate_filled_string(address_dto.number)
        validate_filled_string(address_dto.neighborhood)
        validate_filled_string(address_dto.cep)
        validate_is_integer(address_dto.customer_id)

        address = Address(
            street=address_dto.street,
            number=address_dto.number,
            neighborhood=address_dto.neighborhood,
            cep=address_dto.cep,
            customer_id=address_dto.customer_id,
        )

        try:
            created = self.address_repository.create(address)
            logging.info(f"Endereço criado com sucesso! ID: {created}")
            return created
        except Exception as e:
            logging.error("Erro ao criar endereço!")
            raise e

    def get_address_by_id(self, id: int) -> Address:

        """
        Retorna um endereço pelo ID

        Args:
            id: int: ID do endereço a ser retornado
        Returns:
            Address: Endereço encontrado
        """
        validate_is_integer(id)

        try:
            result = self.address_repository.get_by_id(id)
            logging.info(f"Endereço encontrado com sucesso! ID: {id}")
            return result
        except ValueError as e:
            logging.warning("Endereço não encontrado!")
            raise e

    def get_all_addresses(self) -> List[Address]:
        """
        Retorna todos os endereços

        Args:
            Nenhum
        Returns:
            List[Address]: Lista com todos os endereços
        """
        try:
            result = self.address_repository.get_all()
            logging.info(f"{len(result)} Endereços encontrados com sucesso!")
            return result
        except Exception as e:
            logging.error("Erro ao buscar endereços!")
            raise e

    def update_address(self, address_update_dto: UpdateAddressDTO) -> int:
        """
        Atualiza um endereço

        Args:
            address_update_dto: UpdateAddressDTO: DTO de atualização de endereço
        Returns:
            int: ID do endereço atualizado
        """
        validate_is_integer(address_update_dto.id)
        validate_filled_string(address_update_dto.street)
        validate_filled_string(address_update_dto.number)
        validate_filled_string(address_update_dto.neighborhood)
        validate_filled_string(address_update_dto.cep)

        try:
            updated = self.address_repository.update(address_update_dto)
            logging.info(f"Endereço atualizado com sucesso! ID: {address_update_dto.id}")
            return updated
        except Exception as e:
            logging.error("Erro ao atualizar endereço!")
            raise e

    def delete_address(self, id: int) -> int:
        """
        Deleta um endereço pelo ID
        
        Args:
            id: int: ID do endereço a ser deletado
        Returns:
            int: ID do endereço deletado
        """
        validate_is_integer(id)

        try:
            deleted = self.address_repository.delete(id)
            logging.info(f"Endereço deletado com sucesso! ID: {id}")
            return deleted
        except Exception as e:
            logging.error("Erro ao deletar endereço!")
            raise e