from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.src.infrastructure.database.session import get_db
from backend.src.application.use_cases.submit_contact import SubmitContact
from backend.src.infrastructure.repositories.postgres_contact_repository import PostgresContactRepository

router = APIRouter()


class ContactRequest(BaseModel):
    name: str
    email: str
    message: str


@router.post("/")
def submit_contact(
    data: ContactRequest,
    db: Session = Depends(get_db),
):
    repo = PostgresContactRepository(db)
    use_case = SubmitContact(repo)

    return use_case.execute(
        name=data.name,
        email=data.email,
        message=data.message,
    )