from tabulate import tabulate
from typing import List, Any

def render_table(headers: List[str], datas: List[List[Any]]) -> None:
    """
    Exibe uma tabela formatada no console usando tabulate
    
    Args:
        headers: List[str] - Lista de cabeçalhos da tabela
        datas: List[List[Any]] - Lista de linhas com os dados da tabela
    """
    table = tabulate(datas, headers=headers, tablefmt="grid")
    print(table)
