import os
from os import system

def clear_screen():
    system('cls' if os.name == 'nt' else 'clear')