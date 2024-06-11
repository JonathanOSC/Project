from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_sales():
    return {"message": "Get all sales"}