from collections.abc import Generator
from pathlib import Path
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


DATABASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATABASE_PATH = DATABASE_DIR / "student_tasks.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DATABASE_PATH.as_posix()}")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
