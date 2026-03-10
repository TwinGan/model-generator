# Party Risk Limits Definition Request

**Domain:** Risk Management  
**Message Type:** CS  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request to define or modify risk limits for a party (member). Used for configuring risk limit values, thresholds, and parameters.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CS`
- **Message Name:** Party Risk Limits Definition Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Risk Limits Definition Request (CS)
Gateway → Client: Party Risk Limits Definition Request Ack (CT)
```

### Failure Scenario
```
Client → Gateway: Party Risk Limits Definition Request (CS)
Gateway → Client: Business Message Reject (j) - Invalid request
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CS |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 9519 | RiskLimitGroupName | String | Risk limit group name |
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1325 | RiskLimitRequestID | String | Unique request ID |

## Message Example (Tabby CSV Format)

### Example: Party Risk Limits Definition Request (CS)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,NoPartyDetails,RiskLimitGroupName
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RISKREQ001,1,GROUP1
```

## Processing Rules

### When to Send
- **Initial Setup:** When configuring risk limits for new party
- **Modification:** When updating existing risk limits
- **Configuration:** For both risk limit and MMP configuration

### Validation Requirements
- User must have risk limit administration permissions
- RiskLimitGroupName must exist
- Risk limit values must be within acceptable ranges
- Cannot exceed exchange-level risk limits

## Resulting Messages

### Success Response
- **Message Type:** Party Risk Limits Definition Request Ack (CT)
- **Status:** Accepted/Confirmed
- **Fields:** RiskLimitGroupName, RequestID, AckStatus

### Error Response
- **Message Type:** Business Message Reject (j)
- **Reason:** Invalid configuration or insufficient permissions

### Related Messages
- **Ack:** Party Risk Limits Definition Request Ack (CT)
- **Query:** Party Risk Limits Request (CL)
- **Report:** Party Risk Limits Report (CM)

## Testing Considerations

### Positive Test Cases
1. ✅ Define new risk limits
2. ✅ Update existing risk limits
3. ✅ Configure MMP limits
4. ✅ Configure standard risk limits

### Negative Test Cases
1. ❌ Unauthorized user - should reject
2. ❌ Invalid risk limit group - should reject
3. ❌ Risk limits exceed exchange limits - should reject
4. ❌ Invalid limit values - should reject

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Risk Limits Definition Request (CS)
- **Related:** Party Risk Limits Definition Request Ack (CT)

## Implementation Notes

- Used for both risk limit and MMP configuration
- Changes may require approval workflow
- Real-time updates applied to active sessions
- Risk limits checked pre-trade
