import os
from pathlib import Path


class Settings:
    app_name = "Student Task Management System"
    backend_root = Path(__file__).resolve().parents[2]
    frontend_origins = [
        origin.strip()
        for origin in os.getenv(
            "FRONTEND_ORIGINS",
            "http://localhost:5173,http://127.0.0.1:5173",
        ).split(",")
        if origin.strip()
    ]


settings = Settings()
