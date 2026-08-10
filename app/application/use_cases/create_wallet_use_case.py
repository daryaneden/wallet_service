from app.domain.wallet_repository import WalletRepository

class CreateWalletUseCase:

    def __init__(self, wallet_repository: WalletRepository) -> int:
        self.wallet_repository = wallet_repository

    async def execute (self):
    
        wallet_id = await self.wallet_repository.create()

        return wallet_id
