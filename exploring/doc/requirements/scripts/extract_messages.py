#!/usr/bin/env python3
"""
Extract FIX and Binary messages from LME specifications
Creates individual message files with full specifications
"""

import re
import json
from pathlib import Path
from collections import defaultdict

class MessageExtractor:
    def __init__(self, specs_dir="docs/specs", output_dir="openspec/messages"):
        self.specs_dir = Path(specs_dir)
        self.output_dir = Path(output_dir)
        self.messages = defaultdict(list)
        
        # Create output directories
        self.fix_order_dir = self.output_dir / "fix-order-entry"
        self.binary_order_dir = self.output_dir / "binary-order-entry"
        self.fix_risk_dir = self.output_dir / "fix-risk-management"
        
        for dir_path in [self.fix_order_dir, self.binary_order_dir, self.fix_risk_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def extract_fix_order_messages(self):
        """Extract FIX order entry messages"""
        fix_spec = self.specs_dir / "Order Entry Gateway FIX Specification v 1 9 1.md"
        
        if not fix_spec.exists():
            print(f"✗ FIX order spec not found: {fix_spec}")
            return
        
        print("Extracting FIX Order Entry messages...")
        content = fix_spec.read_text(encoding='utf-8')
        
        # Find message definitions section
        msg_section_pattern = r'4\.11\.\s+Application Messages\s+(.*?)\n\n[A-Z\d]+\.'
        msg_section_match = re.search(msg_section_pattern, content, re.DOTALL)
        
        if not msg_section_match:
            # Try alternative pattern
            msg_section_pattern = r'Application Messages(.*?)($|\n\n[A-Z])'
            msg_section_match = re.search(msg_section_pattern, content, re.DOTALL)
        
        if msg_section_match:
            msg_section = msg_section_match.group(1)
            self._parse_fix_messages(msg_section, "Order Entry")
        
        # Also look for message patterns throughout the document
        self._find_message_patterns(content, "Order Entry")
    
    def extract_binary_order_messages(self):
        """Extract Binary order entry messages"""
        binary_spec = self.specs_dir / "Binary Order Entry Specification v1 9  1.md"
        
        if not binary_spec.exists():
            print(f"✗ Binary order spec not found: {binary_spec}")
            return
        
        print("Extracting Binary Order Entry messages...")
        content = binary_spec.read_text(encoding='utf-8')
        
        # Look for message patterns in binary spec
        self._find_binary_message_patterns(content, "Binary Order Entry")
    
    def extract_fix_risk_messages(self):
        """Extract FIX risk management messages"""
        risk_spec = self.specs_dir / "Risk Management Gateway FIX Specification v1 8.md"
        
        if not risk_spec.exists():
            print(f"✗ FIX risk spec not found: {risk_spec}")
            return
        
        print("Extracting FIX Risk Management messages...")
        content = risk_spec.read_text(encoding='utf-8')
        
        # Look for message patterns in risk spec
        self._find_message_patterns(content, "Risk Management")
    
    def _find_message_patterns(self, content, category):
        """Find FIX message patterns in content"""
        # Pattern: Message Name (MsgType) or Message Name (X)
        pattern = r'([A-Z][a-zA-Z\s]+)\s*\(([A-Za-z0-9])\)'
        
        matches = re.finditer(pattern, content)
        
        for match in matches:
            msg_name = match.group(1).strip()
            msg_type = match.group(2)
            
            # Skip if it's not a real message (too short or common words)
            if len(msg_name) < 5 or msg_name in ['Page', 'Table', 'Figure', 'Section']:
                continue
            
            # Extract message details from surrounding context
            start_pos = max(0, match.start() - 500)
            end_pos = min(len(content), match.end() + 1500)
            context = content[start_pos:end_pos]
            
            message_info = {
                'name': msg_name,
                'type': msg_type,
                'category': category,
                'context': context
            }
            
            self.messages[category].append(message_info)
            print(f"  Found: {msg_name} ({msg_type})")
    
    def _find_binary_message_patterns(self, content, category):
        """Find Binary message patterns in content"""
        # Look for binary message indicators
        patterns = [
            r'(Message Type\s*:\s*\d+)',
            r'(Template ID\s*:\s*\d+)',
            r'(Binary\s+[A-Z][a-zA-Z\s]+Message)',
            r'([A-Z][a-zA-Z]+)\s*\(\d+\s*bytes\)'
        ]
        
        found_messages = []
        
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                message_info = {
                    'name': match.group(0),
                    'type': 'Binary',
                    'category': category,
                    'context': content[max(0, match.start()-200):match.end()+200]
                }
                found_messages.append(message_info)
                print(f"  Found: {match.group(0)[:60]}...")
        
        self.messages[category].extend(found_messages)
    
    def _parse_fix_messages(self, section_content, category):
        """Parse FIX message definitions from section"""
        # Split by message entries
        message_entries = re.split(r'\n\s*\n', section_content)
        
        for entry in message_entries:
            if len(entry.strip()) < 50:  # Skip short entries
                continue
            
            # Look for message header pattern
            header_match = re.match(r'([A-Z][a-zA-Z\s]+)\s*\(([A-Za-z0-9])\)', entry.strip())
            
            if header_match:
                msg_name = header_match.group(1).strip()
                msg_type = header_match.group(2)
                
                message_info = {
                    'name': msg_name,
                    'type': msg_type,
                    'category': category,
                    'context': entry.strip()
                }
                
                self.messages[category].append(message_info)
                print(f"  Parsed: {msg_name} ({msg_type})")
    
    def create_message_files(self):
        """Create individual message files with full specifications"""
        print("\nCreating message files...")
        
        # Process each category
        for category, message_list in self.messages.items():
            print(f"\nProcessing {category} messages...")
            
            for idx, msg_info in enumerate(message_list, 1):
                self._create_single_message_file(msg_info, idx)
        
        print(f"\n{'='*60}")
        print(f"Created {sum(len(msgs) for msgs in self.messages.values())} message files")
    
    def _create_single_message_file(self, msg_info, index):
        """Create a single message specification file"""
        # Determine directory based on category
        if "Risk" in msg_info['category']:
            output_dir = self.fix_risk_dir
            category_slug = "risk-management"
        elif "Binary" in msg_info['category']:
            output_dir = self.binary_order_dir
            category_slug = "binary-order-entry"
        else:
            output_dir = self.fix_order_dir
            category_slug = "fix-order-entry"
        
        # Create filename
        safe_name = re.sub(r'[^a-zA-Z0-9\s]', '', msg_info['name'])
        safe_name = safe_name.replace(' ', '-').lower()
        filename = f"{index:02d}-{safe_name}.md"
        
        # Extract processing rules and resulting messages from context
        processing_rules = self._extract_processing_rules(msg_info['context'])
        resulting_messages = self._extract_resulting_messages(msg_info['context'])
        
        # Create message content
        content = f"""# {msg_info['name']}

**Category:** {msg_info['category']}  
**Message Type:** {msg_info['type']}  
**Index:** {index:02d}

## Message Specification

### Description
{msg_info['name']} message used in {msg_info['category']}.

### Message Type Identifier
- **FIX MsgType:** `{msg_info['type']}` (for FIX messages)
- **Category:** {category_slug}

### Context
```
{msg_info['context'][:800]}{'...' if len(msg_info['context']) > 800 else ''}
```

## Processing Rules

{processing_rules if processing_rules else "Processing rules to be extracted from detailed specification review."}

### Validation Rules
- Message must contain required fields
- Field data types must be valid
- Message sequence must be appropriate for session state
- User permissions must allow this operation

### Business Rules
- Applicable trading rules must be enforced
- Risk limits must be checked (for order messages)
- Market state must allow the operation
- Timing constraints must be observed

## Resulting Messages

{resulting_messages if resulting_messages else "Resulting message flows to be defined based on processing outcomes."}

### Success Response
- **Message Type:** Execution Report or Acknowledgment
- **Status:** Accepted/Executed
- **Fields:** Order ID, Execution details, Timestamp

### Error Response
- **Message Type:** Business Message Reject or Order Reject
- **Status:** Rejected
- **Fields:** Reject reason, Reference to original message

### Related Messages
- Preceding messages that must be sent
- Subsequent messages that may follow
- Alternative message flows for different scenarios

## Testing Considerations

### Positive Test Cases
1. Valid message with all required fields
2. Message with optional fields included
3. Message sequencing in correct order

### Negative Test Cases
1. Missing required fields
2. Invalid field values or data types
3. Unauthorized user attempt
4. Message out of sequence
5. Invalid message type for current session state

### Edge Cases
1. Boundary values for numeric fields
2. Maximum field lengths for strings
3. Concurrent message processing
4. Session recovery scenarios

## Fields Reference

### Required Fields
- Fields to be extracted from detailed specification

### Optional Fields
- Fields to be extracted from detailed specification

### Conditional Fields
- Fields required based on specific conditions

## Implementation Notes

- This message specification is derived from LME documentation
- Refer to source specifications for complete field-level details
- Test environment should validate all processing rules
- Message examples should be included in test cases
"""
        
        # Write file
        output_path = output_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Created: {filename}")
    
    def _extract_processing_rules(self, context):
        """Extract processing rules from message context"""
        rules = []
        
        # Look for rule indicators
        rule_patterns = [
            r'(?i)(must|shall|required)\s+[^.]*',
            r'(?i)(validate|check|verify)\s+[^.]*',
            r'(?i)(if|when)\s+[^.]*\s+(then)\s+[^.]*',
            r'(?i)(processing|handling)\s+[^.]*'
        ]
        
        for pattern in rule_patterns:
            matches = re.findall(pattern, context)
            if matches:
                rules.extend(matches[:3])  # Limit to first 3 matches
        
        if rules:
            return "\n".join(f"- {rule}" for rule in rules[:5])
        
        return ""
    
    def _extract_resulting_messages(self, context):
        """Extract resulting message information"""
        results = []
        
        # Look for response indicators
        response_patterns = [
            r'(?i)(execution report|order ack|order reject)',
            r'(?i)(result|response|reply)\s+[^.]*',
            r'(?i)(sent|returned|generated)\s+[^.]*'
        ]
        
        for pattern in response_patterns:
            matches = re.findall(pattern, context)
            if matches:
                results.extend(matches[:3])
        
        if results:
            return "\n".join(f"- {result}" for result in results[:5])
        
        return ""
    
    def create_message_index(self):
        """Create index file for all messages"""
        index_content = """# LME Options Trading - Message Index

This directory contains extracted message specifications for LME Options Trading.

## Message Categories

### FIX Order Entry Messages
Location: `fix-order-entry/`

Messages for submitting, modifying, and canceling orders via FIX protocol.

### Binary Order Entry Messages
Location: `binary-order-entry/`

Messages for submitting, modifying, and canceling orders via LME's proprietary binary protocol.

### FIX Risk Management Messages
Location: `fix-risk-management/`

Messages for managing pre-trade risk limits and controls via FIX protocol.

## Message File Structure

Each message file contains:
- Message name and type identifier
- Message specification and description
- Processing rules and validation requirements
- Resulting messages and response flows
- Testing considerations and test cases
- Fields reference (to be enhanced with detailed field specs)

## Usage for Testing Environment

1. **Review Message Specifications**: Understand each message type and its requirements
2. **Implement Processing Rules**: Code the validation and business logic
3. **Create Test Cases**: Use the provided testing considerations
4. **Validate Message Flows**: Ensure correct sequencing and responses
5. **Test Error Scenarios**: Verify proper rejection and error handling

## Source

Messages extracted from:
- Order Entry Gateway FIX Specification v1.9.1
- Binary Order Entry Specification v1.9.1
- Risk Management Gateway FIX Specification v1.8
- LMEselect v10 FIX and BINARY Message Examples v10

## Note

This is an initial extraction. Detailed field specifications should be added
by reviewing the source documents and cross-referencing with message examples.
"""
        
        with open(self.output_dir / "README.md", 'w') as f:
            f.write(index_content)
    
    def extract_all(self):
        """Extract all messages"""
        print("="*60)
        print("Extracting Messages from LME Specifications")
        print("="*60)
        
        self.extract_fix_order_messages()
        self.extract_binary_order_messages()
        self.extract_fix_risk_messages()
        
        self.create_message_files()
        self.create_message_index()
        
        # Save extracted data
        with open(self.output_dir / "messages-index.json", 'w') as f:
            json.dump(dict(self.messages), f, indent=2)
        
        print(f"\n{'='*60}")
        print("Message extraction complete!")
        print(f"Output directory: {self.output_dir}")

def main():
    """Main function"""
    extractor = MessageExtractor()
    extractor.extract_all()
    
    print("\nNext steps:")
    print("1. Review extracted messages in openspec/messages/")
    print("2. Enhance message files with detailed field specifications")
    print("3. Add message examples from the examples document")
    print("4. Create test cases based on message specifications")

if __name__ == "__main__":
    main()
