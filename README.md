# Продуктовый API

Инструкция по запуску и использованию API.

# Запуск сервера

1. Установите зависимости:
   ```bash
   pip install fastapi uvicorn
# Создание продукта
1. curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Example Product",
  "description": "This is a test product",
  "price": 99.99
}' http://localhost:8000/api/products
2. если вы запускаете через power shell то команда будет
3. Invoke-WebRequest -Uri "http://localhost:8000/api/products" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{
  "name": "Example Product",
  "description": "This is a test product",
  "price": 99.99
}'
# Получение продукта по ID
1. curl http://localhost:8000/api/products/550e8400-e29b-41d4-a716-446655440000
