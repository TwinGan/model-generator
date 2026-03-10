# Execution Report

**Domain:** Binary Order Entry  
**Template ID:** 20  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Execution Report message for LME Binary Order Entry protocol. Sent by the gateway to report order state changes, fills, and cancellations.

## Message Specification

### Binary Protocol Details
- **Template ID:** 20
- **Message Name:** Execution Report
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §4.10.20

## Message Structure
```
Execution Report (Template ID: 20)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 20
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── OrderID (String)
    ├── ClOrdID (String)
    ├── ExecID (String)
    ├── ExecType (UInt8)
    ├── OrdStatus (UInt8)
    ├── SecurityID (String)
    ├── Side (UInt8)
    ├── OrderQty (Int32)
    ├── LastQty (Int32, conditional)
    ├── LastPx (Int64, conditional)
    └── Additional fields
```

## Message Interaction Flow

### New Order Acknowledgment
```
Client → Gateway: New Order (Template 10)
Gateway → Client: Execution Report (Template 20) with ExecType=0, OrdStatus=0
```

### Fill Report
```
Gateway → Client: Execution Report (Template 20) with ExecType=2, OrdStatus=1 or 2
```

### Cancel Acknowledgment
```
Client → Gateway: Order Cancel (Template 11)
Gateway → Client: Execution Report (Template 20) with ExecType=4, OrdStatus=4
```

## Fields Reference

### Required Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| OrderID | String(20) | Required | Exchange-assigned order ID |
| ClOrdID | String(20) | Required | Client order ID |
| ExecID | String(20) | Required | Unique execution ID |
| ExecType | UInt8 | Required | Type of execution |
| OrdStatus | UInt8 | Required | Current order status |
| SecurityID | String(20) | Required | Instrument symbol |
| Side | UInt8 | Required | Order side (1=Buy, 2=Sell) |
| OrderQty | Int32 | Required | Original order quantity |

### Conditional Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| LastQty | Int32 | Conditional | Fill quantity (present on fills) |
| LastPx | Int64 | Conditional | Fill price (present on fills) |
| LeavesQty | Int32 | Required | Remaining quantity |
| CumQty | Int32 | Required | Cumulative filled quantity |
| AvgPx | Int64 | Required | Average fill price |
| TransactTime | UInt64 | Required | Transaction timestamp |

## ExecType Values
| Code | Name | Description |
|------|------|-------------|
| 0 | NEW | Order acknowledged |
| 1 | PARTIAL_FILL | Partial fill |
| 2 | FILL | Full fill |
| 3 | DONE_FOR_DAY | Done for day |
| 4 | CANCELED | Order cancelled |
| 5 | REPLACE | Order replaced |
| 8 | REJECTED | Order rejected |
| F | TRADE | Trade (alternative to FILL) |

## OrdStatus Values
| Code | Name | Description |
|------|------|-------------|
| 0 | NEW | New order |
| 1 | PARTIALLY_FILLED | Partially filled |
| 2 | FILLED | Fully filled |
| 4 | CANCELLED | Cancelled |
| 8 | REJECTED | Rejected |
| C | EXPIRED | Expired |

## Message Example (Binary Hex Dump)

### Example: New Order Acknowledgment
```
00 3C          # Message Length: 60 bytes
14 00          # Template ID: 20
01 00          # Schema ID: 1
FF             # Presence Map: All fields present
08 4F 52 44 30 30 30 30 31  # OrderID: "ORD00001"
08 43 4C 30 30 30 30 30 31  # ClOrdID: "CL000001"
08 45 58 45 43 30 30 30 31  # ExecID: "EXEC0001"
00             # ExecType: 0 (NEW)
00             # OrdStatus: 0 (NEW)
02 43 41       # SecurityID: "CA"
01             # Side: 1 (Buy)
0A 00 00 00    # OrderQty: 10
0A 00 00 00    # LeavesQty: 10
00 00 00 00    # CumQty: 0
00 00 00 00 00 00 00 00  # AvgPx: 0
```

### Example: Fill Report
```
00 42          # Message Length: 66 bytes
14 00          # Template ID: 20
01 00          # Schema ID: 1
FF             # Presence Map: All fields present
08 4F 52 44 30 30 30 30 31  # OrderID: "ORD00001"
08 43 4C 30 30 30 30 30 31  # ClOrdID: "CL000001"
08 45 58 45 43 30 30 30 32  # ExecID: "EXEC0002"
02             # ExecType: 2 (FILL)
02             # OrdStatus: 2 (FILLED)
02 43 41       # SecurityID: "CA"
01             # Side: 1 (Buy)
0A 00 00 00    # OrderQty: 10
05 00 00 00    # LastQty: 5
00 E2 30 3A 00 00 00 00  # LastPx: 250050000000 (2500.50)
00 00 00 00    # LeavesQty: 0
05 00 00 00    # CumQty: 5
00 E2 30 3A 00 00 00 00  # AvgPx: 250050000000
```

## References

- **Source:** Binary Order Entry Specification v1.9.1 §4.10.20
- **Order Status:** See [state-machines.md](../../reference/state-machines.md)
