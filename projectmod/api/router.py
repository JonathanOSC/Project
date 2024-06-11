from fastapi import APIRouter
#routes
from .endpoints.products import router as products_router
from .endpoints.sales import router as sales_router

api_router = APIRouter()

api_router.include_router(products_router, prefix="/products", tags=["products"])
api_router.include_router(sales_router, prefix="/sales", tags=["sales"])

@api_router.get("/hello-world")
async def hello_world():
    return {"message": "Hello World!"}