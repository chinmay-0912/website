from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass
class Project:
    id: int | None
    title: str
    description: str
    link: str
    owner_id: UUID
    created_at: datetime

    @classmethod
    def create(cls, title: str, description: str, link: str, owner_id: UUID):
        return cls(
            id=None,
            title=title,
            description=description,
            link=link,
            owner_id=owner_id,
            created_at=datetime.utcnow(),
        )