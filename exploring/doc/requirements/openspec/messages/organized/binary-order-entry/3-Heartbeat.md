# Heartbeat

**Domain:** Binary Order Entry  
**Template ID:** 3  
**Category:** Application  
**Direction:** Bidirectional (Client↔Gateway)  

## Message Overview

Heartbeat message for LME Binary Order Entry protocol. Used to monitor connection health and detect disconnections.

## Message Specification

### Binary Protocol Details
- **Template ID:** 3
- **Message Name:** Heartbeat
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §1.4

## Message Structure
```
Heartbeat (Template ID: 3)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 3
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (1 byte)
└── Message Body
    └── TestReqID (optional)
```

## Message Interaction Flow

### Periodic Heartbeat
```
Client ↔ Gateway: Heartbeat (every HeartBtInt seconds)
Response: Heartbeat acknowledgment
```

### Heartbeat After Test Request
```
Gateway → Client: Test Request (with TestReqID)
Client → Gateway: Heartbeat (with same TestReqID)
```

## Fields Reference

### Header Fields (Always Present)
| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| MessageLength | 0 | 2 | UInt16 | Total message length |
| TemplateID | 2 | 2 | UInt16 | Message template ID = 3 |
| SchemaID | 4 | 2 | UInt16 | Schema version |

### Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| TestReqID | String(20) | Optional | Echoed from Test Request |

## Heartbeat Timing Rules

### Default Heartbeat Interval
- **HeartBtInt**: 30 seconds (default)
- Configured during Logon

### Heartbeat Trigger Conditions
1. **Periodic**: Sent every HeartBtInt seconds if no other messages sent
2. **Response**: Sent in response to Test Request with matching TestReqID

### Missed Heartbeat Detection
- If no heartbeat received within 3 x HeartBtInt, connection is considered dead
- Gateway initiates logout sequence

## Message Example (Binary Hex Dump)

### Example: Periodic Heartbeat (no TestReqID)
```
00 06          # Message Length: 6 bytes (header only)
03 00          # Template ID: 3
01 00          # Schema ID: 1
00             # Presence Map: No optional fields
```

### Example: Heartbeat Response to Test Request
```
00 0C          # Message Length: 12 bytes
03 00          # Template ID: 3
01 00          # Schema ID: 1
01             # Presence Map: TestReqID present
04 54 45 53 54  # TestReqID: "TEST" (4 bytes)
```

## Processing Rules

### Binary Protocol Specifics
1. **Field Presence Map:**
   - Bit 0: TestReqID present
   - If TestReqID absent, presence map = 0x00

2. **Byte Ordering:**
   - All multi-byte integers: Little-endian

3. **TestReqID Handling:**
   - Must echo the same TestReqID from Test Request
   - Used to verify round-trip connectivity

### Validation Requirements
- Session must be established
- If TestReqID present, must match pending Test Request
- Message length must be correct

## Testing Considerations

### Positive Test Cases
1. ✅ Periodic heartbeat with no TestReqID
2. ✅ Heartbeat response with matching TestReqID
3. ✅ Heartbeat at correct interval

### Negative Test Cases
1. ❌ Heartbeat with invalid TestReqID
2. ❌ Heartbeat without active session
3. ❌ Message length mismatch

## References

- **Source:** Binary Order Entry Specification v1.9.1 §1.4
- **Session Management:** Binary Spec §1.4
- **Test Request:** Binary Spec §1.5
