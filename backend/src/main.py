from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from backend.src.api.routes.auth import router as auth_router
from backend.src.api.routes.blog import router as blog_router
from backend.src.api.routes.contact import router as contact_router
from backend.src.api.routes.projects import router as project_router


def create_application() -> FastAPI:
    app = FastAPI(
        title="Chinmay Portfolio API",
        description="Backend API for portfolio website",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://[::1]:3000"  # IPv6 support for Chrome
        ],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],  # Explicit list
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Authorization",
            "Accept",
        ],
    )


    # Health Check
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}

    # Register Routers
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])
    app.include_router(blog_router, prefix="/blogs", tags=["Blogs"])
    app.include_router(contact_router, prefix="/contact", tags=["Contact"])
    app.include_router(project_router, prefix="/projects", tags=["Projects"])

    return app


app = create_application()