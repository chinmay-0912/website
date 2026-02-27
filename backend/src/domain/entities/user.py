from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional
from backend.src.domain.value_objects.email import Email


@dataclass(eq=False)
class User:
    _id: UUID = field(repr=False)
    email: Email
    name: str
    password_hash: str
    created_at: datetime
    reset_token: Optional[str] = None
    reset_token_expiry: Optional[datetime] = None

    @property
    def id(self) -> UUID:
        return self._id

    @classmethod
    def create(cls, email: Email, name: str, password_hash: str) -> "User":
        return cls(
            _id=uuid4(),
            email=email,
            name=name,
            password_hash=password_hash,
            created_at=datetime.now(tz=timezone.utc),
            reset_token=None,
            reset_token_expiry=None,
        )

    @classmethod
    def from_orm(
        cls,
        id,
        email: Email,
        name: str,
        hashed_password: str,
        created_at,
        reset_token: Optional[str] = None,
        reset_token_expiry: Optional[datetime] = None,
    ):
        return cls(
            _id=id,
            email=email,
            name=name,
            password_hash=hashed_password,
            created_at=created_at,
            reset_token=reset_token,
            reset_token_expiry=reset_token_expiry,
        )

    def set_reset_token(self, token: str, expiry: datetime):
        self.reset_token = token
        self.reset_token_expiry = expiry

    def clear_reset_token(self):
        self.reset_token = None
        self.reset_token_expiry = None

    def is_reset_token_valid(self, token: str) -> bool:
        if self.reset_token != token:
            return False
        if self.reset_token_expiry is None:
            return False
        return self.reset_token_expiry > datetime.now(tz=timezone.utc)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id