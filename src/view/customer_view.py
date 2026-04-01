from src.utils.header import header
from src.utils.clear_screen import clear_screen
from typing import Dict, List, Callable
from src.models.customer import Customer
from time import sleep
from readchar import readkey
from src.view.suport import show_error, show_success, clear_lines
from src.utils.object_to_table import customers_to_table_data
from src.utils.table_formatter import render_table

def customer_menu():
    """
    Exibe o menu principal de operações com clientes
    """
    clear_screen()
    header("Opções de Clientes")
    print("[1] - Cadastrar Cliente")
    print("[2] - Listar Clientes")
    print("[3] - Listar Cliente por ID")
    print("[4] - Atualizar Cliente")
    print("[5] - Deletar Cliente")
    print("[6] - Sair")

def update_menu():
    """
    Exibe o menu de atualização de campos do cliente
    """
    header("Atualização de Cliente")
    print("[1] - Nome")
    print("[2] - Sobrenome")
    print("[3] - Data de Nascimento")
    print("[4] - Email")
    print("[5] - Telefone")
    print("[6] - Voltar")

def get_option_menu(min_option: int, max_option: int, action_menu: Callable) -> str:
    """
    Captura a opção do menu com validação
    
    Args:
        min_option: int - Opção mínima válida
        max_option: int - Opção máxima válida (opção de saída)
        action_menu: Callable - Função que exibe o menu
        
    Returns:
        str - Opção selecionada ou None se escolher sair
    """
    action_menu()
    while True:
        input_option = input("Digite a opção desejada: ")

        try:
            int_option = int(input_option)
            if int_option == max_option:
                return None
            if min_option <= int_option <= max_option:
                return input_option
            else:
                clear_lines(1)
                print(f"\033[91mErro: Favor digitar uma opção válida entre {min_option} e {max_option}\033[0m")
                sleep(2)
                clear_lines(1)
        except ValueError:
            clear_lines(1)
            print(f"\033[91mErro: Favor digitar um número inteiro\033[0m")
            sleep(2)
            clear_lines(1)

def create_customer_form() -> Dict[str, str]:
    """
    Formulário de cadastro de cliente
    
    Returns:
        Dict[str, str] - Dicionário com os dados do cliente
    """
    clear_screen()
    header("Cadastro de Cliente")
    customer_info: Dict[str, str] = {
        "first_name": input("Digite o nome do cliente: "),
        "last_name": input("Digite o sobrenome do cliente: "),
        "birth_date": input("Digite a data de nascimento do cliente: "),
        "email": input("Digite o email do cliente: "),
        "phone": input("Digite o telefone do cliente: "),
    }
    return customer_info

def get_id_form() -> int:
    """
    Formulário para captura de ID do cliente
    
    Returns:
        int - ID do cliente validado
    """
    clear_screen()
    while True:
        header("Busca de Cliente por ID")
        id_customer = input("Digite o ID do cliente: ")

        try:
            int_id_customer = int(id_customer)
        except ValueError:
            show_error("Valor deve ser um número inteiro")
            continue

        if int_id_customer <= 0:
            show_error("Valor deve ser maior que 0")
            continue

        return int_id_customer

def show_customer(customer: Customer) -> None:
    """
    Exibe os detalhes de um cliente
    
    Args:
        customer: Customer - Objeto do cliente a ser exibido
    """
    clear_screen()
    header("Cliente")
    print(f"ID: {customer.id}")
    print(f"Nome: {customer.first_name}")
    print(f"Sobrenome: {customer.last_name}")
    print(f"Data de Nascimento: {customer.birth_date}")
    print(f"Email: {customer.email}")
    print(f"Telefone: {customer.phone}")
    print(f"Data de Criação: {customer.created_at}")
    print(f"Data de Atualização: {customer.updated_at}")

def show_all_customers(customers: List[Customer]) -> None:
    """
    Exibe todos os clientes em formato de tabela
    
    Args:
        customers: List[Customer] - Lista de clientes a serem exibidos
    """
    clear_screen()
    header("Clientes Cadastrados")

    HEADERS = ["ID", "Nome", "Sobrenome", "Email", "Telefone"]
    DATAS = customers_to_table_data(customers)
    render_table(HEADERS, DATAS)

def show_confirmation_action(message: str, clear_lines_number: int) -> bool:
    """
    Solicita confirmação do usuário (S/N)
    
    Args:
        message: str - Mensagem de confirmação
        clear_lines_number: int - Número de linhas a limpar antes de exibir
        
    Returns:
        bool - True se confirmado (S), False se negado (N)
    """
    if clear_lines_number:
        clear_lines(clear_lines_number)
    print(message)
    while True:
        key = readkey().lower()
        if key == "s":
            return True
        elif key == "n":
            return False
        else:
            show_error("Favor digitar uma opção válida entre S e N")

def show_warning(message: str) -> None:
    """
    Exibe mensagem de aviso em amarelo
    
    Args:
        message: str - Mensagem de aviso
    """
    clear_screen()
    print(f"\033[93mAtenção: {message}\033[0m")
    sleep(3)