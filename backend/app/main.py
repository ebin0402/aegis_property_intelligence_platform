from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="AEGIS Property Intelligence API")

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "AEGIS Backend Running"}
