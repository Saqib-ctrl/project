
from sqlalchemy import Column, Integer, String
from ..database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    location = Column(String)
    skills = Column(String)
    experience = Column(String)

    status = Column(String, default='Pending')  # Admin approval status
