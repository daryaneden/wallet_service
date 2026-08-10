Wallet API
REST API для управления балансом кошельков.
🚀 Стек
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Pytest
📌 Функционал
* Пополнение кошелька (DEPOSIT)
* Списание средств (WITHDRAW)
* Получение текущего баланса
🏗 Архитектура
Проект построен по принципам Clean Architecture:
* domain — бизнес-сущности и правила
* application — use cases
* infrastructure — работа с БД
* presentation — API (FastAPI роутеры)
🔧 Запуск
docker-compose up --build
🧪 Тесты
pytest
📬 Пример запроса
POST /api/v1/wallets/{wallet_id}/operation
{
  "operation_type": "DEPOSIT",
  "amount": 100
}
