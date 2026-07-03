from fastapi import FastAPI
app = FastAPI(title="Aegis Core API")
@app.get("/")
def root(): return {"status": "healthy"}
