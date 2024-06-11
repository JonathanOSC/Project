from fastapi import APIRouter
from projectmod.models.table import TableCreate
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