from app.domain.wallet_repository import WalletRepository
from app.infrastructure.models import WalletModel
from app.domain.wallet_entity import Wallet
from app.infrastructure.database import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert 

class SqlAlchemyWalletRepository(WalletRepository):

    def __init__(self, db_session: AsyncSession = get_db_session()):
        self.db_session = db_session

    async def create(self) -> int:

        query = insert(WalletModel).values(balance = 0).returning(WalletModel.id)
        wallet_id: int = (await self.db_session.execute(query)).scalar_one_or_none()
        return wallet_id

    async def get(self, wallet_id: int) -> WalletModel | None:
        query = select(WalletModel).where(WalletModel.id == wallet_id)
        wallet: WalletModel = (await self.db_session.execute(query)).scalar_one_or_none()

        if wallet is None:
            return None

        return Wallet(id=wallet.id, _balance=wallet.balance)

    async def save(self, wallet_entity: Wallet) -> None:
        query = select(WalletModel).where(WalletModel.id == wallet_entity.id)
        wallet: WalletModel = (await self.db_session.execute(query)).scalar_one_or_none()

        if wallet is None:
            wallet = WalletModel(id = wallet_entity.id,
                                 balance = wallet_entity.balance)

            self.db_session.add(wallet)

        else:
            wallet.balance = wallet_entity.balance


