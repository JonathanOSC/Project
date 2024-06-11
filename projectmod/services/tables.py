from projectmod.models.table import TableModel, TableCreate

class TableService:
  def __init__(self, db) -> None:
    self.db = db
    
  def get_all_tables(self):
    return self.db.query(TableModel).all()
  
  def create_table(self, data: TableCreate):
    table = TableModel(name=data.name)
    self.db.add(table)
    self.db.commit()
    self.db.refresh(table)
    return table