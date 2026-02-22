from src.models.address import Address
from src.dtos.address_dto import CreateAddressDTO
from typing import List
from src.database.connection import get_connection

class AddressRepository:
    def __init__(self) -> None:
        # Como é uma classe apenas de execução de métodos não precisa de inicialização
        # Tendo em vista que os dados já vem preparados para uso
        pass
    
    def create(self, address: CreateAddressDTO) -> int:
        """
        Salva o endereço e retorna o ID final

        Args:
            address: CreateAddressDTO: Endereço a ser salvo
        Returns:
            int: ID do endereço salvo
        """
        with get_connection() as cursor:
            query = """
            INSERT INTO address (street_customer, number, neighborhood, cep, customer_id)
            VALUES (%s, %s, %s, %s, %s)
        """
            params = (address.street, address.number, address.neighborhood, address.cep, address.customer_id)
            cursor.execute(query, params)
            return cursor.lastrowid

    def get_by_id(self, id: int) -> Address:
        """
        Retorna o endereço pelo ID

        Args:
            id: int: ID do endereço a ser retornado
        Returns:
            Address: Endereço encontrado
        """
        with get_connection() as cursor:
            query = """
            SELECT * FROM address
            WHERE id = %s
            """
            params = (id,)
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"Endereço com ID {id} não encontrado")
            return Address(*result)

    def get_all(self) -> List[Address]:
        """
        Retorna lista com todos os endereços

        Returns:
            List[Address]: Lista com todos os endereços
        """
        with get_connection() as cursor:
            query = """
            SELECT * FROM address
            """
            params = ()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return [Address(*result) for result in results]

    def update(self, address: Address) -> int:
        """
        Atualiza o endereço e retorna o ID final
        Args:
            address: Address: Endereço a ser atualizado
        Returns:
            int: Quantidade de linhas afetadas
        """
        with get_connection() as cursor:
            query = """
            UPDATE address
            SET street_customer = %s, number = %s, neighborhood = %s, cep = %s, customer_id = %s
            WHERE id = %s
            LIMIT 1
            """
            params = (address.street, address.number, address.neighborhood, address.cep, address.customer_id, address.id)
            cursor.execute(query, params)
            return cursor.rowcount

    def delete(self, id: int) -> int:
        """
        Deleta o endereço pelo ID
        Args:
            id: int: ID do endereço a ser deletado
        Returns:
            int: Quantidade de linhas afetadas
        """
        with get_connection() as cursor:
            query = """
            DELETE FROM address
            WHERE id = %s
            LIMIT 1
            """
            params = (id,)
            cursor.execute(query, params)
            return cursor.rowcount