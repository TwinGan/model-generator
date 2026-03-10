# Order Rejection Codes

Add LME-specific order rejection reason codes for structured error handling.

## ADDED Requirements

### Requirement: OrderRejectReason Enum Defined

The digital twin SHALL define an OrderRejectReason enum with LME rejection codes.

#### Scenario: Rejection enum includes core codes

- **WHEN** code references OrderRejectReason enum
- **THEN** it SHALL include codes 0-26 and 99 as defined in FIX Spec §4.11.7

### Requirement: Unknown Symbol Rejection

Orders for unknown symbols SHALL use specific rejection code.

#### Scenario: Unknown symbol rejection

- **WHEN** an order is rejected due to unknown symbol
- **THEN** OrderRejectReason SHALL be 1 (UNKNOWN_SYMBOL)

### Requirement: Exchange Closed Rejection

Orders submitted outside trading hours SHALL use specific rejection code.

#### Scenario: Exchange closed rejection

- **WHEN** an order is rejected because exchange is closed
- **THEN** OrderRejectReason SHALL be 2 (EXCHANGE_CLOSED)

### Requirement: Order Exceeds Limit Rejection

Orders exceeding limits SHALL use specific rejection code.

#### Scenario: Order exceeds limit rejection

- **WHEN** an order is rejected for exceeding position or quantity limits
- **THEN** OrderRejectReason SHALL be 3 (ORDER_EXCEEDS_LIMIT)

### Requirement: Invalid Price Rejection

Orders with invalid prices SHALL use specific rejection code.

#### Scenario: Invalid price rejection

- **WHEN** an order is rejected due to invalid price
- **THEN** OrderRejectReason SHALL be 8 (INVALID_PRICE)

### Requirement: Invalid Quantity Rejection

Orders with invalid quantities SHALL use specific rejection code.

#### Scenario: Invalid quantity rejection

- **WHEN** an order is rejected due to invalid quantity
- **THEN** OrderRejectReason SHALL be 9 (INVALID_QUANTITY)

### Requirement: Invalid Order Type Rejection

Orders with invalid order types SHALL use specific rejection code.

#### Scenario: Invalid order type rejection

- **WHEN** an order is rejected due to invalid order type
- **THEN** OrderRejectReason SHALL be 10 (INVALID_ORDER_TYPE)

### Requirement: Risk Limit Exceeded Rejection

Orders exceeding risk limits SHALL use specific rejection code.

#### Scenario: Risk limit exceeded rejection

- **WHEN** an order is rejected due to risk limit breach
- **THEN** OrderRejectReason SHALL be 26 (RISK_LIMIT_EXCEEDED)

### Requirement: Other Rejection With Text

Unspecified rejections SHALL use OTHER code with explanation.

#### Scenario: Other rejection with text

- **WHEN** an order is rejected for a reason not covered by specific codes
- **THEN** OrderRejectReason SHALL be 99 (OTHER)
- **AND** Text (58) field SHALL contain explanation

### Requirement: Rejection In Execution Report

Rejection reasons SHALL be included in Execution Report messages.

#### Scenario: Execution report includes reject reason

- **WHEN** an Execution Report (35=8) is sent with OrdStatus=REJECTED
- **THEN** it SHALL include OrdRejReason (103) field
