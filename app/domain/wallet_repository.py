from abc import ABC, abstractmethod
from app.domain.wallet_entity import Wallet

class WalletRepository(ABC):

    @abstractmethod
    async def create(self, wallet_create_model: Wallet) -> int:
        pass

    @abstractmethod
    async def get(self, wallet_id: int) -> Wallet:
        pass

    @abstractmethod
    async def save(self, wallet: Wallet) -> None:
        pass
