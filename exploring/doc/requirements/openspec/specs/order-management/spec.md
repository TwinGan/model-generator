# Order Management

Order submission, modification, cancellation, and status tracking

## Capabilities

### Order Type Support

**Source:** Order Entry Gateway FIX Specification v 1 9 1.md

Market, Limit, Stop, Stop-Limit, Iceberg, Fill-or-Kill, Good-for-Day, Good-Till-Cancel, Good-Till-Date

### Order Submission

**Source:** Order Entry Gateway FIX Specification v 1 9 1.md

New order placement with validation

### Order Modification and Cancellation

**Source:** Order Entry Gateway FIX Specification v 1 9 1.md

Amend order parameters, cancel orders, mass cancellation

## Functional Requirements


### Order Submission Requirements
- System shall accept valid orders with required fields populated
- Orders must be validated against market rules before acceptance
- System shall support multiple order types (Market, Limit, Stop, Stop-Limit, Iceberg, FOK)
- Order validity conditions must be enforced (Day, GTC, GTD)
- Minimum and maximum order quantities must be validated

### Order Modification Requirements
- System shall allow amendment of working orders
- Price and quantity updates must be validated
- Cancel/replace operations must maintain order priority where applicable
- Partial fills must be tracked accurately
- Mass cancellation must be supported for risk management
