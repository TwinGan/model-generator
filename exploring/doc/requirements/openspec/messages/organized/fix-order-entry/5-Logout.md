# Logout

**Domain:** Order Entry  
**Message Type:** 5  
**Category:** Session  
**Direction:** Bidirectional (Client↔Gateway)  

## Message Overview

Logout message for LME Order Entry Gateway. Used to terminate a FIX session gracefully.

## Message Specification

### FIX Protocol Details
- **Message Type:** `5`
- **Message Name:** Logout
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** FIX Spec §4.8.6

## Message Interaction Flow

### Client-Initiated Logout
```
Client → Gateway: Logout (5)
Gateway → Client: Logout (5) acknowledgment
Connection → Closed
```

### Gateway-Initiated Logout
```
Gateway → Client: Logout (5) with SessionStatus
Connection → Closed
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = 5 |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 1409 | SessionStatus | Int | Optional | Reason for logout |
| 58 | Text | String | Optional | Free-form text description |

## SessionStatus Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | SESSION_ACTIVE | Session active | FIX Spec §4.8.6 |
| 2 | SESSION_LOGOUT_REQUESTED | Session logout requested | FIX Spec §4.8.6 |
| 3 | NEW_SESSION_PASSWORD_DOES_NOT_COMPLY | Password policy violation | FIX Spec §4.8.6 |
| 4 | SESSION_LOGOUT_COMPLETE | Logout complete | FIX Spec §4.8.6 |
| 5 | INVALID_USERNAME_OR_PASSWORD | Invalid credentials | FIX Spec §4.8.6 |
| 6 | ACCOUNT_LOCKED | Account locked | FIX Spec §4.8.6 |
| 7 | LOGONS_NOT_ALLOWED_AT_THIS_TIME | Logons not allowed | FIX Spec §4.8.6 |
| 8 | PASSWORD_EXPIRED | Password expired | FIX Spec §4.8.6 |
| 100 | PASSWORD_CHANGE_IS_REQUIRED | Password change required | FIX Spec §4.8.6 |
| 101 | OTHER | Other | FIX Spec §4.8.6 |

## Message Example (Tabby CSV Format)

### Example: Client-Initiated Logout
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME
```

### Example: Gateway Logout with Reason
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,SessionStatus,Text
FIXT.1.1,,,1,,LME,20240101-12:00:00.000,CLIENT1,6,Account locked due to failed login attempts
```

### Example: Password Expired
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,SessionStatus
FIXT.1.1,,,1,,LME,20240101-12:00:00.000,CLIENT1,8
```

## Processing Rules

### Logout Handling
1. Acknowledge logout request
2. Cancel any pending orders (optional, configurable)
3. Clean up session state
4. Close TCP connection

### Session Cleanup
- Sequence numbers preserved unless ResetSeqNumFlag was set
- Session may be re-established with new Logon
- Pending orders may be cancelled based on configuration

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1 §4.8.6
- **Session Management:** FIX Spec §1.4
