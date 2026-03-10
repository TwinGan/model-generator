# Order Cancel

**Domain:** Binary Order Entry  
**Template ID:** 11  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Order Cancel message for LME Binary Order Entry protocol. Used to request cancellation of an existing order.

## Message Specification

### Binary Protocol Details
- **Template ID:** 11
- **Message Name:** Order Cancel
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §4.10.11

## Message Structure
```
Order Cancel (Template ID: 11)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 11
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── ClOrdID (String)
    ├── OrigClOrdID (String, optional)
    ├── OrderID (String, optional)
    └── Side (UInt8, optional)
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Order Cancel (Binary Template 11)
Gateway → Client: Execution Report (Binary Template 20) with OrdStatus=CANCELLED
```

### Failure Scenario
```
Client → Gateway: Order Cancel (Binary Template 11)
Gateway → Client: Order Cancel Reject (Binary Template 21) with CxlRejReason
```

## Fields Reference

### Required Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| ClOrdID | String(20) | Required | Client order ID for this cancel request |
| OrigClOrdID | String(20) | Conditional | Original order ID (or OrderID) |

### Optional Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| OrderID | String(20) | Conditional | Exchange-assigned order ID |
| Side | UInt8 | Optional | Side of order (1=Buy, 2=Sell) |
| SecurityID | String(20) | Optional | Instrument symbol |
| OrderQty | Int32 | Optional | Order quantity (for verification) |

## Side Values
| Code | Name | Description |
|------|------|-------------|
| 1 | BUY | Buy order |
| 2 | SELL | Sell order |

## Message Example (Binary Hex Dump)

### Example: Cancel Order by OrigClOrdID
```
00 1E          # Message Length: 30 bytes
0B 00          # Template ID: 11
01 00          # Schema ID: 1
03             # Presence Map: ClOrdID + OrigClOrdID present
08 43 4C 30 30 30 30 30 32  # ClOrdID: "CL000002"
08 43 4C 30 30 30 30 30 31  # OrigClOrdID: "CL000001"
```

## Processing Rules

### Validation Requirements
1. Either OrigClOrdID or OrderID must be present
2. Original order must exist and be in cancellable state
3. Cannot cancel orders in FILLED, CANCELLED, REJECTED, or EXPIRED state
4. Valid session must be established

### CxlRejReason Values
| Code | Name | Description |
|------|------|-------------|
| 0 | TOO_LATE_TO_CANCEL | Order already filled |
| 1 | UNKNOWN_ORDER | Order not found |
| 2 | ALREADY_PENDING_CANCEL | Cancel already pending |
| 3 | ALREADY_CANCELLED | Order already cancelled |
| 4 | ALREADY_FILLED | Order fully filled |
| 6 | DUPLICATE_ORDER | ClOrdID already used |

## References

- **Source:** Binary Order Entry Specification v1.9.1 §4.10.11
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
