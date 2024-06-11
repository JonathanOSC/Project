"""
    This class represents the SaleDetail entity.

    Author: Jonathan
"""

from .Product import Product


class SaleDetail:

    def __init__(self, sale_id_detail: int, product: Product, quantity: int):
        self.sale_id_detail = sale_id_detail
        self.product_id = product.product_id
        self.product_name = product.product_name
        self.product_quantity = quantity
        self.product_price = product.product_price
        self.details = {
            'sale_id_detail': self.sale_id_detail,
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_quantity': self.product_quantity,
            'product_price': self.product_price
        }

    def get_detail_sale(self):
        """
        Get the details of the sale.

        :return: A tuple containing the detail ID of the sale, the ID of the product, the quantity of the product, and the price of the product.
        """
        return self.details