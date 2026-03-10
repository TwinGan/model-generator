# Order Cancel Replace Request

**Domain:** Order Entry  
**Message Type:** G  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview
Order Cancel/Replace Request message for LME Order Entry Gateway. Used to modify an existing order (change price, quantity, etc.) or cancel and order.

## Message Specification
### FIX Protocol Details
- **Message Type:** `G`
- **Message Name:** Order Cancel/Replace Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §3.10

## Message Interaction Flow
### Success Scenario - Modify
```
Client → Gateway: Order Cancel/Replace Request (G)
Gateway → Client: Execution Report (8) with OrdStatus=REPLACED
```

### Success Scenario - Cancel
```
Client → Gateway: Order Cancel/Replace Request (G)
Gateway → Client: Execution Report (8) with OrdStatus=CANCELLED
```

### Failure Scenario
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
| 11 | ClOrdID | String | Required | New client order ID for this request |
| 35 | MsgType | String | Required | Message type = G |
| 41 | OrigClOrdID | String | Required | Original client order ID of order to modify |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |

### Modifiable Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 38 | OrderQty | Qty | Optional | New order quantity (if changing) |
| 44 | Price | Price | Optional | New limit price (if changing) |
| 99 | StopPx | Price | Optional | New stop price (if changing) |
| 40 | OrdType | Char | Optional | New order type (if changing) |
| 59 | TimeInForce | Char | Optional | New time in force (if changing) |
| 126 | ExpireTime | UTCTimestamp | Optional | New expiration time |
| 432 | ExpireDate | LocalMktDate | Optional | New expiration date (GTD orders) |
| 1138 | DisplayQty | Qty | Optional | New display quantity (iceberg orders) |
| 4472 | DisplayMethod | Int | Optional | Display method |

### Context Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 37 | OrderID | String | Optional | Exchange-assigned order ID |
| 54 | Side | Char | Optional | Side of order (1=Buy, 2=Sell) |
| 55 | Symbol | String | Optional | Instrument symbol |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |

### LME-Specific Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 452 | PartyRole | Int | Optional | Party role |
| 802 | NoPartyIDs | NumInGroup | Optional | Number of party IDs |
| 58 | Text | String | Optional | Free-form text (cancel/replace reason) |

## Validation Rules
1. Either OrderID (37) or OrigClOrdID (41) must be present
2. At least one modifiable field must be present (otherwise use Order Cancel Request F)
3. Cannot modify FILLED, CANCELLED, REJECTED, or EXPIRED orders
4. Price (44) must be valid per symbol's tick size
5. OrderQty (38) cannot exceed maximum order quantity (9,999 lots)

## Inflight Order Handling
### LMEselect Inflight Rules
- Orders can be modified while resting on the order book
- Price changes trigger immediate re-matching
- Quantity reductions may trigger partial fills

### Processing Steps
1. Validate request (session, sequence, original order exists)
2. Apply modifications to order
3. Check for matching opportunities
4. Generate Execution Report with new state

## Error Codes
| CxlRejReason | Description |
|------------|-------------|
| 0 | TOO_LATE_TO_CANCEL - Order already filled/executed |
| 1 | UNKNOWN_ORDER - Original order not found |
| 5 | ORIG_ORD_MOD_NOT_ALLOWED - Modification not allowed for this order |
| 6 | DUPLICATE_ORDER - ClOrdID already used |
| 7 | OTHER - See Text (58) for details |

## Message Example (Tabby CSV Format)
### Example: Replace Request (change price)
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ClOrdID,OrigClOrdID,OrderID,Price
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,CL000006,CL000001,ORD000001,2500.50
```

### Example: Cancel Request (reduce qty to zero)
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ClOrdID,OrigClOrdID,OrderID,OrderQty
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,CL000007,CL000001,ORD000001,0
```

## References
- **Source:** Order Entry Gateway FIX Specification v1.9.1 §3.10
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **State Machine:** See [state-machines.md](../../reference/state-machines.md)
