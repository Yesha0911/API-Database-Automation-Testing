
import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()

# Remove old table
cursor.execute("DROP TABLE IF EXISTS users")

# Create new table with constraints
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER
)
""")

connection.commit()

print("Users Table Recreated Successfully!")
print("UNIQUE Email Constraint Added!")

connection.close()
