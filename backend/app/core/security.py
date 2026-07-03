from datetime import datetime, timedelta
import jwt

SECRET_KEY = "CHANGE_ME"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
