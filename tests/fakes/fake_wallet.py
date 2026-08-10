from app.infrastructure.models import WalletModel
import factory
from faker import Faker

faker = Faker()

class FakeWalletData(factory.Factory):
    class Meta:
        model = WalletModel

    id = factory.Faker('random_int', min=0, max=100)
    balance = factory.Faker('random_int', min=0, max=10000)