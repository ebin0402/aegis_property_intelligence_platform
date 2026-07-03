from fastapi import APIRouter
from app.api.routes import properties, ai, users, saved

api_router = APIRouter()

api_router.include_router(properties.router, prefix="/properties", tags=["properties"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(saved.router, prefix="/saved", tags=["saved"])
