# Order Reject

**Domain:** Binary Order Entry  
**Template ID:** 21  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Order Reject message for LME Binary Order Entry protocol. Sent when an order is rejected by the gateway.

## Message Specification

### Binary Protocol Details
- **Template ID:** 21
- **Message Name:** Order Reject
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §4.10.21

## Message Structure
```
Order Reject (Template ID: 21)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 21
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── ClOrdID (String)
    ├── OrdRejReason (UInt8)
    └── Text (String, optional)
```

## Message Interaction Flow

### Order Rejection Scenario
```
Client → Gateway: New Order (Template 10)
Gateway → Client: Order Reject (Template 21) with OrdRejReason
```

### Cancel Rejection Scenario
```
Client → Gateway: Order Cancel (Template 11)
Gateway → Client: Order Reject (Template 21) with CxlRejReason
```

## Fields Reference

### Required Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| ClOrdID | String(20) | Required | Client order ID from rejected request |
| OrdRejReason | UInt8 | Required | Reason for rejection |

### Optional Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| Text | String(256) | Optional | Free-form rejection text |
| SecurityID | String(20) | Optional | Instrument symbol |
| Side | UInt8 | Optional | Order side |

## OrdRejReason Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | BROKER | Broker option | Binary Spec §4.10.21 |
| 1 | UNKNOWN_SYMBOL | Unknown symbol | Binary Spec §4.10.21 |
| 2 | EXCHANGE_CLOSED | Exchange closed | Binary Spec §4.10.21 |
| 3 | ORDER_EXCEEDS_LIMIT | Order exceeds limit | Binary Spec §4.10.21 |
| 4 | TOO_LATE_TO_ENTER | Too late to enter | Binary Spec §4.10.21 |
| 5 | UNKNOWN_ORDER | Unknown order | Binary Spec §4.10.21 |
| 6 | DUPLICATE_ORDER | Duplicate ClOrdID | Binary Spec §4.10.21 |
| 8 | INVALID_PRICE | Invalid price | Binary Spec §4.10.21 |
| 9 | INVALID_QUANTITY | Invalid quantity | Binary Spec §4.10.21 |
| 10 | INVALID_ORDER_TYPE | Invalid order type | Binary Spec §4.10.21 |
| 11 | INVALID_SIDE | Invalid side | Binary Spec §4.10.21 |
| 12 | INVALID_TIF | Invalid TimeInForce | Binary Spec §4.10.21 |
| 19 | EXCEEDS_MAXIMUM_QUANTITY | Exceeds max qty (9,999) | Binary Spec §4.10.21 |
| 20 | EXCEEDS_MAXIMUM_VALUE | Exceeds max value | Binary Spec §4.10.21 |
| 25 | INSUFFICIENT_CREDIT | Insufficient credit | Binary Spec §4.10.21 |
| 26 | RISK_LIMIT_EXCEEDED | Risk limit exceeded | Binary Spec §4.10.21 |
| 99 | OTHER | See Text field | Binary Spec §4.10.21 |

## Message Example (Binary Hex Dump)

### Example: Reject for Invalid Symbol
```
00 1C          # Message Length: 28 bytes
15 00          # Template ID: 21
01 00          # Schema ID: 1
07             # Presence Map: ClOrdID + OrdRejReason present
08 43 4C 30 30 30 30 30 31  # ClOrdID: "CL000001"
01             # OrdRejReason: 1 (UNKNOWN_SYMBOL)
```

### Example: Reject for Risk Limit Exceeded
```
00 2A          # Message Length: 42 bytes
15 00          # Template ID: 21
01 00          # Schema ID: 1
0F             # Presence Map: ClOrdID + OrdRejReason + Text
08 43 4C 30 30 30 30 30 32  # ClOrdID: "CL000002"
1A             # OrdRejReason: 26 (RISK_LIMIT_EXCEEDED)
10 45 78 63 65 65 64 73 20 70 6F 73 69 74 69 6F 6E 20 6C 69 6D 69 74  # Text: "Exceeds position limit"
```

## Processing Rules

### Rejection Scenarios
1. **Validation Failure**: Order fails validation rules
2. **Risk Check Failure**: Order exceeds risk limits
3. **Market State**: Order rejected due to market state
4. **Duplicate Order**: ClOrdID already exists

### Response Generation
1. Use ClOrdID from the rejected request
2. Include appropriate OrdRejReason code
3. Include Text with additional details if helpful

## References

- **Source:** Binary Order Entry Specification v1.9.1 §4.10.21
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
