# Logon

**Domain:** Order Entry  
**Message Type:** A  
**Category:** Session  
**Direction:** Bidirectional  

## Message Overview

Establish or accept a FIX session between client and LME gateway.

## Message Specification

### FIX Protocol Details
- **Message Type:** `A`
- **Message Name:** Logon
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Bidirectional (Client→Gateway and Gateway→Client)

### Message Structure
```
Logon (A)
├── Standard Header
│   ├── BeginString (8)
│   ├── BodyLength (9)
│   ├── MsgType (35) = A
│   ├── SenderCompID (49)
│   ├── TargetCompID (56)
│   ├── MsgSeqNum (34)
│   └── SendingTime (52)
├── Message Body
│   ├── EncryptMethod (98) - Must be 0 (None)
│   ├── HeartBtInt (108) - Heartbeat interval in seconds
│   ├── ResetSeqNumFlag (141) - Y/N (optional)
│   ├── Username (553) - Authentication username
│   ├── Password (554) - Authentication password
│   └── DefaultApplVerID (1137) - Application version
└── Standard Trailer
    └── CheckSum (10)
```

## Message Interaction Flow

### Successful Logon
```
Client → Gateway: Logon (A) with credentials
Gateway → Client: Logon (A) acknowledgment
[Session Established]
Client ↔ Gateway: Business messages
```

### Failed Logon
```
Client → Gateway: Logon (A) with invalid credentials
Gateway → Client: Logout (5) with Text (58) explaining reason
[Session Not Established]
```

### Session Reset
```
Client → Gateway: Logon (A) with ResetSeqNumFlag=Y
Gateway → Client: Logon (A) with ResetSeqNumFlag=Y
[Sequence Numbers Reset to 1]
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version (FIXT.1.1) |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = A |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 98 | EncryptMethod | Int | Encryption method: 0=None |
| 108 | HeartBtInt | Int | Heartbeat interval in seconds |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 141 | ResetSeqNumFlag | Boolean | Reset sequence numbers Y/N |
| 553 | Username | String | Username for authentication |
| 554 | Password | String | Password for authentication |
| 1137 | DefaultApplVerID | String | Application version ID |
| 58 | Text | String | Additional information |

## Message Example (Tabby CSV Format)

### Example: Logon (A)

```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,Text,EncryptMethod,HeartBtInt,ResetSeqNumFlag,Username,Password,DefaultApplVerID
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,Sample text,0,30,Y,user123,pass123,9
```

### Example: Logon (A) - Gateway→Client

```csv
# Message: Logon (A)
# Direction: Gateway→Client
# Description: Logon acknowledgment

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version FIXT.1.1
BodyLength,,9,Length,Will be calculated
MsgType,A,35,String,Message type
SenderCompID,LME,49,String,LME CompID
TargetCompID,CLIENT1,56,String,Your CompID
MsgSeqNum,1,34,SeqNum,First message of session
SendingTime,20240101-08:00:00.050,52,UTCTimestamp,Current timestamp
EncryptMethod,0,98,Int,0=None (no encryption)
HeartBtInt,30,108,Int,Heartbeat interval 30 seconds
CheckSum,,10,String,Will be calculated
```

### Notes:
- **BodyLength** (9) and **CheckSum** (10) are calculated automatically
- **SendingTime** (52) should be current UTC timestamp
- **MsgSeqNum** (34) should be 1 for first message of session
- **HeartBtInt** (108) is negotiated value (both sides must agree)
- **EncryptMethod** (98) must be 0 (no encryption) for LME
- **Username** (553) and **Password** (554) are required for authentication

## Processing Rules

### When to Send
- **Initial Logon:** At session startup, before any business messages
- **Session Reset:** When resetting sequence numbers (with ResetSeqNumFlag=Y)
- **Reconnection:** After network disconnect and reconnect

### Validation Requirements
1. **Protocol Version:**
   - BeginString must be supported (FIXT.1.1 for FIX 5.0)
   - DefaultApplVerID must indicate FIX version

2. **Authentication:**
   - Username and password must be valid
   - SenderCompID must be registered
   - IP address may be validated

3. **Session Parameters:**
   - HeartBtInt must be within acceptable range (e.g., 5-60 seconds)
   - EncryptMethod must be 0 (no encryption)
   - Sequence numbers must be valid (or reset if ResetSeqNumFlag=Y)

## Resulting Messages

### Successful Logon
- **Result:** Session established
- **Next Expected:** Heartbeat (0) messages at HeartBtInt interval
- **Business Messages:** Can now be exchanged

### Failed Logon
- **Result:** Session not established
- **Response:** Logout (5) with Text (58) explaining reason
- **Retry:** May retry with correct credentials

### Session Events
- **Heartbeat Timeout:** If no message received within HeartBtInt + reasonable time, send Test Request (1)
- **Sequence Gap:** If gap detected, send Resend Request (2)
- **Logout:** Either party may send Logout (5) to terminate session

## Testing Considerations

### Positive Test Cases
1. ✅ Valid logon with correct credentials
2. ✅ Logon with ResetSeqNumFlag=Y (sequence reset)
3. ✅ Logon with HeartBtInt at minimum value
4. ✅ Logon with HeartBtInt at maximum value
5. ✅ Reconnection after network disconnect

### Negative Test Cases
1. ❌ Invalid username/password - should reject
2. ❌ Unknown SenderCompID - should reject
3. ❌ Invalid HeartBtInt (too low/high) - should reject
4. ❌ Missing Username/Password - should reject
5. ❌ Unsupported EncryptMethod - should reject
6. ❌ Invalid MsgSeqNum (not 1 for new session) - should handle per rules

### Edge Cases
1. ⚠️ Logon while already logged on (should reject or replace)
2. ⚠️ Simultaneous logon from same SenderCompID
3. ⚠️ Logon during market close
4. ⚠️ Logon with mismatched HeartBtInt values
5. ⚠️ Logon after session end time

## Business Rules

### Authentication
- Username and password must match credentials on file
- Account must be active (not suspended)
- User must have permission to logon
- IP restrictions may apply

### Session Management
- Only one session per SenderCompID (typically)
- Sequence numbers must be monotonically increasing
- Gap detection and handling required
- Session state must be tracked (logged on, logged off)

### Heartbeat Management
- Heartbeat messages must be sent at HeartBtInt interval
- Test Request sent if heartbeat missed
- Session terminates if multiple heartbeats missed
- Heartbeats carry sequence numbers

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
- **Section:** 4.8.1 Logon (A)
- **Examples:** LMEselect v10 FIX Message Examples
- **Related:** Heartbeat (0), Test Request (1), Logout (5)

## Implementation Notes

- **Session state:** Track logged on/off state
- **Sequence numbers:** Track next expected inbound/outbound
- **Heartbeat timer:** Send heartbeats at HeartBtInt interval
- **Test request:** Send if no message received in (HeartBtInt + reasonable time)
- **Resend request:** Request retransmission if gap detected
- **Logout:** Graceful termination with Logout message
