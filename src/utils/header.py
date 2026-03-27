def header(message: str) -> None:
    """
    Exibe um cabeçalho com uma mensagem centralizada
    Args:
        message: str: Mensagem a ser exibida
    Returns:
        None
    """
    print(f'{"-"*40}')
    print(f'{message:^40}')
    print(f'{"-"*40}')