from fastapi import APIRouter, Depends, HTTPException
from app.presentation.schemas import OperationRequest, WalletResponseSchema
from app.application.dtos import OperateWalletCommandDto
from app.application.exceptions import WalletNotFoundException, InsufficientFundsException
from app.presentation.dependencies import get_operate_wallet_use_case, get_get_wallet_use_case, get_create_wallet_use_case
from app.application.use_cases.create_wallet_use_case import CreateWalletUseCase
from app.application.use_cases.get_wallet_use_case import GetWalletUseCase
from app.application.use_cases.operate_wallet_use_case import OperateWalletUseCase
from typing import Annotated

router = APIRouter(prefix='/wallets', tags=['wallets'])

@router.post('/', response_model=WalletResponseSchema)
async def create_wallet(create_wallet_use_case: Annotated[CreateWalletUseCase, Depends(get_create_wallet_use_case)],
                        get_wallet_use_case: Annotated[GetWalletUseCase, Depends(get_get_wallet_use_case)]):

    wallet_id = await create_wallet_use_case.execute()

    wallet = await get_wallet_use_case.execute(wallet_id)

    return WalletResponseSchema(
                id=wallet.id,
                balance=wallet.balance
            )


@router.post('/{wallet_id}/operation', response_model=WalletResponseSchema)
async def operate_wallet(
    request: OperationRequest,
    use_case: Annotated[OperateWalletUseCase, Depends(get_operate_wallet_use_case)]
):
    try:
        command = OperateWalletCommandDto(
            wallet_id=request.wallet_id,
            operation_type=request.operation_type,
            amount=request.amount
        )

        wallet = await use_case.execute(command)

        return WalletResponseSchema(
            id=wallet.id,
            balance=wallet.balance
        )

    except WalletNotFoundException as e:
        raise HTTPException(status_code=404, 
                            detail=e.detail)

    except InsufficientFundsException as e:
        raise HTTPException(status_code=400, 
                            detail=e.detail)

    except ValueError as e:
        raise HTTPException(status_code=400, 
                            detail='Неверный тип операции')

@router.get('/{wallet_id}', response_model=WalletResponseSchema)
async def get_wallet(wallet_id: int,
    get_wallet_use_case: Annotated [GetWalletUseCase, Depends(get_get_wallet_use_case)]
):

    try:

        wallet = await get_wallet_use_case.execute(wallet_id)

    except WalletNotFoundException as e:
            raise HTTPException(status_code=404, 
                                detail=e.detail)
    
    return WalletResponseSchema(
        id=wallet.id,
        balance=wallet.balance
    )
