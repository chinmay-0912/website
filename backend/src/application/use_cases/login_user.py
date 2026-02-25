# backend/src/application/use_cases/login_user.py

from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.infrastructure.security.password_hasher import PasswordHasher
from backend.src.infrastructure.security.jwt_service import JWTService
from backend.src.domain.exceptions import InvalidCredentialsException


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
        user = self.user_repository.get_by_email(email)

        if not user:
            raise InvalidCredentialsException("Invalid email or password")

        # 2️⃣ Verify password
        is_valid = self.password_hasher.verify(
            plain_password=password,
            hashed_password=user.password
        )

        if not is_valid:
            raise InvalidCredentialsException("Invalid email or password")

        # 3️⃣ Generate JWT token
        token = self.jwt_service.create_token(user.id)

        return token