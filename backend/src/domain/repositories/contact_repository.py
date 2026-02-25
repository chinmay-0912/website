from abc import ABC, abstractmethod
from backend.src.domain.entities.contact import Contact


class ContactRepository(ABC):

    @abstractmethod
    def save(self, contact: Contact):
        pass