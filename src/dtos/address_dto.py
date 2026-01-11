from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateAddressDTO:
    street: str
    number: str
    neighborhood: str
    cep: str
    customer_id: int