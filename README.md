
# API and Database Automation Testing

An automated API and database testing project built using Python, Pytest, Requests, and SQLite.

This project validates REST API operations and database functionality through automated test cases.

## Project Overview

The project covers:

- REST API testing using Python Requests.
- GET, POST, PUT, PATCH, and DELETE operations.
- API status code and response validation.
- API response time testing.
- API response structure validation.
- Database CRUD operations.
- SQL constraint testing.
- Automated test execution using Pytest.
- HTML test reporting.

## Application Under Test

JSONPlaceholder Demo API:

https://jsonplaceholder.typicode.com/

## Technologies Used

- Python
- Pytest
- Requests
- SQLite
- SQL
- pytest-html
- VS Code
- Git and GitHub

## Project Structure

```text
Project-2-API-Database-Automation/
│
├── .venv/
├── reports/
│   ├── api_report.html
│   └── full_report.html
│
├── database.py
├── test_api.py
├── test_database.py
├── test_cases.md
├── bug_report.md
├── requirements.txt
└── README.md
```

## API Testing

The API test suite covers:

1. GET valid user.
2. GET invalid user.
3. POST create user.
4. PUT update user.
5. PATCH partial update.
6. DELETE user.
7. API response time validation.
8. API response structure validation.
9. Invalid email input behavior.
10. Missing name input behavior.

## Database Testing

The database test suite covers:

1. Verify user records.
2. Check user count.
3. Update user age.
4. Delete user.
5. NOT NULL constraint validation.
6. UNIQUE email constraint validation.

## Test Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

Generate HTML report:

```bash
python -m pytest -v --html=reports/full_report.html --self-contained-html
```

## Test Results

- API Test Cases: 10
- Database Test Cases: 6
- Total Automated Test Cases: 16
- Latest combined test execution: 16 passed

## Documentation

- `test_cases.md` – Test scenarios and expected results.
- `bug_report.md` – Observed API behavior and database constraint results.

## Important Note

JSONPlaceholder is a demo REST API. POST, PUT, PATCH, and DELETE operations simulate responses and do not permanently modify server-side data.

## Author

Yesha Shah

GitHub: https://github.com/Yesha0911
