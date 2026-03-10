## Context

The digital twin test case generator (`digital_twin/`) generates SEND/RECEIVE message pairs but currently lacks a matching engine to simulate actual trade execution. The existing architecture includes:

- `DigitalTwinState`: Maintains symbols, users, members, orderbooks, orders, positions
- `Orderbook`: Contains bids and asks sorted by price-time priority
- `Order`: Tracks order state, fills, remaining quantity
- `Position`: Tracks user positions by symbol
- `TestCaseGenerator`: Orchestrates test case generation

The matching engine is a new layer that processes submitted orders and generates fills based on price-time priority matching, similar to how LMEselect operates.

### Current Flow

```
Generator → MessageHandler → State Update → CSV Output
```

### Target Flow

```
Generator → MessageHandler → MatchingEngine → Fill Generation → State Update → Execution Reports → CSV Output
```

### Constraints

- Must integrate with existing `DigitalTwinState` and `Orderbook` classes
- Should support multiple matching modes (LMEselect, TOM, Ring)
- Must generate FIX-compliant Execution Report (35=8) messages
- No external dependencies beyond standard library
- Performance should handle 1000+ orders per test run

## Goals / Non-Goals

**Goals:**

1. **Order book matching**: Implement price-time priority matching algorithm
2. **Trade execution**: Generate fills with proper price/quantity calculations
3. **Position management**: Track and update positions based on trades
4. **State transitions**: Automatically transition order states (NEW → PARTIALLY_FILLED → FILLED)
5. **Execution reports**: Generate realistic FIX Execution Report messages
6. **Matching modes**: Support LMEselect, TOM, and Ring matching modes

**Non-Goals:**

- Real-time low-latency matching (this is a test case generator, not production exchange)
- FIX session management (handled separately)
- Order routing/smart order routing
- Cross matching (internalization)
- Market making obligations

## Decisions

### Decision 1: Matching Engine Module Structure

**Decision**: Create `digital_twin/matching/` as a new subpackage with separate modules for each concern.

**Rationale**:
- Separation of concerns: order book, matching, positions, trade generation
- Easier to test individual components
- Allows different matching modes to coexist
- Clear module boundaries for future extension

**Alternatives Considered**:
- Single `matching.py` file → Rejected: Would become too large
- Add matching logic to `Orderbook` class → Rejected: Violates single responsibility principle

**Structure**:
```
digital_twin/matching/
├── __init__.py
├── engine.py          # Main MatchingEngine class
├── order_book.py      # OrderBookManager (wraps existing Orderbook)
├── trade.py           # Trade/Fill generation
├── positions.py       # PositionTracker
└── modes.py           # MatchingMode implementations
```

### Decision 2: Price-Time Priority Algorithm

**Decision**: Implement standard price-time priority (first-in-first-out for same price level).

**Rationale**:
- LMEselect uses price-time priority
- Simple to implement and understand
- Deterministic behavior for test reproducibility
- Standard approach used by most electronic exchanges

**Algorithm**:
1. For each new/aggressing order:
   - Check if it crosses best opposite side
   - Match at passive order's price
   - Time priority for same-price orders
2. Continue matching until no more crosses or order is fully filled

### Decision 3: Fill Generation Strategy

**Decision**: Generate fills immediately when orders cross, with partial fill support.

**Rationale**:
- Matches real exchange behavior
- Allows testing of partial fill scenarios
- Enables position tracking per fill

**Implementation**:
- `Trade` dataclass with: fill_qty, fill_price, aggressor_order, passive_order, timestamp
- `FillGenerator` class to create `Trade` objects
- Support for both full and partial fills

### Decision 4: Position Tracking Approach

**Decision**: Extend existing `Position` class with real-time updates per fill.

**Rationale**:
- Existing `Position` class has `update_with_fill()` method
- Add average price calculation
- Track long/short positions per user per symbol
- Support position queries for risk checks

**Implementation**:
```python
class PositionTracker:
    def update_position(self, fill: Trade, state: DigitalTwinState) -> None:
        position = state.get_position(fill.user_id, fill.symbol)
        position.update_with_fill(fill.fill_qty, fill.fill_price)
```

