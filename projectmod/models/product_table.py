""" This module contains the model for the product_table table 
    Author: Jonathan
"""

from sqlalchemy import Column, Integer, String
from projectmod.database.db import Base
from pydantic import BaseModel 

class ProductTableModel(Base):
    """ Table to store the products and tables """
    __tablename__ = "products_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    table_id = Column(Integer)
    quantity = Column(Integer)
