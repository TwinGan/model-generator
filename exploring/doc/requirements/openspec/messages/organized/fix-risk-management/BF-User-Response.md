# User Response

**Domain:** Risk Management  
**Message Type:** BF  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

User Response message from LME Risk Management Gateway. Sent in response to User Request (BE) with user account information.

## Message Specification

### FIX Protocol Details
- **Message Type:** `BF`
- **Message Name:** User Response
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.6.2

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: User Request (BE)
Gateway → Client: User Response (BF) with UserStatus
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = BF |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 923 | UserRequestID | String | Required | ID from the request |
| 926 | UserStatus | Int | Required | User account status |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 553 | Username | String | Optional | Username |
| 927 | UserStatusText | String | Optional | Status description |
| 802 | NoPartyIDs | NumInGroup | Optional | Party identification group |
| 58 | Text | String | Optional | Free-form text |
| 581 | AffectedOrdIDGrp | NumInGroup | Optional | Affected orders group |

## UserStatus Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | ACTIVE | User account is active | Risk Spec §4.6.2 |
| 2 | DISABLED | User account is disabled | Risk Spec §4.6.2 |
| 3 | PASSWORD_EXPIRED | Password has expired | Risk Spec §4.6.2 |
| 4 | ACCOUNT_LOCKED | Account is locked | Risk Spec §4.6.2 |
| 5 | PENDING_ACTIVATION | Awaiting activation | Risk Spec §4.6.2 |

## Message Example (Tabby CSV Format)

### Example: User Response - Active User
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,UserRequestID,UserStatus,Username
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,REQ001,1,trader1
```

### Example: User Response - Account Locked
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,UserRequestID,UserStatus,UserStatusText
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,REQ002,4,Account locked due to failed login attempts
```

## Processing Rules

### Response Generation
1. Look up user information from request
2. Include UserStatus indicating current state
3. Include UserStatusText for non-active statuses

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.6.2
- **FIX Version:** 5.0 with LME extensions
