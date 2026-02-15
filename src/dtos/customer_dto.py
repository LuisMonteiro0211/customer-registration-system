from dataclasses import dataclass
from datetime import date

@dataclass
class CreateCustomerDTO:
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str

@dataclass
class UpdateCustomerDTO:
    id: int
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str