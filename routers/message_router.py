
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from backend import schemas
from ..services import message_service

router = APIRouter(prefix="/messages")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MessageOut)
def send_message(data: schemas.MessageCreate, db: Session = Depends(get_db)):
    return message_service.send_message(db, data)

@router.get("/inbox/{email}", response_model=list[schemas.MessageOut])
def inbox(email: str, db: Session = Depends(get_db)):
    return message_service.get_inbox(db, email)

@router.get("/thread/{user1}/{user2}", response_model=list[schemas.MessageOut])
def thread(user1: str, user2: str, db: Session = Depends(get_db)):
    return message_service.get_thread(db, user1, user2)
