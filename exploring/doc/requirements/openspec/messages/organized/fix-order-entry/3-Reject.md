# Reject

**Domain:** Order Entry  
**Message Type:** 3  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Reject message for LME Order Entry Gateway.

## Message Specification

### FIX Protocol Details
- **Message Type:** `3`
- **Message Name:** Reject
- **FIX Version:** 5.0 (with LME extensions)

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Reject (3)
Gateway → Client: Acknowledgment/Response
```

### Failure Scenario
```
Client → Gateway: Reject (3)
Gateway → Client: Reject (3) or Business Message Reject (j)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = 3 |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

## Message Example (Tabby CSV Format)

### Example: Reject (3)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- Sequence numbers must be in order
- Required fields must be present

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
