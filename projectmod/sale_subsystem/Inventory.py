"""
    This module contains the Inventory class which is responsible for managing the products in the inventory.

    Author: Jonathan
"""
import os
from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from projectmod.models.product import ProductModel, Product

Base = declarative_base()
metadata = MetaData()

inventory_db = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("price", Float),
    Column("quantity_available", Integer),
)   

load_dotenv()

DATABASE_CONNECTION = "sqlite:///inventory.db"
engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

metadata.create_all(engine)


class InventoryDE(BaseModel):
    """ This is a model to represents the inventory of products """
    name: str
    price: float
    quantity_available: int

class Inventory:

    """ This class represents the inventory of products """

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):

        """ This method adds a product to the inventory """

        query = inventory_db.insert().values(
            name=product.product_name, 
            price=product.product_price, 
            quantity_available=product.quantity_available
        )
        session.execute(query)
        session.commit()
        

    def remove_product(self, product_id):

        """ This method removes a product from the inventory """

        query = inventory_db.delete().where(inventory_db.c.id == product_id)
        session.execute(query) 
        session.commit()

    def update_product(self, product_id: int, **kwargs):

        """ This method updates the details of a product """
        
        query = inventory_db.update().where(inventory_db.c.id == product_id).values(**kwargs)
        session.execute(query)
        session.commit()
    def get_all_products(self):
    
        """ This method returns all the products in the inventory """
    
        return session.query(ProductModel).all()

    def get_product(self, product_id: int):

        """ This method returns a product from the inventory """

        query = inventory_db.select().where(inventory_db.c.id == product_id)
        return session.execute(query).fetchone()
