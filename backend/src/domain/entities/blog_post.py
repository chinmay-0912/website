from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass
class BlogPost:
    id: int | None
    title: str
    content: str
    author_id: UUID
    created_at: datetime

    @classmethod
    def create(cls, title: str, content: str, author_id: UUID):
        return cls(
            id=None,
            title=title,
            content=content,
            author_id=author_id,
            created_at=datetime.utcnow(),
        )