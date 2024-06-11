from sqlalchemy import Column, Integer, Float, DateTime
from projectmod.database.db import Base
from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict, Union

class SaleModel(Base):
    __tablename__ = "ventas"
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    total_value = Column(Float)
    time = Column(DateTime)
    

    
class Sale(BaseModel):
    sale_id: int
    total_value: float
    time: datetime
    sale_details: List[Dict[str, Union[int, float]]]