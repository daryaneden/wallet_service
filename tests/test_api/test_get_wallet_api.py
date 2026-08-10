import pytest_asyncio
import pytest
from app.main import app as main_app
from app.presentation.dependencies import get_get_wallet_use_case
from tests.fakes.fake_wallet import FakeWalletData 

@pytest.mark.asyncio

class TestGetWallet:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, get_wallet_use_case):

        main_app.dependency_overrides[get_get_wallet_use_case] = lambda: get_wallet_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_wallet(self, test_session): 

        wallet = FakeWalletData()
        
        test_session.add(wallet)
        await test_session.commit()

        return wallet

    async def test_get_wallet_success(self, client, fake_wallet, setup_dependencies):

        wallet_id = fake_wallet.id
        
        response = await client.get(url=f'/wallets/{wallet_id}')
        
        wallet = response.json()
        
        assert response.status_code == 200
        assert wallet['balance'] == fake_wallet.balance

    async def test_get_wallet_not_found(self, client, setup_dependencies):

        wallet_id = 0
                   
        response = await client.get(url=f'/wallets/{wallet_id}')

        assert response.status_code == 404


