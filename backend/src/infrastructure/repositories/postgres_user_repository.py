from sqlalchemy.orm import Session
from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.domain.entities.user import User
from backend.src.domain.value_objects.email import Email
from backend.src.infrastructure.database.models import UserModel


class PostgresUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    async def get_by_email(self, email: Email):
        db_user = (
            self.db.query(UserModel)
            .filter(UserModel.email == email.value)
            .first()
        )

        if not db_user:
            return None

        return User(
            id=db_user.id,
            email=Email(db_user.email),
            hashed_password=db_user.hashed_password
        )

    async def save(self, user: User):
        db_user = UserModel(
            id=user.id,
            email=user.email.value,
            hashed_password=user.hashed_password
        )

        self.db.add(db_user)
        self.db.commit()