from fastapi import APIRouter, Depends, Response, HTTPException
from pydantic import BaseModel

# Infrastructure / DB
from backend.src.infrastructure.database.session import get_db
from backend.src.infrastructure.repositories.postgres_user_repository import PostgresUserRepository
from backend.src.infrastructure.security.jwt_service import JWTService
from backend.src.infrastructure.security.password_hasher import PasswordHasher

# Application / Use Cases
from backend.src.application.use_cases.login_user import LoginUser
from backend.src.application.use_cases.register_user import RegisterUser
from backend.src.application.use_cases.update_user_profile import UpdateUserProfile
from backend.src.application.use_cases.request_password_reset import RequestPasswordResetUseCase
from backend.src.application.use_cases.reset_password import ResetPasswordUseCase

# Dependencies
from backend.src.api.dependencies import get_current_user

router = APIRouter()


# --- Request Schemas ---

class RegisterRequest(BaseModel):
    email: str
    name: str
    password: str


class UpdateNameRequest(BaseModel):
    name: str


class UpdatePasswordRequest(BaseModel):
    old_password: str
    new_password: str

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


# --- Use Case Factories ---

def get_user_repo(db=Depends(get_db)):
    return PostgresUserRepository(db)


def get_login_use_case(repo=Depends(get_user_repo)):
    return LoginUser(
        user_repository=repo,
        password_hasher=PasswordHasher(),
        jwt_service=JWTService()
    )


def get_register_use_case(repo=Depends(get_user_repo)):
    return RegisterUser(repo, PasswordHasher())


def get_update_user_use_case(repo=Depends(get_user_repo)):
    return UpdateUserProfile(repo)


# --- Routes ---

@router.post("/login")
def login(
        email: str,
        password: str,
        response: Response,
        login_use_case: LoginUser = Depends(get_login_use_case),
):
    try:
        token = login_use_case.execute(email=email, password=password)

        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,  # Set to True in Production (HTTPS)
            samesite="lax",
            max_age=60 * 60 * 24 * 7,
        )
        return {"message": "Login successful"}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/register")
def register(
        request: RegisterRequest,
        use_case: RegisterUser = Depends(get_register_use_case)
):
    try:
        user = use_case.execute(
            email=request.email,
            name=request.name,
            password=request.password
        )
        return {"message": "User registered successfully", "email": user.email.value}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    # Returns current identity from the decoded token/session
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }


@router.get("/me_stats")
def get_me_stats(
        current_user=Depends(get_current_user),
        repo: PostgresUserRepository = Depends(get_user_repo)
):
    # Proper repository call instead of hardcoded logic
    count = repo.get_blog_count(current_user.id)
    return {"blog_count": count}


@router.patch("/update-name")
def update_name(
        request: UpdateNameRequest,
        current_user=Depends(get_current_user),
        use_case: UpdateUserProfile = Depends(get_update_user_use_case)
):
    try:
        updated_user = use_case.execute(user_id=current_user.id, new_name=request.name)
        return {"message": "Name updated successfully", "name": updated_user.name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/update-password")
def update_password(
        request: UpdatePasswordRequest,
        current_user=Depends(get_current_user),
        use_case: UpdateUserProfile = Depends(get_update_user_use_case)
):
    # Verify old password first
    hasher = PasswordHasher()
    if not hasher.verify(request.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect current password")

    try:
        new_hash = hasher.hash(request.new_password)
        use_case.execute(user_id=current_user.id, new_password_hash=new_hash)
        return {"message": "Password updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}

@router.post("/request-password-reset")
def request_password_reset(email: str, repo: PostgresUserRepository = Depends(get_user_repo)):
    try:
        usecase = RequestPasswordResetUseCase(repo)

        token = usecase.execute(email)

        # ⭐ For now return token (later send email)
        return {
            "message": "Reset link generated",
            "reset_link": f"http://localhost:3000/reset-password?token={token}"
        }

    except ValueError:
        # Do NOT reveal whether email exists (security best practice)
        return {"message": "If email exists, reset link sent"}

@router.patch("/reset-password")
def reset_password(
    request: ResetPasswordRequest,
    db=Depends(get_db),
):
    repo = PostgresUserRepository(db)
    hasher = PasswordHasher()
    use_case = ResetPasswordUseCase(repo, hasher)

    try:
        use_case.execute(token=request.token, new_password=request.new_password)
        return {"message": "Password reset successful"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))