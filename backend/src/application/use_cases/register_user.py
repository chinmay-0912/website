from backend.src.domain.entities.user import User
from backend.src.domain.value_objects.email import Email
from backend.src.domain.repositories.user_repository import UserRepository


class RegisterUser:
    def __init__(self, user_repo: UserRepository, password_hasher):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    def execute(self, email: str, name: str, password: str):
        email_vo = Email(email)

        existing_user = self.user_repo.get_by_email(email_vo)
        if existing_user:
            raise ValueError("User already exists")

        hashed_password = self.password_hasher.hash(password)

        user = User.create(
            email=email_vo,
            name=name,
            password_hash=hashed_password
        )

        self.user_repo.save(user)

        return user