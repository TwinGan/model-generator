# Binary Order Entry Specifications Enhancement

Replace placeholder text with actual field definitions from source specification for all 8 Binary protocol messages.

## MODIFIED Requirements

### Requirement: Placeholder Text Replaced

All 8 Binary message specifications SHALL have placeholder text "*Field definitions to be extracted from binary spec*" replaced with actual field definitions.

The following files SHALL be updated:
- `binary-order-entry/1-Logon.md`
- `binary-order-entry/2-Logout.md`
- `binary-order-entry/3-Heartbeat.md`
- `binary-order-entry/10-New-Order.md`
- `binary-order-entry/11-Order-Cancel.md`
- `binary-order-entry/12-Order-Replace.md`
- `binary-order-entry/20-Execution-Report.md`
- `binary-order-entry/21-Order-Reject.md`

#### Scenario: Logon has complete field definitions

- **WHEN** a developer reads 1-Logon.md
- **THEN** they SHALL find all Logon fields: CompID, Password, NewPassword, DefaultApplVerID, NextExpectedMsgSeqNum with data types and presence requirements

#### Scenario: New Order has complete field definitions

- **WHEN** a developer reads 10-New-Order.md
- **THEN** they SHALL find all order fields: ClOrdID, Symbol, Side, OrderQty, OrdType, Price, etc. with data types and presence requirements

### Requirement: Binary Encoding Rules

Binary message specifications SHALL document the binary encoding format.

#### Scenario: Message structure documented

- **WHEN** a developer reads a binary message spec
- **THEN** they SHALL find the message structure: Message Length (2 bytes), Template ID (2 bytes), Message Body fields

#### Scenario: Byte order documented

- **WHEN** a developer implements binary encoding
- **THEN** the spec SHALL document that multi-byte integers use little-endian encoding

#### Scenario: String encoding documented

- **WHEN** a developer implements string fields
- **THEN** the spec SHALL document string encoding (length-prefixed or null-terminated)

### Requirement: Session Management Rules

Binary specifications SHALL document session management rules specific to the binary protocol.

#### Scenario: Password encryption documented

- **WHEN** a developer implements binary Logon
- **THEN** the spec SHALL document RSA+Base64 password encryption per Binary Spec §1.1.2

#### Scenario: Heartbeat interval documented

- **WHEN** a developer implements session management
- **THEN** the spec SHALL document 3-heartbeat-interval timeout (90 seconds with 30-second heartbeat)

### Requirement: Cross-Reference to FIX Equivalents

Binary message specifications SHALL cross-reference equivalent FIX messages.

#### Scenario: Binary New Order references FIX New Order

- **WHEN** a developer reads 10-New-Order.md
- **THEN** the spec SHALL reference FIX New Order Single (D) for business rules not specific to binary encoding

#### Scenario: Binary Execution Report references FIX Execution Report

- **WHEN** a developer reads 20-Execution-Report.md
- **THEN** the spec SHALL reference FIX Execution Report (8) for business rules not specific to binary encoding
