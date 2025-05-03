
from sqlalchemy.orm import Session
from ..models import application
from backend import schemas

def create_application(db: Session, data: schemas.ApplicationCreate):
    new_app = application.Application(
        candidate_email=data.candidate_email,
        job_id=data.job_id,
        status="Pending"
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

def update_application_status(db: Session, data: schemas.ApplicationUpdate):
    app = db.query(application.Application).filter(application.Application.id == data.id).first()
    if app:
        app.status = data.status
        db.commit()
        db.refresh(app)
    return app

def get_applications_by_email(db: Session, email: str):
    return db.query(application.Application).filter(application.Application.candidate_email == email).all()
