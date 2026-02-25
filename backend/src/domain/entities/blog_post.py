from dataclasses import dataclass
from datetime import datetime


@dataclass
class BlogPost:
    id: int | None
    title: str
    content: str
    author_id: int
    created_at: datetime

    @classmethod
    def create(cls, title: str, content: str, author_id: int):
        return cls(
            id=None,
            title=title,
            content=content,
            author_id=author_id,
            created_at=datetime.utcnow(),
        )