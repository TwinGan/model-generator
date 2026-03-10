# Trade Execution

Generate fills when orders match, including partial fills, with proper fill price and quantity calculations.

## ADDED Requirements

### Requirement: Trade Data Structure

Each executed trade SHALL be represented with complete trade details.

#### Scenario: Trade contains required fields

- **WHEN** a trade is executed
- **THEN** it SHALL include: trade_id, symbol, fill_qty, fill_price, aggressor_order_id, passive_order_id, aggressor_user_id, passive_user_id, timestamp

#### Scenario: Trade has unique identifier

- **WHEN** a trade is created
- **THEN** it SHALL have a unique trade_id

#### Scenario: Trade timestamps are recorded

- **WHEN** a trade is executed
- **THEN** it SHALL include the exact timestamp of execution

### Requirement: Fill Quantity Calculation

Fill quantities SHALL be calculated correctly based on order sizes.

#### Scenario: Fill quantity is minimum of order quantities

- **WHEN** aggressor order has qty A and passive order has qty P
- **THEN** fill quantity SHALL be min(A, P)

#### Scenario: Remaining quantity tracked for aggressor

- **WHEN** an aggressor order is partially filled
- **THEN** remaining_qty SHALL equal original_qty - sum_of_fill_quantities

#### Scenario: Cumulative quantity tracked for each order

- **WHEN** an order has multiple fills
- **THEN** cum_qty SHALL equal sum of all fill quantities for that order

### Requirement: Fill Price Determination

Fill prices SHALL be determined consistently per LME rules.

#### Scenario: Passive price used for fills

- **WHEN** a trade is executed
- **THEN** fill_price SHALL be the passive order's limit price

#### Scenario: All fills at same price level use same price

- **WHEN** multiple fills occur at the same price level
- **THEN** all fills SHALL have the same fill_price

### Requirement: Trade Generation Timing

Trades SHALL be generated at the appropriate point in the matching cycle.

#### Scenario: Trade generated immediately on match

- **WHEN** a crossing condition is detected
- **THEN** a trade SHALL be generated immediately

#### Scenario: Multiple trades for single aggressor

- **WHEN** an aggressor order matches multiple passive orders
- **THEN** a separate trade SHALL be generated for each passive order matched

### Requirement: Trade Identifier Generation

Trade identifiers SHALL be unique and traceable.

#### Scenario: Trade ID format

- **WHEN** a trade ID is generated
- **THEN** it SHALL follow format TRD{NNNNNN} (e.g., TRD000001)

#### Scenario: Trade IDs are sequential

- **WHEN** multiple trades are generated
- **THEN** trade IDs SHALL be sequential within a session

### Requirement: Aggressor and Passive Attribution

Each trade SHALL correctly identify aggressor and passive parties.

#### Scenario: Aggressor is the incoming order

- **WHEN** a new order triggers a match
- **THEN** the new order SHALL be marked as aggressor

#### Scenario: Passive is the resting order

- **WHEN** a new order matches an existing book order
- **THEN** the book order SHALL be marked as passive

#### Scenario: Both parties recorded in trade

- **WHEN** a trade is executed
- **THEN** both aggressor_user_id and passive_user_id SHALL be recorded
