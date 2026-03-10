# Digital Twin Generator - Implementation Tasks

## Core Implementation

- [ ] Create project structure
  - [ ] Create `digital_twin/` package directory
  - [ ] Create `digital_twin/__init__.py`
  - [ ] Create `digital_twin/messages/__init__.py`
  - [ ] Create `digital_twin/config/` directory
  - [ ] Create `digital_twin/config/message_weights.yaml`
  - [ ] Create `digital_twin/config/scenarios/` directory

# Digital Twin Generator - Implementation Tasks

## Core Implementation

- [x] Create project structure
  - [x] Create `digital_twin/` package directory
  - [x] Create `digital_twin/__init__.py`
  - [x] Create `digital_twin/messages/__init__.py`
  - [x] Create `digital_twin/config/` directory
  - [x] Create `digital_twin/config/message_weights.yaml`
  - [x] Create `digital_twin/config/scenarios/` directory

- [ ] Implement state model (`digital_twin/state.py`)

- [ ] Implement loader (`digital_twin/loader.py`)
  - [ ] Implement load_initial_state(json_path) function
  - [ ] Add validation for required state components
  - [ ] Implement error handling for missing/invalid data
  - [ ] Create DigitalTwinState from JSON
  - [ ] Return deep copy for independent working state

- [x] Create project structure
  - [x] Create `digital_twin/` package directory
  - [x] Create `digital_twin/__init__.py`
  - [x] Create `digital_twin/messages/__init__.py`
  - [x] Create `digital_twin/config/` directory
  - [x] Create `digital_twin/config/message_weights.yaml`
  - [x] Create `digital_twin/config/scenarios/` directory

- [x] Implement state model (`digital_twin/state.py`)
  - [x] Define Symbol dataclass with instrument_type, underlying, strike_price, expiry, tick_size, lot_size, price_band
  - [x] Define User dataclass with user_id, member_id, permissions, limits
  - [x] Define Member dataclass with member_id, name
 risk_groups
  - [x] Define Orderbook dataclass with bids and asks
  - [x] Define Order dataclass with order_id, cl_ord_id, symbol, side, quantity
 price, order_type
 status
 user_id
 member_id
 filled_qty
 remaining_qty
 create_time
 update_time
  - [x] Define Position dataclass with user_id, symbol
 side
 quantity
 avg_price
  - [x] Define RiskGroup dataclass with risk_group_id
 members
 limits
  - [x] Define PriceBand dataclass with min_price, max_price, tick_size
  - [x] Implement DigitalTwinState dataclass aggregating all state
  - [x] Implement to_dict() and from_dict() methods for JSON serialization
  - [x] Implement deepcopy support via __deepcopy__
  - [x] Add type-safe access methods (get_symbol, get_order, get_orderbook, etc.)

- [x] Implement loader (`digital_twin/loader.py`)
  - [x] Implement load_initial_state(json_path) function
  - [x] Add validation for required state components
  - [x] Implement error handling for missing/invalid data
  - [x] Create DigitalTwinState from JSON
  - [x] Return deep copy for independent working state

- [ ] Implement coverage tracker (`digital_twin/coverage.py`)
  - [ ] Implement message type coverage tracking (set of executed types)
  - [ ] Implement parameter value coverage tracking (enum values, boundary values)
  - [ ] Implement state transition coverage tracking (state machine transitions)
  - [ ] Add coverage gap analysis method
  - [ ] Implement to_dict() for JSON serialization
  - [ ] Add suggestions generation for missing coverage
  - [ ] Ensure non-intrusive tracking (minimal performance impact)

- [ ] Implement CSV writer (`digital_twin/csv_writer.py`)
  - [ ] Define WIDE_COLUMNS list for common fields
  - [ ] Implement write() method for test steps
  - [ ] Add metadata header support (run_id, seed, timestamp)
  - [ ] Implement send/receive row differentiation
  - [ ] Support multiple receive rows per send
  - [ ] Add proper JSON escaping for CSV
  - [ ] Implement payload_json column with complete message data

