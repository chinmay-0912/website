from backend.src.domain.repositories.blog_repository import BlogRepository
from backend.src.infrastructure.database.models import BlogModel
from backend.src.domain.entities.blog_post import BlogPost


class PostgresBlogRepository(BlogRepository):

    def __init__(self, db):
        self.db = db

    def get_all(self):
        db_blogs = self.db.query(BlogModel).all()

        return [
            BlogPost(
                id=b.id,
                title=b.title,
                content=b.content,
                author_id=b.author_id,
                created_at=b.created_at,
            )
            for b in db_blogs
        ]

    def save(self, blog: BlogPost):
        db_model = BlogModel(
            title=blog.title,
            content=blog.content,
            author_id=blog.author_id,
            created_at=blog.created_at,
        )

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model