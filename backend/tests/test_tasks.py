def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={
            "student_name": "Asha",
            "title": "Science Project",
            "description": "Build a solar system model",
            "due_date": "2026-04-01",
            "completed": False,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["student_name"] == "Asha"
    assert data["title"] == "Science Project"
    assert data["completed"] is False


def test_get_all_tasks(client):
    client.post(
        "/tasks/",
        json={
            "student_name": "Asha",
            "title": "Science Project",
            "description": "Build a solar system model",
            "due_date": "2026-04-01",
            "completed": False,
        },
    )

    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["student_name"] == "Asha"


def test_get_single_task(client):
    create_response = client.post(
        "/tasks/",
        json={
            "student_name": "Ravi",
            "title": "English Essay",
            "description": "Write about climate change",
            "due_date": "2026-04-02",
            "completed": False,
        },
    )

    task_id = create_response.json()["id"]
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "English Essay"
    assert data["student_name"] == "Ravi"


def test_update_task(client):
    create_response = client.post(
        "/tasks/",
        json={
            "student_name": "Neha",
            "title": "History Homework",
            "description": "Read chapter 3",
            "due_date": "2026-04-03",
            "completed": False,
        },
    )

    task_id = create_response.json()["id"]
    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "History Homework Updated",
            "completed": True,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "History Homework Updated"
    assert data["completed"] is True
    assert data["student_name"] == "Neha"


def test_delete_task(client):
    create_response = client.post(
        "/tasks/",
        json={
            "student_name": "Kiran",
            "title": "Computer Lab",
            "description": "Practice Python basics",
            "due_date": "2026-04-04",
            "completed": False,
        },
    )

    task_id = create_response.json()["id"]
    delete_response = client.delete(f"/tasks/{task_id}")
    get_response = client.get(f"/tasks/{task_id}")

    assert delete_response.status_code == 204
    assert get_response.status_code == 404


def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
