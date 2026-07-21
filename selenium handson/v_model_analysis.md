# HANDS-ON 2 -- SDLC vs TDLC -- V-Model & Agile QA Integration

## Task 1: V-Model Mapping

``` text
Requirements ---------> Acceptance Testing
System Design --------> System Testing
Architecture Design --> Integration Testing
Module Design --------> Unit Testing
          Coding
```

## SDLC ↔ TDLC Mapping

  SDLC                  TDLC                  Artifact
  --------------------- --------------------- ----------------------------------
  Requirements          Acceptance Testing    Acceptance Test Plan
  System Design         System Testing        System Test Cases
  Architecture Design   Integration Testing   Integration Test Plan
  Module Design         Unit Testing          Unit Test Cases
  Coding                Test Execution        Source Code & Automation Scripts

## Entry & Exit Criteria

### Unit Testing

-   Entry: Module completed, unit test cases ready.
-   Exit: All unit tests passed, critical defects fixed.

### Integration Testing

-   Entry: Modules integrated, integration tests ready.
-   Exit: Interfaces verified, no major defects.

### System Testing

-   Entry: Full application integrated.
-   Exit: Functional and non-functional tests completed with no critical
    defects.

### Acceptance Testing

-   Entry: System testing completed and UAT environment ready.
-   Exit: Customer approval received.

## Early QA Engagement

-   Review requirements for clarity and testability.
-   Review API/system design before coding.

# Task 2: Agile QA & Shift-Left

## Waterfall Problems

1.  Late defect detection.
2.  Higher cost of fixing bugs.
3.  Delayed software release.

## QA in Agile

-   Sprint Planning: Define acceptance criteria.
-   Daily Standup: Report blockers.
-   Sprint Review: Validate completed features.
-   Sprint Retrospective: Improve processes.

## Shift-Left Practices

-   Requirement reviews
-   TDD/BDD
-   Static code analysis
-   API contract testing

## Acceptance Criteria (Given--When--Then)

### Scenario 1

**Given** valid course details\
**When** the admin creates a course\
**Then** the course is created successfully.

### Scenario 2

**Given** a duplicate course code\
**When** the admin submits the form\
**Then** an error message is displayed.

### Scenario 3

**Given** required fields are empty\
**When** the admin submits the form\
**Then** validation messages are displayed and the course is not
created.
