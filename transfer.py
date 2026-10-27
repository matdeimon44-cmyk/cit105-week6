import sqlite3

conn = sqlite3.connect("kanban.db")

conn.execute("""
INSERT OR IGNORE INTO cards
(id, board_id, title, description, status)
SELECT id, 1, title, COALESCE(description, ''), status
FROM tasks
""")

conn.commit()

count = conn.execute(
    "SELECT COUNT(*) FROM cards"
).fetchone()[0]

print("Cards migrated:", count)

conn.close()