from sqlalchemy import Column, Integer, String
from projectmod.database.db import Base
from pydantic import BaseModel 

class TableModel(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    
class Table(BaseModel):
    __tablename__ = "tables"
    id: int
    name: str

class TableCreate(BaseModel):
    __tablename__ = "tables"
    name: str