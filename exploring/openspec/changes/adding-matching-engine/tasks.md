# Implementation Tasks: Adding Matching Engine

## Overview

Add a matching engine to the digital twin test case generator to simulate realistic trade execution with price-time priority matching, fill generation, position tracking, and FIX execution report generation.

**Estimated Effort**: 3-5 days
**Risk Level**: Medium (new package, state integration)

---

## Phase 1: Core Matching (Low Risk)

### Task 1.1: Create matching package structure
- [ ] Create `digital_twin/matching/` directory
- [ ] Create `digital_twin/matching/__init__.py` with exports
- [ ] Add `MatchingEngine` placeholder class in `engine.py`
- **Files**: `digital_twin/matching/__init__.py`, `digital_twin/matching/engine.py`

### Task 1.2: Implement Trade dataclass
- [ ] Create `Trade` dataclass with: `trade_id`, `symbol`, `fill_qty`, `fill_price`, `aggressor_order_id`, `passive_order_id`, `aggressor_user_id`, `passive_user_id`, `timestamp`
- [ ] Add `trade_id` format: `TRD{NNNNNN}`
- [ ] Add trade ID counter to `DigitalTwinState._trade_id_counter`
- **Files**: `digital_twin/matching/trade.py`, `digital_twin/state.py`

### Task 1.3: Implement price-time priority matching algorithm
- [ ] Implement `MatchingEngine.match_order(order, state)` method
- [ ] Check crossing conditions: buy >= best_ask, sell <= best_bid
- [ ] Match at passive order price (not aggressor price)
- [ ] Implement FIFO for same-price orders
- [ ] Handle multi-level matching (sweep across price levels)
- **Files**: `digital_twin/matching/engine.py`

### Task 1.4: Implement FillGenerator
- [ ] Create `FillGenerator` class
- [ ] Generate fills with min(aggressor_qty, passive_qty)
- [ ] Track remaining_qty for aggressor
- [ ] Track cum_qty for each order
- [ ] Generate separate trade for each passive order matched
- **Files**: `digital_twin/matching/trade.py`

### Task 1.5: Add unit tests for matching algorithm
- [ ] Test: Buy order crosses best ask
- [ ] Test: Sell order crosses best bid
- [ ] Test: Same price FIFO ordering
- [ ] Test: No match when no crossing
- [ ] Test: Partial fill handling (aggressor > passive)
- [ ] Test: Partial fill handling (aggressor < passive)
- [ ] Test: Multi-level matching
- **Files**: `tests/test_matching_engine.py`

---

## Phase 2: State Integration (Medium Risk)

### Task 2.1: Extend Order class for fill tracking
- [ ] Add `cum_qty: Decimal` field (sum of all fills)
- [ ] Add `leaves_qty: Decimal` field (alias for remaining_qty, FIX terminology)
- [ ] Ensure `remaining_qty` updates correctly after fills
- [ ] Add `fills: List[Trade]` field for fill history
- **Files**: `digital_twin/state.py`

### Task 2.2: Implement order state transitions
- [ ] Create `OrderStateTransitions` class
- [ ] Implement: NEW → PARTIALLY_FILLED (on partial fill)
- [ ] Implement: NEW → FILLED (on full fill)
- [ ] Implement: PARTIALLY_FILLED → FILLED (on remaining fill)
- [ ] Block transitions from terminal states (FILLED, CANCELLED, REJECTED)
- [ ] Update `update_time` on each state transition
- **Files**: `digital_twin/matching/engine.py` or `digital_twin/matching/transitions.py`

### Task 2.3: Extend Position class for average price
- [ ] Review existing `Position.update_with_fill()` implementation
- [ ] Fix average price calculation for mixed buy/sell
- [ ] Add position side determination (LONG/SHORT/FLAT based on net qty)
- [ ] Add `long_qty` and `short_qty` separate tracking
- **Files**: `digital_twin/state.py`

### Task 2.4: Implement PositionTracker
- [ ] Create `PositionTracker` class
- [ ] Method: `update_position(trade: Trade, state: DigitalTwinState)`
- [ ] Update both aggressor and passive user positions
- [ ] Handle buy fills (increase position)
- [ ] Handle sell fills (decrease position)
- **Files**: `digital_twin/matching/positions.py`

### Task 2.5: Integrate matching with DigitalTwinState
- [ ] Update `Orderbook` after each match (remove/update orders)
- [ ] Update `Order` state and quantities atomically
- [ ] Update `Position` atomically with order state
- [ ] Maintain price-time ordering in orderbook
- **Files**: `digital_twin/matching/engine.py`

### Task 2.6: Add tests for state integration
- [ ] Test: Order state transitions correctly
- [ ] Test: Position updates correctly per fill
- [ ] Test: Average price calculation is correct
- [ ] Test: Orderbook state is consistent after matches
- [ ] Test: State updates are atomic
- **Files**: `tests/test_matching_state.py`

---

## Phase 3: Execution Reports (Low Risk)

### Task 3.1: Create ExecutionReportGenerator class
- [ ] Create `ExecutionReportGenerator` class
- [ ] Method: `generate_fill_report(order: Order, trade: Trade) -> dict`
- [ ] Method: `generate_ack_report(order: Order) -> dict`
- [ ] Method: `generate_cancel_report(order: Order) -> dict`
- **Files**: `digital_twin/matching/execution_report.py`

