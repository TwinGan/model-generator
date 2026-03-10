# New Order Cross

**Domain:** Order Entry  
**Message Type:** s  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

New Order Cross message for LME Order Entry Gateway. Used to submit a cross order where the same member acts as both buyer and seller, or to facilitate crossing between two counterparties.

## Message Specification

### FIX Protocol Details
- **Message Type:** `s`
- **Message Name:** New Order Cross
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §3.14

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: New Order Cross (s)
Gateway → Client: Execution Report (8) for both sides
```

### Failure Scenario
```
Client → Gateway: New Order Cross (s)
Gateway → Client: Business Message Reject (j) with reject reason
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = s |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 548 | CrossID | String | Required | Unique cross order identifier |
| 549 | CrossType | Int | Required | Type of cross order |
| 550 | NoSides | Int | Required | Number of sides (1 or 2) |
| 552 | NoTradingSessions | NumInGroup | Required | Number of trading sessions group |

### Cross Type Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | CROSS_IOC | Cross order which is executed completely or not; partial executions not allowed | FIX Spec §3.14 |
| 2 | CROSS_FOK | Cross order is executed immediately and completely or cancelled | FIX Spec §3.14 |
| 3 | CROSS_ON_CLOSE | Cross order is on close | FIX Spec §3.14 |
| 4 | CROSS_ON_OPEN | Cross order is on open | FIX Spec §3.14 |
| 5 | AUTO_CROSS | Auto cross (internal matching) | FIX Spec §3.14 |

### Side Group Fields (NoSides = 1 or 2)
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 54 | Side | Char | Required | Side of order (1=Buy, 2=Sell) |
| 11 | ClOrdID | String | Required | Client order ID |
| 38 | OrderQty | Qty | Required | Order quantity |
| 44 | Price | Price | Optional | Limit price |
| 453 | NoPartyIDs | NumInGroup | Optional | Party identification group |
| 539 | NoPartyIDs | NumInGroup | Optional | Party IDs for this side |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 551 | CrossPrioritization | Int | Optional | Prioritization of cross order |
| 560 | SecurityIDSource | Int | Optional | Security ID source |
| 48 | SecurityID | String | Optional | Security ID |
| 55 | Symbol | String | Optional | Instrument symbol |
| 526 | SecondaryClOrdID | String | Optional | Secondary order ID |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |
| 59 | TimeInForce | Char | Optional | Time in force |
| 126 | ExpireTime | UTCTimestamp | Optional | Expiration time |
| 432 | ExpireDate | LocalMktDate | Optional | Expiration date |
| 58 | Text | String | Optional | Free-form text |

## CrossPrioritization Values
| Code | Name | Description |
|------|------|-------------|
| 0 | NONE | No prioritization |
| 1 | BUY_SIDE_FIRST | Buy side executed first |
| 2 | SELL_SIDE_FIRST | Sell side executed first |
| 3 | BOTH_SIDES_FIRST | Both sides executed first |

## LME Auto Cross Rules

### Requirements
- Only permitted for certain member types
- Both counterparties must have sufficient credit
- Cross price must be within valid trading range
- Cannot cross against own orders on the book

### Validation
1. Verify cross eligibility for member
2. Validate both sides of cross
3. Check credit limits for both parties
4. Verify price is within band

## Message Example (Tabby CSV Format)

### Example: Two-Sided Cross Order
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,CrossID,CrossType,NoSides,Symbol
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,CROSS001,2,2,CA
```

### Example: One-Sided Auto Cross
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,CrossID,CrossType,NoSides,Symbol
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,CROSS002,5,1,CA
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- Sequence numbers must be in order
- CrossID must be unique
- Both sides must have valid order details
- Counterparties must be authorized for cross orders

### Execution
1. Validate cross order structure
2. Check counterparty eligibility
3. Execute cross if valid
4. Generate Execution Reports for both sides

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §3.14
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **Symbols:** See [symbols.md](../../reference/symbols.md)
