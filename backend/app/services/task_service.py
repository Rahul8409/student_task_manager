from sqlalchemy.orm import Session

from backend.app.models.task import StudentTask
from backend.app.repositories import task_repository
from backend.app.schemas.task import StudentTaskCreate, StudentTaskUpdate


def create_task(db: Session, task: StudentTaskCreate) -> StudentTask:
    return task_repository.create_task(db, task)


def get_tasks(db: Session) -> list[StudentTask]:
    return task_repository.get_tasks(db)


def get_task(db: Session, task_id: int) -> StudentTask | None:
    return task_repository.get_task(db, task_id)


def update_task(
    db: Session,
    task_id: int,
    task_update: StudentTaskUpdate,
) -> StudentTask | None:
    return task_repository.update_task(db, task_id, task_update)


def delete_task(db: Session, task_id: int) -> bool:
    return task_repository.delete_task(db, task_id)
