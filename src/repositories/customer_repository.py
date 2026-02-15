from src.models.customer import Customer
from src.database.connection import get_connection

from typing import List
class CustomerRepository:
    def __init__(self) -> None:
        pass

    def create(self, customer: Customer) -> int:
        # TODO: create(customer) -> Salva o cliente e retorna o ID final
        with get_connection() as cursor:
            query = """
            INSERT INTO customer (first_name, last_name, birth_date, email, phone)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (customer.first_name, customer.last_name, customer.birth_date, customer.email, customer.phone)
            cursor.execute(query, params)
            return cursor.lastrowid

    def get_by_id(self, id: int) -> Customer:
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
        with get_connection() as cursor:
            query = """
            SELECT * FROM customer
            """
            params = ()
            cursor.execute(query, params)
            results = cursor.fetchall()
            
            if len(results) == 0:
                raise ValueError("Nenhum cliente encontrado")

            return [Customer(*result) for result in results]

    def update(self, customer: Customer) -> int:
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
        with get_connection() as cursor:
            query = """
            DELETE FROM customer
            WHERE id = %s
            """
            params = (id,)
            cursor.execute(query, params)
            return cursor.rowcount
            