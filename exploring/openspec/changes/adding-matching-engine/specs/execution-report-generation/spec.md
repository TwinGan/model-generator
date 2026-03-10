# Execution Report Generation

Generate FIX Execution Report (35=8) messages with ExecType, OrdStatus, LastQty, LastPx, LeavesQty, CumQty.

## ADDED Requirements

### Requirement: Execution Report Structure

Execution reports SHALL contain all required FIX fields.

#### Scenario: Report has core identification fields

- **WHEN** an execution report is generated
- **THEN** it SHALL include: ClOrdID (11), OrderID (37), ExecID (17), Symbol (55), Side (54)

#### Scenario: Report has execution details

- **WHEN** an execution report is generated for a fill
- **THEN** it SHALL include: ExecType (150), OrdStatus (39), LastQty (32), LastPx (31)

#### Scenario: Report has quantity tracking fields

- **WHEN** an execution report is generated
- **THEN** it SHALL include: LeavesQty (151), CumQty (14), OrderQty (38)

#### Scenario: Report has timestamp

- **WHEN** an execution report is generated
- **THEN** it SHALL include TransactTime (60)

### Requirement: ExecType Values

ExecType SHALL correctly indicate the type of execution event.

#### Scenario: ExecType NEW for order acknowledgment

- **WHEN** an order is acknowledged (before any fill)
- **THEN** ExecType SHALL be 0 (NEW)

#### Scenario: ExecType FILL for execution

- **WHEN** an order receives a fill
- **THEN** ExecType SHALL be 2 (FILL) or F (TRADE)

#### Scenario: ExecType CANCELED for cancellation

- **WHEN** an order is canceled
- **THEN** ExecType SHALL be 4 (CANCELED)

#### Scenario: ExecType REJECTED for rejection

- **WHEN** an order is rejected
- **THEN** ExecType SHALL be 8 (REJECTED)

### Requirement: OrdStatus Alignment

OrdStatus SHALL reflect the current order state.

#### Scenario: OrdStatus matches order state

- **WHEN** an execution report is generated
- **THEN** OrdStatus SHALL equal the order's current status

#### Scenario: OrdStatus NEW for new orders

- **WHEN** order status is NEW
- **THEN** OrdStatus SHALL be 0 (NEW)

#### Scenario: OrdStatus PARTIALLY_FILLED for partials

- **WHEN** order status is PARTIALLY_FILLED
- **THEN** OrdStatus SHALL be 1 (PARTIALLY_FILLED)

#### Scenario: OrdStatus FILLED for complete fills

- **WHEN** order status is FILLED
- **THEN** OrdStatus SHALL be 2 (FILLED)

### Requirement: Fill Quantity Fields

LastQty and LastPx SHALL reflect the specific fill, not cumulative.

#### Scenario: LastQty is fill quantity

- **WHEN** a fill of Q is executed
- **THEN** LastQty SHALL equal Q (not cumulative)

#### Scenario: LastPx is fill price

- **WHEN** a fill occurs at price P
- **THEN** LastPx SHALL equal P

#### Scenario: LastQty zero for non-fill reports

- **WHEN** an execution report is generated for NEW, CANCEL, REJECT
- **THEN** LastQty SHALL be 0 or omitted

### Requirement: Cumulative Quantity Fields

CumQty and LeavesQty SHALL reflect cumulative position.

#### Scenario: CumQty is total filled quantity

- **WHEN** an order has fills of 10, 15, and 5
- **THEN** CumQty in the third report SHALL be 30

#### Scenario: LeavesQty is remaining quantity

- **WHEN** an order for 50 has cum_qty of 30
- **THEN** LeavesQty SHALL be 20

#### Scenario: LeavesQty zero when fully filled

- **WHEN** an order is fully filled
- **THEN** LeavesQty SHALL be 0

### Requirement: ExecID Uniqueness

Each execution report SHALL have a unique ExecID.

#### Scenario: ExecID is unique per report

- **WHEN** multiple execution reports are generated
- **THEN** each SHALL have a unique ExecID

#### Scenario: ExecID format

- **WHEN** an ExecID is generated
- **THEN** it SHALL follow format EXEC{NNNNNN} (e.g., EXEC000001)

### Requirement: Execution Report Direction

Execution reports SHALL be marked as RECEIVE direction in test cases.

#### Scenario: Execution report is RECEIVE

- **WHEN** an execution report is added to test steps
- **THEN** direction SHALL be "receive"
