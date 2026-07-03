@router.get("/properties")
def get_properties():
    return [
        {
            "id": 1,
            "title": "Kent House 1",
            "price": 250000,
            "lat": 51.27,
            "lng": 0.52,
            "deal_score": 78
        },
        {
            "id": 2,
            "title": "Kent House 2",
            "price": 320000,
            "lat": 51.35,
            "lng": 0.48,
            "deal_score": 82
        }
    ]
