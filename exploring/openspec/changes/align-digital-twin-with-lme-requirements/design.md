## Context

The digital twin test case generator (`digital_twin/`) was implemented as a proof-of-concept using placeholder symbols (ES-DEC24, NQ-DEC24) that don't correspond to actual LME contracts. Meanwhile, the `apply-options-requirements` change has established comprehensive LME reference data in `doc/requirements/openspec/reference/` including:

- `symbols.md` - LME metal symbols with lot sizes, tick sizes
- `trading-hours.md` - Trading venue schedules
- `error-codes.md` - Complete error/rejection code catalog
- `state-machines.md` - Session and order state definitions
- `validation-rules.md` - Field validation constraints

The digital twin needs to consume this reference data to generate realistic test cases.

### Current State

| Component | Current | Required |
|-----------|---------|----------|
| Symbols | ES-DEC24, NQ-DEC24 (placeholders) | AL, CU, NI, ZN, PB, SN, AA, HN (LME metals) |
| Lot Sizes | 50, 20 (arbitrary) | 25t, 6t, 5t, 10t (per metal) |
| Tick Sizes | 0.25, 0.50 (arbitrary) | $0.50/tonne, $5.00/tonne (per metal) |
| Order Types | MARKET, LIMIT, STOP, STOP_LIMIT | + ICEBERG, POST_ONLY |
| Validation | None | Max qty 9,999, max price 9,999,999, tick validation |
| State Machine | OrderStatus enum only | Transition validation |
| Error Codes | None | OrderRejectReason enum |

### Constraints

- Must maintain backward compatibility with existing `DigitalTwinState` dataclass structure
- Reference data is in Markdown format - need to either parse or create Python equivalents
- No external dependencies beyond standard library + pyyaml

## Goals / Non-Goals

**Goals:**

1. **Symbol alignment**: Replace placeholder symbols with actual LME metals in `initial_state.json`
2. **Order type support**: Add ICEBERG and POST_ONLY order types with validation
3. **Validation layer**: Add LME-specific validation rules for order parameters
4. **State machine**: Add order state transition validation
5. **Error codes**: Add structured rejection reason codes
6. **Parameter generators**: Create state-aware generators for test case fields

**Non-Goals:**

- Session state management (future enhancement)
- Binary protocol support (FIX only for now)
- Test case execution (generator only)
- UI/visualization of test cases
- Database persistence (file-based only)

## Decisions

### Decision 1: Inline Constants vs Reference Data Parsing

**Decision**: Define Python constants directly in `digital_twin/constants.py` rather than parsing Markdown reference files.

**Rationale**:
- Simpler implementation - no Markdown parsing needed
- Type-safe constants at import time
- Reference files serve as documentation, code is the source of truth for runtime

**Alternatives Considered**:
- Parse Markdown reference files at runtime → Rejected: Adds complexity, runtime overhead
- Generate Python from Markdown → Rejected: Adds build step, harder to debug

**Implementation**:
```python
# digital_twin/constants.py
LME_SYMBOLS = {
    "CU": {"lot_size": 25, "tick_size": Decimal("0.50"), "price_unit": "USD/tonne"},
    "AL": {"lot_size": 25, "tick_size": Decimal("0.50"), "price_unit": "USD/tonne"},
    "NI": {"lot_size": 6, "tick_size": Decimal("5.00"), "price_unit": "USD/tonne"},
    ...
}

MAX_ORDER_QTY = 9_999
MAX_ORDER_PRICE = Decimal("9_999_999")
```

### Decision 2: Validation Module Location

**Decision**: Create new `digital_twin/validators.py` module rather than adding to `state.py`.

**Rationale**:
- Separation of concerns - state holds data, validators check it
- Easier to test validators independently
- Can be imported by message handlers without circular dependencies

**Alternatives Considered**:
- Add validation methods to `Order` dataclass → Rejected: Mixes data and logic
- Add validation to `DigitalTwinState` → Rejected: Class already too large

### Decision 3: State Machine Implementation

