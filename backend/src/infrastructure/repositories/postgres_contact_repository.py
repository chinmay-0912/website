from backend.src.infrastructure.database.models import ContactModel
from backend.src.domain.entities.contact import Contact


class PostgresContactRepository:

    def __init__(self, db):
        self.db = db

    def save(self, contact: Contact):
        db_model = ContactModel(
            name=contact.name,
            email=contact.email,
            message=contact.message,
            created_at=contact.created_at,
        )

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return Contact(
            id=db_model.id,
            name=db_model.name,
            email=db_model.email,
            message=db_model.message,
            created_at=db_model.created_at,
        )