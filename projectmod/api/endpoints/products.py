from fastapi import APIRouter
from projectmod.sale_subsystem import Inventory, Product
from pydantic import BaseModel


router = APIRouter()
inventory = Inventory()

class CreateProduct(BaseModel):
    name: str
    price: float

class UpdateProduct(BaseModel):
    name: str
    price: float
    quantity_available: int

@router.get("/")
async def get_all_products():
    return inventory.get_all_products()


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return inventory.remove_product(product_id)

@router.post("/")
async def add_product(body: CreateProduct):
    product = Product(body.name, body.price, 10)
    return inventory.add_product(product)

@router.put("/{product_id}")
async def update_product(product_id: int, body: UpdateProduct):
    return inventory.update_product(product_id, **body.dict())