# backend/src/application/use_cases/login_user.py

from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.infrastructure.security.password_hasher import PasswordHasher
from backend.src.infrastructure.security.jwt_service import JWTService
from backend.src.domain.exceptions import InvalidCredentialsException
from backend.src.domain.value_objects.email import Email


class LoginUser:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        jwt_service: JWTService,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.jwt_service = jwt_service

    def execute(self, email: str, password: str) -> str:
        # 1️⃣ Find user by email
        email_vo = Email(email)
        print(f"DEBUG: Looking up user by email: {email}")  # Debug log
        user = self.user_repository.get_by_email(email_vo)
        print(f"DEBUG: User found for email {email}: {user}")  # Debug log

        if not user:
            raise InvalidCredentialsException("Invalid email or password")

        # 2️⃣ Verify password
        is_valid = self.password_hasher.verify(
            plain_password=password,
            password_hash=user.password_hash
        )

        if not is_valid:
            raise InvalidCredentialsException("Invalid email or password")

        # 3️⃣ Generate JWT token
        token = self.jwt_service.create_token(str(user.id))

        return token