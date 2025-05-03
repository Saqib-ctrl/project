
from fastapi import APIRouter
from backend import schemas
from ..services import email_service

router = APIRouter(prefix="/emails")

@router.post("/generate", response_model=schemas.EmailTemplateOutput)
def generate_email(data: schemas.EmailTemplateInput):
    return email_service.generate_email_template(data)
