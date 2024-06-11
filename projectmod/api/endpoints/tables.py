from fastapi import APIRouter
from projectmod.services.tables import TableService
from projectmod.database.db import get_database_session

router = APIRouter()


@router.get("/")
async def get_tables():
    db = get_database_session()
    table_service = TableService(db)
    result = table_service.get_all_tables()
    return result