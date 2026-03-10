# Order State Machine

Add order state transition validation to ensure only valid state changes occur.

## ADDED Requirements

### Requirement: Order States Defined

The digital twin SHALL support all LME order lifecycle states.

#### Scenario: Order state enum includes all states

- **WHEN** code references OrderStatus enum
- **THEN** it SHALL include: NEW (0), PARTIALLY_FILLED (1), FILLED (2), CANCELLED (4), REPLACED (5), PENDING_CANCEL (6), REJECTED (8), EXPIRED (C), PENDING_REPLACE (E)

### Requirement: Valid State Transitions

Order state transitions SHALL follow the LME state machine.

#### Scenario: NEW to PARTIALLY_FILLED transition

- **WHEN** an order in NEW state receives a partial fill
- **THEN** the order state SHALL transition to PARTIALLY_FILLED

#### Scenario: NEW to FILLED transition

- **WHEN** an order in NEW state receives a complete fill
- **THEN** the order state SHALL transition to FILLED

#### Scenario: NEW to CANCELLED transition

- **WHEN** a cancel request is accepted for an order in NEW state
- **THEN** the order state SHALL transition to CANCELLED

#### Scenario: NEW to REJECTED transition

- **WHEN** an order in NEW state fails validation
- **THEN** the order state SHALL transition to REJECTED

#### Scenario: PARTIALLY_FILLED to FILLED transition

- **WHEN** an order in PARTIALLY_FILLED state receives remaining fill
- **THEN** the order state SHALL transition to FILLED

#### Scenario: PARTIALLY_FILLED to CANCELLED transition

- **WHEN** a cancel request is accepted for an order in PARTIALLY_FILLED state
- **THEN** the order state SHALL transition to CANCELLED

### Requirement: Invalid Transitions Rejected

Invalid state transitions SHALL be rejected.

#### Scenario: FILLED cannot transition

- **WHEN** a state transition is attempted on a FILLED order
- **THEN** the transition SHALL be rejected

#### Scenario: CANCELLED cannot transition

- **WHEN** a state transition is attempted on a CANCELLED order
- **THEN** the transition SHALL be rejected

#### Scenario: REJECTED cannot transition

- **WHEN** a state transition is attempted on a REJECTED order
- **THEN** the transition SHALL be rejected

### Requirement: State Transition Validation Function

A validation function SHALL check if transitions are valid.

#### Scenario: Validation function exists

- **WHEN** code needs to validate a state transition
- **THEN** a function `can_transition(current_state, target_state)` SHALL be available

#### Scenario: Validation returns boolean

- **WHEN** the validation function is called
- **THEN** it SHALL return True for valid transitions and False for invalid ones

### Requirement: Terminal States Identified

Terminal states SHALL be identifiable.

#### Scenario: Terminal states defined

- **WHEN** code checks if a state is terminal
- **THEN** FILLED, CANCELLED, REJECTED, and EXPIRED SHALL be identified as terminal states
