## Why

The digital twin test case generator currently generates SEND/RECEIVE message pairs but lacks a matching engine to simulate actual trade execution. Without a matching engine:

1. Generated test cases cannot produce realistic fills
2. Order state transitions (NEW → PARTIALLY_FILLED → FILLED) cannot be simulated
3. Position updates cannot be generated
4. The digital twin produces "empty" test steps with no actual trading behavior

**Why now**: The `align-digital-twin-with-lme-requirements` change is establishing LME symbol data and validation rules. The matching engine is the next logical layer to enable realistic test case generation that simulates actual exchange behavior.

## What Changes

- **Order book matching**: Implement price-time priority matching algorithm for LMEselect-style order books
- **Trade execution**: Generate fills when orders match, with proper fill quantities and prices
- **Position management**: Update user positions based on executed trades
- **Multiple matching modes**: Support LMEselect (continuous), TOM (trade on close), and Ring (open outcry) matching
- **Order state transitions**: Automatically transition order states based on fills (NEW → PARTIALLY_FILLED → FILLED)
- **Execution Report generation**: Generate realistic Execution Report (35=8) messages with proper fill details

## Capabilities

### New Capabilities

- `order-book-matching`: Implement price-time priority matching algorithm that matches buy and sell orders when prices cross, with time priority for same-price orders
- `trade-execution`: Generate fills when orders match, including partial fills, with proper fill price and quantity calculations
- `position-management`: Track and update user positions (long/short) based on executed trades with average price calculation
- `order-state-transitions`: Automatically transition order states based on fills (NEW → PARTIALLY_FILLED → FILLED) with validation
- `execution-report-generation`: Generate FIX Execution Report (35=8) messages with ExecType, OrdStatus, LastQty, LastPx, LeavesQty, CumQty
- `matching-modes`: Support multiple LME matching modes (LMEselect continuous, TOM end-of-day, Ring open outcry)

### Modified Capabilities

- *(none - this is a new capability layer)*

## Impact

**Affected Files**:
- `digital_twin/matching/engine.py` (new) - Core matching engine
- `digital_twin/matching/order_book.py` (new) - Order book management
- `digital_twin/matching/trade.py` (new) - Trade/fill generation
- `digital_twin/matching/positions.py` (new) - Position tracking
- `digital_twin/matching/modes.py` (new) - Matching mode implementations
- `digital_twin/generator.py` - Integrate matching engine into generation flow
- `digital_twin/state.py` - May need position update methods
- `digital_twin/__init__.py` - Export new modules

**Dependencies**:
- Existing `DigitalTwinState`, `Orderbook`, `Order`, `Position` classes
- Existing `OrderStatus`, `OrderSide`, `ExecType` enums
- FIX Execution Report field definitions from constants.py

**Breaking Changes**: None - this is additive functionality
