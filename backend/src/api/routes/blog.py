from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.src.infrastructure.database.session import get_db
from backend.src.api.dependencies import get_current_user
from backend.src.application.use_cases.create_blog import CreateBlog
from backend.src.application.use_cases.get_blog_posts import GetBlogPosts
from backend.src.infrastructure.repositories.postgres_blog_repository import PostgresBlogRepository

router = APIRouter()


# ---- Request Model ----
class BlogCreateRequest(BaseModel):
    title: str
    content: str


# ---- Public: Get All Blogs ----
@router.get("/")
def list_blogs(db: Session = Depends(get_db)):
    repo = PostgresBlogRepository(db)
    use_case = GetBlogPosts(repo)
    return use_case.execute()


# ---- Protected: Create Blog ----
@router.post("/")
def create_blog(
    data: BlogCreateRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    repo = PostgresBlogRepository(db)
    use_case = CreateBlog(repo)

    return use_case.execute(
        title=data.title,
        content=data.content,
        author_id=current_user.id,
    )