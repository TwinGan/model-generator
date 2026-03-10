# Party Entitlements Definition Request Ack

**Domain:** Risk Management  
**Message Type:** DB  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Acknowledgment of Party Entitlements Definition Request (DA). Confirms receipt and processing of entitlement definition request.

## Message Specification

### FIX Protocol Details
- **Message Type:** `DB`
- **Message Name:** Party Entitlements Definition Request Ack
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Entitlements Definition Request (DA)
Gateway → Client: Party Entitlements Definition Request Ack (DB) - Accepted
```

### Failure Scenario
```
Client → Gateway: Party Entitlements Definition Request (DA)
Gateway → Client: Party Entitlements Definition Request Ack (DB) - Rejected
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = DB |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1325 | RiskLimitRequestID | String | Request ID from DA |
| 1518 | PartyDetailsDefinitionStatus | Int | Status of definition |
| 10 | CheckSum | String | Message checksum |

### Status Values
| Value | Meaning |
|-------|---------|
| 0 | Accepted |
| 1 | Rejected |
| 2 | Pending |

## Message Example (Tabby CSV Format)

### Example: Party Entitlements Definition Request Ack (DB)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,PartyDetailsDefinitionStatus
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RISKREQ001,0
```

## Processing Rules

### When Sent
- **Acknowledgment:** Immediately after processing DA message
- **Status:** Indicates acceptance, rejection, or pending

### Validation Requirements
- Must reference valid RiskLimitRequestID from DA
- Status must be valid (0=Accepted, 1=Rejected, 2=Pending)
- If rejected, reason may be in Text (58) field

## Resulting Messages

### Follow-up Actions
- **If Accepted:** Entitlements are applied/updated
- **If Rejected:** No changes made, error details provided
- **If Pending:** Final status will be sent later

### Related Messages
- **Request:** Party Entitlements Definition Request (DA)

## Testing Considerations

### Positive Test Cases
1. ✅ Acknowledgment with Accepted status
2. ✅ Acknowledgment with Rejected status
3. ✅ Acknowledgment with Pending status

### Negative Test Cases
1. ❌ Invalid request ID - should not occur
2. ❌ Invalid status code - should not occur

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Entitlements Definition Request Ack (DB)
- **Related:** Party Entitlements Definition Request (DA)

## Implementation Notes

- Sent in response to every DA message
- Processing typically immediate (synchronous)
- Reject reason provided in Text (58) when applicable
- Pending status used when approval workflow required
- Entitlement changes may require session restart
