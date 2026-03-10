# Session State Model

Add session lifecycle state management for FIX/Binary connections.

## ADDED Requirements

### Requirement: Session States Defined

The digital twin SHALL define all session lifecycle states.

#### Scenario: Session state enum includes all states

- **WHEN** code references SessionState enum
- **THEN** it SHALL include: DISCONNECTED, CONNECTING, AUTHENTICATING, CONNECTED, LOGGING_OUT

### Requirement: Initial Session State

Sessions SHALL start in DISCONNECTED state.

#### Scenario: Session starts disconnected

- **WHEN** a new session is created
- **THEN** its state SHALL be DISCONNECTED

### Requirement: Connection State Transitions

Connection establishment SHALL follow defined state transitions.

#### Scenario: TCP connection initiates

- **WHEN** a TCP connection is initiated
- **THEN** session state SHALL transition to CONNECTING

#### Scenario: Logon sent

- **WHEN** a Logon message is sent
- **THEN** session state SHALL transition to AUTHENTICATING

#### Scenario: Logon accepted

- **WHEN** a Logon response is accepted
- **THEN** session state SHALL transition to CONNECTED

#### Scenario: Logon rejected

- **WHEN** a Logon response is rejected
- **THEN** session state SHALL transition to DISCONNECTED

### Requirement: Logout State Transitions

Session termination SHALL follow defined state transitions.

#### Scenario: Logout initiated

- **WHEN** a Logout message is sent
- **THEN** session state SHALL transition to LOGGING_OUT

#### Scenario: Logout complete

- **WHEN** logout completes
- **THEN** session state SHALL transition to DISCONNECTED

### Requirement: Orders Only In Connected State

Orders SHALL only be accepted when session is CONNECTED.

#### Scenario: Order accepted in connected state

- **WHEN** an order is submitted while session state is CONNECTED
- **THEN** the order SHALL be processed

#### Scenario: Order rejected in non-connected state

- **WHEN** an order is submitted while session state is NOT CONNECTED
- **THEN** the order SHALL be rejected

### Requirement: Session Status In Logout

Logout messages SHALL include session status.

#### Scenario: Logout includes session status

- **WHEN** a Logout (35=5) message is sent
- **THEN** it SHALL include SessionStatus (1409) field with appropriate value
