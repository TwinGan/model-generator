# Order State Transitions

Automatically transition order states based on fills (NEW → PARTIALLY_FILLED → FILLED) with validation.

## ADDED Requirements

### Requirement: Automatic State Transitions

Order states SHALL transition automatically based on fill events.

#### Scenario: New order stays NEW until filled

- **WHEN** a new order is submitted and not yet matched
- **THEN** order status SHALL remain NEW

#### Scenario: Partial fill transitions to PARTIALLY_FILLED

- **WHEN** an order receives a partial fill (fill_qty < order_qty)
- **THEN** order status SHALL transition to PARTIALLY_FILLED

#### Scenario: Full fill transitions to FILLED

- **WHEN** an order is completely filled (cum_qty == order_qty)
- **THEN** order status SHALL transition to FILLED

### Requirement: Transition Validation

State transitions SHALL be validated against the order state machine.

#### Scenario: Valid NEW to PARTIALLY_FILLED transition

- **WHEN** an order in NEW state receives a partial fill
- **THEN** the transition to PARTIALLY_FILLED SHALL be allowed

#### Scenario: Valid NEW to FILLED transition

- **WHEN** an order in NEW state receives a full fill
- **THEN** the transition to FILLED SHALL be allowed

#### Scenario: Valid PARTIALLY_FILLED to FILLED transition

- **WHEN** an order in PARTIALLY_FILLED state receives remaining fill
- **THEN** the transition to FILLED SHALL be allowed

#### Scenario: Terminal states cannot transition

- **WHEN** an order is in FILLED, CANCELLED, or REJECTED state
- **THEN** no further state transitions SHALL be allowed

### Requirement: Quantity Tracking Per State

Order quantities SHALL be accurately tracked through state transitions.

#### Scenario: LeavesQty updated on each fill

- **WHEN** an order receives a fill of Q
- **THEN** leaves_qty SHALL decrease by Q

#### Scenario: CumQty updated on each fill

- **WHEN** an order receives a fill of Q
- **THEN** cum_qty SHALL increase by Q

#### Scenario: LeavesQty zero when fully filled

- **WHEN** an order is fully filled
- **THEN** leaves_qty SHALL be 0

#### Scenario: CumQty equals order_qty when fully filled

- **WHEN** an order is fully filled
- **THEN** cum_qty SHALL equal the original order_qty

### Requirement: Multiple Fill Handling

Orders with multiple partial fills SHALL track state correctly.

#### Scenario: Track state across multiple partial fills

- **WHEN** an order receives fill 1, then fill 2, then fill 3
- **THEN** order state SHALL be PARTIALLY_FILLED after fill 1 and 2
- **AND** order state SHALL be FILLED after fill 3 (if fully filled)

#### Scenario: CumQty accumulates across fills

- **WHEN** an order has fills of 10, 15, and 5
- **THEN** cum_qty SHALL be 30

### Requirement: State Transition Events

State transitions SHALL be observable for test case generation.

#### Scenario: State change is recordable

- **WHEN** an order state transitions
- **THEN** the transition event SHALL be available for coverage tracking

#### Scenario: Transition includes timestamp

- **WHEN** an order state transitions
- **THEN** the update_time SHALL be set to current timestamp
