# Implementation Tasks

## 1. Constants and Enums

- [ ] 1.1 Create `digital_twin/constants.py` with LME_SYMBOLS dictionary (AL, CU, NI, ZN, PB, SN, AA, HN) including lot_size, tick_size, price_unit
- [ ] 1.2 Add MAX_ORDER_QTY = 9_999 and MAX_ORDER_PRICE = 9_999_999 to constants.py
- [ ] 1.3 Add ICEBERG = "ICEBERG" and POST_ONLY = "POST_ONLY" to OrderType enum in state.py
- [ ] 1.4 Add OrderRejectReason enum to state.py with codes 0-26, 99 (per FIX Spec §4.11.7)
- [ ] 1.5 Add SessionState enum to state.py (DISCONNECTED, CONNECTING, AUTHENTICATING, CONNECTED, LOGGING_OUT)

## 2. Order State Machine

- [ ] 2.1 Add VALID_ORDER_TRANSITIONS dictionary to state.py defining all valid state transitions
- [ ] 2.2 Implement `can_transition(current: OrderStatus, target: OrderStatus) -> bool` function
- [ ] 2.3 Add `is_terminal(status: OrderStatus) -> bool` function
- [ ] 2.4 Add unit tests for state transition validation

## 3. Validation Layer

- [ ] 3.1 Create `digital_twin/validators.py` module
- [ ] 3.2 Implement `validate_order(order: Order, symbol: Symbol) -> List[str]` returning error messages
- [ ] 3.3 Implement `validate_quantity(qty: Decimal, symbol: Symbol) -> Optional[str]`
- [ ] 3.4 Implement `validate_price(price: Decimal, symbol: Symbol) -> Optional[str]`
- [ ] 3.5 Implement `validate_tick(price: Decimal, tick_size: Decimal) -> bool`
- [ ] 3.6 Implement `validate_conditional_fields(order: Order) -> List[str]` for order-type-specific requirements
- [ ] 3.7 Add unit tests for validators

## 4. Initial State Update

- [ ] 4.1 Replace ES-DEC24 with CU (Copper, lot_size=25, tick_size=0.50) in initial_state.json
- [ ] 4.2 Replace ES-MAR25 with AL (Aluminium, lot_size=25, tick_size=0.50) in initial_state.json
- [ ] 4.3 Replace NQ-DEC24 with NI (Nickel, lot_size=6, tick_size=5.00) in initial_state.json
- [ ] 4.4 Add ZN (Zinc), PB (Lead), SN (Tin) symbols to initial_state.json
- [ ] 4.5 Update price_bands for all symbols with realistic LME price ranges
- [ ] 4.6 Verify initial_state.json loads correctly with load_initial_state()

## 5. Parameter Generators

- [ ] 5.1 Create `digital_twin/generators.py` module
- [ ] 5.2 Implement `generate_quantity(symbol: Symbol, state: DigitalTwinState, rng: Random) -> Decimal`
- [ ] 5.3 Implement `generate_price(symbol: Symbol, state: DigitalTwinState, rng: Random) -> Decimal`
- [ ] 5.4 Implement `generate_order_type(rng: Random) -> OrderType` with weighted distribution
- [ ] 5.5 Implement `generate_side(rng: Random) -> OrderSide`
- [ ] 5.6 Implement `generate_cl_ord_id(state: DigitalTwinState) -> str`
- [ ] 5.7 Implement `generate_symbol(state: DigitalTwinState, rng: Random) -> str`
- [ ] 5.8 Add conditional field generation (DisplayQty for Iceberg, StopPx for Stop orders)
- [ ] 5.9 Add unit tests for generators

## 6. Integration

- [ ] 6.1 Update `digital_twin/__init__.py` to export new modules (constants, validators, generators)
- [ ] 6.2 Update `TestCaseGenerator._generate_single_step()` to use new validators
- [ ] 6.3 Update `TestCaseGenerator._generate_single_step()` to use new generators
- [ ] 6.4 Add rejection reason to Execution Report when order fails validation
- [ ] 6.5 Verify end-to-end test case generation works with new symbols

## 7. Documentation

- [ ] 7.1 Add docstrings to all new functions in validators.py
- [ ] 7.2 Add docstrings to all new functions in generators.py
- [ ] 7.3 Add docstrings to constants.py explaining LME symbol format
- [ ] 7.4 Update README or add usage examples for new validation features

## 8. Verification

- [ ] 8.1 Run all unit tests and verify passing
- [ ] 8.2 Generate sample test cases and verify symbols are LME metals
- [ ] 8.3 Verify validation catches invalid orders (qty > 9999, invalid ticks)
- [ ] 8.4 Verify state transitions are enforced
- [ ] 8.5 Verify generated test cases have valid ClOrdId, Symbol, Side, Price, Quantity
