from abc import ABC, abstractmethod
from typing import List

class IRepository(ABC):
    """
    Interface para repositórios

    Atributos:
        - Nenhum
        
    Métodos:
        - create(entity) -> int: Cria uma entidade
        - get_by_id(id: int): Retorna uma entidade pelo ID
        - get_all() -> List: Retorna todas as entidades
        - update(entity) -> int: Atualiza uma entidade
        - delete(id: int) -> int: Deleta uma entidade pelo ID
    """

    @abstractmethod
    def create(self, entity) -> int:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def update(self, entity) -> int:
        pass

    @abstractmethod
    def delete(self, id: int) -> int:
        pass