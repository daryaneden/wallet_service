from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel

class OperationType(str, Enum):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'

@dataclass
class OperateWalletCommandDto:
    wallet_id: int
    operation_type: OperationType 
    amount: int
 
class WalletDto(BaseModel):
    id: int = None
    balance: int | None

    class Config:
        from_attributes = True
