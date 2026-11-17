
import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER
)
""")

connection.commit()
connection.close()

print("Database is ready!")
print("Users table created or already exists.")
