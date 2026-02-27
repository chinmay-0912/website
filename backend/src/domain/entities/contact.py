from dataclasses import dataclass
from datetime import datetime


@dataclass
class Contact:
    id: int | None
    name: str
    email: str
    message: str
    created_at: datetime

    @classmethod
    def create(cls, name: str, email: str, message: str):
        return cls(
            id=None,
            name=name,
            email=email,
            message=message,
            created_at=datetime.utcnow(),
        )