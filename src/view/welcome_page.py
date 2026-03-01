from src.utils.clear_screen import clear_screen
from src.utils.header import header

def welcome_page() -> int:
    clear_screen()
    header("SISTEMA DE CADASTRO DE CLIENTES")
    print('- versão 1.0.0')
    print('- by Luis Felipe de Oliveira Monteiro')
    print()
    print(f'Menu:')
    print("[1] - Opções de Clientes\n[2] - Opções de Endereços\n[3] - Sair")
    input_option = int(input("Digite a opção desejada: "))



if __name__ == "__main__":
    welcome_page()
