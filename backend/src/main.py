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

    # CORS (for frontend connection later)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # tighten in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
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