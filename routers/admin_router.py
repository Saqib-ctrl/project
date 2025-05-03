
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from backend import schemas
from ..services import admin_service

router = APIRouter(prefix="/admin")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/candidates")
def list_candidates(db: Session = Depends(get_db)):
    return admin_service.list_candidates(db)

@router.put("/candidates/update-status")
def update_status(data: schemas.CandidateStatusUpdate, db: Session = Depends(get_db)):
    return admin_service.update_candidate_status(db, data)

@router.get("/report", response_model=schemas.ReportSummary)
def get_report(db: Session = Depends(get_db)):
    return admin_service.generate_report(db)
