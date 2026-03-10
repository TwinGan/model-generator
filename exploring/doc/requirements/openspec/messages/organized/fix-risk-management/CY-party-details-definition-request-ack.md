# Party Details Definition Request Ack

**Domain:** Risk Management  
**Message Type:** CY  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Acknowledgment of Party Details Definition Request (CX). Confirms receipt and processing of party details definition request.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CY`
- **Message Name:** Party Details Definition Request Ack
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Details Definition Request (CX)
Gateway → Client: Party Details Definition Request Ack (CY) - Accepted
```

### Failure Scenario
```
Client → Gateway: Party Details Definition Request (CX)
Gateway → Client: Party Details Definition Request Ack (CY) - Rejected
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CY |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1516 | PartyDetailsListReportID | String | Unique report ID from CX |
| 1517 | PartyDetailsListRequestID | String | Unique request ID from CX |
| 1518 | PartyDetailsDefinitionStatus | Int | Status of definition request |
| 10 | CheckSum | String | Message checksum |

### Status Values
| Value | Meaning |
|-------|---------|
| 0 | Accepted |
| 1 | Rejected |
| 2 | Pending |

## Message Example (Tabby CSV Format)

### Example: Party Details Definition Request Ack (CY)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,PartyDetailsListReportID,PartyDetailsListRequestID,PartyDetailsDefinitionStatus
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RPT001,REQ001,0
```

### Example: Party Details Definition Request Ack (CY) - Rejected

```csv
# Message: Party Details Definition Request Ack (CY)
# Direction: Gateway→Client
# Description: Acknowledgment - Request Rejected

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,CY,35,String,Message type
SenderCompID,LME,49,String,LME CompID
TargetCompID,CLIENT1,56,String,Your CompID
MsgSeqNum,20,34,SeqNum,Message sequence number
SendingTime,20240101-12:00:00.100,52,UTCTimestamp,Current timestamp
PartyDetailsListReportID,RPT001,1516,String,Report ID from CX
PartyDetailsListRequestID,REQ001,1517,String,Request ID from CX
PartyDetailsDefinitionStatus,1,1518,Int,1=Rejected
CheckSum,,10,String,Will be calculated
```

## Processing Rules

### When Sent
- **Acknowledgment:** Immediately after processing CX message
- **Status:** Indicates acceptance or rejection of request

### Validation Requirements
- Must reference valid PartyDetailsListReportID from CX
- Must reference valid PartyDetailsListRequestID from CX
- Status must be valid (0=Accepted, 1=Rejected, 2=Pending)

## Resulting Messages

### Follow-up Actions
- **If Accepted:** Party details are applied/updated
- **If Rejected:** No changes made, error details in Text (58)
- **If Pending:** Further updates will be sent

## Testing Considerations

### Positive Test Cases
1. ✅ Acknowledgment with Accepted status
2. ✅ Acknowledgment with Rejected status
3. ✅ Acknowledgment with Pending status

### Negative Test Cases
1. ❌ Invalid Report ID - should not occur
2. ❌ Invalid Request ID - should not occur
3. ❌ Invalid status code - should not occur

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Details Definition Request Ack (CY)
- **Related:** Party Details Definition Request (CX)

## Implementation Notes

- Sent in response to every CX message
- Status indicates result of definition request
- Reject reason may be included in Text (58) field
- Processing is typically immediate (synchronous)
