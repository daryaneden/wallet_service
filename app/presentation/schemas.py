from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class OperationRequest(BaseModel):
    wallet_id: int
    operation_type: OperationType
    amount: int


class WalletResponseSchema(BaseModel):
    id: int
    balance: int
