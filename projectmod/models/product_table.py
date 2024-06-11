from sqlalchemy import Column, Integer, String
from projectmod.database.db import Base
from pydantic import BaseModel 

class ProductTableModel(Base):
    __tablename__ = "products_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    table_id = Column(Integer)
    quantity = Column(Integer)
    
# class Table(BaseModel):
#     __tablename__ = "tables"
#     id: int
#     name: str

# class TableCreate(BaseModel):
#     __tablename__ = "tables"
#     name: str
    