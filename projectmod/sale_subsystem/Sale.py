"""
    this class is responsible for the sale of products

    Author: Jonathan
"""
from .Inventory import Inventory
from datetime import datetime
from projectmod.models.product_sale import ProductSaleCreate, ProductSaleModel
from projectmod.models.sale import SaleModel
from typing import List
from projectmod.models.product import ProductModel
from projectmod.database.db import get_database_session
from sqlalchemy import MetaData, Table, Column, Integer, Float, DateTime
from dotenv import load_dotenv


inventory = Inventory()

metadata = MetaData()

sales_history_db = Table(
    "sales_history",
    metadata,
    Column("sale_id", Integer, primary_key=True, autoincrement=True),
    Column("total_value", Float),
    Column("time", DateTime),
)   

products_sales_db = Table(
    "products_sales",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("product_id", Integer),
    Column("product_quantity", Integer),
    Column("sale_id", Integer),
)

load_dotenv()



class Sale:
    """" This class represents a sale of products """
    def __init__(self):
        self.total_value = 0
        self.time = datetime.now()
        self.products_sale = []
        
        self.session = get_database_session()
        

    def complete_sale(self, products_sale: List[ProductSaleCreate]):
        """ Completes the sale by calculating the total value and updating the inventory """
        self.products_sale = products_sale
        
        
        for product in self.products_sale:
            product_id = product.id
            result = self.session.query(ProductModel.price).filter(ProductModel.id == product_id).first()
            self.total_value += result[0] * product.quantity
        
        #Sales History Add
        query = sales_history_db.insert().values(
            total_value=self.total_value, 
            time=self.time
        )
        result = self.session.execute(query)
        self.session.commit()
            
        #Products Sales Add
        for product in self.products_sale:
            query_primary_key = products_sales_db.insert().values(
                sale_id = result.inserted_primary_key[0],
                product_id = product.id,
                product_quantity = product.quantity,
            )
            self.session.execute(query_primary_key)
        self.session.commit()
        
        return self.total_value
    
    def get_all_sales(self):
        """ Returns all sales """
        return self.session.query(SaleModel).all()
    
    def get_all_products_sales(self, sale_id: int):
        """ Returns all products sold in a sale """
        return self.session.query(ProductSaleModel).filter(ProductSaleModel.sale_id == sale_id).all()
    


