# Test Case Generation Specification

Defines the specification for test case generation including format, output, and replay capabilities.

## ADDED Requirements

### Requirement: Accept Initial State
The system SHALL accept initial state in JSON format containing trading system context (symbols, users, orderbooks, positions, risk groups, price bands).

#### Scenario: Load valid initial state
- **WHEN** initial state JSON file is provided with all required fields
- **THEN** system loads state successfully and initializes internal state model

#### Scenario: Invalid initial state format
- **WHEN** initial state JSON is malformed or missing required fields
- **THEN** system SHALL reject with clear error message indicating missing fields

### Requirement: Accept Scenario Configuration
The system SHALL accept scenario configuration in YAML format with message weights, group weights, and parameter strategies.

#### Scenario: Load valid scenario config
- **WHEN** scenario YAML file is provided with valid weight configuration
- **THEN** system loads weights and applies them to message selection

#### Scenario: Missing weights in config
- **WHEN** scenario config is missing weight definitions
- **THEN** system SHALL use default equal weights for all message types

### Requirement: Accept Volume Target
The system SHALL accept volume target specifying the number of test steps to generate.

#### Scenario: Generate specified volume
- **WHEN** volume target of 10000 steps is specified
- **THEN** system generates exactly 10000 test steps (SEND rows)

#### Scenario: Zero volume target
- **WHEN** volume target is zero or negative
- **THEN** system SHALL reject with validation error

### Requirement: Deterministic Replay Support
The system SHALL support optional seed parameter for deterministic test generation. Same seed plus same initial state SHALL produce identical output.

#### Scenario: Reproducible generation with seed
- **WHEN** same seed (42) and same initial state are used in two runs
- **THEN** both runs produce identical test_cases.csv content

#### Scenario: Different seeds produce different output
- **WHEN** different seeds are used with same initial state
- **THEN** generated test cases differ in message selection and parameters

### Requirement: Output Hybrid CSV Format
The system SHALL output test cases in hybrid CSV format with wide columns for common fields and JSON payload column for complete data.

#### Scenario: CSV contains wide columns
- **WHEN** test cases are generated
- **THEN** CSV includes columns: step_id, direction, message_type, symbol, side, quantity, price, order_id, cl_ord_id, orig_cl_ord_id, status, exec_type, reason, payload_json

#### Scenario: CSV contains JSON payload
- **WHEN** test case with complex parameters is generated
- **THEN** payload_json column contains complete serialized message data

### Requirement: Send/Receive Message Pairs
The system SHALL generate SEND rows for outbound messages and RECEIVE rows for predicted responses, with ID-based mapping between them.

#### Scenario: New order generates send and receive pair
- **WHEN** NewOrderSingle message is generated
- **THEN** CSV contains SEND row with request parameters followed by RECEIVE row(s) with predicted ExecutionReport

#### Scenario: Multiple receives for partial fill
- **WHEN** order results in multiple partial fills
- **THEN** CSV contains one SEND row followed by multiple RECEIVE rows with same cl_ord_id

### Requirement: Output Coverage Report
The system SHALL output coverage report in JSON format with multi-level coverage analysis.

#### Scenario: Coverage report includes message type coverage
- **WHEN** test generation completes
- **THEN** coverage report includes percentage of message types executed

#### Scenario: Coverage report includes gap analysis
- **WHEN** coverage gaps exist
- **THEN** report lists missed message types and suggests areas for additional testing

### Requirement: Save Initial State for Replay
The system SHALL save the initial state used for generation to enable test replay capability.

#### Scenario: Initial state persisted
- **WHEN** test generation completes
- **THEN** initial_state.json file is saved in output directory with exact state used for generation

#### Scenario: Replay uses saved state
- **WHEN** saved initial_state.json is loaded for replay
- **THEN** system produces identical test cases (with same seed)

### Requirement: Output Directory Structure
The system SHALL create output directory with metadata.json, initial_state.json, test_cases.csv, and coverage_report.json.

#### Scenario: Complete output structure
- **WHEN** test generation runs
- **THEN** output directory contains all four required files

#### Scenario: Metadata includes generation info
- **WHEN** metadata.json is created
- **THEN** it includes run_id, seed, scenario, timestamp, and configuration summary
