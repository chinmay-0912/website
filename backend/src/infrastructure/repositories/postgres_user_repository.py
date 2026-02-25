from sqlalchemy.orm import Session
from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.domain.entities.user import User
from backend.src.domain.value_objects.email import Email
from backend.src.infrastructure.database.models import UserModel


class PostgresUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: Email):
        """
        Retrieves a user by email synchronously.
        Returns None if not found, allowing the 'User already exists' check to pass.
        """
        print(f"DEBUG: Querying database for user with email: {email.value}")  # Debug log
        db_user = (
            self.db.query(UserModel)
            .filter(UserModel.email == email.value)
            .first()
        )
        print(f"DEBUG: Database query result for email {email.value}: {db_user.email} \nid: {db_user.id} \npassword:{db_user.password_hash}")  # Debug log

        if not db_user:
            return None

        # Corrected to use db_user.password_hash to match UserModel
        return User.from_orm(
            id=db_user.id,
            email=Email(db_user.email),
            hashed_password=db_user.password_hash,
            created_at=db_user.created_at
        )

    def save(self, user: User):
        """
        Persists a user entity to the database synchronously.
        """
        db_user = UserModel(
            id=user.id,
            email=user.email.value,
            name="New User",  # Included because UserModel requires a name field
            password_hash=user.password_hash  # Corrected field name
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)