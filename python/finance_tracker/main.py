import sqlite3

def add_transaction(date, desc, category, amount):
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions (date, description, category, amount)
    VALUES (?, ?, ?, ?)
    """, (date, desc, category, amount))

    connection.commit()
    connection.close()
