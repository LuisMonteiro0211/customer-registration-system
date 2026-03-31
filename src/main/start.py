from src.controllers.customer_controller import CustomerController
from src.services.customer_service import CustomerService
from src.repositories.customer_repository import CustomerRepository
from src.view.welcome_page import welcome_page
from src.view.suport import show_error

repository_customer = CustomerRepository()
service_customer = CustomerService(repository_customer)
controller_customer = CustomerController(service_customer)

def start():
    print("Iniciando sistema...")
    while True:
        try:
            option = welcome_page()
            if option == 1:
                controller_customer.handle_menu()
            elif option == 2:
                print("Opções de Endereços")
            elif option == 3:
                break
            if option > 3:
                show_error("Opção inválida, favor digitar uma opção válida entre 1 e 3")
        except ValueError as e:
            show_error(f"Erro ao iniciar sistema: {e}")
            