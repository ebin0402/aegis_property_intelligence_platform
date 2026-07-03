from fastapi import APIRouter
from app.services.analytics_service import investment_score

router = APIRouter()

@router.post("/investment-score")
def score(data: dict):
    return investment_score(data)
