# Order Mass Cancel Report

**Domain:** Order Entry  
**Message Type:** r  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Order Mass Cancel Report message for LME Order Entry Gateway. Sent in response to an Order Mass Cancel Request (q), indicating the result of the mass cancel operation.

## Message Specification

### FIX Protocol Details
- **Message Type:** `r`
- **Message Name:** Order Mass Cancel Report
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.11.11

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
| 11 | ClOrdID | String | Required | Client order ID from the request |
| 35 | MsgType | String | Required | Message type = r |
| 37 | OrderID | String | Required | Exchange-assigned mass cancel ID |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 531 | MassCancelResponse | Int | Required | Response to mass cancel request |
| 530 | MassCancelRequestType | Int | Required | Type of mass cancel request |

### Conditional Fields (on Success)
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 533 | TotalAffectedOrders | Int | Required | Number of orders affected |
| 48 | SecurityID | String | Optional | Security ID (if scope was symbol) |
| 55 | Symbol | String | Optional | Symbol (if scope was symbol) |
| 460 | Product | Int | Optional | Product (if scope was product) |
| 1227 | ProductComplex | Int | Optional | Product complex (if scope was complex) |

### Conditional Fields (on Rejection)
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 532 | MassCancelRejectReason | Int | Required | Reason for rejection |
| 58 | Text | String | Optional | Additional rejection details |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 526 | SecondaryClOrdID | String | Optional | Secondary order ID |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |

## MassCancelResponse Values

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | CANCEL_REQUEST_ACCEPTED | Mass cancel request accepted | FIX Spec §4.11.11 |
| 1 | CANCEL_REQUEST_REJECTED | Mass cancel request rejected | FIX Spec §4.11.11 |

## MassCancelRejectReason Values

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | MASS_CANCEL_NOT_SUPPORTED | Mass cancel not supported | FIX Spec §4.11.11 |
| 1 | INVALID_PRODUCT_COMPLEX | Invalid product complex | FIX Spec §4.11.11 |
| 2 | INVALID_INSTRUMENT | Invalid instrument | FIX Spec §4.11.11 |
| 3 | INVALID_SECURITY_ID | Invalid security ID | FIX Spec §4.11.11 |
| 4 | INVALID_UNDERLYING | Invalid underlying | FIX Spec §4.11.11 |
| 5 | NO_ORDERS_FOUND | No orders found to cancel | FIX Spec §4.11.11 |
| 6 | OTHER | Other - see Text (58) | FIX Spec §4.11.11 |

## Processing Rules

### Response Generation
1. **Success (MassCancelResponse=0)**:
   - Include TotalAffectedOrders with count
   - Include scope fields from request
   - Generate OrderID for the mass cancel operation

2. **Rejection (MassCancelResponse=1)**:
   - Include MassCancelRejectReason
   - Include Text with additional details if needed
   - Set TotalAffectedOrders=0

### Validation Checks
1. Verify MassCancelRequestType matches the request
2. Check that scope fields match the request
3. Verify ClOrdID matches the request

## Message Example (Tabby CSV Format)

### Example: Successful Mass Cancel (5 orders cancelled)
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,OrderID,ClOrdID,MassCancelRequestType,MassCancelResponse,TotalAffectedOrders,Symbol
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,MC000001,MCL001,1,0,5,CA
```

### Example: Rejected Mass Cancel (No orders found)
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,OrderID,ClOrdID,MassCancelRequestType,MassCancelResponse,MassCancelRejectReason,Symbol,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,MC000002,MCL002,1,1,5,XX,No orders found for symbol XX
```

### Example: Cancel All Orders (3 orders cancelled)
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,OrderID,ClOrdID,MassCancelRequestType,MassCancelResponse,TotalAffectedOrders
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,MC000003,MCL003,8,0,3
```

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.11.11
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
- **Related Message:** [q-Order-Mass-Cancel-Request.md](./q-Order-Mass-Cancel-Request.md)
