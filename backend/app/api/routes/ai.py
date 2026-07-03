from fastapi import APIRouter
from app.ai.summariser import summarise_property
from app.services.scoring_service import calculate_deal_score

router = APIRouter()

@router.post("/summary")
def summary(data: dict):
    return {
        "summary": summarise_property(data)
    }

@router.post("/deal-score")
def deal_score(data: dict):
    return {
        "score": calculate_deal_score(
            data.get("price", 0),
            data.get("market_value", 0),
            data.get("location_score", 50)
        )
    }
