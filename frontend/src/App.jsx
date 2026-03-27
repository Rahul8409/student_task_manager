import { useEffect, useState } from "react";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

const emptyForm = {
  student_name: "",
  title: "",
  description: "",
  due_date: "",
  completed: false
};

function App() {
  const [tasks, setTasks] = useState([]);
  const [formData, setFormData] = useState(emptyForm);
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchTasks();
  }, []);

  async function fetchTasks() {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_BASE_URL}/tasks/`);
      if (!response.ok) {
        throw new Error("Failed to load tasks");
      }

      const data = await response.json();
      setTasks(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  function handleChange(event) {
    const { name, value, type, checked } = event.target;
    setFormData((current) => ({
      ...current,
      [name]: type === "checkbox" ? checked : value
    }));
  }

  function resetForm() {
    setFormData(emptyForm);
    setEditingTaskId(null);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setSubmitting(true);
    setError("");

    const payload = {
      ...formData,
      due_date: formData.due_date || null
    };

    try {
      const url = editingTaskId
        ? `${API_BASE_URL}/tasks/${editingTaskId}`
        : `${API_BASE_URL}/tasks/`;

      const method = editingTaskId ? "PUT" : "POST";

      const response = await fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        throw new Error("Failed to save task");
      }

      await fetchTasks();
      resetForm();
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setSubmitting(false);
    }
  }

  function handleEdit(task) {
    setEditingTaskId(task.id);
    setFormData({
      student_name: task.student_name,
      title: task.title,
      description: task.description || "",
      due_date: task.due_date || "",
      completed: task.completed
    });
    setError("");
  }

  async function handleDelete(taskId) {
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
        method: "DELETE"
      });

      if (!response.ok) {
        throw new Error("Failed to delete task");
      }

      if (editingTaskId === taskId) {
        resetForm();
      }

      await fetchTasks();
    } catch (err) {
      setError(err.message || "Something went wrong");
    }
  }

  async function handleToggleComplete(task) {
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/${task.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          completed: !task.completed
        })
      });

      if (!response.ok) {
        throw new Error("Failed to update task");
      }

      await fetchTasks();
    } catch (err) {
      setError(err.message || "Something went wrong");
    }
  }

  return (
    <div className="page-shell">
      <div className="hero-panel">
        <p className="eyebrow">Student Task Management System</p>
        <h1>Track assignments, deadlines, and progress in one place.</h1>
        <p className="hero-copy">
          This React frontend connects to your FastAPI backend and supports full
          create, read, update, and delete operations for student tasks.
        </p>
      </div>

      <div className="content-grid">
        <section className="card">
          <div className="card-header">
            <h2>{editingTaskId ? "Edit Task" : "Create Task"}</h2>
            {editingTaskId ? (
              <button className="ghost-button" type="button" onClick={resetForm}>
                Cancel Edit
              </button>
            ) : null}
          </div>

          <form className="task-form" onSubmit={handleSubmit}>
            <label>
              Student Name
              <input
                name="student_name"
                value={formData.student_name}
                onChange={handleChange}
                placeholder="Enter student name"
                required
              />
            </label>

            <label>
              Task Title
              <input
                name="title"
                value={formData.title}
                onChange={handleChange}
                placeholder="Enter task title"
                required
              />
            </label>

            <label>
              Description
              <textarea
                name="description"
                value={formData.description}
                onChange={handleChange}
                placeholder="Enter task description"
                rows="4"
              />
            </label>

            <label>
              Due Date
              <input
                type="date"
                name="due_date"
                value={formData.due_date}
                onChange={handleChange}
              />
            </label>

            <label className="checkbox-row">
              <input
                type="checkbox"
                name="completed"
                checked={formData.completed}
                onChange={handleChange}
              />
              <span>Completed</span>
            </label>

            <button className="primary-button" type="submit" disabled={submitting}>
              {submitting
                ? "Saving..."
                : editingTaskId
                  ? "Update Task"
                  : "Create Task"}
            </button>
          </form>
        </section>

        <section className="card">
          <div className="card-header">
            <h2>All Tasks</h2>
            <button className="ghost-button" type="button" onClick={fetchTasks}>
              Refresh
            </button>
          </div>

          {error ? <p className="error-banner">{error}</p> : null}

          {loading ? (
            <p className="status-text">Loading tasks...</p>
          ) : tasks.length === 0 ? (
            <p className="status-text">No tasks yet. Create your first one.</p>
          ) : (
            <div className="task-list">
              {tasks.map((task) => (
                <article
                  key={task.id}
                  className={`task-item ${task.completed ? "task-complete" : ""}`}
                >
                  <div className="task-top">
                    <div>
                      <h3>{task.title}</h3>
                      <p className="student-name">{task.student_name}</p>
                    </div>
                    <span className={`badge ${task.completed ? "done" : "pending"}`}>
                      {task.completed ? "Completed" : "Pending"}
                    </span>
                  </div>

                  <p className="task-description">
                    {task.description || "No description added."}
                  </p>

                  <p className="due-date">
                    Due Date: {task.due_date || "Not set"}
                  </p>

                  <div className="task-actions">
                    <button
                      className="secondary-button"
                      type="button"
                      onClick={() => handleEdit(task)}
                    >
                      Edit
                    </button>
                    <button
                      className="secondary-button"
                      type="button"
                      onClick={() => handleToggleComplete(task)}
                    >
                      {task.completed ? "Mark Pending" : "Mark Complete"}
                    </button>
                    <button
                      className="danger-button"
                      type="button"
                      onClick={() => handleDelete(task.id)}
                    >
                      Delete
                    </button>
                  </div>
                </article>
              ))}
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;
