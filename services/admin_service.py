
from sqlalchemy.orm import Session
from ..models import candidate, job, application
from backend import schemas

def list_candidates(db: Session):
    return db.query(candidate.Candidate).all()

def update_candidate_status(db: Session, data: schemas.CandidateStatusUpdate):
    user = db.query(candidate.Candidate).filter(candidate.Candidate.email == data.email).first()
    if user:
        user.status = data.status
        db.commit()
        db.refresh(user)
    return user

def generate_report(db: Session):
    return schemas.ReportSummary(
        total_candidates=db.query(candidate.Candidate).count(),
        total_jobs=db.query(job.Job).count(),
        total_applications=db.query(application.Application).count()
    )
