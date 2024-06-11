# SERVICIOS WEB

import os
# from core_subsystem.user import User+
from fastapi import FastAPI
from pydantic import BaseModel
from .sale_subsystem import Inventory
from .sale_subsystem import Product
# from pydantic import BaseModel, SecretStr
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

app = FastAPI(
    title="Sales Managment Project",
    version="0.1",
    description="This is an api web to use services for sales managment.",
)

class LoginInfo(BaseModel):
    name: str
    price: float

@app.post("/login")
def login(body: LoginInfo) -> bool:
    """ This function is used to login in the system """
    print(body)
    inventory = Inventory()
    producto = Product(body.name, body.price, 10)
    inventory.add_product(producto)
    print(inventory.get_all_products())
    
    return True
        