### Decision 5: Execution Report Generation

**Decision**: Create `ExecutionReportGenerator` class that produces FIX Execution Report (35=8) messages.

**Rationale**:
- Separates message generation from matching logic
- Ensures FIX compliance
- Allows customization of report format

**Required Fields** (per FIX Spec):
- ClOrdID (11), OrderID (37), ExecID (17)
- ExecType (150), OrdStatus (39)
- Symbol (55), Side (54)
- LastQty (32), LastPx (31)
- LeavesQty (151), CumQty (14)
- TransactTime (60)

### Decision 6: Matching Mode Strategy

**Decision**: Use strategy pattern for different matching modes.

**Rationale**:
- LME has multiple venues (LMEselect, TOM, Ring)
- Each venue has different matching rules
- Strategy pattern allows easy extension

**Modes**:
- `LMEselectMode`: Continuous matching, immediate fills
- `TOMMode`: End-of-day batch matching
- `RingMode`: Open outcry simulation (periodic clearing)

## Risks / Trade-offs

### Risk 1: Performance with Large Order Books

**Risk**: Matching 1000+ orders may be slow with naive implementation.

**Mitigation**:
- Use sorted data structures (existing Orderbook already sorts)
- Batch matching operations
- Profile and optimize hot paths
- Limit order book depth in test scenarios

### Risk 2: State Consistency

**Risk**: Multiple updates to state may cause inconsistencies.

**Mitigation**:
- All state updates go through `DigitalTwinState` methods
- Use deepcopy pattern already established
- Atomic updates for fill + position + order state

### Risk 3: Non-Deterministic Test Cases

**Risk**: Random fills may make test cases non-reproducible.

**Mitigation**:
- Seeded random number generation (already in TestCaseGenerator)
- Deterministic matching algorithm (price-time priority is deterministic)
- Record matching decisions in test case metadata

### Risk 4: Complexity Creep

**Risk**: Matching engine may become too complex for a test generator.

**Mitigation**:
- Start with simple LMEselect mode only
- Add TOM and Ring modes as separate implementations
- Keep matching logic separate from business logic
- Focus on realistic behavior, not exchange-grade performance

## Migration Plan

### Phase 1: Core Matching (Low Risk)

1. Create `digital_twin/matching/` package structure
2. Implement `MatchingEngine` with basic price-time priority
3. Implement `FillGenerator` for immediate fills
4. Add unit tests for matching algorithm

### Phase 2: State Integration (Medium Risk)

1. Extend `Position` class methods if needed
2. Create `PositionTracker` wrapper
3. Integrate with `DigitalTwinState` updates
4. Add tests for state consistency

### Phase 3: Execution Reports (Low Risk)

1. Create `ExecutionReportGenerator`
2. Define FIX field mappings
3. Integrate with `CSVWriter`
4. Add tests for report generation

### Phase 4: Generator Integration (Medium Risk)

1. Update `TestCaseGenerator` to use `MatchingEngine`
2. Update test case generation flow
3. Verify end-to-end test generation
4. Add integration tests

### Phase 5: Advanced Modes (Future)

1. Implement `TOMMode`
2. Implement `RingMode`
3. Add mode selection in scenarios

### Rollback Strategy

- Each phase is a separate commit
- New package doesn't affect existing code until Phase 4
- Can disable matching engine with feature flag if issues found
- Revert to previous generator if needed

## Open Questions

1. **Fill Price Determination**: Should fills use aggressor price, passive price, or mid-price? LMEselect uses passive order price.

2. **Self-Match Prevention**: Should we implement self-match prevention (same user on both sides)? This is a regulatory requirement but adds complexity.

3. **Minimum Fill Quantity**: Should partial fills have a minimum quantity (e.g., 1 lot)?

4. **Order Book Snapshot**: Should we capture order book state at each step for debugging test cases?

5. **Trade Reporting**: Should we generate separate Trade Capture Report (35=AE) messages in addition to Execution Reports?
