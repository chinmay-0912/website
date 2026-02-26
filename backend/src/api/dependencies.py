from fastapi import Request, HTTPException, Depends
from backend.src.infrastructure.security.jwt_service import JWTService
from backend.src.infrastructure.database.session import get_db
from sqlalchemy.orm import Session
from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.infrastructure.repositories.postgres_user_repository import PostgresUserRepository

def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    jwt_service = JWTService()

    try:
        payload = jwt_service.verify_token(token)
        user_id = payload["sub"]

        user_repo = PostgresUserRepository(db)
        user = user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")