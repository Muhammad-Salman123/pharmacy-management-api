from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.models.medicine import Medicine
from app.models.sales import Sale
from app.schemas.sales import SaleCreate, SaleResponse

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post("/", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(
        Medicine.id == sale.medicine_id).first()

    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")

    if medicine.expiry_date < date.today():
        raise HTTPException(status_code=400, detail="Medicine is expired")

    if sale.quantity > medicine.stock_quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    medicine.stock_quantity -= sale.quantity

    new_sale = Sale(
        medicine_id=sale.medicine_id,
        quantity=sale.quantity
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale
