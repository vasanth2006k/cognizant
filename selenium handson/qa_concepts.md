# HANDS-ON 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### 1. Testing Levels

#### Unit Testing

-   Test the `createCourse()` function independently.
-   **Expected Result:** Course is created only when all required fields
    are valid.

#### Integration Testing

-   Test the interaction between the `POST /api/courses` API endpoint
    and the database.
-   **Expected Result:** API stores the course successfully and returns
    **HTTP 201 Created**.

#### System Testing

-   Test the complete Course Management API workflow.
-   **Expected Result:** Course is created, stored, and displayed
    correctly.

#### User Acceptance Testing (UAT)

-   College administrator creates, edits, and deletes courses.
-   **Expected Result:** The application satisfies business
    requirements.

## 2. Functional vs Non-Functional Testing

  Test                  Type         Reason
  --------------------- ------------ ---------------------------------
  Unit Testing          Functional   Tests function correctness
  Integration Testing   Functional   Tests module interaction
  System Testing        Functional   Tests complete workflow
  UAT                   Functional   Validates business requirements

### Non-Functional Test Example

-   **Performance Testing**
-   Send 1000 concurrent requests to `/api/courses`.
-   **Expected Result:** Response time \< 2 seconds with no server
    failure.

## 3. Black-Box vs White-Box Testing

  Black-Box Testing          White-Box Testing
  -------------------------- --------------------------------
  No source code knowledge   Requires source code knowledge
  Performed by QA testers    Performed by developers
  Tests functionality        Tests internal logic

## 4. Formal Test Cases

  ----------------------------------------------------------------------------------------
  Test Case  Description   Preconditions   Test Steps  Expected     Actual     Pass/Fail
  ID                                                   Result       Result     
  ---------- ------------- --------------- ----------- ------------ ---------- -----------
  TC001      Create course API running     Send POST   HTTP 201                
             with valid                    request     Created                 
             data                                                              

  TC002      Create course API running     Send POST   HTTP 400 Bad            
             with empty                    request     Request                 
             name                                                              

  TC003      Create        Existing course Send        Duplicate               
             duplicate                     duplicate   rejected                
             course                        POST                                
                                           request                             
  ----------------------------------------------------------------------------------------

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

New → Assigned → Open → Fixed → Retest → Verified → Closed

Additional paths: - Rejected (Not a bug / Duplicate / Cannot
reproduce) - Deferred (Fix postponed to a later release)

## 6. Severity & Priority

### a) POST /api/courses returns HTTP 500

-   Severity: Critical
-   Priority: P1

### b) Course names \>150 characters are truncated

-   Severity: Medium
-   Priority: P3

### c) Swagger page has a typo

-   Severity: Low
-   Priority: P4

### d) Login occasionally returns HTTP 401

-   Severity: High
-   Priority: P2

## 7. Defect Report

  Field             Value
  ----------------- -------------------------------------
  Defect ID         BUG-001
  Title             POST /api/courses returns HTTP 500
  Environment       Windows 11, Chrome, FastAPI
  Build Version     v1.0
  Severity          Critical
  Priority          P1
  Steps             Send POST request to `/api/courses`
  Expected Result   HTTP 201 Created
  Actual Result     HTTP 500 Internal Server Error
  Attachments       Screenshot of HTTP 500

## 8. Severity vs Priority

**Severity** measures the impact of a defect on the application.

**Priority** measures how urgently the defect should be fixed.

### Example

A company logo is misaligned on the homepage during a product launch: -
Severity: Low - Priority: High
