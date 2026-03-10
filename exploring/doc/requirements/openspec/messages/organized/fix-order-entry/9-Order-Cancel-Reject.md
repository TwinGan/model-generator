# Order Cancel Reject

**Domain:** Order Entry  
**Message Type:** 9  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Order Cancel Reject message for LME Order Entry Gateway. Sent when an Order Cancel Request (F) or Order Cancel/Replace Request (G) is rejected.

## Message Specification

### FIX Protocol Details
- **Message Type:** `9`
- **Message Name:** Order Cancel Reject
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.11.7

## Message Interaction Flow

### Cancel Reject Scenario
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Order Cancel Reject (9) with CxlRejReason
```

### Replace Reject Scenario
```
Client → Gateway: Order Cancel/Replace Request (G)
Gateway → Client: Order Cancel Reject (9) with CxlRejReason
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 11 | ClOrdID | String | Required | Client order ID from the cancel/replace request |
| 35 | MsgType | String | Required | Message type = 9 |
| 37 | OrderID | String | Required | Exchange-assigned order ID of original order |
| 41 | OrigClOrdID | String | Required | Original client order ID from the request |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 102 | CxlRejReason | Int | Required | Reason for rejection |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 58 | Text | String | Optional | Free-form text (additional details) |
| 55 | Symbol | String | Optional | Instrument symbol |
| 54 | Side | Char | Optional | Side of order (1=Buy, 2=Sell) |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |
| 526 | SecondaryClOrdID | String | Optional | Secondary order ID |

## CxlRejReason Values

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | TOO_LATE_TO_CANCEL | Order already filled/executed | FIX Spec §4.11.7 |
| 1 | UNKNOWN_ORDER | Original order not found | FIX Spec §4.11.7 |
| 2 | ALREADY_PENDING_CANCEL | Cancel already pending | FIX Spec §4.11.7 |
| 3 | ALREADY_CANCELLED | Order already cancelled | FIX Spec §4.11.7 |
| 4 | ALREADY_FILLED | Order already fully filled | FIX Spec §4.11.7 |
| 5 | ORIG_ORD_MOD_NOT_ALLOWED | Original order modification not allowed | FIX Spec §4.11.7 |
| 6 | DUPLICATE_ORDER | ClOrdID already used | FIX Spec §4.11.7 |
| 7 | OTHER | See Text (58) for details | FIX Spec §4.11.7 |

## Processing Rules

### Rejection Scenarios
1. **Unknown Order**: Original order (OrigClOrdID or OrderID) not found
2. **Too Late**: Order already fully filled or executed
3. **Already Cancelled**: Order already in CANCELLED state
4. **Duplicate**: ClOrdID from request already exists
5. **Not Allowed**: Modification not permitted for this order type

### Response Generation
1. Use OrderID from original order
2. Use OrigClOrdID from original order
3. Include CxlRejReason explaining why rejected
4. Include Text with additional details if needed

## Message Example (Tabby CSV Format)

### Example: Unknown Order Reject
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,OrderID,ClOrdID,OrigClOrdID,CxlRejReason,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,LME,ORD000001,CL000008,CL000001,1,Unknown order ID
```

### Example: Too Late to Cancel Reject
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,OrderID,ClOrdID,OrigClOrdID,CxlRejReason
FIXT.1.1,,,1,,LME,20240101-12:00:02.000,LME,ORD000005,CL000009,CL000005,0
```

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.11.7
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **State Machine:** See [state-machines.md](../../reference/state-machines.md)
