from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.src.infrastructure.database.session import get_db
from backend.src.api.dependencies import get_current_user
from backend.src.application.use_cases.create_project import CreateProject
from backend.src.infrastructure.repositories.postgres_project_repository import PostgresProjectRepository

router = APIRouter()


class ProjectCreateRequest(BaseModel):
    title: str
    description: str
    link: str


# Public
@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    repo = PostgresProjectRepository(db)
    return repo.get_all()


# Protected
@router.post("/")
def create_project(
    data: ProjectCreateRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    repo = PostgresProjectRepository(db)
    use_case = CreateProject(repo)

    return use_case.execute(
        title=data.title,
        description=data.description,
        link=data.link,
        owner_id=current_user.id,
    )