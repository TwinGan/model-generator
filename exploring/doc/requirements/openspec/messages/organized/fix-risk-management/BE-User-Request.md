# User Request

**Domain:** Risk Management  
**Message Type:** BE  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

User Request message for LME Risk Management Gateway. Used to request user information or manage user accounts.

## Message Specification

### FIX Protocol Details
- **Message Type:** `BE`
- **Message Name:** User Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.6.1

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: User Request (BE)
Gateway → Client: User Response (BF)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = BE |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 923 | UserRequestID | String | Required | Unique request ID |
| 924 | UserRequestType | Int | Required | Type of user request |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 553 | Username | String | Conditional | Username (for specific user query) |
| 554 | Password | String | Conditional | Password (for password change) |
| 925 | NewPassword | String | Conditional | New password (for password change) |
| 802 | NoPartyIDs | NumInGroup | Optional | Party identification group |

## UserRequestType Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | USER_REQUEST | Request user information | Risk Spec §4.6.1 |
| 2 | USER_ACCOUNT_DISABLE | Disable user account | Risk Spec §4.6.1 |
| 3 | USER_ACCOUNT_ENABLE | Enable user account | Risk Spec §4.6.1 |
| 4 | USER_PASSWORD_CHANGE | Change password | Risk Spec §4.6.1 |

## Message Example (Tabby CSV Format)

### Example: Query User Information
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,UserRequestID,UserRequestType,Username
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,REQ001,1,trader1
```

### Example: Change Password
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,UserRequestID,UserRequestType,Username,Password,NewPassword
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,REQ002,4,trader1,oldpass,newpass
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- User must have appropriate risk management permissions
- UserRequestID must be unique

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.6.1
- **FIX Version:** 5.0 with LME extensions
