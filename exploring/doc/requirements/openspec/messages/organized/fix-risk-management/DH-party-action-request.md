# Party Action Request

**Domain:** Risk Management  
**Message Type:** DH  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request to perform an action on a party (member). Used for emergency actions like suspending trading, reinstating access, or forcing logout.

## Message Specification

### FIX Protocol Details
- **Message Type:** `DH`
- **Message Name:** Party Action Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Action Request (DH)
Gateway → Client: Party Action Report (DI) - Action Completed
```

### Failure Scenario
```
Client → Gateway: Party Action Request (DH)
Gateway → Client: Party Action Report (DI) - Action Failed
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = DH |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1325 | RiskLimitRequestID | String | Unique request ID |
| 1691 | PartyDetailID | String | Target party for action |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 118 | ApplID | String | Operator ID performing action |
| 1348 | PartyActionType | Int | Type of action to perform |
| 1349 | PartyActionResponse | Int | Expected response type |

### Party Action Types
| Value | Meaning | Description |
|-------|---------|-------------|
| 1 | Suspend Trading | Immediately suspend all trading for party |
| 2 | Reinstate Trading | Reinstate trading for suspended party |
| 3 | Force Logout | Force logout all sessions for party |
| 4 | Reset Risk Limits | Reset risk limit utilization to zero |
| 5 | Emergency Cancel | Mass cancel all working orders |

## Message Example (Tabby CSV Format)

### Example: Party Action Request (DH)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,ApplID,RiskLimitRequestID,PartyActionType,PartyActionResponse,PartyDetailID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,OP001,RISKREQ001,1,0,PARTY123
```

## Processing Rules

### When to Send
- **Emergency:** For emergency trading suspension
- **Violation:** When risk limits are breached
- **Administrative:** For administrative actions
- **Security:** For security-related actions

### Validation Requirements
- User must have party action permissions
- PartyDetailID must be valid party
- PartyActionType must be valid
- Operator ID (ApplID) must be authorized
- Some actions may require additional approval

## Resulting Messages

### Success Response
- **Message Type:** Party Action Report (DI)
- **Status:** Action Completed
- **Fields:** RiskLimitRequestID, PartyDetailID, ActionResult

### Failure Response
- **Message Type:** Party Action Report (DI)
- **Status:** Action Failed
- **Fields:** RiskLimitRequestID, PartyDetailID, ErrorReason

### Related Messages
- **Response:** Party Action Report (DI)
- **Query:** Party Risk Limits Report (CM)

## Testing Considerations

### Positive Test Cases
1. ✅ Suspend trading for party
2. ✅ Reinstate trading for party
3. ✅ Force logout party sessions
4. ✅ Reset risk limit utilization
5. ✅ Emergency cancel all orders

### Negative Test Cases
1. ❌ Unauthorized operator - should reject
2. ❌ Invalid party ID - should reject
3. ❌ Invalid action type - should reject
4. ❌ Action on non-existent party - should reject

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Action Request (DH)
- **Related:** Party Action Report (DI)

## Implementation Notes

- Emergency actions take effect immediately
- Audit trail maintained for all party actions
- May trigger notifications to affected parties
- Some actions may be irreversible
- Used by risk managers for emergency control
