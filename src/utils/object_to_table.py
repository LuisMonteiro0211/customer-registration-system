from src.models.customer import Customer
from src.models.address import Address
from typing import List, Any

def customers_to_table_data(customers: List[Customer]) -> List[List[Any]]:
    """
    Converte uma lista de objetos Customer para formato de tabela
    
    Args:
        customers: List[Customer] - Lista de clientes a ser convertida
        
    Returns:
        List[List[Any]] - Lista de listas com dados dos clientes para tabela
    """
    return [[
    c.id, 
    c.first_name, 
    c.last_name,
    c.email, 
    c.phone] 
    for c in customers]