from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes.tasks import router as tasks_router
from backend.app.core.config import settings
from backend.app.models.task import StudentTask
from database.connection import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": f"{settings.app_name} API is running"}
