import sqlite3

conn = sqlite3.connect("budget.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT,
    description TEXT,
    category TEXT,
    amount REAL
)
""")

conn.commit()
conn.close()
