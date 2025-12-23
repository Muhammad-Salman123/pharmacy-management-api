from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    manufacturer = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer)
    expiry_date = Column(Date)
