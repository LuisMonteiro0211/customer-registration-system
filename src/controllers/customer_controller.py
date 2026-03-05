from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO
from src.utils.validators import validate_filled_string, validate_email, validate_phone, validate_date_format
from src.utils.formatters import convert_to_us_date, format_phone_br
from src.view.customer_view import customer_view, create_customer, search_customer, get_customer_by_id, get_all_customers, menu_update_customer, update_customer, delete_customer

class CustomerController:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def _create_customer(self) -> None:
        customer_info = create_customer()
        #Validações básicos se os dados estão preenchidos e dentro do padrão
        #Função básica do controller: Validar os dados montar a DTO e chamar o service

        try:
            validate_filled_string(customer_info["first_name"], "Nome deve ser preenchido")
            validate_filled_string(customer_info["last_name"], "Sobrenome deve ser preenchido")
            validate_date_format(customer_info["birth_date"])
            validate_email(customer_info["email"])
            validate_phone(customer_info["phone"])

            #Formatação dos dados para o formato do banco de dados
            date_formatter = convert_to_us_date(customer_info["birth_date"])
            phone_formatter = format_phone_br(customer_info["phone"])

        except ValueError as e:
            print(f"Erro ao validar/converter os dados do cliente: {e}")
            return

        customer_dto = CreateCustomerDTO(
            first_name=customer_info["first_name"],
            last_name=customer_info["last_name"],
            birth_date=date_formatter,
            email=customer_info["email"],
            phone=phone_formatter
        )
        self.customer_service.create_customer(customer_dto)

    def run(self):
        while True:
            try:
                option = customer_view()
                option = int(option)
                break
            except ValueError as e:
                print(f"Favor digitar um número válido: {e}")
                continue
        
