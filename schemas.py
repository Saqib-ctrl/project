
from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    skills: str
    experience: str

class CandidateOut(CandidateCreate):
    id: int

    class Config:
        orm_mode = True


class ApplicationCreate(BaseModel):
    candidate_email: str
    job_id: int

class ApplicationUpdate(BaseModel):
    id: int
    status: str

class ApplicationOut(BaseModel):
    id: int
    candidate_email: str
    job_id: int
    status: str

    class Config:
        orm_mode = True


class JobCreate(BaseModel):
    title: str
    location: str
    company: str
    deadline: str

class JobOut(JobCreate):
    id: int
    description: str
    class Config:
        orm_mode = True


class CandidateStatusUpdate(BaseModel):
    email: str
    status: str

class ReportSummary(BaseModel):
    total_candidates: int
    total_jobs: int
    total_applications: int


class MessageCreate(BaseModel):
    sender_email: str
    recipient_email: str
    content: str

class MessageOut(BaseModel):
    id: int
    sender_email: str
    recipient_email: str
    content: str
    timestamp: str

    class Config:
        orm_mode = True


class ContractInput(BaseModel):
    candidate_name: str
    job_title: str
    company: str
    salary: str
    duration: str

class ContractOutput(BaseModel):
    content: str


class EmailTemplateInput(BaseModel):
    recipient_type: str  # e.g., Candidate, Employer
    purpose: str         # e.g., Interview invite, Job match, Rejection
    key_points: str      # Additional details to include

class EmailTemplateOutput(BaseModel):
    content: str


class BlogInput(BaseModel):
    title: str
    audience: str
    purpose: str

class BlogOutput(BaseModel):
    content: str


class AnalyticsSummary(BaseModel):
    total_candidates: int
    total_jobs: int
    total_applications: int
    total_messages: int


class AuditLogOut(BaseModel):
    id: int
    actor: str
    action: str
    target: str
    timestamp: str

    class Config:
        orm_mode = True
