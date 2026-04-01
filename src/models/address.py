from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Address:
    """
    Model de Endereço
    
    Atributos:
        street: str - Nome da rua
        number: str - Número do endereço
        neighborhood: str - Bairro
        cep: str - CEP
        customer_id: int - ID do cliente associado
        created_at: Optional[datetime] - Data de criação do registro
        updated_at: Optional[datetime] - Data da última atualização
        id: Optional[int] - ID do endereço
    """
    street: str
    number: str
    neighborhood: str
    cep: str
    customer_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    id: Optional[int] = None
    
        