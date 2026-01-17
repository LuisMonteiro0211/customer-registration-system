from src.models.address import Address
from typing import List

class AddressRepository:
    def __init__(self) -> None:
        # Como é uma classe apenas de execução de métodos não precisa de inicialização
        # Tendo em vista que os dados já vem preparados para uso
        pass
    
    def create(self, address: Address) -> int:
        # TODO: create(address) -> Salva o endereço e retorna o ID final
        pass

    def get_by_id(self, id: int) -> Address:
        # TODO: get_by_id(id) -> Retorna o endereço pelo ID
        pass

    def get_all(self) -> List[Address]:
        # TODO: get_all() -> Retorna lista com todos os endereços
        pass

    def update(self, address: Address) -> int:
        # TODO: update(address) -> Atualiza o endereço e retorna o ID final
        pass

    def delete(self, id: int) -> None:
        # TODO: delete(id) -> Deleta o endereço pelo ID
        pass