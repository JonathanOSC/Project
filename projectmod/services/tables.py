from projectmod.models.table import TableModel, TableCreate
from projectmod.models.product_table import ProductTableModel
from projectmod.models.product import ProductModel

class TableService:
  def __init__(self, db) -> None:
    self.db = db
    
  def get_all_tables(self):
    return self.db.query(TableModel).all()
  
  def get_table(self, table_id):
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
  
  def add_product_to_table(self, table_id, product_id, quantity):
    product_table = ProductTableModel(product_id=product_id, table_id=table_id, quantity=quantity)
    self.db.add(product_table)
    self.db.commit()
    self.db.refresh(product_table)
    return product_table