
import sqlite3
import pytest


@pytest.fixture
def db_connection(tmp_path):
    db_path = tmp_path / "qa_test.db"
    connection = sqlite3.connect(db_path)

    connection.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    connection.executemany(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        [
            (1, "Leanne Graham", "Sincere@april.biz"),            
            (2, "Priya", "priya@test.com"),
            (3, "Aman", "aman@test.com")
        ]
    )

    yield connection
    connection.close()


def test_user_count(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()

    assert result[0] == 3


def test_email_is_unique(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(DISTINCT email) FROM users"
    ).fetchone()

    assert result[0] == 3


def test_no_missing_user_names(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(*) FROM users WHERE name IS NULL"
    ).fetchone()

    assert result[0] == 0


import requests


def test_api_data_matches_database(db_connection):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    assert response.status_code == 200

    api_user = response.json()

    db_user = db_connection.execute(
        "SELECT id, name, email FROM users WHERE id = ?",
        (1,)
    ).fetchone()

    assert db_user is not None
    assert api_user["id"] == db_user[0]
    assert api_user["name"] == db_user[1]
    assert api_user["email"] == db_user[2]


def test_user_not_found(db_connection):
    result = db_connection.execute(
        "SELECT * FROM users WHERE id = ?",
        (999,)
    ).fetchone()

    assert result is None


def test_duplicate_email_not_allowed(db_connection):
    with pytest.raises(sqlite3.IntegrityError):
        db_connection.execute(
            "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
            (4, "Test User", "Sincere@april.biz")
        )
