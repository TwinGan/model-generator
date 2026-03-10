# Order Mass Cancel Request

**Domain:** Order Entry  
**Message Type:** q  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Order Mass Cancel Request message for LME Order Entry Gateway. Used to cancel multiple orders at once based on specified criteria (symbol, product complex, all orders, etc.).

## Message Specification

### FIX Protocol Details
- **Message Type:** `q`
- **Message Name:** Order Mass Cancel Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §3.12, §4.11.10

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Order Mass Cancel Request (q)
Gateway → Client: Order Mass Cancel Report (r) with MassCancelResponse=0
```

### Partial Success Scenario
```
Client → Gateway: Order Mass Cancel Request (q)
Gateway → Client: Order Mass Cancel Report (r) with TotalAffectedOrders > 0
```

### Failure Scenario
```
Client → Gateway: Order Mass Cancel Request (q)
Gateway → Client: Order Mass Cancel Report (r) with MassCancelRejectReason
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 11 | ClOrdID | String | Required | Unique client order ID for this request |
| 35 | MsgType | String | Required | Message type = q |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 530 | MassCancelRequestType | Int | Required | Scope of mass cancel |

### Optional Scope Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 48 | SecurityID | String | Optional | Security ID to cancel orders for |
| 22 | SecurityIDSource | Int | Optional | Security ID source (8=Exchange Symbol) |
| 55 | Symbol | String | Optional | Instrument symbol |
| 460 | Product | Int | Optional | Product code |
| 1227 | ProductComplex | Int | Optional | Product complex |
| 452 | PartyRole | Int | Optional | Party role filter |
| 453 | NoPartyIDs | NumInGroup | Optional | Party identification group |
| 526 | SecondaryClOrdID | String | Optional | Secondary order ID |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |
| 58 | Text | String | Optional | Free-form text |

## MassCancelRequestType Values

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | CANCEL_SYMBOL | Cancel all orders for a specific symbol | FIX Spec §3.12 |
| 2 | CANCEL_SECURITY_TYPE | Cancel all orders for a security type | FIX Spec §3.12 |
| 3 | CANCEL_PRODUCT | Cancel all orders for a product | FIX Spec §3.12 |
| 4 | CANCEL_CFICODE | Cancel all orders for a CFICode | FIX Spec §3.12 |
| 5 | CANCEL_SECURITYTYPE_AND_CFICODE | Cancel all orders for security type and CFICode | FIX Spec §3.12 |
| 6 | CANCEL_PRODUCT_AND_SECURITYTYPE | Cancel all orders for product and security type | FIX Spec §3.12 |
| 7 | CANCEL_PRODUCT_AND_CFICODE | Cancel all orders for product and CFICode | FIX Spec §3.12 |
| 8 | CANCEL_ALL_ORDERS | Cancel all orders for the trading session | FIX Spec §3.12 |
| 9 | CANCEL_PRODUCT_COMPLEX | Cancel all orders for a product complex | FIX Spec §3.12 |

## LME-Specific Scopes

| Request Type | Required Fields | Notes |
|--------------|-----------------|-------|
| CANCEL_SYMBOL (1) | Symbol (55) or SecurityID (48) | Cancels all orders for specified symbol |
| CANCEL_PRODUCT_COMPLEX (9) | ProductComplex (1227) | Cancels all orders for product complex |
| CANCEL_ALL_ORDERS (8) | None | Cancels ALL orders for the member |

## Processing Rules

### Validation Requirements
1. Valid session must be established
2. Sequence numbers must be in order
3. ClOrdID must be unique per trading day
4. Required scope fields must be present for specific request types

### Execution Logic
1. Determine scope from MassCancelRequestType
2. Find all matching orders for the client
3. Cancel all eligible orders
4. Generate Mass Cancel Report with results

### Restrictions
- Cannot cancel orders in FILLED, CANCELLED, REJECTED, or EXPIRED state
- Only orders owned by the requesting member are cancelled
- Partially filled orders can be cancelled (remaining quantity)

## Message Example (Tabby CSV Format)

### Example: Cancel All Orders for Symbol CA
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ClOrdID,MassCancelRequestType,Symbol
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,MCL001,1,CA
```

### Example: Cancel All Orders for Member
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ClOrdID,MassCancelRequestType
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,MCL002,8
```

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §3.12, §4.11.10
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **Related Message:** [r-Order-Mass-Cancel-Report.md](./r-Order-Mass-Cancel-Report.md)
