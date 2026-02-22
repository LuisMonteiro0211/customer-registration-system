from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Address:
    street: str
    number: str
    neighborhood: str
    cep: str
    customer_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    id: Optional[int] = None
    
        