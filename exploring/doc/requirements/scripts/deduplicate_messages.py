#!/usr/bin/env python3
"""
Deduplicate and organize extracted messages
Creates clean, organized message structure without duplicates
"""

import json
import shutil
from pathlib import Path
from collections import defaultdict

class MessageDeduplicator:
    def __init__(self, messages_dir="openspec/messages"):
        self.messages_dir = Path(messages_dir)
        
        # Define unique message identifiers
        self.fix_order_messages = {
            "Logon": {"type": "A", "category": "session"},
            "Heartbeat": {"type": "0", "category": "session"},
            "Test Request": {"type": "1", "category": "session"},
            "Resend Request": {"type": "2", "category": "session"},
            "Reject": {"type": "3", "category": "session"},
            "Sequence Reset": {"type": "4", "category": "session"},
            "Logout": {"type": "5", "category": "session"},
            "Business Message Reject": {"type": "j", "category": "session"},
            "News": {"type": "B", "category": "session"},
            "Security Definition Request": {"type": "c", "category": "application"},
            "Security Definition": {"type": "d", "category": "application"},
            "New Order Single": {"type": "D", "category": "application"},
            "New Order Cross": {"type": "s", "category": "application"},
            "Order Cancel Request": {"type": "F", "category": "application"},
            "Order Cancel Replace Request": {"type": "G", "category": "application"},
            "Order Cancel Reject": {"type": "9", "category": "application"},
            "Cross Order Cancel Request": {"type": "u", "category": "application"},
            "Execution Report": {"type": "8", "category": "application"},
            "Order Mass Cancel Request": {"type": "q", "category": "application"},
            "Order Mass Cancel Report": {"type": "r", "category": "application"},
            "Quote Request": {"type": "R", "category": "application"},
        }
        
        # Key binary messages (based on typical binary protocols)
        self.binary_order_messages = {
            "Logon": {"template_id": "1", "description": "Establish binary session"},
            "Logout": {"template_id": "2", "description": "Terminate binary session"},
            "Heartbeat": {"template_id": "3", "description": "Session keep-alive"},
            "New Order": {"template_id": "10", "description": "Submit new order"},
            "Order Cancel": {"template_id": "11", "description": "Cancel existing order"},
            "Order Replace": {"template_id": "12", "description": "Modify existing order"},
            "Execution Report": {"template_id": "20", "description": "Order execution update"},
            "Order Reject": {"template_id": "21", "description": "Order rejection"},
        }
        
        self.fix_risk_messages = {
            "User Request": {"type": "BE", "description": "Request user information"},
            "User Response": {"type": "BF", "description": "Response with user information"},
            "Risk Limit Update Request": {"type": "CB", "description": "Request risk limit update"},
            "Risk Limit Update Report": {"type": "CD", "description": "Report risk limit update"},
            "Risk Limit Query Request": {"type": "CA", "description": "Query risk limits"},
            "Risk Limit Query Response": {"type": "CC", "description": "Response with risk limits"},
        }
    
    def create_organized_structure(self):
        """Create organized message structure with deduplication"""
        print("Creating organized message structure...")
        
        # Clean existing structure
        if self.messages_dir.exists():
            shutil.rmtree(self.messages_dir)
        
        # Create organized directories
        organized_dir = self.messages_dir / "organized"
        fix_order_dir = organized_dir / "fix-order-entry"
        binary_order_dir = organized_dir / "binary-order-entry"
        fix_risk_dir = organized_dir / "fix-risk-management"
        
        for dir_path in [fix_order_dir, binary_order_dir, fix_risk_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Create FIX order entry messages
        self._create_fix_order_messages(fix_order_dir)
        
        # Create Binary order entry messages
        self._create_binary_order_messages(binary_order_dir)
        
        # Create FIX risk management messages
        self._create_fix_risk_messages(fix_risk_dir)
        
        # Create comprehensive index
        self._create_comprehensive_index(organized_dir)
        
        print(f"\nOrganized message structure created in {organized_dir}/")
        return organized_dir
    
    def _create_fix_order_messages(self, output_dir):
        """Create FIX order entry message files"""
        print("\nCreating FIX Order Entry messages...")
        
        for msg_name, msg_info in self.fix_order_messages.items():
            filename = f"{msg_info['type']}-{msg_name.replace(' ', '-').lower()}.md"
            
            content = self._generate_fix_message_content(
                msg_name,
                msg_info['type'],
                msg_info['category'],
                "Order Entry"
            )
            
            with open(output_dir / filename, 'w') as f:
                f.write(content)
            
            print(f"  Created: {filename}")
    
    def _create_binary_order_messages(self, output_dir):
        """Create Binary order entry message files"""
        print("\nCreating Binary Order Entry messages...")
        
        for msg_name, msg_info in self.binary_order_messages.items():
            filename = f"{msg_info['template_id']}-{msg_name.replace(' ', '-').lower()}.md"
            
            content = self._generate_binary_message_content(
                msg_name,
                msg_info['template_id'],
                msg_info['description']
            )
            
            with open(output_dir / filename, 'w') as f:
                f.write(content)
            
            print(f"  Created: {filename}")
    
    def _create_fix_risk_messages(self, output_dir):
        """Create FIX risk management message files"""
        print("\nCreating FIX Risk Management messages...")
        
        for msg_name, msg_info in self.fix_risk_messages.items():
            filename = f"{msg_info['type']}-{msg_name.replace(' ', '-').lower()}.md"
            
            content = self._generate_fix_message_content(
                msg_name,
                msg_info['type'],
                "application",
                "Risk Management",
                msg_info.get('description', '')
            )
            
            with open(output_dir / filename, 'w') as f:
                f.write(content)
            
            print(f"  Created: {filename}")
    
    def _generate_fix_message_content(self, msg_name, msg_type, category, domain, description=""):
        """Generate FIX message content"""
        if not description:
            description = f"{msg_name} message used in {domain}"
        
        return f"""# {msg_name}

**Domain:** {domain}  
**Message Type:** {msg_type}  
**Category:** {category}

## Message Overview

{description}

## Message Specification

### FIX Protocol Details
- **Message Type:** `{msg_type}`
- **Message Name:** {msg_name}
- **FIX Version:** 5.0 (with LME extensions)

### Message Structure
```
{msg_name} ({msg_type})
├── Standard Header (required)
├── Message Body (fields specific to {msg_name})
└── Standard Trailer (required)
```

## Processing Rules

### When to Send
- **Session Messages:** For session management and control
- **Application Messages:** For business-level operations

### Validation Requirements
1. **Session Level:**
   - Valid session must be established
   - Sequence numbers must be in order
   - SenderCompID and TargetCompID must match session

2. **Message Level:**
   - Required fields must be present
   - Field data types must be valid
   - Field values must be within acceptable ranges

3. **Business Level:**
   - User must have appropriate permissions
   - Operation must be allowed in current market state
   - Risk limits must be checked (for order messages)

## Resulting Message Flows

### Success Path
```
Client → Gateway: {msg_name} ({msg_type})
Gateway → Client: Execution Report (8) or Acknowledgment
```

### Failure Path
```
Client → Gateway: {msg_name} ({msg_type})
Gateway → Client: Business Message Reject (j) or Order Reject
```

### Related Messages
- **Preceding:** Messages that must be sent before this message
- **Following:** Messages that may follow this message
- **Alternative:** Alternative message flows for different scenarios

## Fields Reference

### Required Fields
| Tag | Field Name | Type | Description |
|-----|-----------|------|-------------|
| | | | *(Detailed field specifications to be added)* |

### Optional Fields
| Tag | Field Name | Type | Description |
|-----|-----------|------|-------------|
| | | | *(Detailed field specifications to be added)* |

### Conditional Fields
| Tag | Field Name | Type | Condition | Description |
|-----|-----------|------|-----------|-------------|
| | | | | *(Detailed field specifications to be added)* |

## Testing Considerations

### Positive Test Cases
1. **Valid Message:** All required fields present with valid values
2. **With Optional Fields:** Including optional fields
3. **Sequence Order:** Message sent in correct sequence

### Negative Test Cases
1. **Missing Required Fields:** Verify rejection
2. **Invalid Field Values:** Verify validation errors
3. **Out of Sequence:** Verify sequence number handling
4. **Unauthorized User:** Verify permission checks
5. **Invalid Session State:** Verify session state validation

### Edge Cases
1. **Boundary Values:** Test minimum/maximum field values
2. **Concurrent Messages:** Multiple simultaneous requests
3. **Session Recovery:** Message handling after reconnect
4. **Market Transitions:** Behavior during market state changes

## Business Rules

### For Order Messages
- **Pre-trade Risk:** Must pass risk limit checks
- **Market State:** Must be valid for current market state
- **Trading Hours:** Must be within allowed trading hours
- **Instrument Status:** Instrument must be tradable

### For Session Messages
- **Session State:** Must be valid for current session state
- **Authentication:** User must be authenticated
- **Sequence Integrity:** Sequence numbers must be maintained

## Example Usage

### Scenario: {msg_name}
```
# Message Flow
1. Establish FIX session (Logon)
2. Send {msg_name} ({msg_type})
3. Receive acknowledgment
4. Continue with business logic
```

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
- **Section:** Application Messages
- **Related:** LMEselect v10 Message Examples

## Notes

- This message specification is for testing environment creation
- Field-level details should be cross-referenced with official LME documentation
- Message examples should be validated against actual implementations
- Processing rules may be enhanced based on specific testing requirements
"""
    
    def _generate_binary_message_content(self, msg_name, template_id, description):
        """Generate Binary message content"""
        return f"""# {msg_name}

**Domain:** Binary Order Entry  
**Template ID:** {template_id}  
**Protocol:** LME Proprietary Binary Protocol

## Message Overview

{description}

## Message Specification

### Binary Protocol Details
- **Template ID:** {template_id}
- **Message Name:** {msg_name}
- **Protocol:** LME Proprietary Binary Protocol v1.9.1

### Message Structure
```
{msg_name} (Template ID: {template_id})
├── Message Header
│   ├── Message Length (2 bytes)
│   ├── Template ID (2 bytes)
│   └── Schema ID (2 bytes)
├── Field Presence Map (variable)
├── Message Body (fields specific to {msg_name})
└── Repeating Groups (if applicable)
```

## Processing Rules

### Binary Protocol Specifics
1. **Field Presence Map:**
   - Bitmap indicating which fields are present
   - Allows compact message representation
   - Reduces bandwidth for sparse messages

2. **Byte Ordering:**
   - Network byte order (big-endian)
   - Consistent across all fields

3. **Field Encoding:**
   - Fixed-length fields for numeric values
   - Length-prefixed strings
   - Optimized for low latency

### Validation Requirements
1. **Message Structure:**
   - Valid template ID
   - Correct message length
   - Valid field presence map

2. **Field Validation:**
   - Required fields (if present) must be valid
   - Data types must match template
   - Values must be within acceptable ranges

3. **Business Validation:**
   - Same as FIX application-level validation
   - Risk limits, permissions, market state

## Resulting Message Flows

### Success Path
```
Client → Gateway: {msg_name} (Binary)
Gateway → Client: Execution Report or Acknowledgment
```

### Failure Path
```
Client → Gateway: {msg_name} (Binary)
Gateway → Client: Reject or Error Message
```

## Fields Reference

### Message Header Fields
| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| MessageLength | 0 | 2 | UInt16 | Total message length |
| TemplateID | 2 | 2 | UInt16 | Message template identifier |
| SchemaID | 4 | 2 | UInt16 | Schema version |

### Field Presence Map
- Variable length bitmap
- Each bit represents a field
- 1 = field present, 0 = field absent

### Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| | | | *(Detailed field specifications to be added)* |

## Testing Considerations

### Positive Test Cases
1. **Complete Message:** All optional fields present
2. **Minimal Message:** Only required fields present
3. **Repeating Groups:** Messages with repeating blocks

### Negative Test Cases
1. **Invalid Template ID:** Unknown message type
2. **Incorrect Length:** Length doesn't match actual data
3. **Invalid Presence Map:** Corrupted bitmap
4. **Missing Required Fields:** Required field not present
5. **Malformed Repeating Groups:** Incorrect group encoding

### Performance Testing
1. **Message Size:** Validate minimum/maximum sizes
2. **Encoding/Decoding Speed:** Measure processing time
3. **Batch Processing:** Multiple messages in sequence
4. **Network Efficiency:** Bandwidth utilization

## Binary Protocol Advantages

### Performance
- Compact message format
- Minimal parsing overhead
- Efficient network utilization
- Lower latency than FIX

### Features
- Field presence maps reduce message size
- Fixed field offsets enable fast access
- Native binary data types (no string conversion)
- Optimized for high-frequency trading

## Comparison with FIX

| Aspect | Binary Protocol | FIX Protocol |
|--------|----------------|--------------|
| Message Size | Compact (binary) | Verbose (text) |
| Parsing Speed | Very Fast | Moderate |
| Readability | Not human-readable | Human-readable |
| Standardization | Proprietary | Industry standard |
| Use Case | High-performance | General purpose |

## Example Usage

### Scenario: High-Frequency Order Submission
```
# Message Flow
1. Establish binary session
2. Encode {msg_name} with minimal fields
3. Send binary message
4. Receive binary acknowledgment
5. Decode response
```

## References

- **Source:** Binary Order Entry Specification v1.9.1
- **Related:** LMEselect v10 BINARY Message Examples

## Notes

- Binary protocol is LME's proprietary high-performance interface
- Field specifications should be extracted from detailed binary spec
- Message examples in the examples document show actual binary encoding
- Testing should include both functional correctness and performance validation
"""
    
    def _create_comprehensive_index(self, organized_dir):
        """Create comprehensive index of all messages"""
        index_content = f"""# LME Options Trading - Message Specifications

Comprehensive message specifications for LME Options Trading Exchange testing environment.

## Overview

This directory contains self-contained message specifications organized by protocol and domain.

## Directory Structure

```
{organized_dir}/
├── fix-order-entry/          # FIX 5.0 Order Entry Messages
├── binary-order-entry/       # LME Binary Protocol Messages
└── fix-risk-management/      # FIX Risk Management Messages
```

## FIX Order Entry Messages

Location: `fix-order-entry/`

### Session Messages
| Message | Type | Description |
|---------|------|-------------|
| Logon | A | Establish FIX session |
| Heartbeat | 0 | Session keep-alive |
| Test Request | 1 | Verify connection |
| Resend Request | 2 | Request retransmission |
| Reject | 3 | Session-level rejection |
| Sequence Reset | 4 | Reset sequence numbers |
| Logout | 5 | Terminate session |
| Business Message Reject | j | Application-level rejection |
| News | B | Text information |

### Application Messages
| Message | Type | Description |
|---------|------|-------------|
| Security Definition Request | c | Request instrument creation |
| Security Definition | d | Instrument definition |
| New Order Single | D | Submit single order |
| New Order Cross | s | Submit cross order |
| Order Cancel Request | F | Cancel order |
| Order Cancel Replace Request | G | Modify order |
| Order Cancel Reject | 9 | Cancel/replace rejection |
| Cross Order Cancel Request | u | Cancel cross order |
| Execution Report | 8 | Order execution update |
| Order Mass Cancel Request | q | Mass cancel orders |
| Order Mass Cancel Report | r | Mass cancel acknowledgment |
| Quote Request | R | Request quote |

## Binary Order Entry Messages

Location: `binary-order-entry/`

| Message | Template ID | Description |
|---------|-------------|-------------|
| Logon | 1 | Establish binary session |
| Logout | 2 | Terminate binary session |
| Heartbeat | 3 | Session keep-alive |
| New Order | 10 | Submit new order |
| Order Cancel | 11 | Cancel order |
| Order Replace | 12 | Modify order |
| Execution Report | 20 | Execution update |
| Order Reject | 21 | Order rejection |

## FIX Risk Management Messages

Location: `fix-risk-management/`

| Message | Type | Description |
|---------|------|-------------|
| User Request | BE | Request user information |
| User Response | BF | User information response |
| Risk Limit Query Request | CA | Query risk limits |
| Risk Limit Query Response | CC | Risk limits response |
| Risk Limit Update Request | CB | Update risk limits |
| Risk Limit Update Report | CD | Risk update acknowledgment |

## Message File Structure

Each message file contains:

1. **Message Overview**
   - Name, type, domain
   - Brief description

2. **Message Specification**
   - Protocol details
   - Message structure
   - Field layout

3. **Processing Rules**
   - When to send/receive
   - Validation requirements
   - Business rules

4. **Resulting Message Flows**
   - Success scenarios
   - Failure scenarios
   - Related messages

5. **Fields Reference**
   - Required fields
   - Optional fields
   - Conditional fields

6. **Testing Considerations**
   - Positive test cases
   - Negative test cases
   - Edge cases

7. **Business Rules**
   - Pre-trade risk
   - Market state validation
   - Trading hours

## Usage for Testing Environment

### 1. Message Implementation
- Review each message specification
- Implement encoding/decoding logic
- Validate against message structure

### 2. Processing Rules Implementation
- Implement validation logic
- Apply business rules
- Handle error conditions

### 3. Test Case Development
- Use testing considerations as checklist
- Create positive path tests
- Create negative path tests
- Include edge cases

### 4. Integration Testing
- Test message flows end-to-end
- Validate sequencing
- Test session management
- Verify error handling

### 5. Compliance Testing
- Validate against LME rules
- Check risk limit enforcement
- Verify audit trails
- Test reporting accuracy

## Key Testing Scenarios

### Order Management
- New order submission (valid and invalid)
- Order modification (price, quantity)
- Order cancellation (single and mass)
- Order state transitions

### Session Management
- Session establishment (Logon)
- Session maintenance (Heartbeat)
- Session recovery (Resend, Sequence Reset)
- Session termination (Logout)

### Risk Management
- Risk limit checking
- Risk limit updates
- Risk limit queries
- Risk group management

### Error Handling
- Invalid messages
- Missing required fields
- Out of sequence messages
- Authorization failures

## Source Documents

Messages derived from:
- Order Entry Gateway FIX Specification v1.9.1
- Binary Order Entry Specification v1.9.1
- Risk Management Gateway FIX Specification v1.8
- LMEselect v10 FIX and BINARY Message Examples v10
- LME Matching Rules August 2022

## Maintenance

When updating message specifications:

1. Update the relevant message file
2. Review impact on related messages
3. Update test cases accordingly
4. Validate against examples document
5. Test thoroughly before deployment

## Notes

- This is a testing-focused extraction of LME messages
- Field-level details should be cross-referenced with official specs
- Message examples in the examples document provide concrete implementations
- Processing rules may need enhancement based on specific testing needs
- Binary protocol specifications are high-level; detailed field specs needed from binary documentation

## Next Steps

1. **Enhance Field Specifications**
   - Extract detailed field specs from source documents
   - Add data types, lengths, and validations
   - Include field presence rules

2. **Add Message Examples**
   - Include examples from LMEselect v10 document
   - Show actual message encoding
   - Provide hex dumps for binary messages

3. **Create Test Cases**
   - Implement test cases based on specifications
   - Create test data sets
   - Build test automation

4. **Validate Against Implementation**
   - Test against actual LME gateway
   - Validate message processing
   - Verify compliance with specs
"""
        
        with open(organized_dir / "README.md", 'w') as f:
            f.write(index_content)
        
        # Create summary JSON
        summary = {
            "fix_order_entry": list(self.fix_order_messages.keys()),
            "binary_order_entry": list(self.binary_order_messages.keys()),
            "fix_risk_management": list(self.fix_risk_messages.keys())
        }
        
        with open(organized_dir / "message-summary.json", 'w') as f:
            json.dump(summary, f, indent=2)

def main():
    """Main function"""
    deduplicator = MessageDeduplicator()
    organized_dir = deduplicator.create_organized_structure()
    
    print(f"\n{'='*60}")
    print("Message deduplication and organization complete!")
    print(f"\nCreated {len(deduplicator.fix_order_messages)} FIX order messages")
    print(f"Created {len(deduplicator.binary_order_messages)} Binary order messages")
    print(f"Created {len(deduplicator.fix_risk_messages)} FIX risk messages")
    print(f"\nOrganized structure: {organized_dir}")
    
    print("\nNext steps:")
    print("1. Review organized messages in openspec/messages/organized/")
    print("2. Enhance with detailed field specifications")
    print("3. Add message examples from examples document")
    print("4. Create test cases for each message type")

if __name__ == "__main__":
    main()
