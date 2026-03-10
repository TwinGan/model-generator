# Party Action Report

**Domain:** Risk Management  
**Message Type:** DI  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Report of party action completion or failure. Response to Party Action Request (DH) or unsolicited notification of party action.

## Message Specification

### FIX Protocol Details
- **Message Type:** `DI`
- **Message Name:** Party Action Report
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Action Request (DH)
Gateway → Client: Party Action Report (DI) - Completed
```

### Unsolicited Scenario
```
Gateway → Client: Party Action Report (DI) - Party Action Taken
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = DI |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1325 | RiskLimitRequestID | String | Request ID from DH |
| 1691 | PartyDetailID | String | Party ID action was taken on |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1348 | PartyActionType | Int | Type of action performed |
| 1349 | PartyActionResponse | Int | Result of action |
| 1350 | PartyActionRejectReason | Int | Reason if action failed |
| 58 | Text | String | Additional information |

### Party Action Response Values
| Value | Meaning |
|-------|---------|
| 0 | Completed Successfully |
| 1 | Failed |
| 2 | Partially Completed |

### Party Action Reject Reasons
| Value | Meaning |
|-------|---------|
| 0 | Unknown Party |
| 1 | Invalid Action Type |
| 2 | Insufficient Permissions |
| 3 | System Error |
| 99 | Other |

## Message Example (Tabby CSV Format)

### Example: Party Action Report (DI)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,Text,RiskLimitRequestID,PartyActionType,PartyActionResponse,PartyActionRejectReason,PartyDetailID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,Sample text,RISKREQ001,1,0,1,PARTY123
```

### Example: Party Action Report (DI) - Failed

```csv
# Message: Party Action Report (DI)
# Direction: Gateway→Client
# Description: Party action failed

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,DI,35,String,Message type
SenderCompID,LME,49,String,LME CompID
TargetCompID,CLIENT1,56,String,Your CompID
MsgSeqNum,65,34,SeqNum,Message sequence number
SendingTime,20240101-12:00:00.100,52,UTCTimestamp,Current timestamp
RiskLimitRequestID,ACTION001,1325,String,Request ID from DH
PartyDetailID,PARTY123,1691,String,Target party ID
PartyActionType,1,1348,Int,1=Suspend Trading
PartyActionResponse,1,1349,Int,1=Failed
PartyActionRejectReason,2,1350,Int,2=Insufficient Permissions
Text,Insufficient permissions for action,58,String,Error details
CheckSum,,10,String,Will be calculated
```

## Processing Rules

### When Sent
- **Response:** In response to Party Action Request (DH)
- **Unsolicited:** When automated action taken (e.g., breach suspension)
- **Timing:** Immediately after action completes

### Validation Requirements
- Must reference valid RiskLimitRequestID from DH (if response)
- PartyDetailID must be valid party
- PartyActionResponse must be valid status code
- If failed, reject reason must be provided

## Resulting Messages

### Follow-up Actions
- **If Completed:** Action has taken effect
- **If Failed:** No action taken, error details provided
- **If Partial:** Some parts of action completed

### Unsolicited Reports
- Sent when automated risk actions triggered
- Example: Automatic suspension on risk limit breach
- Example: System-initiated forced logout

### Related Messages
- **Request:** Party Action Request (DH)
- **Limits:** Party Risk Limits Report (CM)

## Testing Considerations

### Positive Test Cases
1. ✅ Report successful action completion
2. ✅ Report failed action
3. ✅ Unsolicited breach suspension
4. ✅ Unsolicited forced logout

### Negative Test Cases
1. ❌ Invalid request ID - should not occur
2. ❌ Invalid response code - should not occur

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Action Report (DI)
- **Related:** Party Action Request (DH)

## Implementation Notes

- Critical for emergency risk management
- Unsolicited reports important for monitoring
- May trigger notifications to operations team
- Action results are typically immediate
- Failed actions require manual intervention
