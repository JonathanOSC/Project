from fastapi import APIRouter
from projectmod.sale_subsystem.Sale import Sale
from pydantic import BaseModel
from datetime import datetime as DateTime
from projectmod.models.product_sale import ProductSaleCreate
from typing import List

router = APIRouter()

# class Sale(BaseModel):
#     sale_id: int
#     total_value: float
#     time: DateTime
#     info_organization: GeneralInfo
#     sale_details: List[Dict[str, Union[int, float]]]
    
# # sales = Sale()

# # @router.get("/")
# # async def get_sales():
    
# #     return sales.get_all_sales()

@router.post("/")
async def create_sale(sale_parm: List[ProductSaleCreate]):
    sale = Sale()
    
    return sale.complete_sale(sale_parm)

@router.get("/")
async def get_sales():
    sale = Sale()
    
    return sale.get_all_sales()

@router.get("/{sale_id}")
async def get_products_sale(sale_id: int):
    sale = Sale()
    
    return sale.get_all_products_sales(sale_id)

