from src.models.customer import Customer
from src.database.connection import get_connection

from typing import List
class CustomerRepository:
    """
    Repositório de clientes
    
    Atributos:
        - Nenhum

    Métodos:
        - create(customer: Customer) -> int: Salva o cliente e retorna o ID final
        - get_by_id(id: int) -> Customer: Retorna o cliente pelo ID
        - get_all() -> List[Customer]: Retorna lista com todos os clientes
        - update(customer: Customer) -> int: Atualiza o cliente e retorna o ID final
        - delete(id: int) -> int: Deleta o cliente pelo ID
    """
    def __init__(self) -> None:
        pass

    def create(self, customer: Customer) -> int:
        """
        Salva o cliente e retorna o ID final
        Args:
            customer: Customer: Cliente a ser salvo
        Returns:
            int: ID do cliente salvo
        """
        with get_connection() as cursor:
            query = """
            INSERT INTO customer (first_name, last_name, birth_date, email, phone)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (customer.first_name, customer.last_name, customer.birth_date, customer.email, customer.phone)
            cursor.execute(query, params)
            return cursor.lastrowid

    def get_by_id(self, id: int) -> Customer:
        """
        Retorna o cliente pelo ID
        Args:
            id: int: ID do cliente a ser retornado
        Returns:
            Customer: Cliente encontrado
        """
        with get_connection() as cursor:
            query = """
            SELECT * FROM customer
            WHERE id = %s
            """
            params = (id,)
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"Cliente com ID {id} não encontrado")

            return Customer(*result)

    def get_all(self) -> List[Customer]:
        """
        Retorna lista com todos os clientes
        Returns:
            List[Customer]: Lista com todos os clientes
        """
        with get_connection() as cursor:
            query = """
            SELECT * FROM customer
            """
            params = ()
            cursor.execute(query, params)
            results = cursor.fetchall()

            return [Customer(*result) for result in results]

    def update(self, customer: Customer) -> int:
        """
        Atualiza o cliente e retorna o ID final
        Args:
            customer: Customer: Cliente a ser atualizado
        Returns:
            int: ID do cliente atualizado
        """
        with get_connection() as cursor:
            query = """
            UPDATE customer
            SET first_name = %s, last_name = %s, birth_date = %s, email = %s, phone = %s
            WHERE id = %s
            """
            params = (customer.first_name, customer.last_name, customer.birth_date, customer.email, customer.phone, customer.id)
            cursor.execute(query, params)

            return cursor.rowcount

    def delete(self, id: int) -> int:
        """
        Deleta o cliente pelo ID
        Args:
            id: int: ID do cliente a ser deletado
        Returns:
            int: Número de linhas deletadas
        """
        with get_connection() as cursor:
            query = """
            DELETE FROM customer
            WHERE id = %s
            """
            params = (id,)
            cursor.execute(query, params)
            return cursor.rowcount
            