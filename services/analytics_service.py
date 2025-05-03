
from sqlalchemy.orm import Session
from ..models import candidate, job, application, message
from ..schemas import AnalyticsSummary

def get_summary(db: Session) -> AnalyticsSummary:
    return AnalyticsSummary(
        total_candidates=db.query(candidate.Candidate).count(),
        total_jobs=db.query(job.Job).count(),
        total_applications=db.query(application.Application).count(),
        total_messages=db.query(message.Message).count()
    )
