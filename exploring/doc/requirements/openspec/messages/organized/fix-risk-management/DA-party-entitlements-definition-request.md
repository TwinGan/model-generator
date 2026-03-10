# Party Entitlements Definition Request

**Domain:** Risk Management  
**Message Type:** DA  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Request to define or modify party entitlements. Used for configuring trading permissions, instrument access, and entitlement groups.

## Message Specification

### FIX Protocol Details
- **Message Type:** `DA`
- **Message Name:** Party Entitlements Definition Request
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Party Entitlements Definition Request (DA)
Gateway → Client: Party Entitlements Definition Request Ack (DB)
```

### Failure Scenario
```
Client → Gateway: Party Entitlements Definition Request (DA)
Gateway → Client: Business Message Reject (j) - Invalid request
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = DA |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 1325 | RiskLimitRequestID | String | Unique request ID |
| 1691 | PartyDetailID | String | Target party ID |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 1518 | PartyDetailsDefinitionStatus | Int | Status of request |
| 1670 | NoPartyDetails | NumInGrp | Number of party detail entries |
| 1884 | NoEntitlements | NumInGrp | Number of entitlements |
| 1885 | EntitlementType | Int | Type of entitlement |
| 1886 | EntitlementID | String | Entitlement identifier |

### Entitlement Types
| Value | Meaning |
|-------|---------|
| 1 | Trading Permission |
| 2 | Instrument Access |
| 3 | Market Data Access |
| 4 | Order Type Permission |
| 5 | Risk Group Assignment |

## Message Example (Tabby CSV Format)

### Example: Party Entitlements Definition Request (DA)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,PartyDetailsDefinitionStatus,NoPartyDetails,PartyDetailID,NoEntitlements,EntitlementType,EntitlementID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,RISKREQ001,0,1,PARTY123,1,1,ENT001
```

## Processing Rules

### When to Send
- **Initial Setup:** When configuring entitlements for new party
- **Modification:** When updating existing entitlements
- **Bulk Update:** When multiple entitlement changes needed

### Validation Requirements
- User must have entitlement administration permissions
- PartyDetailID must be valid party
- EntitlementType must be valid
- EntitlementID must reference valid entitlement

## Resulting Messages

### Success Response
- **Message Type:** Party Entitlements Definition Request Ack (DB)
- **Status:** Accepted/Confirmed
- **Fields:** RiskLimitRequestID, PartyDetailID, AckStatus

### Error Response
- **Message Type:** Business Message Reject (j)
- **Reason:** Invalid configuration or insufficient permissions

### Related Messages
- **Ack:** Party Entitlements Definition Request Ack (DB)

## Testing Considerations

### Positive Test Cases
1. ✅ Define new entitlements
2. ✅ Update existing entitlements
3. ✅ Add instrument access
4. ✅ Modify trading permissions
5. ✅ Assign risk groups

### Negative Test Cases
1. ❌ Unauthorized user - should reject
2. ❌ Invalid party ID - should reject
3. ❌ Invalid entitlement type - should reject
4. ❌ Invalid entitlement ID - should reject

## References

- **Source:** Risk Management Gateway FIX Specification v1.8
- **Section:** Party Entitlements Definition Request (DA)
- **Related:** Party Entitlements Definition Request Ack (DB)

## Implementation Notes

- Entitlements control trading permissions and access
- Changes take effect immediately or at next login
- May require approval workflow
- Audit trail maintained for all changes
- Used for both initial setup and ongoing maintenance
