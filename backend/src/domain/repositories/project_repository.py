from abc import ABC, abstractmethod
from backend.src.domain.entities.project import Project


class ProjectRepository(ABC):

    @abstractmethod
    def save(self, project: Project):
        pass

    @abstractmethod
    def get_all(self):
        pass