
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from backend import schemas
from ..services import application_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/apply", response_model=schemas.ApplicationOut)
def apply(data: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return application_service.create_application(db, data)

@router.put("/update-status", response_model=schemas.ApplicationOut)
def update_status(data: schemas.ApplicationUpdate, db: Session = Depends(get_db)):
    return application_service.update_application_status(db, data)

@router.get("/applications/{email}", response_model=list[schemas.ApplicationOut])
def get_applications(email: str, db: Session = Depends(get_db)):
    return application_service.get_applications_by_email(db, email)
