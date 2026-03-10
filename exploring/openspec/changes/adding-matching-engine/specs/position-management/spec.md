# Position Management

Track and update user positions (long/short) based on executed trades with average price calculation.

## ADDED Requirements

### Requirement: Position Tracking Per User Per Symbol

Positions SHALL be tracked for each user for each symbol traded.

#### Scenario: Position created on first trade

- **WHEN** a user executes their first trade in a symbol
- **THEN** a new position SHALL be created for that user/symbol combination

#### Scenario: Position key is user_id:symbol

- **WHEN** a position is stored
- **THEN** it SHALL be keyed by user_id and symbol

#### Scenario: Long position for buy fills

- **WHEN** a user's buy order is filled
- **THEN** the user's position SHALL increase (go long)

#### Scenario: Short position for sell fills

- **WHEN** a user's sell order is filled
- **THEN** the user's position SHALL decrease (go short)

### Requirement: Average Price Calculation

Position average price SHALL be calculated correctly for multiple fills.

#### Scenario: Average price for single fill

- **WHEN** a position has a single fill
- **THEN** avg_price SHALL equal the fill price

#### Scenario: Average price for multiple fills

- **WHEN** a position has multiple fills at different prices
- **THEN** avg_price SHALL equal weighted average: sum(qty * price) / sum(qty)

#### Scenario: Average price updated on each fill

- **WHEN** a new fill is executed for an existing position
- **THEN** avg_price SHALL be recalculated including the new fill

### Requirement: Position Side Determination

Position side (long/short) SHALL be determined by net position.

#### Scenario: Long position when net quantity positive

- **WHEN** total buy quantity > total sell quantity for a position
- **THEN** position side SHALL be LONG

#### Scenario: Short position when net quantity negative

- **WHEN** total sell quantity > total buy quantity for a position
- **THEN** position side SHALL be SHORT

#### Scenario: Flat position when net quantity zero

- **WHEN** total buy quantity == total sell quantity for a position
- **THEN** position side SHALL be FLAT (or closed)

### Requirement: Position Quantity Tracking

Position quantities SHALL accurately reflect all executed trades.

#### Scenario: Position quantity increases on buy

- **WHEN** a buy fill of Q is executed
- **THEN** position quantity SHALL increase by Q

#### Scenario: Position quantity decreases on sell

- **WHEN** a sell fill of Q is executed
- **THEN** position quantity SHALL decrease by Q

#### Scenario: Position reflects cumulative fills

- **WHEN** viewing a position
- **THEN** quantity SHALL equal sum of all buy fills minus sum of all sell fills

### Requirement: Position State Integration

Position updates SHALL integrate with DigitalTwinState.

#### Scenario: Position accessible from state

- **WHEN** code needs to check a position
- **THEN** it SHALL be retrievable via state.get_position(user_id, symbol)

#### Scenario: Position updates are atomic

- **WHEN** a trade is executed
- **THEN** position update SHALL happen atomically with order state update

#### Scenario: Position changes reflected in state

- **WHEN** a position is updated
- **THEN** the change SHALL be reflected in DigitalTwinState.positions dictionary

### Requirement: Realized PnL Not Required

Position tracking SHALL NOT include realized PnL calculation.

#### Scenario: No PnL tracking in initial implementation

- **WHEN** a position is closed (goes flat)
- **THEN** no PnL calculation is required for this change
