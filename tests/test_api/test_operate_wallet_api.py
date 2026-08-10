import pytest_asyncio
import pytest
from app.main import app as main_app
from app.presentation.dependencies import get_operate_wallet_use_case
from tests.fakes.fake_wallet import FakeWalletData 
from tests.fakes.fake_operation_request_data import FakeDepositRequestData, FakeWithdrawRequestData

@pytest.mark.asyncio

class TestOperateWalletRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, operate_wallet_use_case):

        main_app.dependency_overrides[get_operate_wallet_use_case] = lambda: operate_wallet_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_wallet(self, test_session): 

        wallet = FakeWalletData(balance = 1000)
        
        test_session.add(wallet)
        await test_session.commit()

        return wallet

    async def test_operate_wallet_withdraw_success(self, client, fake_wallet, setup_dependencies):

        request = FakeWithdrawRequestData(wallet_id = fake_wallet.id, amount = 100)

        wallet_id = fake_wallet.id
        
        response = await client.post(url=f'/wallets/{wallet_id}/operation', json=request.model_dump())
        
        wallet = response.json()
        
        assert response.status_code == 200
        assert wallet['balance'] == 900

    async def test_operate_wallet_deposit_success(self, client, fake_wallet, setup_dependencies):

        request = FakeDepositRequestData(wallet_id = fake_wallet.id)

        wallet_id = fake_wallet.id

        new_balance = fake_wallet.balance + request.amount

        response = await client.post(url=f'/wallets/{wallet_id}/operation', json=request.model_dump())

        wallet = response.json()

        assert response.status_code == 200
        assert wallet['balance'] == new_balance

    async def test_operate_wallet_insuffisent_funds(self, client, fake_wallet, setup_dependencies):

       request = FakeWithdrawRequestData(wallet_id = fake_wallet.id, amount = 1000)

       fake_wallet.balance = 999
       
       wallet_id = fake_wallet.id

       response = await client.post(url=f'/wallets/{wallet_id}/operation', json=request.model_dump())

       assert response.status_code == 400
       
    async def test_operate_wallet_not_found(self, client, fake_wallet, setup_dependencies):

        request = FakeWithdrawRequestData(wallet_id = 0)
               
        wallet_id = request.wallet_id

        response = await client.post(url=f'/wallets/{wallet_id}/operation', json=request.model_dump())

        assert response.status_code == 404

    async def test_operate_invalid_operation(self, client, fake_wallet, setup_dependencies):

        request = {'wallet_id': fake_wallet.id,
            'operation_type': 'INVALID',
            'amount': 100}

        wallet_id = fake_wallet.id

        response = await client.post(url=f'/wallets/{wallet_id}/operation', json=request)

        assert response.status_code == 422
    


               
        
