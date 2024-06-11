from sqlalchemy import Column, Integer, String, Float
from projectmod.db import Base

class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Float)
    quantity_available = Column(Integer)
    

class Product:
    """ This class represents a product """
    def __init__(self, product_name: str, product_price: int, quantity_available: int):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity_available = quantity_available

    