### Task 3.2: Implement FIX field mappings
- [ ] Core identification: ClOrdID (11), OrderID (37), ExecID (17), Symbol (55), Side (54)
- [ ] Execution details: ExecType (150), OrdStatus (39), LastQty (32), LastPx (31)
- [ ] Quantity tracking: LeavesQty (151), CumQty (14), OrderQty (38)
- [ ] Timestamp: TransactTime (60)
- [ ] Use `digital_twin/constants.py` FIX_TAG_* constants
- **Files**: `digital_twin/matching/execution_report.py`

### Task 3.3: Implement ExecType/OrdStatus logic
- [ ] ExecType NEW (0) for acknowledgment
- [ ] ExecType FILL (2) or TRADE (F) for fills
- [ ] ExecType CANCELED (4) for cancellations
- [ ] ExecType REJECTED (8) for rejections
- [ ] OrdStatus matches order.status (0=NEW, 1=PARTIALLY_FILLED, 2=FILLED)
- **Files**: `digital_twin/matching/execution_report.py`

### Task 3.4: Implement ExecID generation
- [ ] Use `DigitalTwinState.next_exec_id()` for unique IDs
- [ ] Format: `EXEC{NNNNNN}`
- [ ] Ensure sequential IDs within session
- **Files**: `digital_twin/matching/execution_report.py`

### Task 3.5: Mark execution reports as RECEIVE direction
- [ ] Add `direction: "receive"` to execution report dict
- [ ] Integrate with CSV writer for RECEIVE column
- **Files**: `digital_twin/matching/execution_report.py`

### Task 3.6: Add tests for execution reports
- [ ] Test: Fill report has all required fields
- [ ] Test: ExecType matches fill event type
- [ ] Test: OrdStatus matches order state
- [ ] Test: LastQty/LastPx are per-fill, not cumulative
- [ ] Test: CumQty/LeavesQty are cumulative
- [ ] Test: ExecID is unique
- **Files**: `tests/test_execution_report.py`

---

## Phase 4: Generator Integration (Medium Risk)

### Task 4.1: Update TestCaseGenerator to use MatchingEngine
- [ ] Import `MatchingEngine` in `generator.py`
- [ ] Initialize `MatchingEngine` in `TestCaseGenerator.__init__`
- [ ] Call matching engine after order submission
- [ ] Collect generated trades
- **Files**: `digital_twin/generator.py`

### Task 4.2: Generate execution reports in test flow
- [ ] After each match, generate execution report
- [ ] Add execution reports to test step list
- [ ] Mark execution reports as RECEIVE direction
- [ ] Include both aggressor and passive execution reports
- **Files**: `digital_twin/generator.py`

### Task 4.3: Update CSV output for execution reports
- [ ] Ensure CSV writer handles execution report messages
- [ ] Add EXECUTION_REPORT to message type column
- [ ] Include all FIX fields in payload JSON
- **Files**: `digital_twin/csv_writer.py`

### Task 4.4: Add coverage tracking for matching scenarios
- [ ] Track: Partial fill scenario covered
- [ ] Track: Full fill scenario covered
- [ ] Track: Multi-level match scenario covered
- [ ] Track: Each order state transition covered
- **Files**: `digital_twin/coverage.py`

### Task 4.5: Add integration tests
- [ ] Test: End-to-end order → match → fill → execution report flow
- [ ] Test: Multiple orders, multiple matches
- [ ] Test: Position tracking across multiple trades
- [ ] Test: CSV output contains execution reports
- **Files**: `tests/test_generator_matching.py`

---

## Phase 5: Matching Modes (Future - Lower Priority)

### Task 5.1: Create MatchingMode base class
- [ ] Create abstract `MatchingMode` class
- [ ] Define interface: `match(order, state) -> List[Trade]`
- **Files**: `digital_twin/matching/modes.py`

### Task 5.2: Implement LMEselectMode (continuous)
- [ ] Immediate matching on order submission
- [ ] Already implemented in Phase 1-4, just wrap in class
- **Files**: `digital_twin/matching/modes.py`

### Task 5.3: Implement TOMMode (end-of-day batch)
- [ ] Collect orders during session
- [ ] Batch match at deadline
- [ ] Single clearing price for all matches
- **Files**: `digital_twin/matching/modes.py`

### Task 5.4: Add RingMode placeholder
- [ ] Raise NotImplementedError for Ring mode
- [ ] Document as future work
- **Files**: `digital_twin/matching/modes.py`

### Task 5.5: Add mode selection to scenarios
- [ ] Add `matching_mode` field to scenario config
- [ ] Default to "lmeselect"
- [ ] Pass mode to MatchingEngine constructor
- **Files**: `digital_twin/config/scenarios/*.yaml`, `digital_twin/generator.py`

---

## Verification Checklist

Before marking complete:
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] `lsp_diagnostics` clean on all new files
- [ ] No type errors (no `as any`, `@ts-ignore` equivalents)
- [ ] Code follows existing patterns in `digital_twin/`
- [ ] Matching algorithm is deterministic (same input = same output)
- [ ] Execution reports are FIX-compliant
- [ ] Positions track correctly across multiple trades

---

## Dependencies

- **Depends on**: `digital_twin/state.py` (Order, Orderbook, Position, DigitalTwinState)
- **Depends on**: `digital_twin/constants.py` (FIX tags, LME symbols)
- **Depends on**: `digital_twin/generator.py` (TestCaseGenerator)
- **Depends on**: `digital_twin/csv_writer.py` (CSV output)

---

## Rollback Strategy

- Phase 1-3 can be committed independently
- Phase 4 integration can be feature-flagged
- If issues found, disable matching engine and revert to previous generator behavior
- Each phase is a separate logical commit
