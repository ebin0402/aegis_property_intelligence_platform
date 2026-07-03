from fastapi import APIRouter

router = APIRouter()

SAVED = []

@router.post("/")
def save_property(item: dict):
    SAVED.append(item)
    return {"status": "saved"}

@router.get("/")
def get_saved():
    return SAVED
