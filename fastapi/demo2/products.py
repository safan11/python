from fastapi import FastAPI
from models import Product

app = FastAPI()

# Temporary database
products = []


# CREATE
@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product


# READ ALL
@app.get("/products")
def get_products():
    return products


# READ ONE
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}


# UPDATE
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products:
        if product.id == product_id:
            product.name = updated_product.name
            product.price = updated_product.price
            return product
    return {"message": "Product not found"}


# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted"}
    return {"message": "Product not found"}