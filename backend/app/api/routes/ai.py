from fastapi import APIRouter

router = APIRouter()

@router.post("/summary")
def property_summary(data: dict):
    return {
        "summary": f"This property at {data.get('location', 'unknown')} is a strong candidate for buyers seeking value and location balance.",
        "risks": ["Market volatility", "Interest rate sensitivity"],
        "opportunities": ["Capital appreciation", "Rental yield potential"]
    }


@router.post("/deal-score")
def deal_score(data: dict):
    price = data.get("price", 300000)
    estimated_market = data.get("market_value", 320000)

    score = int(((estimated_market - price) / estimated_market) * 100)

    return {
        "score": max(min(score, 100), 0),
        "explanation": "Based on price vs estimated market value"
    }
