
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..services import audit_service
from ..schemas import AuditLogOut

router = APIRouter(prefix="/logs")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AuditLogOut])
def get_audit_logs(db: Session = Depends(get_db)):
    return audit_service.get_logs(db)
