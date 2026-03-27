from sqlalchemy.orm import Session

from backend.app.models.task import StudentTask
from backend.app.schemas.task import StudentTaskCreate, StudentTaskUpdate


def create_task(db: Session, task: StudentTaskCreate) -> StudentTask:
    db_task = StudentTask(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session) -> list[StudentTask]:
    return db.query(StudentTask).order_by(StudentTask.id).all()


def get_task(db: Session, task_id: int) -> StudentTask | None:
    return db.query(StudentTask).filter(StudentTask.id == task_id).first()


def update_task(
    db: Session,
    task_id: int,
    task_update: StudentTaskUpdate,
) -> StudentTask | None:
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    db_task = get_task(db, task_id)
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()
    return True
