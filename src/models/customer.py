from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
    birth_date: date
    email: str
    phone: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]