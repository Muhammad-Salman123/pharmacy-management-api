from fastapi import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date
from app.database import get_db
from app.models.medicine import Medicine
from app.schemas.medicine import MedicineCreate, MedicineResponse
from app.schemas.medicine import MedicineUpdate

router = APIRouter(
    prefix="/medicines",
    tags=["Medicines"]
)


@router.post("/", response_model=MedicineResponse, status_code=status.HTTP_201_CREATED)
def create_medicine(medicine: MedicineCreate, db: Session = Depends(get_db)):
    new_medicine = Medicine(
        name=medicine.name,
        manufacturer=medicine.manufacturer,
        price=medicine.price,
        stock_quantity=medicine.stock_quantity,
        expiry_date=medicine.expiry_date
    )

    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)

    return new_medicine


@router.get("/", response_model=list[MedicineResponse])
def get_all_medicines(db: Session = Depends(get_db)):
    medicines = db.query(Medicine).all()
    return medicines


@router.get("/{medicine_id}", response_model=MedicineResponse)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()

    if not medicine:
        raise HTTPException(
            status_code=404,
            detail="Medicine not found"
        )

    return medicine


@router.put("/{medicine_id}", response_model=MedicineResponse)
def update_medicine(
    medicine_id: int,
    medicine_data: MedicineUpdate,
    db: Session = Depends(get_db)
):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()

    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")

    for field, value in medicine_data.dict(exclude_unset=True).items():
        setattr(medicine, field, value)

    db.commit()
    db.refresh(medicine)

    return medicine


@router.delete("/{medicine_id}", status_code=204)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()

    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")

    db.delete(medicine)
    db.commit()

    return


@router.get("/expired", response_model=list[MedicineResponse])
def get_expired_medicines(db: Session = Depends(get_db)):
    return db.query(Medicine).filter(Medicine.expiry_date < date.today()).all()


@router.get("/low-stock", response_model=list[MedicineResponse])
def low_stock(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(Medicine).filter(Medicine.stock_quantity <= threshold).all()
