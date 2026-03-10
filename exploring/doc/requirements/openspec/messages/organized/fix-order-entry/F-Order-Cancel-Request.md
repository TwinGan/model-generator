# Order Cancel Request

**Domain:** Order Entry  
**Message Type:** F  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Order Cancel Request message for LME Order Entry Gateway. Used to request cancellation of an existing order.

## Message Specification

### FIX Protocol Details
- **Message Type:** `F`
- **Message Name:** Order Cancel Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.11.6

## Message Interaction Flow
### Success Scenario
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Execution Report (8) with OrdStatus=CANCELLED
```

### Failure Scenario
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Order Cancel Reject (9) with CxlRejReason
```

### Alternative Scenario
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Execution Report (8) with OrdStatus=PARTIALLY_FILLED (partial cancel)
```

## Fields Reference
### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version (e.g., FIXT.1.1) |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum (3-byte) |
| 11 | ClOrdID | String | Required | Unique client order ID for this cancel request |
| 35 | MsgType | String | Required | Message type = F |
| 41 | OrigClOrdID | String | Required | Original client order ID of order to cancel |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 54 | Side | Char | Required | Side of original order (1=Buy, 2=Sell) |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 37 | OrderID | String | Optional | Exchange-assigned order ID (if known) |
| 55 | Symbol | String | Optional | Instrument symbol |
| 38 | OrderQty | Qty | Optional | Order quantity (for verification) |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |
| 453 | SecurityType | Int | Optional | Security type |
| 448 | SecurityIDSource | Int | Optional | Security ID source |
| 526 | SecondaryClOrdID | String | Optional | Secondary order ID |
| 544 | SecondaryOrderID | String | Optional | Secondary order ID |
| 58 | Text | String | Optional | Free-form text (cancel reason) |

### LME-Specific Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 452 | PartyRole | Int | Optional | Party role (LME extension) |
| 802 | NoPartyIDs | NumInGroup | Optional | Number of party IDs |

## Validation Rules
1. Either OrderID (37) or OrigClOrdID (41) must be present
2. Symbol (55) should match a valid LME symbol (AL, CU, ZN, PB, NI, SN, AA, HN)
3. Side (54) must match the side of the original order
4. ClOrdID (11) must be unique per trading day

## Message Example (Tabby CSV Format)
### Example: Cancel Request for Order ORD000001
```csv
BeginString,BodyLength,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ClOrdID,OrigClOrdID,OrderID,Side,Symbol,Text
FIXT.1.1,,,F,CLIENT1,20240101-12:00:00.000,LME,CL000005,CL000001,ORD000001,1,CA,Customer requested cancel
```

## Processing Rules
### Cancel Matching Logic
1. Locate original order by OrigClOrdID (41) or OrderID (37)
2. Verify order exists and is a cancellable state (NEW or PARTIALLY_FILLED)
3. Cancel order and update state to CANCELLED
4. Generate Execution Report with OrdStatus=CANCELLED

### Validation Requirements
- Valid session must be established
- Sequence numbers must be in order
- Original order must exist and be in cancellable state
- Cannot cancel orders in FILLED, REJECTED, or EXPIRED state

## Error Codes
| CxlRejReason | Description |
|------------|-------------|
| 0 | TOO_LATE_TO_CANCEL - Order already filled/executed |
| 1 | UNKNOWN_ORDER - Original order not found |
| 2 | ALREADY_PENDING_CANCEL - Cancel already pending |
| 3 | ALREADY_CANCELLED - Order already cancelled |
| 4 | ALREADY_FILLED - Order already fully filled |
| 6 | DUPLICATE_ORDER - ClOrdID already used |
| 7 | OTHER - See Text (58) for details |

## References
- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.11.6
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **State Machine:** See [state-machines.md](../../reference/state-machines.md)
