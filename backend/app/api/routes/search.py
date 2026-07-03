from fastapi import APIRouter
from app.services.search_service import search_properties

router = APIRouter()

MOCK_PROPERTIES = [
    {"id": 1, "title": "Family Home", "price": 300000, "bedrooms": 3, "location": "Kent"},
    {"id": 2, "title": "City Flat", "price": 450000, "bedrooms": 2, "location": "London"},
    {"id": 3, "title": "Budget Home", "price": 200000, "bedrooms": 2, "location": "Kent"},
]

@router.post("/")
def search(filters: dict):
    return search_properties(MOCK_PROPERTIES, filters)
