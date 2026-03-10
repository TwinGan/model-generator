# Party Risk Limits Report

**Domain:** Risk Management  
**Message Type:** CM  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Report containing current risk limits and utilization for a party. Response to Party Risk Limits Request (CL).

## Message Specification

### FIX Protocol Details
- **Message Type:** `CM`
- **Message Name:** Party Risk Limits Report
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Risk Limits Request (CL)
Gateway → Client: Party Risk Limits Report (CM)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = CM |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1325 | RiskLimitRequestID | String | Request ID from CL |
| 1518 | PartyDetailsDefinitionStatus | Int | Status of report |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 9519 | RiskLimitGroupName | String | Risk limit group name |
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1327 | RiskLimitReportID | String | Unique report ID |
| 1673 | RiskLimitReportStatus | Int | Status of risk limit report |

### Risk Limit Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1326 | RiskLimitID | String | Unique risk limit ID |
| 1533 | RiskLimitType | Int | Type of risk limit |
| 1534 | RiskLimitAmount | Float | Risk limit amount |
| 1535 | RiskLimitUtilization | Float | Current utilization |
| 1536 | RiskLimitCurrency | String | Currency of limit |
| 1537 | RiskLimitVelocity | Int | Velocity limit (if applicable) |

### Status Values
| Value | Meaning |
|-------|---------|
| 0 | Accepted |
| 1 | Rejected |
| 2 | Pending |

### Risk Limit Types
| Value | Meaning |
|-------|---------|
| 1 | Per order quantity |
| 2 | Per order notional value |
| 3 | Gross long quantity |
| 4 | Gross short quantity |
| 5 | Gross position value |
| 6 | Net position quantity |
| 7 | Net position value |

## Message Example (Tabby CSV Format)

### Example: Party Risk Limits Report (CM)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,RiskLimitReportID,PartyDetailsDefinitionStatus,NoPartyDetails,RiskLimitReportStatus,RiskLimitGroupName
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RISKREQ001,RPT001,0,1,0,GROUP1
```

## Processing Rules

### When Sent
- **Response:** In response to Party Risk Limits Request (CL)
- **Update:** May be sent unsolicited for limit breaches
- **Timing:** Typically immediate (synchronous)

### Validation Requirements
- Must reference valid RiskLimitRequestID from CL
- Status must be valid (0=Accepted, 1=Rejected, 2=Pending)
- Risk limit data must be current and accurate

## Resulting Messages

### Report Content
- **Status:** Success or failure of query
- **Risk Limits:** Configured limits for party
- **Utilization:** Current usage against limits
- **Format:** Repeating groups of risk limit data

### Unsolicited Updates
- May be sent when risk limits are breached
- May be sent when limits are updated
- May be sent periodically for monitoring

### Related Messages
- **Request:** Party Risk Limits Request (CL)
- **Definition:** Party Risk Limits Definition Request (CS)
- **Ack:** Party Risk Limits Definition Request Ack (CT)

## Testing Considerations

### Positive Test Cases
1. ✅ Report with multiple risk limits
2. ✅ Report with utilization data
3. ✅ Report showing limit breaches
4. ✅ Unsolicited limit breach notification

### Negative Test Cases
1. ❌ Invalid request ID - should not occur
2. ❌ Invalid status code - should not occur

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Risk Limits Report (CM)
- **Related:** Party Risk Limits Request (CL)

## Implementation Notes

- This is the message the user specifically asked about (CL/CM pair)
- Contains current risk limits and real-time utilization
- Used for both query responses and unsolicited notifications
- Critical for pre-trade risk checking
- May include multiple risk limit types per party
