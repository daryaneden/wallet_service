from dataclasses import dataclass

@dataclass
class Wallet:

    id: int | None
    _balance: int

    def __post_init__(self):
        if self._balance < 0:
            raise ValueError('Баланс не может быть ниже нуля')

    @property
    def balance(self) -> int:
        return self._balance

    def change_balance(self, value: int) -> None:
        self._validate_balance(value)
        self._balance = value

    def _validate_balance(self, value: int) -> None:
        if value < 0:
            raise ValueError('Баланс не может быть ниже нуля')