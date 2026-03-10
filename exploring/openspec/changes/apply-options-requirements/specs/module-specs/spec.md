# Module Specifications Enhancement

Add concrete values, state machines, and validation rules to all 7 functional modules.

## MODIFIED Requirements

### Requirement: Concrete Numeric Values in Modules

All 7 module specifications SHALL include concrete numeric values extracted from source specifications.

The following modules SHALL be updated:
- `specs/session-management/spec.md`
- `specs/order-management/spec.md`
- `specs/risk-management/spec.md`
- `specs/matching-engine/spec.md`
- `specs/reliability/spec.md`
- `specs/connectivity/spec.md`
- `specs/examples/spec.md`

#### Scenario: Session management has timeout values

- **WHEN** a developer reads session-management/spec.md
- **THEN** they SHALL find: Heartbeat interval = 30 seconds, Session timeout = 90 seconds (3 heartbeats), Max failed auth attempts = 5

#### Scenario: Order management has limit values

- **WHEN** a developer reads order-management/spec.md
- **THEN** they SHALL find: Max OrderQty = 9,999 lots, Max Price = 9,999,999, Min OrderQty = 1 lot

#### Scenario: Matching engine has trading hours

- **WHEN** a developer reads matching-engine/spec.md
- **THEN** they SHALL find: LMEselect hours = 01:00-19:00 London time, TOM Trading Deadline = 12:30, TOM Matching Deadline = 13:30, Trade Input Deadline = 20:00

### Requirement: State Machine References in Modules

All module specifications SHALL reference the formal state machine definitions.

#### Scenario: Session module references session state machine

- **WHEN** a developer reads session-management/spec.md
- **THEN** they SHALL find a reference to the session state machine in `openspec/reference/state-machines.md`

#### Scenario: Order module references order state machine

- **WHEN** a developer reads order-management/spec.md
- **THEN** they SHALL find a reference to the order state machine in `openspec/reference/state-machines.md`

#### Scenario: Risk module references risk state machine

- **WHEN** a developer reads risk-management/spec.md
- **THEN** they SHALL find a reference to the risk state machine in `openspec/reference/state-machines.md`

### Requirement: Validation Rule References in Modules

All module specifications SHALL reference the validation rule catalog.

#### Scenario: Order module references validation rules

- **WHEN** a developer reads order-management/spec.md
- **THEN** they SHALL find references to relevant validation rules in `openspec/reference/validation-rules.md`

#### Scenario: Session module references validation rules

- **WHEN** a developer reads session-management/spec.md
- **THEN** they SHALL find references to Logon validation rules in `openspec/reference/validation-rules.md`

### Requirement: Test Templates Replaced with Actual Test Cases

All test.md files SHALL have template placeholders replaced with actual test cases.

#### Scenario: Session test.md has actual tests

- **WHEN** a developer reads session-management/test.md
- **THEN** they SHALL find test cases with specific IDs (TC-SESSION-001, etc.), specific input values, and expected outputs

#### Scenario: Order test.md has actual tests

- **WHEN** a developer reads order-management/test.md
- **THEN** they SHALL find test cases for order submission, modification, cancellation with specific values

#### Scenario: Risk test.md has actual tests

- **WHEN** a developer reads risk-management/test.md
- **THEN** they SHALL find test cases for limit checking, breach handling with specific values

### Requirement: Connectivity Capability Definition

The connectivity module SHALL have complete capability definitions (currently placeholder).

#### Scenario: Connectivity capabilities defined

- **WHEN** a developer reads connectivity/spec.md
- **THEN** they SHALL find defined capabilities for FIX protocol support and Binary protocol support (not placeholder text)

#### Scenario: FIX version documented

- **WHEN** a developer reads connectivity capabilities
- **THEN** they SHALL find that LME uses FIX 4.4/5.0 with LME extensions
