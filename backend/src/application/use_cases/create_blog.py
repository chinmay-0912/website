# backend/src/application/use_cases/create_blog.py

from backend.src.domain.repositories.blog_repository import BlogRepository
from backend.src.domain.entities.blog_post import BlogPost
from backend.src.domain.exceptions import DomainError


class CreateBlog:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    def execute(self, title: str, content: str, author_id: int):
        if not title or not content:
            raise DomainError("Title and content are required")

        blog = BlogPost.create(
            title=title,
            content=content,
            author_id=author_id,
        )

        return self.blog_repository.save(blog)