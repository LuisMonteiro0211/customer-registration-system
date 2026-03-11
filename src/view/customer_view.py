from src.utils.header import header, clear_screen
from typing import Dict, List
from src.models.customer import Customer
from time import sleep

def show_error(message: str) -> None:
    clear_screen()
    print(f"\033[91mErro: {message}\033[0m")
    sleep(3)

def show_success(message: str) -> None:
    clear_screen()
    print(f"\033[92mSucesso: {message}\033[0m")
    sleep(3)

def customer_menu():
    header("Opções de Clientes")
    print("[1] - Cadastrar Cliente")
    print("[2] - Listar Clientes")
    print("[3] - Listar Cliente por ID")
    print("[4] - Atualizar Cliente")
    print("[5] - Deletar Cliente")
    print("[6] - Sair")


def get_option_menu() -> str:
    while True:
        customer_menu()
        input_option = input("Digite a opção desejada: ")

        try:
            int_option = int(input_option)
            if 1 <= int_option <= 6:
                return input_option
            else:
                show_error("Favor digitar uma opção válida entre 1 e 6")
        except ValueError as e:
            show_error(f"Favor digitar um número inteiro: {e}")


def create_customer_form() -> Dict[str, str]:
    header("Cadastro de Cliente")
    customer_info: Dict[str, str] = {
        "first_name": input("Digite o nome do cliente: "),
        "last_name": input("Digite o sobrenome do cliente: "),
        "birth_date": input("Digite a data de nascimento do cliente: "),
        "email": input("Digite o email do cliente: "),
        "phone": input("Digite o telefone do cliente: "),
    }
    return customer_info

def get_id_form() -> str:
    while True:
        header("Busca de Cliente por ID")
        id_customer = input("Digite o ID do cliente: ")

        try:
            id_customer_int = int(id_customer)
            if id_customer_int > 0: return id_customer
            else: show_error("Favor digitar um ID maior que 0")

        except ValueError as e:
            show_error(f"Favor digitar um número inteiro: {e}")

def show_customer(customer: Customer) -> None:
    print(f"ID: {customer.id}")
    print(f"Nome: {customer.first_name} {customer.last_name}")
    print(f"Data de Nascimento: {customer.birth_date}")
    print(f"Email: {customer.email}")
    print(f"Telefone: {customer.phone}")
    print(f"Data de Criação: {customer.created_at}")
    print(f"Data de Atualização: {customer.updated_at}")
    print("--------------------------------")

def show_all_customers(customers: List[Customer]) -> None:
    for customer in customers:
        show_customer(customer)

if __name__ == "__main__":
    create_customer_form()