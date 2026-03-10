# State Machine Definitions

Define formal state machines for session lifecycle, order states, risk states, and matching states using Mermaid notation.

## ADDED Requirements

### Requirement: Session State Machine

The requirements documentation SHALL include a formal state machine diagram for FIX/Binary session lifecycle.

#### Scenario: Developer implements session handling

- **WHEN** a developer needs to implement session state transitions
- **THEN** they can reference `openspec/reference/state-machines.md` for the session state diagram with states: DISCONNECTED, CONNECTING, AUTHENTICATING, CONNECTED, CLOSING

#### Scenario: Session state transitions documented

- **WHEN** the session state machine is consulted
- **THEN** it SHALL show valid transitions:
  - DISCONNECTED → CONNECTING (on socket connect)
  - CONNECTING → AUTHENTICATING (on Logon sent)
  - AUTHENTICATING → CONNECTED (on Logon ack)
  - AUTHENTICATING → DISCONNECTED (on auth failure)
  - CONNECTED → CLOSING (on Logout initiated)
  - CLOSING → DISCONNECTED (on connection close)

### Requirement: Order State Machine

The requirements documentation SHALL include a formal state machine diagram for order lifecycle.

#### Scenario: Developer implements order handling

- **WHEN** a developer needs to implement order state transitions
- **THEN** they can reference `openspec/reference/state-machines.md` for the order state diagram with states: NEW, PARTIALLY_FILLED, FILLED, CANCELLED, REJECTED, EXPIRED

#### Scenario: Order state transitions documented

- **WHEN** the order state machine is consulted
- **THEN** it SHALL show valid transitions:
  - NEW → PARTIALLY_FILLED (partial execution)
  - NEW → FILLED (full execution)
  - NEW → CANCELLED (cancel request honored)
  - NEW → REJECTED (validation failure)
  - PARTIALLY_FILLED → FILLED (remaining execution)
  - PARTIALLY_FILLED → CANCELLED (cancel remaining)

### Requirement: Risk State Machine

The requirements documentation SHALL include a formal state machine diagram for risk limit states.

#### Scenario: Developer implements risk monitoring

- **WHEN** a developer needs to implement risk limit monitoring
- **THEN** they can reference `openspec/reference/state-machines.md` for the risk state diagram with states: WITHIN_LIMITS, APPROACHING_LIMIT, AT_LIMIT, BREACHED

#### Scenario: Risk state transitions documented

- **WHEN** the risk state machine is consulted
- **THEN** it SHALL show valid transitions:
  - WITHIN_LIMITS → APPROACHING_LIMIT (utilization exceeds 80%)
  - APPROACHING_LIMIT → AT_LIMIT (utilization reaches 100%)
  - AT_LIMIT → BREACHED (order exceeds limit)
  - BREACHED → WITHIN_LIMITS (limit increased or position reduced)

### Requirement: Mermaid Notation

All state machine diagrams SHALL use Mermaid stateDiagram-v2 syntax.

#### Scenario: State diagram renders in GitHub

- **WHEN** a state machine is viewed on GitHub
- **THEN** it SHALL render as a visual diagram using Mermaid syntax

#### Scenario: State diagram is validatable

- **WHEN** a state machine definition is processed
- **THEN** it SHALL be valid Mermaid stateDiagram-v2 syntax
