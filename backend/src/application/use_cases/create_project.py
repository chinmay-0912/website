from backend.src.domain.repositories.project_repository import ProjectRepository
from backend.src.domain.entities.project import Project
from backend.src.domain.exceptions import DomainError
from uuid import UUID

class CreateProject:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, title: str, description: str, link: str, owner_id: UUID):
        if not title or not description:
            raise DomainError("Title and description are required")

        project = Project.create(
            title=title,
            description=description,
            link=link,
            owner_id=owner_id,
        )

        return self.project_repository.save(project)