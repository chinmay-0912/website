from sqlalchemy.orm import Session
from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.domain.entities.user import User
from backend.src.domain.value_objects.email import Email
from backend.src.infrastructure.database.models import BlogModel
from backend.src.infrastructure.database.models import UserModel
from uuid import UUID
from datetime import datetime, timezone


class PostgresUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: Email):
        db_user = (
            self.db.query(UserModel)
            .filter(UserModel.email == email.value)
            .first()
        )

        if not db_user:
            return None

        return User.from_orm(
            id=db_user.id,
            email=Email(db_user.email),
            name=db_user.name,
            hashed_password=db_user.password_hash,
            created_at=db_user.created_at,
            reset_token=db_user.reset_token,
            reset_token_expiry=db_user.reset_token_expiry
        )

    def save(self, user: User):
        db_user = UserModel(
            id=user.id,
            email=user.email.value,
            name="New User",
            password_hash=user.password_hash
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

    def get_by_id(self, user_id: UUID) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            return None

        return User.from_orm(
            id=db_user.id,
            email=Email(db_user.email),
            name=db_user.name,
            hashed_password=db_user.password_hash,
            created_at=db_user.created_at,
            reset_token=db_user.reset_token,
            reset_token_expiry=db_user.reset_token_expiry
        )

    def update(self, user: object) -> object:
        db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        if not db_user:
            raise ValueError("User not found")

        if user.name is not None:
            db_user.name = user.name
        if user.password_hash is not None:
            db_user.password_hash = user.password_hash

        self.db.commit()
        self.db.refresh(db_user)

        return User.from_orm(
            id=db_user.id,
            email=Email(db_user.email),
            name=db_user.name,
            hashed_password=db_user.password_hash,
            created_at=db_user.created_at
        )

    def get_blog_count(self, user_id: int) -> int:
        return self.db.query(BlogModel).filter(BlogModel.author_id == user_id).count()

    # ⭐ NEW METHODS — password reset infra

    def save_password_reset_token(self, user_id: UUID, token: str, expiry: datetime):
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            raise ValueError("User not found")

        db_user.reset_token = token
        db_user.reset_token_expiry = expiry

        self.db.commit()
        self.db.refresh(db_user)

    def get_user_by_reset_token(self, token: str) -> User | None:
        db_user = (
            self.db.query(UserModel)
            .filter(UserModel.reset_token == token)
            .first()
        )

        if not db_user:
            return None

        return User.from_orm(
            id=db_user.id,
            email=Email(db_user.email),
            name=db_user.name,
            hashed_password=db_user.password_hash,
            created_at=db_user.created_at,
            reset_token=db_user.reset_token,
            reset_token_expiry=db_user.reset_token_expiry.replace(tzinfo=timezone.utc)
        )

    def clear_password_reset_token(self, user_id: UUID):
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            return

        db_user.reset_token = None
        db_user.reset_token_expiry = None
        self.db.commit()