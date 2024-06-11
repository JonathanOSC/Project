from fastapi import APIRouter
from projectmod.models.table import TableCreate, TableAddProduct
from projectmod.services.tables import TableService
from projectmod.database.db import get_database_session

router = APIRouter()

db = get_database_session()

@router.get("/")
async def get_tables():
    table_service = TableService(db)
    result = table_service.get_all_tables()
    return result

@router.post("/")
async def create_table(table: TableCreate):
    table_service = TableService(db)
    result = table_service.create_table(table)
    return result

@router.get("/{table_id}")
async def get_table(table_id: int):
    table_service = TableService(db)
    result = table_service.get_table(table_id)
    return result

@router.post("/{table_id}")
async def add_product_to_table(table_id: int, data: TableAddProduct):
    table_service = TableService(db)
    result = table_service.add_product_to_table(table_id, data.product_id, data.quantity)
    return result

@router.delete("/{table_id}/{product_id}")
async def remove_product_to_table(table_id: int, product_id: int):
    table_service = TableService(db)
    result = table_service.remove_product_to_table(table_id, product_id)
    return result

@router.post("/{table_id}/close")
async def close_table(table_id: int):
    table_service = TableService(db)
    result = table_service.close_table(table_id)
    return result