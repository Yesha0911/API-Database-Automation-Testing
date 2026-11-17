
import requests


def test_get_user():

    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["username"] == "Bret"


def test_invalid_user():

    url = "https://jsonplaceholder.typicode.com/users/999"
    response = requests.get(url)

    assert response.status_code == 404


def test_create_user():

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test User"
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"


def test_update_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    payload = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com"
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Updated User"
    assert data["username"] == "updateduser"
    assert data["email"] == "updated@example.com"


def test_patch_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    payload = {
        "name": "Patched User"
    }

    response = requests.patch(url, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Patched User"


def test_delete_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.delete(url)

    assert response.status_code == 200


def test_api_response_time():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3


def test_response_structure():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    required_fields = [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ]

    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    print("API Response Structure Validation Passed!")


def test_create_user_with_invalid_email():

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Test User",
        "username": "testuser",
        "email": "invalid-email"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "invalid-email"

    print("Invalid Email API Test Completed!")


def test_create_user_without_name():

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "username": "testuser",
        "email": "test@example.com"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert "name" not in data

    print("Missing Name API Test Completed!")
