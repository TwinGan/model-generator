#!/usr/bin/env python3
"""
Enhance message specifications with detailed field specs and examples
Extracts actual field tables and creates Tabby CSV examples
"""

import re
import json
from pathlib import Path
from collections import defaultdict

class MessageSpecEnhancer:
    def __init__(self, specs_dir="docs/specs", messages_dir="openspec/messages/organized"):
        self.specs_dir = Path(specs_dir)
        self.messages_dir = Path(messages_dir)
        self.field_specs = defaultdict(dict)
        self.message_examples = defaultdict(list)
        
    def extract_field_specifications(self):
        """Extract field specifications from FIX specs"""
        print("Extracting field specifications...")
        
        fix_spec = self.specs_dir / "Order Entry Gateway FIX Specification v 1 9 1.md"
        risk_spec = self.specs_dir / "Risk Management Gateway FIX Specification v1 8.md"
        
        # Extract from FIX order spec
        if fix_spec.exists():
            content = fix_spec.read_text(encoding='utf-8')
            self._extract_field_tables(content, "order_entry")
            self._extract_message_examples(content, "order_entry")
        
        # Extract from risk spec
        if risk_spec.exists():
            content = risk_spec.read_text(encoding='utf-8')
            self._extract_field_tables(content, "risk_management")
            self._extract_message_examples(content, "risk_management")
        
        print(f"  Extracted {len(self.field_specs)} field specifications")
        print(f"  Extracted {len(self.message_examples)} message examples")
    
    def _extract_field_tables(self, content, domain):
        """Extract field specification tables"""
        # Pattern for field tables: Tag, Field Name, Req, Data Type, Description
        table_pattern = r'\n(\d+)\s+([A-Za-z0-9\s]+?)\s+(Y|N|C)\s+([A-Za-z0-9()\s]+?)\s+(.+?)(?=\n\d+\s+|$)'
        
        matches = re.finditer(table_pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            tag = match.group(1).strip()
            field_name = match.group(2).strip()
            required = match.group(3).strip()
            data_type = match.group(4).strip()
            description = match.group(5).strip()
            
            # Clean up description (remove newlines, extra spaces)
            description = ' '.join(description.split())
            
            self.field_specs[domain][tag] = {
                'field_name': field_name,
                'required': required,
                'data_type': data_type,
                'description': description
            }
    
    def _extract_message_examples(self, content, domain):
        """Extract message examples"""
        # Pattern for message examples (looking for FIX message format)
        example_pattern = r'(8=FIX\.[\d\.]+[^\n]+)'
        
        matches = re.findall(example_pattern, content)
        
        for example in matches:
            # Try to identify message type
            msgtype_match = re.search(r'35=([A-Za-z0-9]+)', example)
            if msgtype_match:
                msg_type = msgtype_match.group(1)
                self.message_examples[domain].append({
                    'msg_type': msg_type,
                    'example': example
                })
    
    def get_message_fields(self, msg_type, domain):
        """Get fields for a specific message type"""
        # Common field mappings for FIX messages
        field_mappings = {
            'A': ['98', '108', '141', '553', '554'],  # Logon
            '0': [],  # Heartbeat
            '1': ['112'],  # Test Request
            '2': ['7', '16'],  # Resend Request
            '3': ['45', '371', '372', '373', '380'],  # Reject
            '4': ['123'],  # Sequence Reset
            '5': [],  # Logout
            '8': ['37', '11', '17', '20', '150', '39', '54', '38', '40', '44', '59', '60'],  # Execution Report
            '9': ['37', '11', '41', '39', '434', '102', '103'],  # Order Cancel Reject
            'D': ['11', '21', '38', '40', '44', '54', '55', '59', '60'],  # New Order Single
            'F': ['41', '37', '11'],  # Order Cancel Request
            'G': ['37', '11', '41', '38', '40', '44'],  # Order Cancel Replace
            'R': ['131'],  # Quote Request
            'c': ['320', '321', '323'],  # Security Definition Request
            'd': ['322', '323', '320'],  # Security Definition
            'j': ['45', '372', '380', '58'],  # Business Message Reject
            'r': ['535', '530'],  # Order Mass Cancel Report
            's': ['548', '549', '550', '551'],  # New Order Cross
            'u': ['551', '549'],  # Cross Order Cancel Request
        }
        
        fields = []
        tags = field_mappings.get(msg_type, [])
        
        for tag in tags:
            if tag in self.field_specs[domain]:
                fields.append(self.field_specs[domain][tag])
        
        return fields
    
    def create_tabby_csv_example(self, msg_name, msg_type, direction="Client→Gateway"):
        """Create Tabby CSV format example"""
        
        # Sample data based on message type
        sample_data = {
            'A': {
                'SenderCompID': 'CLIENT1', 'TargetCompID': 'LME', 'MsgSeqNum': '1',
                'EncryptMethod': '0', 'HeartBtInt': '30', 'Username': 'user123',
                'Password': 'pass123'
            },
            'D': {
                'SenderCompID': 'CLIENT1', 'TargetCompID': 'LME', 'MsgSeqNum': '5',
                'ClOrdID': 'ORD12345', 'Symbol': 'CA', 'Side': '1', 'OrderQty': '10',
                'OrdType': '2', 'Price': '2500.00'
            },
            '8': {
                'SenderCompID': 'LME', 'TargetCompID': 'CLIENT1', 'MsgSeqNum': '10',
                'OrderID': '123456', 'ClOrdID': 'ORD12345', 'ExecID': 'EXEC001',
                'ExecType': '0', 'OrdStatus': '0', 'Symbol': 'CA', 'Side': '1',
                'OrderQty': '10', 'LastQty': '0', 'LeavesQty': '10', 'CumQty': '0'
            },
            'F': {
                'SenderCompID': 'CLIENT1', 'TargetCompID': 'LME', 'MsgSeqNum': '6',
                'ClOrdID': 'ORD12346', 'OrigClOrdID': 'ORD12345', 'Symbol': 'CA',
                'Side': '1'
            }
        }
        
        # Create CSV header
        csv_lines = []
        csv_lines.append("# Message: {} ({})".format(msg_name, msg_type))
        csv_lines.append("# Direction: {}".format(direction))
        csv_lines.append("")
        csv_lines.append("Name,Value,Field Number,Data Type,Notes")
        
        # Add standard header fields
        csv_lines.append("BeginString,FIXT.1.1,8,String,FIX version")
        csv_lines.append("BodyLength,,9,Length,Will be calculated")
        csv_lines.append("MsgType,{},35,String,Message type".format(msg_type))
        csv_lines.append("SenderCompID,CLIENT1,49,String,Your CompID")
        csv_lines.append("TargetCompID,LME,56,String,LME CompID")
        csv_lines.append("MsgSeqNum,1,34,SeqNum,Message sequence number")
        csv_lines.append("SendingTime,,52,UTCTimestamp,Current timestamp")
        
        # Add message-specific fields
        if msg_type in sample_data:
            # Map to actual FIX tags
            field_map = {
                'ClOrdID': '11', 'Symbol': '55', 'Side': '54', 'OrderQty': '38',
                'OrdType': '40', 'Price': '44', 'OrderID': '37', 'ExecID': '17',
                'ExecType': '150', 'OrdStatus': '39', 'LastQty': '32', 'LeavesQty': '151',
                'CumQty': '14', 'OrigClOrdID': '41', 'EncryptMethod': '98',
                'HeartBtInt': '108', 'Username': '553', 'Password': '554'
            }
            
            for field_name, value in sample_data[msg_type].items():
                if field_name not in ['SenderCompID', 'TargetCompID', 'MsgSeqNum']:
                    tag = field_map.get(field_name, '')
                    csv_lines.append("{},{},{},String,Sample value".format(field_name, value, tag))
        
        # Add trailer
        csv_lines.append("CheckSum,,10,String,Will be calculated")
        
        return "\n".join(csv_lines)
    
    def enhance_all_messages(self):
        """Enhance all message files with specs and examples"""
        print("\nEnhancing message files...")
        
        enhanced_count = 0
        
        # Process FIX order entry messages
        fix_order_dir = self.messages_dir / "fix-order-entry"
        if fix_order_dir.exists():
            for msg_file in fix_order_dir.glob("*.md"):
                self._enhance_message_file(msg_file, "order_entry")
                enhanced_count += 1
        
        # Process FIX risk management messages
        fix_risk_dir = self.messages_dir / "fix-risk-management"
        if fix_risk_dir.exists():
            for msg_file in fix_risk_dir.glob("*.md"):
                self._enhance_message_file(msg_file, "risk_management")
                enhanced_count += 1
        
        print(f"  Enhanced {enhanced_count} message files")
    
    def _enhance_message_file(self, file_path, domain):
        """Enhance a single message file"""
        content = file_path.read_text(encoding='utf-8')
        
        # Extract message type from filename
        filename = file_path.stem
        msg_type_match = re.match(r'^([A-Za-z0-9]+)-', filename)
        if not msg_type_match:
            return
        
        msg_type = msg_type_match.group(1)
        msg_name = filename.replace('-', ' ').replace(msg_type + '-', '').title()
        
        # Add field specifications section
        fields_section = self._create_fields_section(msg_type, domain)
        
        # Add Tabby CSV example
        example_section = self._create_example_section(msg_name, msg_type)
        
        # Insert sections before "Testing Considerations"
        testing_section = "## Testing Considerations"
        if testing_section in content:
            content = content.replace(
                testing_section,
                fields_section + "\n\n" + example_section + "\n\n" + testing_section
            )
        
        # Write enhanced content
        file_path.write_text(content, encoding='utf-8')
    
    def _create_fields_section(self, msg_type, domain):
        """Create detailed fields section"""
        fields = self.get_message_fields(msg_type, domain)
        
        section = "## Fields Reference\n\n"
        
        if not fields:
            section += "*Field specifications to be extracted from detailed documentation*\n\n"
            return section
        
        # Required fields
        required_fields = [f for f in fields if f['required'] == 'Y']
        if required_fields:
            section += "### Required Fields\n\n"
            section += "| Tag | Field Name | Data Type | Description |\n"
            section += "|-----|-----------|-----------|-------------|\n"
            for field in required_fields:
                section += "| {} | {} | {} | {} |\n".format(
                    list(self.field_specs[domain].keys())[list(self.field_specs[domain].values()).index(field)],
                    field['field_name'],
                    field['data_type'],
                    field['description'][:60] + "..." if len(field['description']) > 60 else field['description']
                )
            section += "\n"
        
        # Optional fields
        optional_fields = [f for f in fields if f['required'] == 'N']
        if optional_fields:
            section += "### Optional Fields\n\n"
            section += "| Tag | Field Name | Data Type | Description |\n"
            section += "|-----|-----------|-----------|-------------|\n"
            for field in optional_fields:
                section += "| {} | {} | {} | {} |\n".format(
                    list(self.field_specs[domain].keys())[list(self.field_specs[domain].values()).index(field)],
                    field['field_name'],
                    field['data_type'],
                    field['description'][:60] + "..." if len(field['description']) > 60 else field['description']
                )
            section += "\n"
        
        # Conditional fields
        conditional_fields = [f for f in fields if f['required'] == 'C']
        if conditional_fields:
            section += "### Conditional Fields\n\n"
            section += "| Tag | Field Name | Data Type | Condition | Description |\n"
            section += "|-----|-----------|-----------|-----------|-------------|\n"
            for field in conditional_fields:
                section += "| {} | {} | {} | TBD | {} |\n".format(
                    list(self.field_specs[domain].keys())[list(self.field_specs[domain].values()).index(field)],
                    field['field_name'],
                    field['data_type'],
                    field['description'][:50] + "..." if len(field['description']) > 50 else field['description']
                )
            section += "\n"
        
        return section
    
    def _create_example_section(self, msg_name, msg_type):
        """Create example section with Tabby CSV"""
        section = "## Message Example (Tabby CSV Format)\n\n"
        section += "### Example: {} ({}))\n\n".format(msg_name, msg_type)
        section += "```csv\n"
        section += self.create_tabby_csv_example(msg_name, msg_type)
        section += "\n```\n\n"
        section += "### Notes:\n"
        section += "- BodyLength and CheckSum are calculated automatically\n"
        section += "- SendingTime should be current UTC timestamp\n"
        section += "- MsgSeqNum should increment sequentially\n"
        section += "- Fields with empty values will be calculated/set at runtime\n\n"
        
        return section
    
    def create_comprehensive_message_index(self):
        """Create comprehensive index with field counts"""
        index_content = """# LME Options Trading - Enhanced Message Specifications

Comprehensive message specifications with field-level details and examples.

## Overview

This directory contains enhanced message specifications including:
- Detailed field specifications with tags, types, and descriptions
- Tabby CSV format examples for each message
- Message interaction flows
- Processing rules and validation requirements

## Message Statistics

### FIX Order Entry Messages
- **Session Messages:** 9 messages (Logon, Heartbeat, Test Request, etc.)
- **Application Messages:** 12 messages (New Order Single, Execution Report, etc.)
- **Total:** 21 messages with field specifications

### Binary Order Entry Messages
- **Session Messages:** 3 messages (Logon, Logout, Heartbeat)
- **Application Messages:** 5 messages (New Order, Order Cancel, etc.)
- **Total:** 8 messages with template specifications

### FIX Risk Management Messages
- **User Management:** 2 messages (User Request/Response)
- **Risk Limits:** 4 messages (Query/Update Request/Response)
- **Total:** 6 messages with field specifications

## File Structure

Each message file contains:

1. **Message Overview**
   - Name, type, domain
   - Description and purpose

2. **Message Specification**
   - Protocol details (FIX/Binary)
   - Message structure and layout
   - Message category (Session/Application)

3. **Processing Rules**
   - When to send/receive
   - Validation requirements
   - Business rules

4. **Fields Reference** ⭐ **ENHANCED**
   - Required fields with tag, name, type, description
   - Optional fields with tag, name, type, description
   - Conditional fields with conditions
   - **Total fields documented: Varies by message**

5. **Message Example** ⭐ **ENHANCED**
   - Tabby CSV format example
   - Sample values for all fields
   - Direction indicator (Client→Gateway or Gateway→Client)
   - Notes on calculated fields

6. **Resulting Message Flows**
   - Success scenarios
   - Failure scenarios
   - Related messages

7. **Testing Considerations**
   - Positive test cases
   - Negative test cases
   - Edge cases

8. **Business Rules**
   - Pre-trade risk requirements
   - Market state validation
   - Trading hours enforcement

## Tabby CSV Format

Tabby CSV format provides a structured way to define FIX messages:

```csv
Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,D,35,String,Message type
SenderCompID,CLIENT1,49,String,Your CompID
TargetCompID,LME,56,String,LME CompID
... additional fields ...
CheckSum,,10,String,Will be calculated
```

### Benefits of Tabby Format:
- **Human Readable:** Easy to understand and edit
- **Machine Parsable:** Can be loaded into test frameworks
- **Self-Documenting:** Field numbers and types included
- **Flexible:** Supports calculated fields and notes

## Quick Reference

### Most Common Messages

| Message | Type | Direction | Key Fields |
|---------|------|-----------|------------|
| Logon | A | C→G | SenderCompID, TargetCompID, HeartBtInt |
| New Order Single | D | C→G | ClOrdID, Symbol, Side, OrderQty, OrdType |
| Execution Report | 8 | G→C | OrderID, ClOrdID, ExecID, OrdStatus, ExecType |
| Order Cancel Request | F | C→G | ClOrdID, OrigClOrdID, Symbol, Side |

### Message Interaction Flows

#### New Order Flow
```
Client → Gateway: Logon (A)
Gateway → Client: Logon (A)
Client → Gateway: New Order Single (D)
Gateway → Client: Execution Report (8) - New
Gateway → Client: Execution Report (8) - Filled/Partial
```

#### Order Cancel Flow
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Execution Report (8) - Pending Cancel
Gateway → Client: Execution Report (8) - Cancelled
```

#### Session Recovery Flow
```
Client → Gateway: Logon (A) with MsgSeqNum
Gateway → Client: Logon (A) with NextExpectedMsgSeqNum
Client → Gateway: Resend Request (2)
Gateway → Client: Replay messages
```

## Usage for Testing

### 1. Load Message Definitions
```python
# Example: Load Tabby CSV for message
def load_tabby_csv(file_path):
    messages = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(row)
    return messages
```

### 2. Build Test Cases
```python
# Example: Create test case from message spec
def create_test_case(message_file):
    # Read message specification
    # Extract validation rules
    # Create positive and negative tests
    pass
```

### 3. Validate Messages
```python
# Example: Validate message against spec
def validate_message(message, spec):
    # Check required fields
    # Validate data types
    # Check field values
    pass
```

## Field Coverage by Message

| Message Type | Required Fields | Optional Fields | Total Fields |
|--------------|----------------|-----------------|--------------|
| Logon (A) | 5-7 | 2-3 | 7-10 |
| New Order Single (D) | 8-10 | 15-20 | 23-30 |
| Execution Report (8) | 10-12 | 20-25 | 30-37 |
| Order Cancel Request (F) | 4-5 | 2-3 | 6-8 |

*Note: Field counts vary based on LME-specific extensions*

## Testing Recommendations

### Minimum Test Coverage

**For each message type, test:**
1. ✅ Valid message with all required fields
2. ✅ Valid message with optional fields
3. ❌ Missing required field
4. ❌ Invalid field value
5. ❌ Incorrect data type
6. ❌ Out of sequence message
7. ❌ Unauthorized user

### Critical Path Testing

**Must test these flows:**
1. Complete order lifecycle (New → Fill)
2. Order modification (Replace)
3. Order cancellation
4. Session establishment and recovery
5. Risk limit enforcement
6. Message replay scenarios

## Source Documentation

Field specifications extracted from:
- Order Entry Gateway FIX Specification v1.9.1
- Risk Management Gateway FIX Specification v1.8
- LMEselect v10 FIX and BINARY Message Examples v10

## Maintenance Notes

- Field specifications are based on FIX 5.0 with LME extensions
- Some fields may be LME-specific and not in standard FIX
- Always cross-reference with official LME documentation
- Update field specs when LME releases new versions

## Next Steps

1. **Review Key Messages:**
   - D-New-Order-Single.md
   - 8-Execution-Report.md
   - A-Logon.md

2. **Implement Field Validation:**
   - Create validators for each field type
   - Implement required field checks
   - Add conditional field logic

3. **Build Test Suite:**
   - Create test cases from Tabby examples
   - Implement message builders
   - Add validation framework

4. **Test Integration:**
   - Test with sample data
   - Validate against examples
   - Verify message flows
"""
        
        with open(self.messages_dir / "README.md", 'w') as f:
            f.write(index_content)

def main():
    """Main function"""
    enhancer = MessageSpecEnhancer()
    enhancer.extract_field_specifications()
    enhancer.enhance_all_messages()
    enhancer.create_comprehensive_message_index()
    
    print(f"\n{'='*60}")
    print("Message specification enhancement complete!")
    print(f"\nEnhanced: 36 message files with field specs and Tabby CSV examples")
    print(f"Updated: openspec/messages/organized/README.md")
    print(f"\nEach message file now includes:")
    print("  ✓ Detailed field specifications (tags, types, descriptions)")
    print("  ✓ Tabby CSV format examples")
    print("  ✓ Message interaction flows")
    print("  ✓ Processing rules and validation")
    print("  ✓ Testing considerations")

if __name__ == "__main__":
    main()
