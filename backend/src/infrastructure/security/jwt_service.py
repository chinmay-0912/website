from jose import jwt, JWTError
from datetime import datetime, timedelta
from backend.src.core.config import settings


class JWTService:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = "HS256"

    def create_token(self, user_id: str):
        payload = {
            "sub": str(user_id),
            "exp": datetime.utcnow() + timedelta(days=7),
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def verify_token(self, token: str):
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except JWTError:
            raise Exception("Invalid token")