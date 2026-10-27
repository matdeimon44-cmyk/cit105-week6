import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "kanban.db"


def migrate():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'To Do'
                    CHECK (status IN ('To Do', 'In Progress', 'Done'))
            )
        """)

        conn.commit()

    print("SQLite database initialized successfully!")
    print(f"Database location: {DB_PATH}")


if __name__ == "__main__":
    migrate()