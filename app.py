from flask import Flask, request, redirect, render_template_string
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).parent / "kanban.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                status TEXT NOT NULL DEFAULT 'To Do'
                    CHECK(status IN ('To Do', 'In Progress', 'Done'))
            )
        """)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Kanban Task Manager</title>
    <style>
        body {font-family: Arial; background: #f1f5f9; padding: 30px;}
        h1 {text-align: center; color: #1e293b;}
        form {margin: 12px 0;}
        input, select, button {padding: 10px; margin: 4px;}
        .board {display: flex; gap: 20px; margin-top: 30px;}
        .column {background: #e2e8f0; padding: 20px;
                 border-radius: 12px; flex: 1;}
        .task {background: white; padding: 15px;
               border-radius: 8px; margin: 12px 0;}
        button {background: #2563eb; color: white;
                border: none; border-radius: 5px; cursor: pointer;}
    </style>
</head>
<body>
    <h1>Kanban Task Manager</h1>
    <p style="text-align:center">Created by Matthew Espinel</p>

    <form action="/add" method="post">
        <input name="title" placeholder="Task title" required>
        <input name="description" placeholder="Description">
        <button type="submit">Add Task</button>
    </form>

    <div class="board">
    {% for status in statuses %}
        <div class="column">
            <h2>{{ status }}</h2>
            {% for task in tasks %}
                {% if task["status"] == status %}
                <div class="task">
                    <h3>{{ task["title"] }}</h3>
                    <p>{{ task["description"] }}</p>
                    <form action="/update/{{ task['id'] }}" method="post">
                        <select name="status">
                        {% for option in statuses %}
                            <option value="{{ option }}"
                            {% if option == task["status"] %}selected{% endif %}>
                                {{ option }}
                            </option>
                        {% endfor %}
                        </select>
                        <button type="submit">Update</button>
                    </form>
                    <form action="/delete/{{ task['id'] }}" method="post">
                        <button type="submit">Delete</button>
                    </form>
                </div>
                {% endif %}
            {% endfor %}
        </div>
    {% endfor %}
    </div>
</body>
</html>
"""

STATUSES = ["To Do", "In Progress", "Done"]

@app.route("/")
def index():
    with get_connection() as conn:
        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()
    return render_template_string(
        HTML, tasks=tasks, statuses=STATUSES
    )

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if title:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                (title, description)
            )
    return redirect("/")

@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    status = request.form.get("status")
    if status in STATUSES:
        with get_connection() as conn:
            conn.execute(
                "UPDATE tasks SET status = ? WHERE id = ?",
                (status, task_id)
            )
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect("/")

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)