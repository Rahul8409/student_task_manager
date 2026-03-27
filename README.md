# Student Task Management System

This is a simple FastAPI CRUD project for managing student tasks.

## Features

- Create a student task
- Get all tasks
- Get a single task by ID
- Update a task
- Delete a task

## Run the project

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

- `POST /tasks/`
- `GET /tasks/`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Example request body

```json
{
  "student_name": "Rahul",
  "title": "Math Assignment",
  "description": "Complete chapter 5 exercises",
  "due_date": "2026-03-30",
  "completed": false
}
```
