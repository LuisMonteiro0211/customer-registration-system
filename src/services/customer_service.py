# TODO: create_customer(dto) -> Salva o cliente e retorna o ID final
# TODO: get_customer_by_id(id) -> Chama o repositório para buscar o cliente pelo ID
# TODO: get_all_customers() -> Chama o repositório para buscar todos os clientes
# TODO: update_customer(id, dto) -> Atualiza o cliente e retorna o ID final
# TODO: delete_customer(id) -> Chama o repositório para deletar o cliente pelo ID

from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import CreateCustomerDTO


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository # Recebe uma instância do repositório já pronta para uso

    def create_customer(self, customer_dto: CreateCustomerDTO) -> int:
        pass