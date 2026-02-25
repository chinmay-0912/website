from fastapi import APIRouter, Depends, Response, HTTPException
from backend.src.infrastructure.database.session import get_db
from backend.src.application.use_cases.login_user import LoginUser
from backend.src.infrastructure.security.jwt_service import JWTService
from backend.src.infrastructure.security.password_hasher import PasswordHasher
from backend.src.api.dependencies import get_current_user
from backend.src.infrastructure.repositories.postgres_user_repository import PostgresUserRepository
from pydantic import BaseModel
from backend.src.application.use_cases.register_user import RegisterUser

router = APIRouter()

def get_login_use_case(db=Depends(get_db)):

    user_repo = PostgresUserRepository(db)
    password_hasher = PasswordHasher()
    jwt_service = JWTService()

    return LoginUser(
        user_repository=user_repo,
        password_hasher=password_hasher,
        jwt_service=jwt_service
    )

class RegisterRequest(BaseModel):
    email: str
    password: str


def get_register_use_case(db=Depends(get_db)):
    user_repo = PostgresUserRepository(db)
    password_hasher = PasswordHasher()
    return RegisterUser(user_repo, password_hasher)


@router.post("/login")
def login(
    email: str,
    password: str,
    response: Response,
    login_use_case: LoginUser = Depends(get_login_use_case),
):
    print(f"DEBUG: Login attempt for email: {email} and password: {password}")
    try:
        token = login_use_case.execute(email=email, password=password)
        print(f"DEBUG: Login successful, generated token: {token}")

        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,  # True in prod
            samesite="lax",
            max_age=60 * 60 * 24 * 7,
        )
        print(f"DEBUG: Set cookie successful, generated cookie")
        return {"message": "Login successful"}

    except Exception:
        print(f"LOGIN ERROR: {Exception}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}


@router.post("/register")
def register(
    request: RegisterRequest,
    use_case: RegisterUser = Depends(get_register_use_case)
):
    try:
        user = use_case.execute(
            email=request.email,
            password=request.password
        )
        return {"message": "User registered successfully", "email": user.email.value}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))