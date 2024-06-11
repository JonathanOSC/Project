from projectmod.models.table import TableModel, TableCreate
from projectmod.models.product_table import ProductTableModel
from projectmod.models.product import ProductModel
from projectmod.models.product_sale import ProductSaleCreate
from projectmod.sale_subsystem.Sale import Sale


class TableService:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_tables(self):
        return self.db.query(TableModel).all()
  
    def get_table(self, table_id: int):
        result = self.db.query(TableModel).filter(TableModel.id == table_id).first()
        result.total = 0
        result.products = self.db.query(ProductTableModel).filter(ProductTableModel.table_id == table_id).all()
        for product in result.products:
            product_details = self.db.query(ProductModel).filter(ProductModel.id == product.product_id).first()
            product.name = product_details.name
            product.price = product_details.price

            result.total += product.quantity * product_details.price

        return result
  
    def create_table(self, data: TableCreate):
        table = TableModel(name=data.name)
        self.db.add(table)
        self.db.commit()
        self.db.refresh(table)
        return table
  
    def add_product_to_table(self, table_id: int, product_id: int, quantity: int):
        product_table = self.db.query(ProductTableModel).filter_by(product_id=product_id, table_id=table_id).first()
        product = self.db.query(ProductModel).filter_by(id=product_id).first()
        #CORRECT

        if product_table:

            if product.quantity_available < quantity:
                return "Not enough quantity available"
            
            else:

                product_table.quantity += quantity
                self.db.query(ProductTableModel).filter_by(product_id=product_id, table_id=table_id).update({"quantity": product_table.quantity})
        else:
            if product.quantity_available < quantity:
                return "Not enough quantity available"
            
            else:
                product_table = ProductTableModel(product_id=product_id, table_id=table_id, quantity=quantity)
                self.db.add(product_table)
    
        self.db.commit()
        self.db.refresh(product_table)
        return product_table

    def remove_product_to_table(self, table_id: int, product_id: int):
        product_table = self.db.query(ProductTableModel).filter_by(product_id=product_id, table_id=table_id).first()

        if product_table:
            self.db.query(ProductTableModel).filter_by(product_id=product_id, table_id=table_id).delete()
        else:
            return "Product not found in table"

        self.db.commit()
        return product_table
    
    def close_table(self, table_id: int):
        table = self.get_table(table_id)
        sale = Sale()
        print(table.products)
        product_to_sale = []

        for product in table.products:
            #update quantity in inventory
            product_details = self.db.query(ProductModel).filter(ProductModel.id == product.product_id).first()
            product_details.quantity_available -= product.quantity #Falta verificación de cantidad disponible en add product to table
            self.db.query(ProductModel).filter(ProductModel.id == product.product_id).update({"quantity_available": product_details.quantity_available})

            produc_sale_create = ProductSaleCreate(id=product.product_id, quantity=product.quantity)
            product_to_sale.append(produc_sale_create)

        self.db.commit()


        sale.complete_sale(product_to_sale)

        self.db.query(ProductTableModel).filter_by(table_id=table_id).delete()
        self.db.commit()         


# lista -> id, quantity
