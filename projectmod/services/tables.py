from projectmod.models.table import TableModel

class TableService:
  def __init__(self, db) -> None:
    self.db = db
    
  def get_all_tables(self):
    return self.db.query(TableModel).all()
  
  def create_table(self, table):
    self.db.add(table)
    self.db.commit()
    self.db.refresh(table)
    return table