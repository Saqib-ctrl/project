
from sqlalchemy.orm import Session
from models import candidate
import schemas

def create_or_update_candidate(db: Session, data: schemas.CandidateCreate):
    existing = db.query(candidate.Candidate).filter(candidate.Candidate.email == data.email).first()
    if existing:
        for field, value in data.dict().items():
            setattr(existing, field, value)
    else:
        existing = candidate.Candidate(**data.dict())
        db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

def get_candidate_by_email(db: Session, email: str):
    return db.query(candidate.Candidate).filter(candidate.Candidate.email == email).first()
