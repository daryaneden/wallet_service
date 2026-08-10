class WalletNotFoundException(Exception):
    detail = 'Кошелек не найден'

class InsufficientFundsException(Exception):
    detail = 'Неправильная сумма операции'
