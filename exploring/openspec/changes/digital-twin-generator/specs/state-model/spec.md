# State Model Specification

Defines the specification for data structures representing trading system state.

## ADDED Requirements

### Requirement: Symbol Support
The state model SHALL support symbols representing options on futures contracts with complete definition.

#### Scenario: Load symbols from initial state
- **WHEN** initial state JSON contains symbol definitions
- **THEN** state model creates Symbol objects with all properties (symbol_id, instrument_type, underlying, strike_price, expiry, tick_size, lot_size, price_band, is_active)

#### Scenario: Access symbol by ID
- **WHEN** code requests symbol by symbol_id
- **THEN** state returns Symbol object or None if not found

### Requirement: User and Member Support
The state model SHALL support users (traders) and members (clearing organizations).

#### Scenario: Load users from initial state
- **WHEN** initial state JSON contains user definitions
- **THEN** state model creates User objects with properties (user_id, member_id, permissions, limits)

#### Scenario: Load members from initial state
- **WHEN** initial state JSON contains member definitions
- **THEN** state model creates Member objects with properties (member_id, name, risk_groups)

### Requirement: Orderbook Support
The state model SHALL support orderbooks with bid/ask spread per symbol.

#### Scenario: Access orderbook by symbol
- **WHEN** code requests orderbook for symbol
- **THEN** state returns Orderbook object with bids and asks sorted by price

#### Scenario: Orderbook updates on order creation
- **WHEN** new limit order is added
- **THEN** orderbook is updated with new price level

### Requirement: Order Support
The state model SHALL support orders with complete lifecycle (NEW, PARTIALLY_FILLED, FILLED, CANCELLED).

#### Scenario: Create new order
- **WHEN** order is created
- **THEN** state creates Order object with status NEW

#### Scenario: Update order status
- **WHEN** order status changes (e.g., to FILLED)
- **THEN** state updates Order object status and timestamp

### Requirement: Position Support
The state model SHALL support user positions by symbol with quantity and average price tracking.

#### Scenario: Access position by user and symbol
- **WHEN** code requests position for user_id and symbol
- **THEN** state returns Position object or creates new if not exists

#### Scenario: Update position on fill
- **WHEN** order fill occurs
- **THEN** position quantity and updated with fill details

### Requirement: Risk Group Support
The state model SHALL support risk groupings for risk management.

#### Scenario: Load risk groups from initial state
- **WHEN** initial state JSON contains risk group definitions
- **THEN** state model creates RiskGroup objects with properties (risk_group_id, members, limits)

#### Scenario: Access user's risk group
- **WHEN** code requests risk group for user
- **THEN** state returns RiskGroup based on user's member association

### Requirement: Price Band Support
The state model SHALL support price bands per symbol for price validation.

#### Scenario: Load price bands from initial state
- **WHEN** initial state JSON contains price band definitions
- **THEN** state model creates PriceBand objects with min_price, max_price, tick_size

#### Scenario: Validate price against band
- **WHEN** code checks if price is within band
- **THEN** state returns True if price >= min_price and price <= max_price

### Requirement: JSON Serialization
All state entities SHALL be JSON-serializable for persistence and initial state loading.

#### Scenario: Serialize state to JSON
- **WHEN** state is serialized to JSON
- **THEN** all entities (symbols, users, orders, etc.) are included with correct structure

#### Scenario: Deserialize state from JSON
- **WHEN** valid initial state JSON is loaded
- **THEN** state model creates all entities correctly

### Requirement: Deep Copy Support
The state model SHALL support deep copy for state preservation during test generation.

#### Scenario: Deep copy preserves state
- **WHEN** state is deep copied
- **THEN** modifications to copy do not affect original state

#### Scenario: Deep copy includes all nested objects
- **WHEN** state with nested objects (orderbook entries, positions) is deep copied
- **THEN** all nested objects are independently copied

### Requirement: Type-Safe State Access
The state model SHALL provide type-safe access methods for state entities.

#### Scenario: Type-safe symbol access
- **WHEN** code accesses symbol
- **THEN** return type is Symbol (not dict)

#### Scenario: Type-safe order access
- **WHEN** code accesses order
- **THEN** return type is Order (not dict)

### Requirement: Efficient State Lookups
The state model SHALL support efficient lookups and filtering of state entities.

#### Scenario: Lookup order by ID
- **WHEN** code looks up order by order_id
- **THEN** lookup completes in O(1) time

#### Scenario: Filter orders by status
- **WHEN** code filters orders by status (e.g., NEW)
- **THEN** filtered results returned efficiently without full state scan

### Requirement: No External Dependencies
State model classes SHALL have no external dependencies beyond Python standard library.

#### Scenario: State model imports only standard library
- **WHEN** state module is loaded
- **THEN** only dataclasses, typing, datetime, decimal, enum are imported

#### Scenario: State model is self-contained
- **WHEN** state model is used
- **THEN** no external packages (pandas, numpy, etc.) are required
