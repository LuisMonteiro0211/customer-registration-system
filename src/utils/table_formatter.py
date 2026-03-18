from tabulate import tabulate
from typing import List, Any

def render_table(headers: List[str], datas: List[List[Any]]) -> None:
    """
    Exibe uma tabela com os dados passados, utilizando a biblioteca tabulate

    Args:
        headers: List[str]: Lista de headers da tabela
        datas: List[List[Any]]: Lista de dados da tabela
    Returns:
        None
    """
    table = tabulate(datas, headers=headers, tablefmt="grid")
    print(table)
