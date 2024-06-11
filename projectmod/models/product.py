from sqlalchemy import Column, Integer, String, Float
from projectmod.db import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Float)
    quantity_available = Column(Integer)