from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from .db import engine

metadata = MetaData()

tables_db = Table(
    "tables",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
)   


metadata.create_all(engine)