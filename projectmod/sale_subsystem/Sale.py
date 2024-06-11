"""
    this class is responsible for the sale of products

    Author: Jonathan
"""
from .Inventory import Inventory
from datetime import datetime
from .GeneralInfo import GeneralInfo
from .SaleDetail import SaleDetail
from projectmod.models.product_sale import ProductSaleCreate
from projectmod.models.sale import SaleModel
from typing import List
from projectmod.models.product import ProductModel
from projectmod.db import get_database_session
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
            
        query = sales_history_db.insert().values(
            total_value=self.total_value, 
            time=self.time
        )
        self.session.execute(query)
        self.session.commit()
            
            
            
        return sales_history_db.select(sales_history_db.c.sale_id).order_by(sales_history_db.c.sale_id.desc()).first()[0]
            
            
            # product = inventory.get_product(product_id)
            
            # product.quantity_available -= detail['product_quantity']
            
            # self.sales_history.append(self.sale_id)

    def print_sale_check(self):
        """ Prints the sale check """
        print(f"Sale ID: {self.sale_id}")
        print(f"Organization Name: {self.info_organization.name_organization}")
        print(f"Address: {self.info_organization.address}")
        print(f"NIT: {self.info_organization.nit}")
        print(f"Time: {self.time}")
        for detail in self.sale_details:
            print(f"Product ID: {detail['product_id']}, Quantity: {detail['product_quantity']}, Price: {detail['product_price']}")
        print(f"Total Value: {self.total_value}")

    def add_sale_detail(self, sale_detail: SaleDetail):
        self.sale_details.append(sale_detail.get_detail_sale())

    def delete_sale_detail(self):
        """ Deletes a sale detail from the sale """
        self.sale_details = [detail for detail in self.sale_details if detail['sale_id_detail'] != sale_id_detail]
        
    def get_all_sales(self):
        return self.session.query(sales_history_db).all()


