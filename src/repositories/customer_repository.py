from models.customer import Customer
from typing import List
class CustomerRepository:
    def __init__(self) -> None:
        pass

    def create(self, customer: Customer) -> int:
        # TODO: create(customer) -> Salva o cliente e retorna o ID final
        pass

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