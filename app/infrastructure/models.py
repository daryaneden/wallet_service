from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base

class WalletModel(Base):
    __tablename__ = 'wallet'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    balance: Mapped[int]