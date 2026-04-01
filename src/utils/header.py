def header(message: str) -> None:
    """
    Exibe um cabeçalho formatado com mensagem centralizada
    
    Args:
        message: str - Mensagem a ser exibida no cabeçalho
    """
    print(f'{"-"*40}')
    print(f'{message:^40}')
    print(f'{"-"*40}')