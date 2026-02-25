from abc import ABC, abstractmethod
from typing import Optional
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
