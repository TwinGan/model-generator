# Party Details List Report

**Domain:** Risk Management  
**Message Type:** CG  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Report containing list of party details in response to Party Details List Request (CF). Provides configuration information about parties.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CG`
- **Message Name:** Party Details List Report
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Details List Request (CF)
Gateway → Client: Party Details List Report (CG)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CG |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1516 | PartyDetailsListReportID | String | Report ID matching CF |
| 1517 | PartyDetailsListRequestID | String | Request ID matching CF |
| 1518 | PartyDetailsDefinitionStatus | Int | Status of report |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1691 | PartyDetailID | String | Party detail identifier |
| 1672 | PartyDetailStatus | Int | Status of party detail |
| 1671 | PartyDetailAction | Int | Action performed |

## Message Example (Tabby CSV Format)

### Example: Party Details List Report (CG)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,PartyDetailsListReportID,PartyDetailsListRequestID,PartyDetailsDefinitionStatus,NoPartyDetails,PartyDetailAction,PartyDetailStatus,PartyDetailID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RPT001,REQ001,0,1,1,1,PARTY123
```

## Processing Rules

### When Sent
- **Response:** In response to Party Details List Request (CF)
- **Timing:** Typically immediate (synchronous)

### Validation Requirements
- Must reference valid PartyDetailsListReportID from CF
- Must reference valid PartyDetailsListRequestID from CF
- Status must reflect result of query

## Resulting Messages

### Report Content
- **Status:** Success or failure of query
- **Details:** Repeating groups of party details (if successful)
- **Format:** Standard party detail structure

### Related Messages
- **Request:** Party Details List Request (CF)
- **Definition:** Party Details Definition Request (CX)
- **Ack:** Party Details Definition Request Ack (CY)

## Testing Considerations

### Positive Test Cases
1. ✅ Report with multiple party details
2. ✅ Report with single party detail
3. ✅ Report with no matching parties (empty)

### Negative Test Cases
1. ❌ Invalid request reference - should not occur

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Details List Report (CG)
- **Related:** Party Details List Request (CF)

## Implementation Notes

- Sent in response to every CF message
- Contains repeating groups of party details
- May be large for "all parties" queries
- Status indicates success/failure of query
