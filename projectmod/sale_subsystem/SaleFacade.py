""""
    Facade for the Sale subsystem

    Author: Jonathan
"""
from datetime import datetime as DateTime
from .GeneralInfo import GeneralInfo
from .Sale import Sale
from .SaleDetail import SaleDetail


class SaleFacade:
    def __init__(self):
        self.sales_history = []

    def create_sale(self, sale_id: int,  total_value: float, time: DateTime, info_organization: GeneralInfo):
        """ Creates a sale and adds it to the sales history """
        sale = Sale(sale_id, total_value, time, info_organization)
        self.sales_history.append(sale)
        return sale

    def complete_sale(self, sale: Sale):
        """ Completes a sale """
        sale.complete_sale()

    def print_sale_check(self, sale: Sale):
        """ Prints the sale check """
        sale.print_sale_check()

    def add_sale_detail(self, sale: Sale, sale_detail: SaleDetail):
        """ Adds a sale detail to the sale """
        sale.add_sale_detail(sale_detail)

    def delete_sale_detail(self, sale: Sale, sale_id_detail: int):
        """ Deletes a sale detail from the sale """
        sale.delete_sale_detail(sale_id_detail)
