# SERVICIOS WEB

import os
# from core_subsystem.user import User+
from fastapi import FastAPI
from pydantic import BaseModel
from .sale_subsystem import Inventory
# from pydantic import BaseModel, SecretStr
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

app = FastAPI(
    title="Sales Managment Project",
    version="0.1",
    description="This is an api web to use services for sales managment.",
)

class LoginInfo(BaseModel):
    product_name: str
    price: float


@app.post("/login")
def login(body: LoginInfo) -> bool:
    """ This function is used to login in the system """
    print(body)
    inventory = Inventory()
    inventory.add_product(body)
    
    return True
    # return user_info.username == "admin" and user_info.password == "admin"
        
