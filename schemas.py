from datetime import date

from pydantic import BaseModel, Field


class StudentTaskBase(BaseModel):
    student_name: str = Field(..., min_length=1, max_length=100)
    title: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    due_date: date | None = None
    completed: bool = False


class StudentTaskCreate(StudentTaskBase):
    pass


class StudentTaskUpdate(BaseModel):
    student_name: str | None = Field(default=None, min_length=1, max_length=100)
    title: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = None
    due_date: date | None = None
    completed: bool | None = None


class StudentTaskResponse(StudentTaskBase):
    id: int

    class Config:
        from_attributes = True
