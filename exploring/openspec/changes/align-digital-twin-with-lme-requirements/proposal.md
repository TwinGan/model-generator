## Why

The digital twin test case generator was created using placeholder symbols (ES-DEC24, NQ-DEC24) that than actual LME metals (CU, AL, NI, ZN, PB, SN, AA, HN). The creates a disconnect between the test case generator and the production options on futures trading system it The tests will not reflect real-world LME trading scenarios.

**Why now**: The `apply-options-requirements` change established comprehensive LME specifications in `doc/requirements/openspec/reference/`. The digital twin should use these official symbols definitions, lot sizes, tick sizes, and validation rules to generate realistic test cases.

## What Changes

- **Symbol data replacement**: Replace placeholder symbols in `initial_state.json` with actual LME metals (CU, AL, NI, ZN, PB, SN, AA, HN) including lot sizes (25t, 6t, 5t, 10t), tick sizes ($0.50-$5.00/tonne)
- **Order type extension**: Add `ICEBERG` and `POST_ONLY` to `OrderType` enum
- **Validation rules**: Implement LME validation constraints (max qty 9,999 lots, max price 9,999,999)
- **State machine validation**: Add order state transition validation to prevent invalid state changes
- **Error codes**: Add `OrderRejectReason` enum with LME-specific rejection codes

## Capabilities

### New Capabilities
- `lme-symbol-alignment`: Configure digital twin with actual LME metal symbols (AL, CU, NI, ZN, PB, SN, AA, HN) including lot sizes, tick sizes, price bands, and validation constraints
- `order-type-extension`: Add support for ICEBERG and POST_ONLY order types with appropriate validation rules
- `order-validation-rules`: Implement LME order validation constraints including max quantity, max price, and conditional field requirements (Price for Limit, StopPx for Stop orders)
- `order-state-machine`: Add order state transition validation to ensure only valid state changes occur (NEW → PART/Fill → Fill/Cancelled)
- `order-rejection-codes`: Add LME-specific order rejection reason codes to structured error handling
- `session-state-model`: Add session lifecycle state management (DISCONNECTED, CONNECTING, AUTHENTICATING, CONNECTED, LOGGING_OUT)
- `parameter-generators`: Create state-aware parameter generators for order fields that respect symbol constraints and market state

### Modified Capabilities
- *(none - this is a new codebase)*

## Impact
**Affected Files**:
- `digital_twin/state.py` - Add enums, validation functions, state transitions
- `digital_twin/config/initial_state.json` - Replace symbols with LME metals
- `digital_twin/messages/` - Add message handlers for new order types
- `digital_twin/generator.py` - Update parameter generation logic
- `digital_twin/validators.py` (new) - Add validation module
