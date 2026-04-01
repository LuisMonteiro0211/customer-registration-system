from abc import ABC, abstractmethod
from typing import List

class IRepository(ABC):
    """
    Interface base para repositórios
    
    Métodos:
        create(entity) -> int - Cria uma entidade
        get_by_id(id: int) - Retorna uma entidade pelo ID
        get_all() -> List - Retorna todas as entidades
        update(entity) -> int - Atualiza uma entidade
        delete(id: int) -> int - Deleta uma entidade pelo ID
    """

    @abstractmethod
    def create(self, entity) -> int:
        """
        Cria uma nova entidade no banco de dados
        
        Args:
            entity - Entidade a ser criada
            
        Returns:
            int - ID da entidade criada
        """
        pass
    
    @abstractmethod
    def get_by_id(self, id: int):
        """
        Busca uma entidade pelo ID
        
        Args:
            id: int - ID da entidade
            
        Returns:
            Entidade encontrada
        """
        pass

    @abstractmethod
    def get_all(self) -> List:
        """
        Retorna todas as entidades
        
        Returns:
            List - Lista com todas as entidades
        """
        pass

    @abstractmethod
    def update(self, entity) -> int:
        """
        Atualiza uma entidade existente
        
        Args:
            entity - Entidade com dados atualizados
            
        Returns:
            int - Número de linhas afetadas
        """
        pass

    @abstractmethod
    def delete(self, id: int) -> int:
        """
        Deleta uma entidade pelo ID
        
        Args:
            id: int - ID da entidade a ser deletada
            
        Returns:
            int - Número de linhas afetadas
        """
        pass