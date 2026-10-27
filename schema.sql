PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS boards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_id INTEGER NOT NULL,
    title TEXT NOT NULL CHECK(length(trim(title)) > 0),
    description TEXT DEFAULT '',
    status TEXT NOT NULL DEFAULT 'To Do'
        CHECK(status IN ('To Do', 'In Progress', 'Done')),
    priority TEXT NOT NULL DEFAULT 'Medium'
        CHECK(priority IN ('Low', 'Medium', 'High')),
    FOREIGN KEY (board_id)
        REFERENCES boards(id)
        ON DELETE CASCADE
);

INSERT OR IGNORE INTO boards (id, name)
VALUES (1, 'Kanban Task Manager');