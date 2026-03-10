# Test Specification Implementation

Replace test templates with actual test cases using specific values and expected results.

## ADDED Requirements

### Requirement: Test Case Structure

All test.md files SHALL follow a consistent structure with specific test case IDs.

#### Scenario: Test case has unique ID

- **WHEN** a test case is created
- **THEN** it SHALL have an ID in format TC-{MODULE}-{NNN} (e.g., TC-ORDER-001)

#### Scenario: Test case has type classification

- **WHEN** a test case is created
- **THEN** it SHALL be classified as Positive, Negative, or Edge case

### Requirement: Test Case Input Specification

Each test case SHALL specify exact input values for all relevant fields.

#### Scenario: Test input has specific values

- **WHEN** a test case specifies input for New Order Single
- **THEN** it SHALL include specific values like Symbol=CU, Side=1, OrderQty=10, OrdType=2, Price=8500.00

#### Scenario: Test input uses valid reference data

- **WHEN** a test case uses symbol values
- **THEN** the symbols SHALL be from the official LME symbol list in `openspec/reference/symbols.md`

### Requirement: Test Case Expected Output

Each test case SHALL specify the expected output or behavior.

#### Scenario: Expected response documented

- **WHEN** a positive test case for order submission is created
- **THEN** it SHALL specify expected ExecType=0 (New) and OrdStatus=0 (New)

#### Scenario: Expected rejection documented

- **WHEN** a negative test case for invalid order is created
- **THEN** it SHALL specify expected rejection reason code (e.g., OrdRejReason=1 for unknown symbol)

### Requirement: Preconditions Documentation

Each test case SHALL document any preconditions required for execution.

#### Scenario: Session preconditions

- **WHEN** a test case requires an authenticated session
- **THEN** the test case SHALL document "Precondition: Valid FIX session established"

#### Scenario: Market state preconditions

- **WHEN** a test case requires market to be open
- **THEN** the test case SHALL document "Precondition: Market in Open state"

### Requirement: Module Test Coverage

Each module's test.md SHALL include test cases covering:

#### Scenario: Happy path coverage

- **WHEN** test.md for order-management is reviewed
- **THEN** it SHALL include positive test cases for order submission, modification, and cancellation

#### Scenario: Error path coverage

- **WHEN** test.md for order-management is reviewed
- **THEN** it SHALL include negative test cases for invalid inputs, missing fields, and business rule violations

#### Scenario: Boundary coverage

- **WHEN** test.md for order-management is reviewed
- **THEN** it SHALL include edge cases for minimum/maximum quantities, boundary prices
