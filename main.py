from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Модель продукта
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    created_at: str

# Модель для создания продукта
class CreateProductRequest(BaseModel):
    name: str
    description: str
    price: float

# Хранилище продуктов в памяти
products = []

# a. API для создания продукта
@app.post("/api/products", response_model=Product)
def create_product(product: CreateProductRequest):
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be a positive number")

    new_product = Product(
        id=str(uuid4()),
        name=product.name,
        description=product.description,
        price=product.price,
        created_at=datetime.now().isoformat(),
    )
    products.append(new_product)
    return new_product

# b. API для получения страницы продуктов
@app.get("/api/products", response_model=List[Product])
def get_products(page: int = 1, page_size: int = 10):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return products[start_index:end_index]

# c. API для получения продукта по ID
@app.get("/api/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: str):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)