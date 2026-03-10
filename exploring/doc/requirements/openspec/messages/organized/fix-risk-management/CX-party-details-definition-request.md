# Party Details Definition Request

**Domain:** Risk Management  
**Message Type:** CX  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request to define or modify party details in the risk management system. Used for configuring party (member) settings, risk groups, and entitlements.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CX`
- **Message Name:** Party Details Definition Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

### Message Structure
```
Party Details Definition Request (CX)
├── Standard Header
│   ├── BeginString (8)
│   ├── BodyLength (9)
│   ├── MsgType (35) = CX
│   ├── SenderCompID (49)
│   ├── TargetCompID (56)
│   ├── MsgSeqNum (34)
│   └── SendingTime (52)
├── Message Body
│   ├── PartyDetailsListReportID (1516) - Unique report ID
│   ├── PartyDetailsListRequestID (1517) - Unique request ID
│   ├── PartyDetailsDefinitionStatus (1518) - Status of request
│   ├── NoPartyDetails (1670) - Number of party detail entries
│   └── PartyDetailGroup (repeating)
│       ├── PartyDetailID (1691) - Party detail identifier
│       ├── PartyDetailStatus (1672) - Status of party detail
│       └── PartyDetailAction (1671) - Action to perform
└── Standard Trailer
    └── CheckSum (10)
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Details Definition Request (CX)
Gateway → Client: Party Details Definition Request Ack (CY)
```

### Failure Scenario
```
Client → Gateway: Party Details Definition Request (CX)
Gateway → Client: Business Message Reject (j) - Invalid request
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CX |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1516 | PartyDetailsListReportID | String | Unique report ID |
| 1517 | PartyDetailsListRequestID | String | Unique request ID |
| 1518 | PartyDetailsDefinitionStatus | Int | Status of definition request |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1691 | PartyDetailID | String | Party detail identifier |
| 1672 | PartyDetailStatus | Int | Status of party detail |
| 1671 | PartyDetailAction | Int | Action to perform (1=Add, 2=Update, 3=Delete) |

## Message Example (Tabby CSV Format)

### Example: Party Details Definition Request (CX)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,PartyDetailsListReportID,PartyDetailsListRequestID,PartyDetailsDefinitionStatus,NoPartyDetails,PartyDetailAction,PartyDetailStatus,PartyDetailID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RPT001,REQ001,0,1,1,1,PARTY123
```

## Processing Rules

### When to Send
- **Initial Setup:** When configuring new party details
- **Modification:** When updating existing party configurations
- **Bulk Update:** When multiple party details need to be defined

### Validation Requirements
1. **Authorization:**
   - User must have party administration permissions
   - Must be risk management administrator

2. **Data Validation:**
   - PartyDetailsListReportID must be unique
   - PartyDetailAction must be valid (1=Add, 2=Update, 3=Delete)
   - PartyDetailStatus must be valid status code

3. **Business Rules:**
   - Cannot modify party details of active sessions
   - Party entitlements must be consistent
   - Risk limit groups must exist before assignment

## Resulting Messages

### Success Response
- **Message Type:** Party Details Definition Request Ack (CY)
- **Status:** Accepted/Confirmed
- **Fields:** PartyDetailsListReportID, PartyDetailsListRequestID, AckStatus

### Error Response
- **Message Type:** Business Message Reject (j)
- **Reason Codes:**
  - 1 = Unknown party
  - 2 = Invalid party status
  - 3 = Insufficient permissions
  - 99 = Other

### Related Messages
- **Response:** Party Details Definition Request Ack (CY)
- **Query:** Party Details List Request (CF)
- **Report:** Party Details List Report (CG)

## Testing Considerations

### Positive Test Cases
1. ✅ Define new party details
2. ✅ Update existing party details
3. ✅ Delete party details
4. ✅ Bulk party details definition

### Negative Test Cases
1. ❌ Unauthorized user - should reject
2. ❌ Invalid party ID - should reject
3. ❌ Invalid action code - should reject
4. ❌ Duplicate report ID - should reject

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Details Definition Request (CX)
- **Related:** Party Details Definition Request Ack (CY)

## Implementation Notes

- Party details include member information, risk groups, entitlements
- Changes may require approval workflow
- Audit trail maintained for all party detail modifications
- Real-time updates applied to active sessions where applicable
