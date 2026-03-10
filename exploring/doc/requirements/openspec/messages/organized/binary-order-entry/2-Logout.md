# Logout

**Domain:** Binary Order Entry  
**Template ID:** 2  
**Category:** Application  
**Direction:** Bidirectional (Client↔Gateway)  

## Message Overview

Logout message for LME Binary Order Entry protocol. Used to terminate a binary session gracefully.

## Message Specification

### Binary Protocol Details
- **Template ID:** 2
- **Message Name:** Logout
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §1.6

## Message Structure
```
Logout (Template ID: 2)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 2
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    └── SessionStatus (optional)
    └── Text (optional)
```

## Message Interaction Flow

### Client-Initiated Logout
```
Client → Gateway: Logout (Binary Template 2)
Gateway → Client: Logout Acknowledgment (Binary Template 2)
Connection → Closed
```

### Gateway-Initiated Logout
```
Gateway → Client: Logout (Binary Template 2) with SessionStatus
Connection → Closed
```

## Fields Reference

### Header Fields (Always Present)
| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| MessageLength | 0 | 2 | UInt16 | Total message length |
| TemplateID | 2 | 2 | UInt16 | Message template ID = 2 |
| SchemaID | 4 | 2 | UInt16 | Schema version |

### Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| SessionStatus | UInt8 | Optional | Reason for logout |
| Text | String(256) | Optional | Free-form text description |

## SessionStatus Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | SESSION_ACTIVE | Session active | Binary Spec §1.6 |
| 2 | SESSION_LOGOUT_REQUESTED | Logout requested | Binary Spec §1.6 |
| 3 | NEW_SESSION_PASSWORD_DOES_NOT_COMPLY | Password policy violation | Binary Spec §1.6 |
| 4 | SESSION_LOGOUT_COMPLETE | Logout complete | Binary Spec §1.6 |
| 5 | INVALID_USERNAME_OR_PASSWORD | Invalid credentials | Binary Spec §1.6 |
| 6 | ACCOUNT_LOCKED | Account locked | Binary Spec §1.6 |
| 7 | LOGONS_NOT_ALLOWED | Logons not allowed | Binary Spec §1.6 |
| 8 | PASSWORD_EXPIRED | Password expired | Binary Spec §1.6 |
| 100 | PASSWORD_CHANGE_REQUIRED | Password change required | Binary Spec §1.6 |

## Message Example (Binary Hex Dump)

### Example: Logout (Template ID: 2)
```
00 12          # Message Length: 18 bytes
02 00          # Template ID: 2
01 00          # Schema ID: 1
03             # Presence Map: SessionStatus present
04             # SessionStatus: 4 (Logout Complete)
08 47 6F 6F 64 62 79 65  # Text: "Goodbye" (8 bytes)
```

### Example: Logout with Account Locked
```
00 10          # Message Length: 16 bytes
02 00          # Template ID: 2
01 00          # Schema ID: 1
03             # Presence Map: SessionStatus present
06             # SessionStatus: 6 (Account Locked)
```

## Processing Rules

### Binary Protocol Specifics
1. **Field Presence Map:**
   - Bitmap indicating which optional fields are present
   - Bit 0: SessionStatus present
   - Bit 1: Text present

2. **Byte Ordering:**
   - All multi-byte integers: Little-endian

3. **Session Cleanup:**
   - All pending orders may be cancelled
   - Sequence numbers preserved unless ResetSeqNumFlag was set

### Validation Requirements
- Session must be established before logout
- Template ID must be valid (2)
- Message length must match actual length

## Testing Considerations

### Positive Test Cases
1. ✅ Client-initiated logout
2. ✅ Logout with SessionStatus
3. ✅ Logout with Text message

### Negative Test Cases
1. ❌ Logout without active session
2. ❌ Invalid SessionStatus code
3. ❌ Message length mismatch

## References

- **Source:** Binary Order Entry Specification v1.9.1 §1.6
- **Session Management:** Binary Spec §1.4
- **SessionStatus:** Binary Spec §1.6
