
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
from services import candidate_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/candidate", response_model=schemas.CandidateOut)
def save_candidate(data: schemas.CandidateCreate, db: Session = Depends(get_db)):
    return candidate_service.create_or_update_candidate(db, data)

@router.get("/candidate/{email}", response_model=schemas.CandidateOut)
def fetch_candidate(email: str, db: Session = Depends(get_db)):
    result = candidate_service.get_candidate_by_email(db, email)
    if not result:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return result
