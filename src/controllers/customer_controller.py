from this import d
from src.view.customer_view import show_error
from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO
from src.utils.validators import validate_filled_string, validate_email, validate_phone, validate_date_format
from src.utils.formatters import convert_to_us_date, format_phone_br

class CustomerController:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def handle_menu(self):
        from src.view.customer_view import customer_menu
        while True:
            option = customer_menu()
            if option == "1":
                self._create_customer()
            elif option == "2":
                self._list_all_customers()
            elif option == "3":
                self._list_customer_by_id()
            elif option == "4":
                self._update_customer()
            elif option == "5":
                self._delete_customer()
            elif option == "6":
                break

    def _create_customer(self) -> int:
        from src.view.customer_view import create_customer_form
        customer_info = create_customer_form()

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
            show_error(f"Erro ao validar/converter os dados do cliente: {e}")
            return

        customer_dto = CreateCustomerDTO(
            first_name=customer_info["first_name"],
            last_name=customer_info["last_name"],
            birth_date=date_formatter,
            email=customer_info["email"],
            phone=phone_formatter
        )
        try:
            result = self.customer_service.create_customer(customer_dto)
            return result
        except Exception as e:
            show_error(f"Erro ao criar cliente: {e}")

    def _list_all_customers(self) -> None:
        from src.view.customer_view import show_all_customers
        try:
            customers = self.customer_service.get_all_customers()
            show_all_customers(customers)
        except Exception as e:
            show_error(f"Erro ao listar clientes: {e}")

    def _list_customer_by_id(self) -> None:
        from src.view.customer_view import get_id_form
        from src.view.customer_view import show_customer

        id_customer = get_id_form()
        try:
            customer = self.customer_service.get_customer_by_id(int(id_customer))
            show_customer(customer)
        except Exception as e:
            show_error(f"Erro ao listar cliente: {e}")

    def _delete_customer(self) -> None:
        from src.view.customer_view import get_id_form
        from src.view.customer_view import show_success

        id_customer = get_id_form()
        try:
            self.customer_service.delete_customer(int(id_customer))
            show_success(f"Cliente deletado com sucesso! ID: {id_customer}")
        except Exception as e:
            show_error(f"Erro ao deletar cliente: {e}")
