from src.utils.clear_screen import clear_screen
from src.utils.header import header
from typing import Dict, List
from src.models.customer import Customer

UPDATE_CUSTOMER_OPTIONS = {
    "1": "NOME",
    "2": "SOBRENOME",
    "3": "DATA DE NASCIMENTO",
    "4": "EMAIL",
    "5": "TELEFONE"
}

def customer_view() -> str:
    header("Opções de Clientes")
    print("[1] - Cadastrar Cliente")
    print("[2] - Opções de Buscas")
    print("[3] - Atualizar Cliente")
    print("[4] - Deletar Cliente")
    print("[5] - Sair")
    input_option = input("Digite a opção desejada: ")
    return input_option

def create_customer() -> Dict[str, str]:
    header("Cadastrar Cliente")

    first_name = input("Digite o nome do cliente: ")
    last_name = input("Digite o sobrenome do cliente: ")
    birth_date = input("Digite a data de nascimento do cliente: ")
    email = input("Digite o email do cliente: ")
    phone = input("Digite o telefone do cliente: ")

    customer: Dict[str, str] = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "email": email,
        "phone": phone
    }

    return customer

def search_customer() -> str:
    header("Opções de Buscas")
    print("[1] - Buscar Cliente por ID")
    print("[2] - Buscar todos os Clientes")
    input_option = input("Digite a opção desejada: ")

    return input_option

def get_customer_by_id() -> str:
    header("Buscar Cliente por ID")
    id = input("Digite o ID do cliente: ")
    return id

def get_all_customers(list_customers: List[Customer]) -> str:
    header("Buscar todos os Clientes")
    for customer in list_customers:
        print(f"ID: {customer.id}, Nome: {customer.first_name} {customer.last_name}, Data de Nascimento: {customer.birth_date}, Email: {customer.email}, Telefone: {customer.phone}")

def menu_update_customer() -> str:
    header("Atualizar Cliente")
    print("Informe um campo para atualizar: ")
    print("[1] - Nome")
    print("[2] - Sobrenome")
    print("[3] - Data de Nascimento")
    print("[4] - Email")
    print("[5] - Telefone")
    input_option = input("Digite a opção desejada: ")
    return input_option

def update_customer(option: str,old_value: str) -> str:
    header("Atualizar Cliente")
    print(f"O valor atual do campo {UPDATE_CUSTOMER_OPTIONS[option]} é: {old_value}")
    print(f"Informe um novo valor para o campo {UPDATE_CUSTOMER_OPTIONS[option]}: ")
    new_value = input("Digite o novo valor: ")
    return new_value

def delete_customer() -> str:
    header("Deletar Cliente")
    id = input("Digite o ID do cliente: ")
    return id

if __name__ == "__main__":
    pass