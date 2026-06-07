import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    department TEXT NOT NULL,
    designation TEXT NOT NULL
)
""")

conn.commit()

conn.close()

print("Database created successfully.")