
from fastapi import APIRouter
from backend import schemas
from ..services import contract_service

router = APIRouter(prefix="/contracts")

@router.post("/generate", response_model=schemas.ContractOutput)
def generate_contract(data: schemas.ContractInput):
    return contract_service.generate_contract(data)
