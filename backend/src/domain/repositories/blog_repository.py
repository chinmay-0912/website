from abc import ABC, abstractmethod
from backend.src.domain.entities.blog_post import BlogPost


class BlogRepository(ABC):

    @abstractmethod
    def save(self, blog: BlogPost):
        pass

    @abstractmethod
    def get_all(self):
        pass