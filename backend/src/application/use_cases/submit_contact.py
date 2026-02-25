from backend.src.domain.repositories.contact_repository import ContactRepository
from backend.src.domain.entities.contact import Contact
from backend.src.domain.exceptions import DomainError


class SubmitContact:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, name: str, email: str, message: str):
        if not name or not email or not message:
            raise DomainError("All fields are required")

        contact = Contact.create(
            name=name,
            email=email,
            message=message,
        )

        return self.contact_repository.save(contact)