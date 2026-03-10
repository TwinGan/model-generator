# Parameter Generators Specification

Defines the specification for parameter generators that create valid message parameters based on state and specification constraints.

## ADDED Requirements

### Requirement: Parameter Generation per Message Type
Each message type SHALL have a dedicated parameter generator that produces valid parameters.

#### Scenario: Generator registration
- **WHEN** generator module is loaded
- **THEN** generator is registered in generator registry with its message type

#### Scenario: Generator produces valid parameters
- **WHEN** NewOrderSingle generator is invoked with valid state
- **THEN** generator produces parameters with valid symbol, side, quantity, price

### Requirement: State-Aware Parameter Selection
Generators SHALL use current state to select valid parameter values (e.g., existing symbols, orderbook state).

#### Scenario: Symbol selection from state
- **WHEN** generator needs to select symbol
- **THEN** generator chooses from active symbols in current state

#### Scenario: Order ID selection for existing orders
- **WHEN** cancel request generator needs order_id
- **THEN** generator chooses from orders in current state

### Requirement: Boundary Value Testing Support
Generators SHALL support boundary value testing via configurable strategy with positive and negative testing weights.

#### Scenario: Positive boundary testing
- **WHEN** strategy specifies boundary_priority of 30%
- **THEN** 30% of generated parameters use boundary values (min/max quantity, min/max price)

#### Scenario: Negative testing for invalid parameters
- **WHEN** strategy specifies negative weight of 20%
- **THEN** 20% of generated parameters are intentionally invalid (negative quantity, zero price)

### Requirement: Parameter Dependency Resolution
Generators SHALL handle dependencies between parameters (e.g., cancel requires existing order ID, amend requires original cl_ord_id).

#### Scenario: Cancel references existing order
- **WHEN** OrderCancelRequest generator runs
- **THEN** orig_cl_ord_id references existing order's cl_ord_id

#### Scenario: Amend references original and new values
- **WHEN** OrderModifyRequest generator runs
- **THEN** orig_cl_ord_id references original order and new parameters differ from original

### Requirement: Weighted Random Selection
Generators SHALL support weighted random selection for parameter values.

#### Scenario: Weighted side selection
- **WHEN** config specifies BUY weight 60 and SELL weight 40
- **THEN** 60% of generated orders are BUY side

#### Scenario: Equal weights with no config
- **WHEN** no weights are configured
- **THEN** each value has equal probability of selection

### Requirement: JSON Serialization
All generated parameters SHALL be JSON-serializable for CSV output.

#### Scenario: Parameters serialize to JSON
- **WHEN** parameters are generated
- **THEN** parameters can be serialized to JSON without errors

#### Scenario: Complex nested parameters serialize
- **WHEN** parameters include nested objects (e.g., fill details)
- **THEN** JSON serialization preserves nested structure

### Requirement: Specification Range Enforcement
Generators SHALL respect parameter ranges from specification (min/max values, valid enums, tick sizes).

#### Scenario: Quantity within specification range
- **WHEN** specification defines quantity range as 1 to 1000
- **THEN** generated quantities fall within 1 to 1000 (unless negative testing)

#### Scenario: Price respects tick size
- **WHEN** specification defines tick size as 0.25
- **THEN** generated prices are multiples of 0.25

### Requirement: Precondition Validation
Generators SHALL ensure generated parameters satisfy message preconditions.

#### Scenario: Generated parameters pass preconditions
- **WHEN** parameters are generated for message
- **THEN** parameters satisfy all preconditions defined for that message type

#### Scenario: Retry on precondition failure
- **WHEN** generated parameters fail preconditions
- **THEN** generator retries with different parameters (up to max retries)
