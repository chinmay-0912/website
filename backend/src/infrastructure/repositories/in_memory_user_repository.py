from __future__ import annotations

from typing import Dict
from uuid import UUID

from backend.src.domain.entities.user import User
from backend.src.domain.repositories.user_repository import UserRepository
from backend.src.domain.value_objects.email import Email


class InMemoryUserRepository(UserRepository):
    """
    In-memory implementation of UserRepository.

    Intended for:
    - Unit testing
    - Local development
    - Simple runtime demos

    NOT intended for production persistence.
    """

    def __init__(self) -> None:
        # Primary storage indexed by user ID
        self._users_by_id: Dict[UUID, User] = {}

        # Secondary index for fast email lookup
        self._users_by_email: Dict[str, User] = {}

    # =========================
    # Write Operations
    # =========================

    def save(self, user: User) -> None:
        """
        Persist a user entity in memory.
        Overwrites existing user with same ID.
        """

        self._users_by_id[user.id] = user
        self._users_by_email[user.email.value] = user

    # =========================
    # Read Operations
    # =========================

    def get_by_id(self, user_id: UUID) -> User | None:
        """
        Retrieve a user by its unique identifier.
        Returns None if not found.
        """
        return self._users_by_id.get(user_id)

    def get_by_email(self, email: Email) -> User | None:
        """
        Retrieve a user by email value object.
        Returns None if not found.
        """
        return self._users_by_email.get(email.value)

    # =========================
    # Utility (Optional)
    # =========================

    def list_all(self) -> list[User]:
        """
        Return all users (primarily for debugging/testing).
        """
        return list(self._users_by_id.values())