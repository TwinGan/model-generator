# Digital Twin Test case Generator - Design Document
# <!-- Document technical decisions, architecture, and implementation approach -->

## Overview
AI-generated test case generator for options on futures trading systems. Uses LLM to generate Python code from structured specifications, producing hybrid CSV output with built-in coverage tracking and replay capabilities.

# Architecture
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DESIGN Time (LLM)                       │
│  PDF Specs ──▶ Sub-Specs ──▶ Generated Python Code                │
│                                                              │
│  state.py                  generator.py                 │
│  selector.py                 coverage.py                  │
│  csv_writer.py                loader.py                  │
│  messages/*.py               config/*.yaml                               │
│                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
                        Runtime (No LLM)                         │
┌─────────────────────────────────────────────────────────────────────────────┐
│  Input                         Digital Twin                              Output                        │
│  ──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   │
│  │ initial_state.json  │   │  state.py           │   │  test_cases.csv   │   │
│  │ scenario.yaml      │   │  (internal state)    │   │  coverage_report.json│   │
│  │ num_steps             │   │                    │   │  metadata.json      │   │
│  │ (seed)               │   │                    │   │                    │   │
│  └─────────────────────┘   └──────────────────┘   └──────────────────────┘   │
│                                                │                              │
│                                                ▼                              │
│                                    ┌─────────────────┐    │
│                                    │ Generation Loop │    │
│                                    └────────┬───────┘    │
│                                             │                │
│   1. Load initial state from JSON                                   │
│   2. Select message type (weighted + preconditions)               │
│   3. Generate parameters (state-aware + spec constraints)            │
│   4. Execute handler (simulate business logic, update state)            │
│   5. Output SEND row (test case)                                │
│   6. Execute handler (predict response, update state)             │
│   7. Output receive row(s) (predicted response)                         │
│   8. Track coverage (message type, parameters, state transition)│
│   9. Repeat until volume target reached                      │
│   10. Output all artifacts (CSV, coverage report, saved initial state)              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Components

### State Model (`state.py`)
Immutable dataclasses representing trading system state:
- **Symbol**: Option/future contract definition
- **User**: Trader information
- **Member**: Clearing member
- **Orderbook**: Outstanding bids/asks per symbol
- **Order**: Active/filled/cancelled orders
- **Position**: User positions by symbol
- **RiskGroup**: Risk management groupings
- **PriceBand**: Price limits per symbol

- Deep copy support for state preservation
- JSON serialization/deserialization
- Type-safe access methods

- No external dependencies

### Message Selector (`selector.py`)
Weighted random message selection with precondition checking.
- **Precondition Registry**: Each message registers its preconditions
- **Weight Configuration**: Load from YAML config
- **Selection Algorithm**:
  1. Weighted random selection from message groups
  2. Weighted random selection within group
  3. Check preconditions against current state
  4. Retry if preconditions not met (up to max retries)
  5. Fallback to "no valid message" error
- Deterministic when seed provided

- No external dependencies

### Parameter Generators (per message type)
Generate valid parameters based on state and specification constraints.
- **Range Extraction**: Parse min/max/valid values from specs
- **Boundary Testing**: Support configurable positive/negative testing weights
- **State-Aware Selection**: Use current state to select valid values (e.g., existing order IDs for cancel)
- **Dependency Resolution**: Generate parameters that reference state values (e.g., orig_cl_ord_id references cl_ord_id)
- **JSON Serialization**: All parameters JSON-serializable
- Deterministic when seed provided

- No external dependencies

### Message Handlers (per message type)
Execute business logic and update internal state.
- **Input Validation**: Check required fields, valid ranges, business rules
- **State Updates**: Modify internal state based on message processing
- **Response Generation**: Return list of predicted responses (0 or more for partial fills)
- **ID Generation**: Generate unique IDs (order_id, exec_id, cl_ord_id)
- **Deterministic**: Same input + seed = same output
- No external dependencies



### Coverage Tracker (`coverage.py`)
Multi-level test coverage tracking.
- **Level 1 - Message Type**: Track which message types were executed
- **Level 2 - Parameter Values**: Track which parameter combinations were tested
 including:
  - Enum values (side, order_type, etc.)
  - Boundary values (min/max quantity, price)
  - State-derived values (symbol from orderbook)
- **Level 3 - State Transitions**: Track state machine transitions
  - Track unique state transitions (e.g., NEW → FILLED)
  - Identify unvisited transitions
- **Gap Analysis**: Identify missing coverage and suggest areas for additional testing
- **Coverage Report**: Output JSON with summary and details
- Non-intrusive: No impact on test generation performance
- **Persistence**: Coverage data JSON-serializable for later analysis
- **No external dependencies**

### CSV Writer (`csv_writer.py`)
Hybrid CSV output (wide columns + JSON payload).
- **Wide Columns**: Common fields for easy viewing:
  - step_id, direction, message_type
  - symbol, side, quantity, price
  - order_id, cl_ord_id, orig_cl_ord_id
  - status, exec_type, reason
- **JSON Payload**: Complete message data in payload_json column
- **Metadata Header**: Include run_id, seed, timestamp in CSV comments
- **Send/Receive Direction**: Differentiate outbound from predicted responses
- **Multiple Rece Rows**: Support multiple predicted responses per send
- **JSON Escaping**: Proper CSV escaping for JSON strings
- **No external dependencies**

### Loader (`loader.py`)
Load initial state from JSON.
- **JSON Parsing**: Load initial_state.json
- **Validation**: Verify required state components exist
- **State Initialization**: Create DigitalTwinState from JSON
- **Deep Copy**: Create independent working copy
- **Error Handling**: Clear error messages for missing/invalid data
- **No external dependencies**

## Sub-Spec Format
Each sub-spec (YAML) contains all information needed to generate one message type:
 handler:
```yaml
message_type: NewOrderSingle
message_group: OrderEntry
description: Create a new order

input_schema:
  symbol: { type: string, required: true }
  side: { type: enum, values: [BUY, SELL], required: true }
  quantity: { type: decimal, required: true }
  price: { type: decimal, required: false }
  order_type: { type: enum, values: [MARKET, LIMIT], required: true }

  
output_schema:
  order_id: { type: string }
  cl_ord_id: { type: string }
  status: { type: enum, values: [NEW, PARTIALLY_FILLED, FILLED, CANCELLED, REJECTED] }
  
preconditions:
  - state.symbols must not be empty
  - at least one active symbol
  
parameter_generation:
  symbol:
    source: state.active_symbols
    selection: random
  side:
    source: enum
    values: [BUY, SELL]
    selection: random
  quantity:
    ranges:
      positive:
        valid: [1, lot_size, lot_size * 10]
        boundary_test: true
      negative:
        invalid: [0, -1, -lot_size]
    selection_strategy:
      type: weighted
      weights: { positive: 80, negative: 20 }
      boundary_priority: 30
  
business_rules:
  - if symbol not found in state.symbols: reject with INVALID_SYMBOL
  - if quantity <= 0: reject with INVALID_QUANTITY
  - if price outside price_band: reject with PRICE_OUT_OF_BAND
  - create order with NEW status
  - add to orderbook
  
state_effects:
  on_success:
    - create Order entity
    - add to orderbook[symbol]
  on_failure:
    - no state changes
```

## Data Flow
```
initial_state.json
       │
       ▼
       ├── State (DigitalTwinState)
       │
       ├── Selector ──────────────────────┐
       │           │                       │
       │           ▼                       │
       │    Parameter Generator ──▶ Handler ──▶ CSV Writer
       │    (generates params)     (executes logic)     │
       │    (valid for state)         (updates state)         │
       │           │                       │
       │           ▼                       │
       │    Coverage Tracker (records) ◀─────────────────────┘
```

## Output Format
### Hybrid CSV Structure
```csv
step_id,direction,message_type,symbol,side,quantity,price,order_id,cl_ord_id,orig_cl_ord_id,status,exec_type,reason,payload_json
1,send,NewOrderSingle,ES-DEC24,BUY,100,4500.50,CL001,,,"{...full NewOrderSingle params...}"
2,receive,ExecutionReport,ES-DEC24,BUY,100,4500.50,ORD001,CL001,CL001,NEW,NEW,100,4500.50,"{...execution report...}"
```

### Send/Receive Mapping
ID fields link outbound messages to their predicted responses:
- **cl_ord_id**: Client-generated order ID (matches request to response)
- **order_id**: System-assigned order ID (from first response)
- **orig_cl_ord_id**: References original order (for cancel/amend)
- **step_id**: Sequential step number (same for all rows in a logical operation)

- **direction**: `send` or `receive` to differentiate purpose
- **Multiple receive rows** can have multiple responses per send
### Coverage Report Structure
```json
{
  "summary": {
    "message_types": { "covered": 18, "total": 20, "pct": 90 },
    "parameters": { "covered": 45, "total": 60, "pct": 75 },
    "transitions": { "covered": 12, "total": 18, "pct": 67 }
  },
  "details": {
    "message_types_covered": ["NewOrderSingle", "OrderCancelRequest", ...],
    "message_types_missed": ["MassOrder", "OrderMassCancel"],
    "gaps": [
      {
        "area": "MarketData",
        "suggestion": "Increase MarketData weight or add spread order scenarios"
      }
    ],
    "suggestions": [...]
  }
}
```

## Replay Strategy
1. **Save initial_state.json** with each test run
2. **Sync to state to SUT** (via external system)
3. **Execute test_cases.csv** against SUT
4. **Compare results** (via external system)
5. **Analyze failures** and coverage gaps

 This enables:
- **Regression testing**: Reproduce bugs reliably
- **Bug investigation**: Replay specific steps to isolate failure cause
- **Test coverage improvement**: Generate targeted tests for known coverage gaps

- **CI/CD integration**: Deterministic test generation for reproducible builds

- **Compliance testing**: Verify system behavior matches specification requirements

- **Documentation**: Clear audit trail of test generation

- **Root cause analysis**: Trace failures back to specific test steps
- **Regression validation**: Verify fixes work correctly

- **New feature validation**: Validate new capabilities work as expected

- **Integration testing**: Test with external systems
- **Replay testing**: Verify reproducibility across different seeds
- **Performance testing**: Verify generation speed is acceptable for volume
- **Coverage regression**: Track coverage improvements over time
- **Edge case exploration**: Test boundary conditions and error scenarios
- **Failure injection**: Test invalid parameters and error handling
- **Long-running stability**: Extended execution for memory leaks, performance degradation
- **Test data persistence**: Large CSV files may disk usage
- **Non-determinism**: Random selection may produce different results each run
- **Complex dependencies**: Multi-step dependencies between messages hard to model completely
- **Specification drift**: If specs change, code may diverge from behavior
- **Validation coverage**: Boundary testing may miss edge cases
- **Performance**: Large state objects could cause memory overhead
- **Initial sync**: Requires external system to synchronize state to SUT
- **External dependencies**: Adding dependencies on external packages increases complexity
- **Learning curve**: Generated code may not debugging
- **Error handling**: Generated error handling may not match specific requirements
- **Code review**: LLM-generated code needs careful review
- **Testing**: Generated code needs comprehensive testing
- **Documentation**: Generated code needs clear documentation
- **Maintenance**: Who maintains generated code after initial generation?
- **Specification Quality**: PDF parsing accuracy affects code quality
- **Complex Domains**: Options on futures domain is highly complex
- **State Management**: Deep state copies may cause memory issues
- **ID Conflicts**: Multiple ID generation strategies need coordination
- **Boundary Testing**: May not catch all edge cases
- **Response Prediction**: Prediction accuracy depends on spec quality
- **CSV Size**: Large test suites create big files
- **Coverage Gaps**: May not achieve full coverage
- **Replay Determinism**: Random seed selection affects reproducibility
- **Integration Complexity**: Connecting to external systems adds complexity
- **State Synchronization**: External dependency for initial state sync

- **Error Diagnosis**: Limited ability to diagnose root cause of failures
- **Spec Evolution**: Specs may change over time, requiring code updates
- **Code Maintainability**: Generated code may be harder to maintain manually
- **Debugging**: Complex generated logic can be difficult to debug
- **Documentation**: Need comprehensive docs for generated code structure

- **Performance Testing**: Need benchmarks for volume scenarios
- **Failure Scenario Testing**: Need negative test cases for edge cases
- **State Explosion Testing**: Test with complex state combinations
- **Long-Running Tests**: Verify stability over extended execution
- **Integration Tests**: End-to-end testing with external systems

- **Seed Verification**: Verify determinism across different seeds
- **Memory Profiling**: Profile memory usage with large state
- **CSV Validation**: Verify CSV output format compatibility
- **Coverage Accuracy**: Verify coverage tracking accuracy
- **Concurrent Access**: Test thread safety of state access
