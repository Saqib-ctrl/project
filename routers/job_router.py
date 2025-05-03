
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from backend import schemas
from ..services import job_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs", response_model=schemas.JobOut)
def post_job(data: schemas.JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, data)

@router.get("/jobs", response_model=list[schemas.JobOut])
def list_jobs(db: Session = Depends(get_db)):
    return job_service.get_jobs(db)
