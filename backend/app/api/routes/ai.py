from fastapi import APIRouter
from app.ai.investor_agent import analyse_opportunity

router = APIRouter()

@router.post("/investor-analysis")
def investor_analysis(data: dict):
    return {
        "analysis": analyse_opportunity(data)
    }
