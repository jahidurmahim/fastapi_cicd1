from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    isAvailable: bool

products: List[Product] = []

@app.get("/")
def home():
    return {"message": "Welcome to the Book Management System"}

@app.get("/book")
def get_products():
    return products

@app.post("/book")
def add_product(product: Product):
    products.append(product)
    return products

@app.put("/book/{book_id}")
def update_product(book_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == book_id:
            products[index] = updated_product
            return updated_product
    return {"error": "Book Not Found"}

@app.delete("/book/{book_id}")
def delete_product(book_id: int):
    for index, product in enumerate(products):
        if product.id == book_id:
            deleted = products.pop(index)
            return {"message": f"Book '{deleted.name}' deleted successfully"}
    return {"error": "Book not found, deletion failed"}
