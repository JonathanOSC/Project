""""
This file contains the Product class which is used to create product objects.

Author: Jonathan
"""



class Product:
    """ This class represents a product """
    def __init__(self, product_name: str, product_price: int, quantity_available: int):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity_available = quantity_available

    