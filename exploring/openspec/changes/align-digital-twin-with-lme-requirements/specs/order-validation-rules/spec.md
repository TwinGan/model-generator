# Order Validation Rules

Implement LME order validation constraints including max quantity, max price, and conditional field requirements.

## ADDED Requirements

### Requirement: Maximum Order Quantity

Orders SHALL be validated against maximum quantity limits.

#### Scenario: Order quantity within limit

- **WHEN** an order is submitted with OrderQty <= 9,999 lots
- **THEN** the order SHALL pass quantity validation

#### Scenario: Order quantity exceeds limit

- **WHEN** an order is submitted with OrderQty > 9,999 lots
- **THEN** the order SHALL be rejected with reason EXCEEDS_MAXIMUM_QUANTITY

### Requirement: Minimum Order Quantity

Orders SHALL be validated against minimum quantity limits.

#### Scenario: Order quantity at minimum

- **WHEN** an order is submitted with OrderQty = 1 lot
- **THEN** the order SHALL pass quantity validation

#### Scenario: Order quantity below minimum

- **WHEN** an order is submitted with OrderQty < 1 lot
- **THEN** the order SHALL be rejected with reason INVALID_QUANTITY

### Requirement: Maximum Order Price

Orders SHALL be validated against maximum price limits.

#### Scenario: Order price within limit

- **WHEN** an order is submitted with Price <= 9,999,999
- **THEN** the order SHALL pass price validation

#### Scenario: Order price exceeds limit

- **WHEN** an order is submitted with Price > 9,999,999
- **THEN** the order SHALL be rejected with reason INVALID_PRICE

### Requirement: Price Tick Validation

Order prices SHALL be valid multiples of the symbol's tick size.

#### Scenario: Price is valid tick

- **WHEN** an order is submitted with Price that is a multiple of tick_size
- **THEN** the order SHALL pass tick validation

#### Scenario: Price is invalid tick

- **WHEN** an order is submitted with Price that is NOT a multiple of tick_size
- **THEN** the order SHALL be rejected with reason INVALID_PRICE

### Requirement: Conditional Field Requirements

Required fields SHALL be validated based on order type.

#### Scenario: Limit order missing price

- **WHEN** a LIMIT order is submitted without Price
- **THEN** the order SHALL be rejected with reason CONDITIONALLY_REQUIRED_FIELD_MISSING

#### Scenario: Stop order missing StopPx

- **WHEN** a STOP order is submitted without StopPx
- **THEN** the order SHALL be rejected with reason CONDITIONALLY_REQUIRED_FIELD_MISSING

#### Scenario: Iceberg order missing DisplayQty

- **WHEN** an ICEBERG order is submitted without DisplayQty
- **THEN** the order SHALL be rejected with reason INVALID_DISPLAY_QUANTITY

### Requirement: Symbol Validation

Orders SHALL be validated against known symbols.

#### Scenario: Order for valid symbol

- **WHEN** an order is submitted for a configured symbol
- **THEN** the order SHALL pass symbol validation

#### Scenario: Order for unknown symbol

- **WHEN** an order is submitted for an unconfigured symbol
- **THEN** the order SHALL be rejected with reason UNKNOWN_SYMBOL

### Requirement: Side Validation

Order side SHALL be a valid value.

#### Scenario: Order with valid side

- **WHEN** an order is submitted with Side=1 (Buy) or Side=2 (Sell)
- **THEN** the order SHALL pass side validation

#### Scenario: Order with invalid side

- **WHEN** an order is submitted with invalid Side value
- **THEN** the order SHALL be rejected with reason INVALID_SIDE
