from pydantic import BaseModel
from datetime import date


class SaleCreate(BaseModel):
    medicine_id: int
    quantity: int


class SaleResponse(BaseModel):
    id: int
    medicine_id: int
    quantity: int
    sale_date: date

    class Config:
        from_attributes = True
