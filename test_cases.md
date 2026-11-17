
# API and Database Automation Testing

## Project Overview

This project contains automated API and database tests using Python, Pytest, Requests, and SQLite.

## API Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| API-01 | Get valid user | Status 200 |
| API-02 | Get invalid user | Status 404 |
| API-03 | Create new user | Status 201 |
| API-04 | Update existing user | Status 200 |
| API-05 | Partially update user | Status 200 |
| API-06 | Delete user | Status 200 |
| API-07 | Check API response time | Under 3 seconds |
| API-08 | Validate response structure | Required fields present |
| API-09 | Create user with invalid email | Demo API returns submitted email |
| API-10 | Create user without name | Demo API accepts missing name |

## Database Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| DB-01 | Verify user record | Record does not exist after deletion |
| DB-02 | Check user count | Count is zero or more |
| DB-03 | Update user age | Age updates to 25 |
| DB-04 | Delete user | Record is deleted |
| DB-05 | Insert NULL name | Database rejects NULL |
| DB-06 | Insert duplicate email | Database rejects duplicate |

## Tools and Technologies

- Python
- Pytest
- Requests
- SQLite
- SQL
- HTML Test Reports

## Test Execution

Run all tests:

python -m pytest -v

Generate HTML report:

python -m pytest -v --html=reports/full_report.html --self-contained-html
