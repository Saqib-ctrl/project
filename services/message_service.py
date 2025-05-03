
from sqlalchemy.orm import Session
from ..models import message
from backend import schemas

def send_message(db: Session, data: schemas.MessageCreate):
    new_msg = message.Message(**data.dict())
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

def get_inbox(db: Session, email: str):
    return db.query(message.Message).filter(message.Message.recipient_email == email).all()

def get_thread(db: Session, user1: str, user2: str):
    return db.query(message.Message).filter(
        ((message.Message.sender_email == user1) & (message.Message.recipient_email == user2)) |
        ((message.Message.sender_email == user2) & (message.Message.recipient_email == user1))
    ).order_by(message.Message.timestamp).all()
