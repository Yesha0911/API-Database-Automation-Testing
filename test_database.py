
import sqlite3
import pytest


def test_user_exists_in_database():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        ("test@example.com",)
    )

    user = cursor.fetchone()

    assert user is None

    connection.close()


def test_user_count():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")

    count = cursor.fetchone()[0]

    assert count >= 0

    connection.close()


def test_update_user_age():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, age)
        VALUES (?, ?, ?)
    """, ("Test User", "test@example.com", 22))

    connection.commit()

    cursor.execute(
        "UPDATE users SET age = ? WHERE email = ?",
        (25, "test@example.com")
    )

    connection.commit()

    cursor.execute(
        "SELECT age FROM users WHERE email = ?",
        ("test@example.com",)
    )

    updated_age = cursor.fetchone()[0]

    assert updated_age == 25

    connection.close()


def test_delete_user():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM users WHERE email = ?",
        ("test@example.com",)
    )

    connection.commit()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        ("test@example.com",)
    )

    user = cursor.fetchone()

    assert user is None

    connection.close()


def test_name_not_null_constraint():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    with pytest.raises(sqlite3.IntegrityError):

        cursor.execute("""
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?)
        """, (None, "invalid@example.com", 22))

    connection.close()


def test_duplicate_email_constraint():

    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, age)
        VALUES (?, ?, ?)
    """, ("First User", "duplicate@example.com", 22))

    connection.commit()

    with pytest.raises(sqlite3.IntegrityError):

        cursor.execute("""
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?)
        """, ("Second User", "duplicate@example.com", 25))

    connection.rollback()

    cursor.execute(
        "DELETE FROM users WHERE email = ?",
        ("duplicate@example.com",)
    )

    connection.commit()
    connection.close()

    print("Duplicate Email Constraint Test Passed!")
