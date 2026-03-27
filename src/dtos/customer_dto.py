from dataclasses import dataclass
from datetime import date
from typing import List
@dataclass
class CreateCustomerDTO:
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str

@dataclass
class UpdateCustomerDTO:
    """DTO para atualização de clientes - Lista de tuplas (campo, valor)
    
    Exemplo:
    [["first_name", "João"], ["last_name", "Silva"], 
    ["birth_date", "1990-01-01"], 
    ["email", "joao.silva@example.com"], 
    ["phone", "(11) 99999-9999"]]
    """
    list_fields: List[tuple[str, str]]