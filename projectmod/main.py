# SERVICIOS WEB
from fastapi import FastAPI
from .api import router as api_router
from .database.tables import create_tables


app = FastAPI(
    title="Sales Managment Project",
    version="0.1",
    description="This is an api web to use services for sales managment.",
)

create_tables()

app.include_router(api_router.api_router, prefix="/api")
