
# Bug Report – API and Database Automation Testing

## Project Information

**Project:** API and Database Automation Testing

**Testing Type:** API Testing and Database Testing

**Tools:** Python, Pytest, Requests, SQLite

---

## Bug Report 1 – Invalid Email Accepted

**Bug ID:** BUG-001

**Module:** API – Create User

**Test Data:** invalid-email

**Steps to Reproduce:**
1. Send POST request to /users.
2. Provide an invalid email address.
3. Check the API response.

**Expected Result:**
The application should reject an invalid email address.

**Actual Result:**
JSONPlaceholder returned status code 201 and accepted the submitted email in its response.

**Status:** Observed limitation of demo API. Not a confirmed defect in a production application.

---

## Bug Report 2 – Missing Name Accepted

**Bug ID:** BUG-002

**Module:** API – Create User

**Steps to Reproduce:**
1. Send POST request to /users.
2. Exclude the name field.
3. Check the API response.

**Expected Result:**
The application should reject the request because name is a required field.

**Actual Result:**
JSONPlaceholder returned status code 201 without the name field.

**Status:** Observed limitation of demo API. Not a confirmed defect in a production application.

---

## Database Constraint Testing

**Test 1:** NULL name rejected successfully.

**Test 2:** Duplicate email rejected successfully.

Both database constraints behaved as expected.
