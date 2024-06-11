"""
    This class is used to represent a table in the restaurant.

    Author: Jonathan
"""
from .Sale import Sale

class Table:
    def __init__(self, table_id: int, sale: Sale):
        self.table_id = table_id
        self.sale = sale