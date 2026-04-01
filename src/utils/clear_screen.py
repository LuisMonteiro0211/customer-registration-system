import os
from os import system

def clear_screen():
    """
    Limpa a tela do console
    
    Usa 'cls' no Windows e 'clear' em sistemas Unix
    """
    system('cls' if os.name == 'nt' else 'clear')