- [ ] Implement main generator (`digital_twin/generator.py`)
  - [ ] Define TestCaseGenerator class
  - [ ] Implement __init__ with scenario config, initial state, seed
  - [ ] Implement generate(num_steps) method with main loop
  - [ ] Add _select_message() helper with precondition checking
  - [ ] Add _next_cl_ord_id() helper for ID generation
  - [ ] Implement GeneratorResult dataclass
  - [ ] Add save() method to write all artifacts
  - [ ] Support both fuzzy and replay modes

## Per-Message Implementation (Generated from Sub-Specs)

- [ ] Create message handler template (`digital_twin/messages/base.py`)
  - [ ] Define MessageHandler base class
  - [ ] Define ParameterGenerator base class
  - [ ] Define Precondition base class
  - [ ] Define HandlerResult dataclass
  - [ ] Define MESSAGE_REGISTRY dict

- [ ] Generate message modules from sub-specs (one per message type)
  - [ ] Parse sub-spec YAML files
  - [ ] Generate precondition checker class
  - [ ] Generate parameter generator class with boundary testing
  - [ ] Generate handler class with business logic
  - [ ] Register in MESSAGE_REGISTRY

## Configuration

- [ ] Create default message weights config
  - [ ] Define message groups with weights
  - [ ] Define message types within groups with weights
  - [ ] Create config/message_weights.yaml

- [ ] Create sample scenario configs
  - [ ] Create config/scenarios/default.yaml
  - [ ] Create config/scenarios/high_frequency_trading.yaml
  - [ ] Include message weights, parameter strategies, volume targets

## Testing

- [ ] Create unit tests for state model
  - [ ] Test Symbol, User, Member, Orderbook dataclasses
  - [ ] Test Order, Position dataclasses
  - [ ] Test JSON serialization/deserialization
  - [ ] Test deep copy functionality
  - [ ] Test type-safe access methods

- [ ] Create unit tests for loader
  - [ ] Test valid initial state loading
  - [ ] Test invalid/missing data handling
  - [ ] Test state initialization from JSON

- [ ] Create unit tests for selector
  - [ ] Test weighted random selection
  - [ ] Test precondition checking
  - [ ] Test deterministic behavior with seed
  - [ ] Test retry logic

- [ ] Create unit tests for coverage tracker
  - [ ] Test message type coverage
  - [ ] Test parameter value coverage
  - [ ] Test state transition coverage
  - [ ] Test gap analysis
  - [ ] Test JSON serialization

- [ ] Create unit tests for CSV writer
  - [ ] Test wide column output
  - [ ] Test JSON payload column
  - [ ] Test metadata header
  - [ ] Test send/receive rows
  - [ ] Test multiple receive rows per send
  - [ ] Test JSON escaping

- [ ] Create integration tests for generator
  - [ ] Test full generation loop
  - [ ] Test output artifact creation
  - [ ] Test replay mode (deterministic)
  - [ ] Test fuzzy mode (random)
  - [ ] Test with sample initial state

## Documentation

- [ ] Create README.md for digital_twin package
  - [ ] Document architecture and components
  - [ ] Document usage examples
  - [ ] Document configuration format
  - [ ] Document output format

- [ ] Create sub-spec format documentation
  - [ ] Document YAML structure
  - [ ] Document required fields
  - [ ] Provide examples for each message type

- [ ] Create configuration guide
  - [ ] Document message weight configuration
  - [ ] Document scenario configuration
  - [ ] Document parameter strategies

## LLM Generation Pipeline (Future Work)

- [ ] Create PDF extraction module
  - [ ] Parse structured PDF specifications
  - [ ] Identify message types and groups
  - [ ] Extract input/output schemas
  - [ ] Parse business rules

- [ ] Create sub-spec generator
  - [ ] Generate YAML sub-specs from extracted data
  - [ ] Identify parameter ranges and constraints
  - [ ] Determine preconditions for each message
  - [ ] Define state effects

- [ ] Create code generator
  - [ ] Generate state.py from aggregated state effects
  - [ ] Generate message handlers from business rules
  - [ ] Generate parameter generators from parameter_generation specs
  - [ ] Generate precondition checkers from preconditions
