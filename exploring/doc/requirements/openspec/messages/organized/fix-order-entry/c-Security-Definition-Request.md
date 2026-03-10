# Security Definition Request

**Domain:** Order Entry  
**Message Type:** c  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Security Definition Request message for LME Order Entry Gateway.

## Message Specification

### FIX Protocol Details
- **Message Type:** `c`
- **Message Name:** Security Definition Request
- **FIX Version:** 5.0 (with LME extensions)

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Security Definition Request (c)
Gateway → Client: Acknowledgment/Response
```

### Failure Scenario
```
Client → Gateway: Security Definition Request (c)
Gateway → Client: Reject (3) or Business Message Reject (j)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = c |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

## Message Example (Tabby CSV Format)

### Example: Security Definition Request (c)

```csv
# Message: Security Definition Request (c)
# Direction: Client→Gateway

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,c,35,String,Message type
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
