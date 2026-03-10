# Parameter Generators

Create state-aware parameter generators for order fields that respect symbol constraints and market state.

## ADDED Requirements

### Requirement: Symbol-Aware Quantity Generator

Quantity generator SHALL produce values within symbol's lot size constraints.

#### Scenario: Quantity is valid lot multiple

- **WHEN** a quantity is generated
- **THEN** it SHALL be a multiple of the symbol's lot size

#### Scenario: Quantity within max limit

- **WHEN** a quantity is generated
- **THEN** it SHALL not exceed 9,999 lots

#### Scenario: Quantity at least minimum

- **WHEN** a quantity is generated
- **THEN** it SHALL be at least 1 lot

### Requirement: Symbol-Aware Price Generator

Price generator SHALL produce values within symbol's price band.

#### Scenario: Price within band

- **WHEN** a price is generated
- **THEN** it SHALL be within the symbol's min_price and max_price

#### Scenario: Price is valid tick

- **WHEN** a price is generated
- **THEN** it SHALL be a multiple of the symbol's tick_size

### Requirement: Order Type Generator

Order type generator SHALL produce valid order types with matching required fields.

#### Scenario: Limit order has price

- **WHEN** a LIMIT order is generated
- **THEN** it SHALL include a Price field

#### Scenario: Stop order has StopPx

- **WHEN** a STOP order is generated
- **THEN** it SHALL include a StopPx field

#### Scenario: Stop-limit has both prices

- **WHEN** a STOP_LIMIT order is generated
- **THEN** it SHALL include both Price and StopPx fields

#### Scenario: Iceberg has DisplayQty

- **WHEN** an ICEBERG order is generated
- **THEN** it SHALL include DisplayQty field less than OrderQty

### Requirement: Symbol Selector

Symbol selector SHALL choose from configured LME symbols.

#### Scenario: Symbol from configured set

- **WHEN** a symbol is selected
- **THEN** it SHALL be one of: AL, CU, NI, ZN, PB, SN, AA, HN

#### Scenario: Symbol distribution

- **WHEN** multiple symbols are selected over time
- **THEN** distribution SHALL be roughly uniform across all symbols

### Requirement: Side Generator

Side generator SHALL produce valid buy/sell values.

#### Scenario: Side is valid

- **WHEN** a side is generated
- **THEN** it SHALL be either BUY (1) or SELL (2)

#### Scenario: Side distribution

- **WHEN** multiple sides are generated
- **THEN** distribution SHALL be roughly 50/50

### Requirement: ClOrdId Generator

ClOrdId generator SHALL produce unique identifiers.

#### Scenario: ClOrdId is unique

- **WHEN** a ClOrdId is generated
- **THEN** it SHALL be unique within the trading day

#### Scenario: ClOrdId format

- **WHEN** a ClOrdId is generated
- **THEN** it SHALL be a string of max 20 characters

### Requirement: State-Aware Generation

Generators SHALL be aware of current market state.

#### Scenario: Price near market

- **WHEN** a price is generated
- **THEN** it MAY be influenced by current orderbook state (near best bid/ask)

#### Scenario: Quantity respects position limits

- **WHEN** a quantity is generated for a user
- **THEN** it SHALL not cause position to exceed risk limits

### Requirement: Seedable Randomness

Generators SHALL support deterministic mode via seed.

#### Scenario: Seeded generation is reproducible

- **WHEN** generators are initialized with same seed
- **THEN** they SHALL produce identical sequences of values
