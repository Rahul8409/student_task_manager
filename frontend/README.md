# Frontend

This is a React frontend for the Student Task Management System backend.

## Run the frontend

```bash
npm install
npm run dev
```

The app runs on `http://localhost:5173`.

## Backend

Start the FastAPI backend first:

```bash
uvicorn main:app --reload
```

The frontend expects the backend at `http://127.0.0.1:8000`.
