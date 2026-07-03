from fastapi import APIRouter

router = APIRouter()

MOCK_PROPERTIES = [
    {
        "id": 1,
        "title": "Modern Family Home",
        "price": 350000,
        "location": "Kent",
        "bedrooms": 3
    },
    {
        "id": 2,
        "title": "City Apartment",
        "price": 275000,
        "location": "London",
        "bedrooms": 2
    }
]

@router.get("/")
def list_properties():
    return MOCK_PROPERTIES

@router.get("/{property_id}")
def get_property(property_id: int):
    for p in MOCK_PROPERTIES:
        if p["id"] == property_id:
            return p
    return {"error": "Property not found"}
