from abc import ABC, abstractmethod
from src.repositories.interfaces.interface_repository import IRepository

class ICustomerRepository(IRepository):

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def exists_by_phone(self, phone: str) -> bool:
        pass