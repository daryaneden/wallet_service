from app.application.dtos import WalletDto
from app.domain.wallet_repository import WalletRepository
from app.application.exceptions import WalletNotFoundException

class GetWalletUseCase:

    def __init__(self, wallet_repository: WalletRepository) -> WalletDto | None:
        self.wallet_repository = wallet_repository

    async def execute (self, wallet_id: int):
    
        wallet = await self.wallet_repository.get(wallet_id)

        if wallet is None:
            raise WalletNotFoundException

        return WalletDto.model_validate(wallet)

            