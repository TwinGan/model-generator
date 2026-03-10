# Business Message Reject

**Domain:** Order Entry  
**Message Type:** j  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Business Message Reject message for LME Order Entry Gateway. Used when a business-level message cannot be processed.

## Message Specification

### FIX Protocol Details
- **Message Type:** `j`
- **Message Name:** Business Message Reject
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.9.1

## Message Interaction Flow

### Rejection Scenario
```
Client → Gateway: Application Message (D, F, G, etc.)
Gateway → Client: Business Message Reject (j) with BusinessRejectReason
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = j |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 45 | RefSeqNum | SeqNum | Required | Sequence number of rejected message |
| 372 | RefMsgType | String | Required | Message type of rejected message |
| 379 | BusinessRejectRefID | String | Required | Reference ID from rejected message |
| 380 | BusinessRejectReason | Int | Required | Reason for rejection |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 58 | Text | String | Optional | Free-form text explanation |
| 371 | RefTagID | Int | Conditional | Tag number causing rejection |
| 1369 | RefMsgTypeDescription | String | Optional | Human readable message type |

## BusinessRejectReason Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | OTHER | Other - see Text (58) for details | FIX Spec §4.9.1 |
| 1 | UNKNOWN_ID | Unknown ID | FIX Spec §4.9.1 |
| 2 | UNKNOWN_SECURITY | Unknown security | FIX Spec §4.9.1 |
| 3 | UNSUPPORTED_MESSAGE_TYPE | Unsupported message type | FIX Spec §4.9.1 |
| 4 | APPLICATION_NOT_AVAILABLE | Application not available | FIX Spec §4.9.1 |
| 5 | CONDITIONALLY_REQUIRED_FIELD_MISSING | Conditionally required field missing | FIX Spec §4.9.1 |
| 6 | NOT_AUTHORIZED | Not authorized | FIX Spec §4.9.1 |
| 7 | DELIVER_TO_FIRM_NOT_AVAILABLE | Deliver to firm not available | FIX Spec §4.9.1 |
| 8 | THROTTLE_LIMIT_EXCEEDED | Throttle limit exceeded | FIX Spec §4.9.1 |
| 9 | THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECTED | Throttle limit exceeded, disconnect | FIX Spec §4.9.1 |

## Message Example (Tabby CSV Format)

### Example: Reject for Unknown Security
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RefSeqNum,RefMsgType,BusinessRejectRefID,BusinessRejectReason,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,100,D,CL000001,2,Unknown symbol: INVALID
```

### Example: Reject for Missing Required Field
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RefSeqNum,RefMsgType,BusinessRejectRefID,BusinessRejectReason,RefTagID,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,101,D,CL000002,5,44,Price required for limit orders
```

### Example: Reject for Not Authorized
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RefSeqNum,RefMsgType,BusinessRejectRefID,BusinessRejectReason,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,102,s,CROSS001,6,User not authorized for cross orders
```

### Example: Reject for Throttle Limit
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RefSeqNum,RefMsgType,BusinessRejectRefID,BusinessRejectReason,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,103,D,CL000003,8,Message rate limit exceeded. Please retry.
```

## Processing Rules

### When to Use Business Message Reject
1. Business-level validation failure
2. Unknown security or symbol
3. Missing conditionally required fields
4. Authorization failure
5. Throttle limit exceeded

### When NOT to Use
1. Session-level errors (use Reject 35=3)
2. Syntax errors (use Reject 35=3)
3. Sequence number errors (use Sequence Reset 35=4)

### Response Generation
1. Include RefSeqNum of rejected message
2. Include RefMsgType of rejected message
3. Include appropriate BusinessRejectReason
4. Include Text with additional details when helpful

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.9.1
- **Error Codes:** See [error-codes.md](../../reference/error-codes.md)
