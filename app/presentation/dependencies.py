from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db_session
from app.infrastructure.sqlalchemy_wallet_repository import SqlAlchemyWalletRepository
from app.application.use_cases.operate_wallet_use_case import OperateWalletUseCase
from app.application.use_cases.get_wallet_use_case import GetWalletUseCase
from app.application.use_cases.create_wallet_use_case import CreateWalletUseCase

async def get_sqlalchemy_wallet_repository(db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> SqlAlchemyWalletRepository:
    return SqlAlchemyWalletRepository(db_session)

async def get_operate_wallet_use_case(repo : Annotated[SqlAlchemyWalletRepository, Depends(get_sqlalchemy_wallet_repository)]):
    return OperateWalletUseCase(repo)

async def get_get_wallet_use_case(repo : Annotated[SqlAlchemyWalletRepository, Depends(get_sqlalchemy_wallet_repository)]):
    return GetWalletUseCase(repo)

async def get_create_wallet_use_case(repo : Annotated[SqlAlchemyWalletRepository, Depends(get_sqlalchemy_wallet_repository)]):
    return CreateWalletUseCase(repo)
