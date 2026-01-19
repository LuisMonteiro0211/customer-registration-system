from src.utils.clear_screen import clear_screen

def welcome_page() -> int:
    clear_screen()
    print(f'{"-"*40}')
    print(f'{"SISTEMA DE CADASTRO DE CLIENTES":^40}')
    print(f'{"-"*40}')
    print('- versão 1.0.0')
    print('- by Luis Felipe de Oliveira Monteiro')
    print()
    print(f'Menu:')
    print("[1] - Opções de Clientes\n[2] - Opções de Endereços\n[3] - Sair")
    input_option = int(input("Digite a opção desejada: "))



if __name__ == "__main__":
    welcome_page()
