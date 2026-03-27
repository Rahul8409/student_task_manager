from sqlalchemy import Boolean, Column, Date, Integer, String, Text

from database.connection import Base


class StudentTask(Base):
    __tablename__ = "student_tasks"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(100), nullable=False, index=True)
    title = Column(String(150), nullable=False, index=True)
    description = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
