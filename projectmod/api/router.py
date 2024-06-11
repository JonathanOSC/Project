from fastapi import APIRouter
#routes
from .endpoints.products import router as products_router

api_router = APIRouter()

api_router.include_router(products_router, prefix="/products", tags=["products"])

@api_router.get("/hello-world")
async def hello_world():
    return {"message": "Hello World!"}