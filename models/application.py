
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    candidate_email = Column(String, index=True)
    job_id = Column(Integer, index=True)
    status = Column(String, default="Pending")
