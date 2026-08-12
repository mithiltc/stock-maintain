from fastapi import FastAPI, HTTPException
from model import product
from database import LocalSession,engine
import databasemodel

app = FastAPI()
databasemodel.Base.metadata.create_all(bind=engine)

products = [
    product(id=1, name="laptop", price=999.99),
    product(id=2, name="phone", price=499.99),
    product(id=3, name="tablet", price=299.99)
]


@app.get("/")
def hello():
    return "hello mithil"


@app.get("/products")
def get_products():
    db=LocalSession()
    db.query()
    return products


@app.get("/products/{id}")
def get_product_id(id: int):
    for item in products:
        if item.id == id:
            return item

    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def create_products(new_product: product):
    products.append(new_product)
    return new_product


@app.put("/products/{id}")
def put_product(id: int, updated_product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return updated_product

    raise HTTPException(status_code=404, detail="Product not found")
@app.delete("/products/{id}")    
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del(products[i])
    raise HTTPExcption(status_code=404,detail="product not found")        

