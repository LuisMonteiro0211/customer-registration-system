# TODO [X]: create_customer(dto) -> Salva o cliente e retorna o ID final
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

        if customer.birth_date> date.today() or customer.birth_date < date(1900, 1, 1):
            raise ValueError("Data de nascimento inválida!")

        if not customer.email or customer.email.isspace() or "@" not in customer.email:
            ## Validação do email do cliente
            raise ValueError("Email do cliente inválido")
        
        if not customer.phone or customer.phone.isspace() or len(customer.phone) != 15:
            ## Validação do telefone do cliente
            raise ValueError("Telefone do cliente inválido")
        
        return self.customer_repository.create(customer)