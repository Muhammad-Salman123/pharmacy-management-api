from fastapi import FastAPI
from app.database import engine, Base
from app.models import medicine
from app.routers import medicine as medicine_router
from app.routers import medicine as medicine_router
from app.routers import sales as sale_router

app = FastAPI(
    title="Pharmacy Management API",
    description="Backend API for managing pharmacy inventory, sales, and stock control",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(medicine_router.router)
app.include_router(medicine_router.router)
app.include_router(sale_router.router)


@app.get("/")
def root():
    return {"message": "Pharmacy API is running"}
