# Message Handlers Specification

Defines the specification for message handlers that process trading messages according to specification and generate predicted responses.

## ADDED Requirements

### Requirement: Handler Implementation Per Message Type
Each message type SHALL have a dedicated handler implementing business logic from specifications.

#### Scenario: Handler registration
- **WHEN** handler module is loaded
- **THEN** handler is registered in MESSAGE registry with its message type

#### Scenario: Handler implements specification logic
- **WHEN** NewOrderSingle handler receives valid order request
- **THEN** handler validates parameters, creates order, updates state, and returns predicted response

### Requirement: Input Parameter Validation
Handlers SHALL validate input parameters against specification constraints before processing.

#### Scenario: Valid parameters accepted
- **WHEN** handler receives parameters within valid ranges
- **THEN** handler processes message normally

#### Scenario: Invalid parameters rejected
- **WHEN** handler receives parameters outside valid ranges (e.g., negative quantity)
- **THEN** handler returns rejection response with reason

### Requirement: Internal State Updates
Handlers SHALL update internal state based on message processing results.

#### Scenario: Order creation updates state
- **WHEN** NewOrderSingle handler creates order successfully
- **THEN** internal state includes new order in orders dict and orderbook

#### Scenario: Order fill updates position
- **WHEN** ExecutionReport indicates fill
- **THEN** internal state updates position quantity and positions dict

### Requirement: Multiple Predicted Responses
Handlers SHALL return list of predicted responses (0 or more) to support scenarios like partial fills.

#### Scenario: Single response for immediate fill
- **WHEN** market order matches completely
- **THEN** handler returns single ExecutionReport with FILLED status

#### Scenario: Multiple responses for partial fills
- **WHEN** limit order matches partially multiple times
- **THEN** handler returns multiple ExecutionReports, each with partial fill details

### Requirement: Stateless Handler Execution
Handlers SHALL be stateless with no side effects beyond internal state updates.

#### Scenario: Handler produces no external calls
- **WHEN** handler executes
- **THEN** no network calls, file I/O, or external service interactions occur

#### Scenario: Handler depends only on passed state
- **WHEN** handler receives state object
- **THEN** handler modifies only the state copy (not external state)

### Requirement: Deterministic Handler Behavior
Handlers SHALL be deterministic - same input plus same internal state SHALL produce same output.

#### Scenario: Reproducible handler results
- **WHEN** handler is called twice with identical parameters and state
- **THEN** both calls return identical response

#### Scenario: Different state produces different results
- **WHEN** handler is called with same parameters but different state (e.g., different orderbook)
- **THEN** responses may differ (e.g., different fill prices)

### Requirement: Response ID Generation
Handlers SHALL generate unique IDs for orders, executions, and other entities.

#### Scenario: Order ID generation
- **WHEN** handler creates new order
- **THEN** order_id is unique and follows sequential pattern

#### Scenario: Execution ID generation
- **WHEN** handler generates fill response
- **THEN** exec_id is unique per fill

### Requirement: Business Rule Enforcement
Handlers SHALL enforce all business rules from specification including validation rules, price band constraints, and order matching logic.

#### Scenario: Price band enforcement
- **WHEN** order price exceeds price band limits
- **THEN** handler rejects order with PRICE_OUT_OF_BAND reason

#### Scenario: Order matching enforcement
- **WHEN** limit order is submitted against existing orderbook
- **THEN** handler matches against opposite side orders and price/time priority
