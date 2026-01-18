from models.customer import Customer
from typing import List
from database.connection import get_connection
from mysql.connector import Error
class CustomerRepository:
    def __init__(self) -> None:
    # TODO: Adicionar uma função para gerenciar o contexto da conexão com o banco de dados (Função Helper)
        pass

    def create(self, customer: Customer) -> int:
        # TODO: create(customer) -> Salva o cliente e retorna o ID final
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            INSERT INTO customer (first_name, last_name, birth_date, email, phone)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (customer.first_name, customer.last_name, customer.birth_date, customer.email, customer.phone)

            cursor.execute(query, params)
            connection.commit()
            return cursor.lastrowid
            
        except Error as error:
            raise error # Re-lança o erro para ser tratado pelo chamador
        finally:
            cursor.close() # Fecha o cursor
            connection.close() # Fecha a conexão


    def get_by_id(self, id: int) -> Customer:
        # TODO: get_by_id(id) -> Retorna o cliente pelo ID
        pass

    def get_all(self) -> List[Customer]:
        # TODO: get_all() -> Retorna lista com todos os clientes
        pass

    def update(self, customer: Customer) -> int:
        # TODO: update(customer) -> Atualiza o cliente e retorna o ID final
        pass

    def delete(self, id: int) -> None:
        # TODO: delete(id) -> Deleta o cliente pelo ID
        pass