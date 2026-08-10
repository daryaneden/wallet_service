from app.presentation.schemas import OperationRequest
from app.application.dtos import OperationType
import factory
from faker import Faker

faker = Faker()

class FakeWithdrawRequestData(factory.Factory):
    class Meta:
        model = OperationRequest

    wallet_id = factory.Faker('random_int', min=0, max=100)
    operation_type = OperationType.WITHDRAW
    amount = factory.Faker('random_int', min=1, max=100)

class FakeDepositRequestData(factory.Factory):
    class Meta:
        model = OperationRequest

    wallet_id = factory.Faker('random_int', min=0, max=100)
    operation_type = OperationType.DEPOSIT
    amount = factory.Faker('random_int', min=1, max=100)
