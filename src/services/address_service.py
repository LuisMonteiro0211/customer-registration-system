from src.repositories.address_repository import AddressRepository
from src.dtos.address_dto import CreateAddressDTO

class AddressService:
    def __init__(self, address_repository: AddressRepository):
        self.address_repository = address_repository # Recebe uma instância do repositório já pronta para uso

    def create_address(self, address_dto: CreateAddressDTO) -> int:
        pass
