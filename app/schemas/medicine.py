from pydantic import BaseModel
from datetime import date
from typing import Optional


class MedicineBase(BaseModel):
    name: str
    manufacturer: str
    price: float
    stock_quantity: int
    expiry_date: date


class MedicineCreate(MedicineBase):
    pass


class MedicineResponse(MedicineBase):
    id: int

    class Config:
        from_attributes = True


class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    expiry_date: Optional[date] = None
