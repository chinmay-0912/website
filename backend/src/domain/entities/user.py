from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from backend.src.domain.value_objects.email import Email


@dataclass(eq=False)
class User:
    _id: UUID = field(repr=False)
    email: Email
    password_hash: str
    created_at: datetime

    @property
    def id(self) -> UUID:
        return self._id

    @classmethod
    def create(cls, email: Email, password_hash: str) -> "User":
        return cls(
            _id=uuid4(),
            email=email,
            password_hash=password_hash,
            created_at=datetime.now(tz=timezone.utc),
        )

    @classmethod
    def from_orm(cls, id, email: Email, hashed_password: str, created_at):
        return cls(
            _id=id,
            email=email,
            password_hash=hashed_password,
            created_at=created_at
        )

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id
