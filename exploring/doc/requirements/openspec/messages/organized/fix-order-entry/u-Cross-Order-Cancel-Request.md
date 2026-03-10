# Cross Order Cancel Request

**Domain:** Order Entry  
**Message Type:** u  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Cross Order Cancel Request message for LME Order Entry Gateway.

## Message Specification

### FIX Protocol Details
- **Message Type:** `u`
- **Message Name:** Cross Order Cancel Request
- **FIX Version:** 5.0 (with LME extensions)

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Cross Order Cancel Request (u)
Gateway → Client: Acknowledgment/Response
```

### Failure Scenario
```
Client → Gateway: Cross Order Cancel Request (u)
Gateway → Client: Reject (3) or Business Message Reject (j)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = u |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

## Message Example (Tabby CSV Format)

### Example: Cross Order Cancel Request (u)

```csv
# Message: Cross Order Cancel Request (u)
# Direction: Client→Gateway

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,u,35,String,Message type
SenderCompID,CLIENT1,49,String,Your CompID
TargetCompID,LME,56,String,LME CompID
MsgSeqNum,1,34,SeqNum,Message sequence number
SendingTime,,52,UTCTimestamp,Current timestamp
CheckSum,,10,String,Will be calculated
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- Sequence numbers must be in order
- Required fields must be present

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
