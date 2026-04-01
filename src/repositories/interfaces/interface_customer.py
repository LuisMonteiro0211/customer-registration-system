from abc import ABC, abstractmethod
from src.repositories.interfaces.interface_repository import IRepository

class ICustomerRepository(IRepository):
    """
    Interface específica para repositório de clientes
    
    Estende IRepository com métodos específicos de clientes
    """

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        """
        Verifica se existe um cliente com o email informado
        
        Args:
            email: str - Email a ser verificado
            
        Returns:
            bool - True se existir, False caso contrário
        """
        pass

    @abstractmethod
    def exists_by_phone(self, phone: str) -> bool:
        """
        Verifica se existe um cliente com o telefone informado
        
        Args:
            phone: str - Telefone a ser verificado
            
        Returns:
            bool - True se existir, False caso contrário
        """
        pass