"""
    this class is responsible for the sale of products

    Author: Jonathan
"""

inventory = Inventory()

class Sale:
    """" This class represents a sale of products """
    def __init__(self, sale_id: int, total_value: float, time: DateTime, info_organization: GeneralInfo):
        self.sale_id = sale_id
        self.total_value = total_value
        self.time = time
        self.info_organization = info_organization
        self.sale_details = []

    def complete_sale(self):
        """ Completes the sale by calculating the total value and updating the inventory """
        self.total_value = sum(detail['product_price'] * detail['product_quantity'] for detail in self.sale_details)
        for detail in self.sale_details:
            product_id = detail['product_id']
            product = inventory.get_product(product_id)

            product.quantity_available -= detail['product_quantity']

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


