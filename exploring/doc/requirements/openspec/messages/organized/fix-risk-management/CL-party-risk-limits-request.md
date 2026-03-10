# Party Risk Limits Request

**Domain:** Risk Management  
**Message Type:** CL  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request current risk limits and utilization for a party. Used for querying risk limit configuration and current usage.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CL`
- **Message Name:** Party Risk Limits Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Risk Limits Request (CL)
Gateway → Client: Party Risk Limits Report (CM)
```

### Failure Scenario
```
Client → Gateway: Party Risk Limits Request (CL)
Gateway → Client: Business Message Reject (j) - Invalid request
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CL |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1325 | RiskLimitRequestID | String | Unique request ID |
| 9519 | RiskLimitGroupName | String | Risk limit group name (filter) |
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |

## Message Example (Tabby CSV Format)

### Example: Party Risk Limits Request (CL)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,NoPartyDetails,RiskLimitGroupName
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RISKREQ001,1,GROUP1
```

## Processing Rules

### When to Send
- **Query All:** To retrieve all risk limits
- **Query Specific:** To retrieve limits for specific party or group
- **Monitoring:** For real-time risk limit monitoring
- **Verification:** To verify risk limit configuration

### Validation Requirements
- User must have risk limit view permissions
- If RiskLimitGroupName specified, must exist
- Request must be from authorized party

## Resulting Messages

### Success Response
- **Message Type:** Party Risk Limits Report (CM)
- **Content:** Current risk limits and utilization
- **Format:** Repeating groups of risk limit data

### Error Response
- **Message Type:** Business Message Reject (j)
- **Reason:** Insufficient permissions or invalid request

### Related Messages
- **Response:** Party Risk Limits Report (CM)
- **Definition:** Party Risk Limits Definition Request (CS)
- **Ack:** Party Risk Limits Definition Request Ack (CT)

## Testing Considerations

### Positive Test Cases
1. ✅ Query all risk limits
2. ✅ Query specific party limits
3. ✅ Query by risk limit group
4. ✅ Query current utilization

### Negative Test Cases
1. ❌ Unauthorized user - should reject
2. ❌ Invalid risk limit group - should reject

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Risk Limits Request (CL)
- **Related:** Party Risk Limits Report (CM)

## Implementation Notes

- Real-time query of current risk limits
- Includes both configured limits and current utilization
- May be used for monitoring dashboards
- Response is typically immediate (synchronous)
