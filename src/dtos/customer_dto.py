from dataclasses import dataclass
from datetime import date
from typing import List
@dataclass
class CreateCustomerDTO:
    """
    DTO para criação de clientes
    
    Atributos:
        first_name: str - Primeiro nome
        last_name: str - Sobrenome
        birth_date: date - Data de nascimento
        email: str - Email
        phone: str - Telefone
    """
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str

@dataclass
class UpdateCustomerDTO:
    """
    DTO para atualização de clientes
    
    Atributos:
        list_fields: List[tuple[str, object]] - Lista de tuplas (campo, valor) a serem atualizados
        customer_id_to_update: int - ID do cliente a ser atualizado
        
    Exemplo:
        [["first_name", "João"], ["last_name", "Silva"], 
        ["birth_date", "1990-01-01"], 
        ["email", "joao.silva@example.com"], 
        ["phone", "(11) 99999-9999"]]
    """
    list_fields: List[tuple[str, object]]
    customer_id_to_update: int