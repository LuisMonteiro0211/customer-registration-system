from abc import ABC, abstractmethod
from src.repositories.interfaces.interface_repository import IRepository

class ICustomerRepository(IRepository):

    @abstractmethod
    def get_email(self, email: str):
        pass

    @abstractmethod
    def get_phone(self, phone: str):
        pass