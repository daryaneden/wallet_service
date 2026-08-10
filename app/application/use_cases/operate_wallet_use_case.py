from app.application.dtos import OperationType, OperateWalletCommandDto, WalletDto
from app.application.exceptions import InsufficientFundsException, WalletNotFoundException
from app.domain.wallet_repository import WalletRepository

class OperateWalletUseCase:

    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    async def execute (self, command: OperateWalletCommandDto):

        wallet = await self.wallet_repository.get(command.wallet_id)

        if not wallet:
            raise WalletNotFoundException

        if command.amount <= 0:
            raise InsufficientFundsException

        if command.operation_type == OperationType.DEPOSIT:
            new_balance = wallet.balance + command.amount

        elif command.operation_type == OperationType.WITHDRAW:

            if command.amount > wallet.balance:
                raise InsufficientFundsException
            
            new_balance = wallet.balance - command.amount

        else:
            raise ValueError('Неверный тип операции')

        wallet.change_balance(new_balance)

        await self.wallet_repository.save(wallet)

        return WalletDto.model_validate(wallet)
