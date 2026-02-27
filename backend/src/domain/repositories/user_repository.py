from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime
from uuid import UUID

from backend.src.domain.entities.user import User
from backend.src.domain.value_objects.email import Email


class UserRepository(ABC):
    """
    Repository contract for User aggregate.
    Infrastructure layer will implement this.
    """

    @abstractmethod
    def get_by_email(self, email: Email) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[object]:
        pass

    @abstractmethod
    def update(self, user: object) -> object:
        pass

    @abstractmethod
    def get_blog_count(self, user_id: int) -> int:
        pass

    @abstractmethod
    def save_password_reset_token(
        self,
        user_id: UUID,
        token: str,
        expiry: datetime,
    ) -> None:
        pass

    @abstractmethod
    def get_user_by_reset_token(self, token: str) -> Optional[User]:
        pass

    @abstractmethod
    def clear_password_reset_token(self, user_id: UUID) -> None:
        pass