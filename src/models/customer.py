from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Customer:
    """
    Model de Cliente
    
    Atributos:
        first_name: str - Primeiro nome do cliente
        last_name: str - Sobrenome do cliente
        birth_date: date - Data de nascimento
        email: str - Email do cliente
        phone: str - Telefone do cliente
        created_at: Optional[datetime] - Data de criação do registro
        updated_at: Optional[datetime] - Data da última atualização
        id: Optional[int] - ID do cliente
    """
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    id: Optional[int] = None