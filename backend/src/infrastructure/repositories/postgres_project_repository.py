from backend.src.infrastructure.database.models import ProjectModel
from backend.src.domain.entities.project import Project


class PostgresProjectRepository:

    def __init__(self, db):
        self.db = db

    def save(self, project: Project):
        db_model = ProjectModel(
            title=project.title,
            description=project.description,
            link=project.link,
            owner_id=project.owner_id,
            created_at=project.created_at,
        )

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return Project(
            id=db_model.id,
            title=db_model.title,
            description=db_model.description,
            link=db_model.link,
            owner_id=db_model.owner_id,
            created_at=db_model.created_at,
        )

    def get_all(self):
        db_projects = self.db.query(ProjectModel).order_by(ProjectModel.created_at.desc()).all()

        return [
            Project(
                id=p.id,
                title=p.title,
                description=p.description,
                link=p.link,
                owner_id=p.owner_id,
                created_at=p.created_at,
            )
            for p in db_projects
        ]