
from sqlalchemy.orm import Session
from ..models import audit_log

def log_action(db: Session, actor: str, action: str, target: str):
    log = audit_log.AuditLog(actor=actor, action=action, target=target)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_logs(db: Session):
    return db.query(audit_log.AuditLog).order_by(audit_log.AuditLog.timestamp.desc()).all()
