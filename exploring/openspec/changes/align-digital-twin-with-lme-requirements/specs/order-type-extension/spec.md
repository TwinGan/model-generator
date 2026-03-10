# Order Type Extension

Add support for ICEBERG and POST_ONLY order types with appropriate validation rules.

## ADDED Requirements

### Requirement: ICEBERG Order Type Supported

The digital twin SHALL support ICEBERG order type for hidden quantity orders.

#### Scenario: Iceberg order accepted

- **WHEN** an order is submitted with OrdType=K (Iceberg)
- **THEN** the order SHALL be accepted if DisplayQty is provided

#### Scenario: Iceberg order requires DisplayQty

- **WHEN** an order is submitted with OrdType=K (Iceberg)
- **AND** DisplayQty is not provided
- **THEN** the order SHALL be rejected with reason INVALID_DISPLAY_QUANTITY

#### Scenario: Iceberg DisplayQty less than total quantity

- **WHEN** an ICEBERG order is submitted
- **THEN** DisplayQty SHALL be less than or equal to OrderQty

### Requirement: POST_ONLY Order Type Supported

The digital twin SHALL support POST_ONLY order type for maker-only orders.

#### Scenario: Post-only order accepted

- **WHEN** an order is submitted with OrdType=L (Post-Only)
- **THEN** the order SHALL be accepted if Price is provided

#### Scenario: Post-only order requires Limit

- **WHEN** a POST_ONLY order is submitted
- **THEN** it SHALL have a Price (acts as a limit order)

#### Scenario: Post-only rejected if would cross

- **WHEN** a POST_ONLY order would immediately match
- **THEN** the order SHALL be rejected (not take liquidity)

### Requirement: Order Type Enum Extended

The OrderType enum SHALL include all LME-supported order types.

#### Scenario: OrderType enum includes all types

- **WHEN** code references OrderType enum
- **THEN** it SHALL include: MARKET (1), LIMIT (2), STOP (3), STOP_LIMIT (4), ICEBERG (K), POST_ONLY (L)

### Requirement: Order Type Validation

Each order type SHALL have defined required and optional fields.

#### Scenario: Market order requires no price

- **WHEN** OrdType=1 (Market) is submitted
- **THEN** Price field SHALL NOT be required

#### Scenario: Limit order requires price

- **WHEN** OrdType=2 (Limit) is submitted
- **THEN** Price field SHALL be required

#### Scenario: Stop order requires StopPx

- **WHEN** OrdType=3 (Stop) is submitted
- **THEN** StopPx field SHALL be required

#### Scenario: Stop-limit order requires both prices

- **WHEN** OrdType=4 (Stop-Limit) is submitted
- **THEN** both Price and StopPx fields SHALL be required
