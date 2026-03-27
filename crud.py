from sqlalchemy.orm import Session

import models
import schemas


def create_task(db: Session, task: schemas.StudentTaskCreate) -> models.StudentTask:
    db_task = models.StudentTask(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session) -> list[models.StudentTask]:
    return db.query(models.StudentTask).order_by(models.StudentTask.id).all()


def get_task(db: Session, task_id: int) -> models.StudentTask | None:
    return db.query(models.StudentTask).filter(models.StudentTask.id == task_id).first()


def update_task(
    db: Session, task_id: int, task_update: schemas.StudentTaskUpdate
) -> models.StudentTask | None:
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
