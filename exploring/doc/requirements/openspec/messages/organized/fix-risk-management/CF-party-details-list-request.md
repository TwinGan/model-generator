# Party Details List Request

**Domain:** Risk Management  
**Message Type:** CF  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request a list of party details from the risk management system. Used for querying configured parties and their details.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CF`
- **Message Name:** Party Details List Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Details List Request (CF)
Gateway → Client: Party Details List Report (CG)
```

### Failure Scenario
```
Client → Gateway: Party Details List Request (CF)
Gateway → Client: Business Message Reject (j) - Invalid request
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CF |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1515 | PartyDetailsListRequestType | Int | Type of list request |
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1691 | PartyDetailID | String | Party detail identifier (filter) |

## Message Example (Tabby CSV Format)

### Example: Party Details List Request (CF)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,PartyDetailsListRequestType,NoPartyDetails,PartyDetailID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,1,1,PARTY123
```

## Processing Rules

### When to Send
- **Query All:** To retrieve all party details
- **Query Specific:** To retrieve details for specific party
- **Synchronization:** To synchronize party details

### Validation Requirements
- User must have party view permissions
- If PartyDetailID specified, must be valid party
- PartyDetailsListRequestType must be valid

## Resulting Messages

### Success Response
- **Message Type:** Party Details List Report (CG)
- **Content:** List of party details matching request criteria
- **Format:** Repeating groups of party details

### Error Response
- **Message Type:** Business Message Reject (j)
- **Reason:** Insufficient permissions or invalid request

### Related Messages
- **Response:** Party Details List Report (CG)
- **Definition:** Party Details Definition Request (CX)

## Testing Considerations

### Positive Test Cases
1. ✅ Request all party details
2. ✅ Request specific party details
3. ✅ Request by party type

### Negative Test Cases
1. ❌ Unauthorized user - should reject
2. ❌ Invalid party ID filter - should return empty or error

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Details List Request (CF)
- **Related:** Party Details List Report (CG)

## Implementation Notes

- Used for querying party configuration
- Can request all parties or filter by criteria
- Response may be large for "all parties" request
- Pagination may be supported for large result sets
