from src.utils.clear_screen import clear_screen
from time import sleep
from readchar import readkey

def clear_lines(n: int) -> None:
    """
    Limpa n linhas do console
    
    Args:
        n: int - Número de linhas a serem limpas
    """
    for _ in range(n):
        print("\033[A\033[K", end="")

def show_error(message: str) -> None:
    """
    Exibe mensagem de erro em vermelho e aguarda 3 segundos
    
    Args:
        message: str - Mensagem de erro
    """
    clear_screen()
    print(f"\033[91mErro: {message}\033[0m")
    sleep(3)

def show_success(message: str) -> None:
    """
    Exibe mensagem de sucesso em verde e aguarda 3 segundos
    
    Args:
        message: str - Mensagem de sucesso
    """
    clear_screen()
    print(f"\033[92mSucesso: {message}\033[0m")
    sleep(3)

def new_interaction(message: str) -> bool:
    """
    Solicita confirmação do usuário (S/N)
    
    Args:
        message: str - Mensagem de confirmação
        
    Returns:
        bool - True se o usuário digitar S, False se digitar N
    """
    clear_lines(1)
    print(message)

    while True:
        key = readkey().lower()

        if key == "s":
            return True
        elif key == "n":
            return False
        else:
            show_error("Favor digitar uma opção válida entre S e N")