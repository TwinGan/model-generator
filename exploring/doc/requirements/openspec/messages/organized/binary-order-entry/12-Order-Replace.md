# Order Replace

**Domain:** Binary Order Entry  
**Template ID:** 12  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Order Replace message for LME Binary Order Entry protocol. Used to modify an existing order (change price, quantity, etc.).

## Message Specification

### Binary Protocol Details
- **Template ID:** 12
- **Message Name:** Order Replace
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §4.10.12

## Message Structure
```
Order Replace (Template ID: 12)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 12
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── ClOrdID (String)
    ├── OrigClOrdID (String)
    ├── OrderQty (Int32, optional)
    ├── Price (Int64, optional)
    └── StopPx (Int64, optional)
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Order Replace (Binary Template 12)
Gateway → Client: Execution Report (Binary Template 20) with OrdStatus=REPLACED
```

### Failure Scenario
```
Client → Gateway: Order Replace (Binary Template 12)
Gateway → Client: Order Cancel Reject (Binary Template 21) with CxlRejReason
```

## Fields Reference

### Required Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| ClOrdID | String(20) | Required | New client order ID for this request |
| OrigClOrdID | String(20) | Required | Original client order ID |

### Modifiable Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| OrderQty | Int32 | Optional | New order quantity |
| Price | Int64 | Optional | New limit price (scaled by 10^8) |
| StopPx | Int64 | Optional | New stop price (scaled by 10^8) |
| TimeInForce | UInt8 | Optional | New time in force |
| ExpireDate | UInt16 | Optional | New expiration date |
| DisplayQty | Int32 | Optional | New display quantity (iceberg) |

## Message Example (Binary Hex Dump)

### Example: Modify Price
```
00 28          # Message Length: 40 bytes
0C 00          # Template ID: 12
01 00          # Schema ID: 1
1F             # Presence Map: ClOrdID + OrigClOrdID + Price
08 43 4C 30 30 30 30 30 33  # ClOrdID: "CL000003"
08 43 4C 30 30 30 30 30 31  # OrigClOrdID: "CL000001"
00 F4 3B 49 00 00 00 00  # Price: 260000000000 (2600.00)
```

## Processing Rules

### Validation Requirements
1. Original order must exist and be in modifiable state
2. Cannot modify FILLED, CANCELLED, REJECTED, or EXPIRED orders
3. At least one modifiable field must be present
4. Price changes may trigger re-matching

## References

- **Source:** Binary Order Entry Specification v1.9.1 §4.10.12
