
import sqlite3
import pytest


@pytest.fixture
def db_connection(tmp_path):

    db_path = tmp_path / "test_database.db"
    connection = sqlite3.connect(db_path)

    connection.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )
    """)

    yield connection

    connection.close()


def test_user_exists_in_database(db_connection):

    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Test User", "test@example.com", 22)
    )

    user = db_connection.execute(
        "SELECT * FROM users WHERE email = ?",
        ("test@example.com",)
    ).fetchone()

    assert user is not None
    assert user[1] == "Test User"
    assert user[2] == "test@example.com"
    assert user[3] == 22


def test_user_count(db_connection):

    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Test User", "test@example.com", 22)
    )

    count = db_connection.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    assert count == 1


def test_update_user_age(db_connection):

    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Test User", "test@example.com", 22)
    )

    db_connection.execute(
        "UPDATE users SET age = ? WHERE email = ?",
        (25, "test@example.com")
    )

    age = db_connection.execute(
        "SELECT age FROM users WHERE email = ?",
        ("test@example.com",)
    ).fetchone()[0]

    assert age == 25


def test_delete_user(db_connection):

    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Test User", "test@example.com", 22)
    )

    db_connection.execute(
        "DELETE FROM users WHERE email = ?",
        ("test@example.com",)
    )

    user = db_connection.execute(
        "SELECT * FROM users WHERE email = ?",
        ("test@example.com",)
    ).fetchone()

    assert user is None


def test_name_not_null_constraint(db_connection):

    with pytest.raises(sqlite3.IntegrityError):

        db_connection.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (None, "invalid@example.com", 22)
        )


def test_duplicate_email_constraint(db_connection):

    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("First User", "duplicate@example.com", 22)
    )

    with pytest.raises(sqlite3.IntegrityError):

        db_connection.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Second User", "duplicate@example.com", 25)
        )
