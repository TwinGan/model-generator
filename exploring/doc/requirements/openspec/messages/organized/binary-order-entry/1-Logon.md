# Logon

**Domain:** Binary Order Entry  
**Template ID:** 1  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Logon message for LME Binary Order Entry protocol. Used to authenticate and establish a binary session with the gateway.

## Message Specification

### Binary Protocol Details
- **Template ID:** 1
- **Message Name:** Logon
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §1.1

## Message Structure
```
Logon (Template ID: 1)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 1
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── CompID (String)
    ├── Password (String)
    └── EncryptedPassword (optional)
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Logon (Binary Template 1)
Gateway → Client: Logon Response (Binary Template 1)
```

### Failure Scenario
```
Client → Gateway: Logon (Binary Template 1)
Gateway → Client: Logout (Binary Template 2) with SessionStatus
```

## Fields Reference

### Header Fields (Always Present)
| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| MessageLength | 0 | 2 | UInt16 | Total message length |
| TemplateID | 2 | 2 | UInt16 | Message template ID = 1 |
| SchemaID | 4 | 2 | UInt16 | Schema version |

### Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| CompID | String(20) | Required | Company identifier |
| Password | String(64) | Required | Session password |
| EncryptedPassword | String(256) | Optional | RSA-encrypted password |
| HeartBtInt | UInt16 | Optional | Heartbeat interval (seconds) |
| DefaultApplVerID | UInt8 | Optional | Application version ID |
| ResetSeqNumFlag | Boolean | Optional | Reset sequence numbers |

## Binary Encoding Rules

### Field Presence Map
- Bitmap indicating which optional fields are present
- 1 bit per optional field
- Little-endian byte order

### Byte Ordering
- All multi-byte integers: **Little-endian**
- String encoding: UTF-8, length-prefixed (1-byte length)

### String Encoding
```
[String Field]
├── Length (1 byte, UInt8)
└── Data (N bytes, UTF-8)
```

## RSA Encryption Rules
1. Password may be encrypted using RSA-2048
2. Public key obtained from exchange
3. Encrypted password sent in EncryptedPassword field
4. If encrypted, Password field is empty

## Message Example (Binary Hex Dump)

### Example: Logon (Template ID: 1)
```
00 1E          # Message Length: 30 bytes
01 00          # Template ID: 1
01 00          # Schema ID: 1
FF             # Presence Map: All fields present
08 43 4C 49 45 4E 54 31  # CompID: "CLIENT1" (8 bytes)
08 50 41 53 53 57 4F 52 44  # Password: "PASSWORD" (8 bytes)
1E 00          # HeartBtInt: 30 seconds
```

## Processing Rules

### Validation Requirements
- CompID must be registered with exchange
- Password must match stored credentials
- EncryptedPassword must decrypt successfully if present
- Session must not already exist for CompID

### Authentication Flow
1. Parse binary message
2. Validate header fields
3. Extract credentials
4. Decrypt password if encrypted
5. Authenticate against member database
6. Create session if valid

## Testing Considerations

### Positive Test Cases
1. ✅ Valid logon with correct credentials
2. ✅ Logon with encrypted password
3. ✅ Logon with custom HeartBtInt
4. ✅ Logon with ResetSeqNumFlag=true

### Negative Test Cases
1. ❌ Invalid CompID
2. ❌ Incorrect password
3. ❌ Invalid encrypted password
4. ❌ Session already exists
5. ❌ Invalid template ID
6. ❌ Message length mismatch

## References

- **Source:** Binary Order Entry Specification v1.9.1 §1.1
- **Encryption:** RSA-2048 per Binary Spec §1.2
- **Session Management:** Binary Spec §1.4
