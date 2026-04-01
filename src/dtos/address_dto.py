from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateAddressDTO:
    """
    DTO para criação de endereços
    
    Atributos:
        street: str - Nome da rua
        number: str - Número
        neighborhood: str - Bairro
        cep: str - CEP
        customer_id: int - ID do cliente associado
    """
    street: str
    number: str
    neighborhood: str
    cep: str
    customer_id: int

@dataclass
class UpdateAddressDTO:
    """
    DTO para atualização de endereços
    
    Atributos:
        id: int - ID do endereço a ser atualizado
        street: str - Nome da rua
        number: str - Número
        neighborhood: str - Bairro
        cep: str - CEP
        customer_id: int - ID do cliente associado
    """
    id: int
    street: str
    number: str
    neighborhood: str
    cep: str
    customer_id: int