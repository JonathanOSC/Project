from sqlalchemy import Column, Integer, Float
from projectmod.database.db import Base
from pydantic import BaseModel


class ProductSaleModel(Base):
    __tablename__ = "products_sales"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    product_quantity = Column(Integer)
    sale_id = Column(Integer)
    
class ProductSale(BaseModel):
    """ This class represents a product sale """
    def __init__(self, product_id: int, product_price: float, product_quantity: int, sale_id: int):
        self.product_id = product_id
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.sale_id = sale_id
        
class ProductSaleCreate(BaseModel):
    """ This class represents a product sale """
    id: int
    quantity: int