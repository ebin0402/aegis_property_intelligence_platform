from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def users():
    return [{"id": 1, "name": "Test User"}]