**Decision**: Implement state transition validation as a dictionary-based lookup table.

**Rationale**:
- Simple and explicit - all valid transitions visible in one place
- Easy to test - cover all combinations
- No external state machine library needed

**Implementation**:
```python
VALID_ORDER_TRANSITIONS = {
    OrderStatus.NEW: {OrderStatus.PARTIALLY_FILLED, OrderStatus.FILLED, OrderStatus.CANCELLED, OrderStatus.REJECTED},
    OrderStatus.PARTIALLY_FILLED: {OrderStatus.FILLED, OrderStatus.CANCELLED},
    OrderStatus.FILLED: set(),  # Terminal
    ...
}

def can_transition(current: OrderStatus, target: OrderStatus) -> bool:
    return target in VALID_ORDER_TRANSITIONS.get(current, set())
```

### Decision 4: Error Code Integration

**Decision**: Add `OrderRejectReason` enum to `state.py` alongside existing enums.

**Rationale**:
- Consistent with existing enum organization
- Co-located with `OrderStatus` which it relates to
- Simple addition without new files

### Decision 5: Parameter Generator Architecture

**Decision**: Create generators as functions in `digital_twin/generators.py` that take state as parameter.

**Rationale**:
- Stateless functions are easier to test
- Can be composed and customized
- Consistent with existing `ParameterGenerator` base class pattern

**Implementation**:
```python
def generate_quantity(symbol: Symbol, state: DigitalTwinState, rng: random.Random) -> Decimal:
    """Generate valid quantity for symbol."""
    max_by_symbol = MAX_ORDER_QTY * symbol.lot_size
    max_by_state = state.get_remaining_position_capacity(symbol.symbol_id)
    max_qty = min(max_by_symbol, max_by_state)
    lots = rng.randint(1, max_qty)
    return Decimal(lots * symbol.lot_size)
```

## Risks / Trade-offs

### Risk 1: Reference Data Drift

**Risk**: Python constants may diverge from Markdown reference files if LME changes specs.

**Mitigation**: 
- Add comment in constants.py linking to source reference file
- Include "Last Synced" date in constants
- Consider adding validation tests that check constants match reference

### Risk 2: Breaking Existing Tests

**Risk**: Changing symbols may break any tests that hardcode ES-DEC24 or NQ-DEC24.

**Mitigation**:
- Search codebase for hardcoded symbol references
- Update any found references to use new symbols
- Add deprecation notice if needed

### Risk 3: Generator Complexity

**Risk**: State-aware generators may become complex and slow.

**Mitigation**:
- Keep generators simple - focus on common cases
- Add performance benchmarks for generation
- Consider caching computed values

## Migration Plan

### Phase 1: Constants and Enums (Low Risk)

1. Create `digital_twin/constants.py` with LME symbols, validation limits
2. Add `ICEBERG`, `POST_ONLY` to `OrderType` enum
3. Add `OrderRejectReason` enum
4. Add state transition validation function

### Phase 2: Initial State Update (Medium Risk)

1. Update `initial_state.json` with LME metals
2. Remove placeholder symbols
3. Verify state loads correctly

### Phase 3: Validation Layer (Low Risk)

1. Create `digital_twin/validators.py`
2. Implement `validate_order()` function
3. Integrate with message handlers

### Phase 4: Parameter Generators (Medium Risk)

1. Create `digital_twin/generators.py`
2. Implement symbol-aware generators
3. Integrate with `TestCaseGenerator`

### Rollback Strategy

- Git branches for each phase
- Revert commit if issues found
- `initial_state.json` can be restored from previous version
- New files (validators.py, generators.py) can be deleted if problematic

## Open Questions

1. **Symbol Selection Strategy**: Should generators prefer certain metals (e.g., higher volume CU/AL) or uniform distribution?

2. **Price Generation**: Should prices be generated relative to current orderbook state or random within band?

3. **DisplayQty for Iceberg**: What ratio of DisplayQty to OrderQty should generators use?

4. **Session State Integration**: Should we implement full session state machine or defer to future change?
