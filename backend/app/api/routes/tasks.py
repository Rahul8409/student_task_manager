from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.services import task_service
from backend.app.schemas.task import StudentTaskCreate, StudentTaskResponse, StudentTaskUpdate
from database.connection import get_db


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "/",
    response_model=StudentTaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student_task(
    task: StudentTaskCreate,
    db: Session = Depends(get_db),
) -> StudentTaskResponse:
    return task_service.create_task(db, task)


@router.get("/", response_model=list[StudentTaskResponse])
def read_all_tasks(db: Session = Depends(get_db)) -> list[StudentTaskResponse]:
    return task_service.get_tasks(db)


@router.get("/{task_id}", response_model=StudentTaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)) -> StudentTaskResponse:
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=StudentTaskResponse)
def update_student_task(
    task_id: int,
    task_update: StudentTaskUpdate,
    db: Session = Depends(get_db),
) -> StudentTaskResponse:
    updated_task = task_service.update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_task(task_id: int, db: Session = Depends(get_db)) -> None:
    deleted = task_service.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
