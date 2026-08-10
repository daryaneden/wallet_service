import pytest_asyncio
import pytest
from app.main import app as main_app
from app.presentation.dependencies import get_create_wallet_use_case

@pytest.mark.asyncio

class TestCreateWalletApi:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, create_wallet_use_case):

        main_app.dependency_overrides[get_create_wallet_use_case] = lambda: create_wallet_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    async def test_create_wallet_success(self, client, setup_dependencies):

        response = await client.post(url=f'/wallets/')

        wallet = response.json()

        assert wallet['id'] == 1
        assert wallet['balance'] == 0