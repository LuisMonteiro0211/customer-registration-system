from datetime import datetime
from src.view.suport import show_error, show_success, new_interaction, clear_lines
from time import sleep
from src.services.customer_service import CustomerService
from src.dtos.customer_dto import CreateCustomerDTO, UpdateCustomerDTO
from src.utils.validators import validate_filled_string, validate_email, validate_phone, validate_date_format
from src.utils.formatters import convert_to_us_date, format_phone_br

class CustomerController:
    """
    Controlador de clientes - Intermedia a interação entre a view e o service
    
    Atributos:
        customer_service: CustomerService - Serviço de clientes
        menu_options: dict - Dicionário com as opções do menu
        
    Métodos:
        handle_menu() -> None - Gerencia o menu principal de clientes
    """
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service
        self.menu_options = {
            "1": self._create_customer,
            "2": self._list_all_customers,
            "3": self._list_customer_by_id,
            "4": self._update_customer,
            "5": self._delete_customer,
        }

    def handle_menu(self):
        """
        Gerencia o menu principal de operações com clientes
        
        Exibe o menu e executa as ações selecionadas pelo usuário
        """
        from src.view.customer_view import get_option_menu
        from src.view.customer_view import customer_menu

        while True:
            option = get_option_menu(1, 6, customer_menu)

            if option == "6":
                break
                
            action = self.menu_options.get(option)
            if action:
                action()
                if not new_interaction("Deseja realizar outra ação? [S/N]"):
                    break

    def _create_customer(self) -> int:
        """
        Cria um novo cliente
        
        Coleta os dados via formulário, valida e envia ao serviço
        
        Returns:
            int - ID do cliente criado ou None em caso de erro
        """
        from src.view.customer_view import create_customer_form
        customer_info = create_customer_form()

        try:
            # Teste de validação de dados - Try para capturar os erros de validação
            validate_filled_string(customer_info["first_name"], "Nome deve ser preenchido")
            validate_filled_string(customer_info["last_name"], "Sobrenome deve ser preenchido")
            validate_date_format(customer_info["birth_date"])
            validate_email(customer_info["email"])
            validate_phone(customer_info["phone"])

            #Formatação dos dados para o formato do banco de dados
            date_formatter = datetime.strptime(customer_info["birth_date"], "%d/%m/%Y").date()
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
            # Try para capturar erros no processamento do serviço - Banco Serviço - Repositório
            result = self.customer_service.create_customer(customer_dto)
            return result
        except Exception as e:
            show_error(f"Erro ao criar cliente: {e}")

    def _list_all_customers(self) -> None:
        """
        Lista todos os clientes cadastrados
        
        Busca todos os clientes e exibe em formato de tabela
        """
        from src.view.customer_view import show_all_customers
        try:
            customers = self.customer_service.get_all_customers()
            show_all_customers(customers)
        except Exception as e:
            show_error(f"Erro ao listar clientes: {e}")

    def _list_customer_by_id(self) -> None:
        """
        Lista um cliente específico pelo ID
        
        Solicita o ID, busca o cliente e exibe seus detalhes
        """
        from src.view.customer_view import get_id_form
        from src.view.customer_view import show_customer

        while True:
            id_customer = get_id_form()
            try:
                customer = self.customer_service.get_customer_by_id(int(id_customer))
                if customer:
                    show_customer(customer)
                    break
            except Exception as e:
                show_error(f"Erro ao listar cliente: {e}")

    def _update_customer(self) -> None:
        """
        Atualiza os dados de um cliente
        
        Permite atualizar um ou mais campos de um cliente existente
        """
        from src.view.customer_view import get_id_form
        from src.view.customer_view import get_option_menu
        from src.view.customer_view import show_customer
        from src.view.customer_view import update_menu
        from src.view.customer_view import show_warning
        LIST_ACTIONS = {
            "1": ["first_name", validate_filled_string],
            "2": ["last_name", validate_filled_string],
            "3": ["birth_date", validate_date_format],
            "4": ["email", validate_email],
            "5": ["phone", validate_phone],
        }

        while True:
            #Passo 1: Buscar o cliente pelo ID
            customer_id_to_update = get_id_form()
            try:
                customer_to_update = self.customer_service.get_customer_by_id(customer_id_to_update)
                if customer_to_update: 
                    break
            except Exception as e:
                show_error(f"Erro ao buscar cliente: {e}")

        list_fields_to_update = []

        while True:
            #Passo 2: Mostrar o cliente encontrado e exibir o menu de atualização
            show_customer(customer_to_update)
            field_to_update = get_option_menu(1, 6, update_menu)

            if not field_to_update:
                break

            while True:
                #Passo 3: Solicitar o novo valor para o campo
                value_to_update = input("Digite um novo valor para o campo: ")

                try:
                    validate_filled_string(value_to_update, f"O campo deve ser preenchido com um valor válido")

                    #Passo 4: Validar o novo valor para o campo de forma específica
                    action = LIST_ACTIONS.get(field_to_update)[1]
                    if action:
                        action(value_to_update)
                    break
                except ValueError as e:
                    clear_lines(1)
                    show_error(f"Erro ao validar/converter os dados do cliente: {e}")
                    sleep(2)
                    clear_lines(2)

            #Passo 5: Adicionar o campo e o novo valor à lista de campos a serem atualizados
            field_name = LIST_ACTIONS.get(field_to_update)[0]
            if field_name == "birth_date":
                value_to_update = datetime.strptime(value_to_update, "%d/%m/%Y").date()
            list_fields_to_update.append((field_name, value_to_update))

            if not new_interaction("Deseja atualizar outro campo? [S/N]"):
                break

        if not list_fields_to_update:
            show_warning("Nenhum campo foi atualizado")
            return

        customer_update_dto = UpdateCustomerDTO(customer_id_to_update=customer_id_to_update, list_fields=list_fields_to_update)

        try:
            #Passo 6: Atualizar o cliente
            result = self.customer_service.update_customer(customer_update_dto)
            show_success(f"Cliente atualizado com sucesso, foi afetado {result} linhas")
        except Exception as e:
            show_error(f"Erro ao atualizar cliente: {e}")

    def _delete_customer(self) -> None:
        """
        Deleta um cliente pelo ID
        
        Solicita confirmação antes de deletar permanentemente
        """
        from src.view.customer_view import get_id_form
        from src.view.customer_view import show_success, show_warning
        from src.view.customer_view import show_confirmation_action

        
        while True:
            id_customer = get_id_form()
            try:
                customer_is_exists = self.customer_service.get_customer_by_id(int(id_customer))

                if not customer_is_exists:
                    show_error("Cliente não encontrado")
                    continue
                else:
                    if show_confirmation_action("Deseja realmente deletar o cliente? [S/N]", 1):
                        self.customer_service.delete_customer(int(id_customer))
                        show_success(f"Cliente deletado com sucesso! ID: {id_customer}")
                        break
                    else:
                        show_warning("Ação cancelada")
                        break
            except Exception as e:
                show_error(f"Erro ao deletar cliente: {e}")