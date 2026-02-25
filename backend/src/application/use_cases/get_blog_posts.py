# backend/src/application/use_cases/get_blog_posts.py

from backend.src.domain.repositories.blog_repository import BlogRepository


class GetBlogPosts:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    def execute(self):
        return self.blog_repository.get_all()