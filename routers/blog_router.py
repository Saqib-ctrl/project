
from fastapi import APIRouter
from backend import schemas
from ..services import blog_service

router = APIRouter(prefix="/blogs")

@router.post("/generate", response_model=schemas.BlogOutput)
def generate_blog(data: schemas.BlogInput):
    return blog_service.generate_blog(data)
