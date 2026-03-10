# Heartbeat

**Domain:** Order Entry  
**Message Type:** 0  
**Category:** Session  
**Direction:** Bidirectional (Client↔Gateway)  

## Message Overview

Heartbeat message for LME Order Entry Gateway. Used to monitor session health and confirm connectivity.

## Message Specification

### FIX Protocol Details
- **Message Type:** `0`
- **Message Name:** Heartbeat
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.8.4

## Message Interaction Flow

### Periodic Heartbeat
```
Client ↔ Gateway: Heartbeat (0) every HeartBtInt seconds
```

### Heartbeat After Test Request
```
Gateway → Client: Test Request (1) with TestReqID
Client → Gateway: Heartbeat (0) with same TestReqID
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = 0 |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 112 | TestReqID | String | Conditional | Echoed from Test Request |

## TestReqID Handling
- **Periodic Heartbeat**: TestReqID is NOT present
- **Test Request Response**: TestReqID MUST match the Test Request
- Used to verify round-trip connectivity

## Message Example (Tabby CSV Format)

### Example: Periodic Heartbeat
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME
```

### Example: Heartbeat Response to Test Request
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,TestReqID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,TEST123
```

## Processing Rules

### Heartbeat Timing
- **HeartBtInt**: Default 30 seconds (configured in Logon)
- Send heartbeat if no other message sent within HeartBtInt
- If no message received within 3 x HeartBtInt, send Test Request

### Validation Requirements
- Valid session must be established
- Sequence numbers must be in order
- TestReqID must match pending Test Request if present

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.8.4
- **Session Management:** FIX Spec §1.4
