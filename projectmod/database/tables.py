from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from .db import engine

metadata = MetaData()

tables_db = Table(
    "tables",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
)   

def create_tables():
    metadata.create_all(engine)