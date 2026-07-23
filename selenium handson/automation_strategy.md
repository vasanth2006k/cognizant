# HANDS-ON 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### Five Criteria

1.  Repetitive execution
2.  Regression testing
3.  High-risk features
4.  Stable requirements
5.  Data-driven scenarios

**Scenario:** POST /api/courses returns HTTP 201. Decision: **Automate**
because it is repetitive, critical, stable, regression, and data-driven.

### Manual vs Automate

  Test                  Decision   Reason
  --------------------- ---------- -----------------------------
  CRUD Regression       Automate   Repeated every release
  Exploratory Testing   Manual     Needs human intuition
  Performance Test      Automate   Load tools required
  Login Form            Automate   Frequently executed
  Swagger Check         Manual     Simple documentation review
  Smoke Test            Automate   Runs after deployment

### Automation ROI

-   Automation: 4 hours
-   Manual: 30 min/run
-   Break-even: **8 runs**
-   After 10th run add 20% maintenance.

### Flaky Test

A flaky test passes/fails inconsistently. Example: Selenium login
without waits. Prevention: Explicit waits, stable locators, remove hard
sleeps.

# Task 2: Framework Types

## Linear

Simple sequential scripts. - Advantage: Easy - Disadvantage: Hard to
maintain

## Modular

Reusable modules. - Advantage: Reusable - Disadvantage: Initial effort

## Data-Driven

External test data. - Advantage: Multiple datasets - Disadvantage: Data
management

## Keyword-Driven

Keyword-based actions. - Advantage: Non-programmers can contribute -
Disadvantage: Complex setup

## Hybrid

Combination of Modular + Data-Driven + Keyword. - Advantage: Flexible
and scalable - Disadvantage: Higher setup cost

## Recommendation

Use a **Hybrid Framework** for the Course Management system.

## Folder Structure

\``text CourseManagementFramework/ ├── testcases/ ├── pages/ ├── testdata/ ├── utilities/ ├── config/ ├── reports/ ├── screenshots/ └── drivers/`
