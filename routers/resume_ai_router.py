
from fastapi import APIRouter, UploadFile, File
from ..services import resume_ai_service

router = APIRouter()

@router.post("/analyze-resume-ai")
async def analyze_resume_ai(file: UploadFile = File(...)):
    return await resume_ai_service.parse_resume_and_generate_bio(file, "./backend/uploads")
