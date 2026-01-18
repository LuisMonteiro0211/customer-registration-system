# TODO: create_customer(dto) -> Salva o cliente e retorna o ID final
# TODO: get_customer_by_id(id) -> Chama o repositório para buscar o cliente pelo ID
# TODO: get_all_customers() -> Chama o repositório para buscar todos os clientes
# TODO: update_customer(id, dto) -> Atualiza o cliente e retorna o ID final
# TODO: delete_customer(id) -> Chama o repositório para deletar o cliente pelo ID

from datetime import date

from src.repositories.customer_repository import CustomerRepository
from src.dtos.customer_dto import CreateCustomerDTO

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository # Recebe uma instância do repositório já pronta para uso

    def create_customer(self, customer_dto: CreateCustomerDTO) -> int:
        customer = customer_dto

        if not customer.first_name or customer.first_name.isspace():
            ## Validação do primeiro nome do cliente
            raise ValueError("Nome do cliente invpalido")
        
        if not customer.last_name or customer.last_name.isspace():
            ## Validação do sobrenome do cliente
            raise ValueError("Sobrenome do cliente invpalido")
        
        if not customer.birth_date:
            ## Validação se tem valor para a data de nascimento
            raise ValueError("Data de nascimento invalida")
            
        


if __name__ == "__main__":
    print(f"Testando data: {date.today()}")