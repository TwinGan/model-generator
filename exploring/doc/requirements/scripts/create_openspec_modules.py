#!/usr/bin/env python3
"""
Create OpenSpec Module Structure for LME Options Trading
Generates module directories with enriched specifications including testing best practices
"""

import json
import shutil
from pathlib import Path

class OpenSpecModuleCreator:
    def __init__(self, analysis_dir="docs/analysis", output_dir="openspec/specs"):
        self.analysis_dir = Path(analysis_dir)
        self.output_dir = Path(output_dir)
        
        # Load analyzed capabilities
        with open(self.analysis_dir / "modules.json", 'r') as f:
            self.modules = json.load(f)
        
        # Testing best practices template
        self.testing_best_practices = """
## Testing Best Practices

### Functional Test Cases

#### Positive Path Tests
- **Happy Path**: Verify successful execution under normal conditions
- **Boundary Values**: Test at minimum/maximum allowed values
- **Typical Usage**: Simulate common trading scenarios

#### Negative Path Tests
- **Invalid Inputs**: Reject orders with malformed data
- **Missing Required Fields**: Proper error handling for incomplete messages
- **Out-of-Range Values**: Reject values outside acceptable ranges
- **Authorization Failures**: Deny access without proper credentials

#### Edge Cases
- **Concurrent Operations**: Multiple simultaneous requests
- **Session Recovery**: Message replay after disconnections
- **Race Conditions**: Timing-dependent scenarios
- **Resource Limits**: Maximum connections, message rates

### Test Data Strategy

#### Representative Data
- Use realistic market conditions
- Include various order types and sizes
- Cover all supported asset classes
- Test with different user roles and permissions

#### Negative Test Data
- Malformed messages
- Invalid field combinations
- Unauthorized operations
- Exceeded limits and thresholds

### Performance Considerations (for testing context)
- Message throughput validation
- Latency measurements
- Session scalability
- Recovery time objectives

### Compliance Testing
- Regulatory requirement validation
- Audit trail completeness
- Risk limit enforcement
- Reporting accuracy
"""
        
        # Module-specific testing guidance
        self.module_testing_guidance = {
            "session-management": """
### Session Management Testing

#### Authentication Tests
- Valid credentials acceptance
- Invalid credentials rejection
- Password change workflows
- Session timeout handling
- Concurrent session limits

#### Session Lifecycle Tests
- Successful logon/logoff sequences
- Heartbeat mechanism validation
- Sequence number synchronization
- Graceful session termination
- Unexpected disconnect recovery
""",
            "order-management": """
### Order Management Testing

#### Order Submission Tests
- Valid order acceptance and acknowledgment
- Invalid order rejection with proper error codes
- Order type validation (Market, Limit, Stop, etc.)
- Order validity period testing (Day, GTC, GTD)
- Minimum/maximum quantity enforcement

#### Order Modification Tests
- Successful parameter amendments
- Price/quantity updates
- Cancel/replace operations
- Partial fill handling
- Mass cancellation functionality

#### Order State Transitions
- New → Pending → Working → Filled
- New → Pending → Rejected
- Working → Cancelled
- Working → Partially Filled → Filled
- Working → Partially Filled → Cancelled
""",
            "risk-management": """
### Risk Management Testing

#### Pre-Trade Risk Tests
- Order quantity limit enforcement
- Notional value limit validation
- Gross position limit checking
- Cross-order risk aggregation
- Real-time limit monitoring

#### Risk Group Tests
- User role permission validation
- View-only access restrictions
- Risk limit inheritance
- Emergency risk cutoff functionality
- Risk exposure calculations
""",
            "matching-engine": """
### Matching Engine Testing

#### Price Validation Tests
- Price tolerance checks
- Reference price comparisons
- Failed check handling workflows
- Manual price override procedures
- Price reasonableness validation

#### Trading Hours Tests
- Session open/close boundaries
- Deadline enforcement (TOM, trade input)
- Timezone handling
- Holiday calendar compliance
- After-hours rejection

#### Matching Logic Tests
- Price-time priority validation
- FIFO order matching
- Trade reporting accuracy
- Execution price verification
- Market impact scenarios
""",
            "reliability": """
### Reliability Testing

#### Message Recovery Tests
- Gap detection and fill requests
- Resend request handling
- Duplicate message detection
- Out-of-sequence message handling
- Message persistence validation

#### Fault Tolerance Tests
- Network disconnect simulation
- Server failover scenarios
- Queue overflow handling
- Resource exhaustion recovery
- Graceful degradation validation
""",
            "connectivity": """
### Connectivity Testing

#### Protocol Compliance Tests
- FIX message structure validation
- Binary protocol format verification
- Field presence and data type checks
- Message sequencing accuracy
- Checksum/integrity validation

#### Integration Tests
- End-to-end order flow
- Multi-session handling
- Concurrent connection management
- Protocol translation accuracy
- Message routing verification
""",
            "examples": """
### Example-Based Testing

#### Message Example Tests
- FIX message parsing and validation
- Binary message encoding/decoding
- Example message replay tests
- Round-trip message conversion
- Example scenario execution
"""
        }
    
    def create_module(self, module_id, module_data):
        """Create a single OpenSpec module"""
        module_dir = self.output_dir / module_id
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Create spec.md
        spec_content = self._generate_spec_content(module_id, module_data)
        with open(module_dir / "spec.md", 'w') as f:
            f.write(spec_content)
        
        # Create test.md
        test_content = self._generate_test_content(module_id, module_data)
        with open(module_dir / "test.md", 'w') as f:
            f.write(test_content)
        
        print(f"✓ Created module: {module_id}")
        return module_dir
    
    def _generate_spec_content(self, module_id, module_data):
        """Generate specification content for a module"""
        content = f"# {module_data['name']}\n\n"
        content += f"{module_data['description']}\n\n"
        
        # Add capabilities section
        if module_data['capabilities']:
            content += "## Capabilities\n\n"
            # Remove duplicates
            unique_caps = {}
            for cap in module_data['capabilities']:
                key = cap['capability']
                if key not in unique_caps:
                    unique_caps[key] = cap
            
            for cap in unique_caps.values():
                content += f"### {cap['capability']}\n\n"
                content += f"**Source:** {cap['source']}\n\n"
                content += f"{cap['description']}\n\n"
        else:
            content += "## Capabilities\n\n"
            content += "*Capabilities to be defined based on detailed specification review*\n\n"
        
        # Add functional requirements section
        content += "## Functional Requirements\n\n"
        content += self._get_functional_requirements(module_id)
        
        return content
    
    def _generate_test_content(self, module_id, module_data):
        """Generate test specification content"""
        content = f"# {module_data['name']} - Test Specification\n\n"
        content += f"Test specifications for {module_data['name']} module.\n\n"
        
        # Add module-specific testing guidance
        if module_id in self.module_testing_guidance:
            content += self.module_testing_guidance[module_id]
        else:
            content += "## Testing Guidance\n\n"
            content += "*Module-specific testing guidance to be defined*\n\n"
        
        # Add general best practices
        content += self.testing_best_practices
        
        # Add test case templates
        content += self._get_test_case_templates(module_id)
        
        return content
    
    def _get_functional_requirements(self, module_id):
        """Get functional requirements for a module"""
        requirements = {
            "session-management": """
### Authentication Requirements
- System shall support FIX session authentication with CompID and password
- Passwords must be encrypted during transmission
- System shall support password change operations
- Failed authentication attempts must be logged
- Sessions must timeout after period of inactivity

### Session Lifecycle Requirements
- System shall establish FIX sessions following standard FIX protocols
- Sequence numbers must be maintained per session
- Heartbeat messages must be exchanged to keep sessions alive
- Sessions must support graceful termination
- System shall handle session re-establishment after disconnections
""",
            "order-management": """
### Order Submission Requirements
- System shall accept valid orders with required fields populated
- Orders must be validated against market rules before acceptance
- System shall support multiple order types (Market, Limit, Stop, Stop-Limit, Iceberg, FOK)
- Order validity conditions must be enforced (Day, GTC, GTD)
- Minimum and maximum order quantities must be validated

### Order Modification Requirements
- System shall allow amendment of working orders
- Price and quantity updates must be validated
- Cancel/replace operations must maintain order priority where applicable
- Partial fills must be tracked accurately
- Mass cancellation must be supported for risk management
""",
            "risk-management": """
### Pre-Trade Risk Requirements
- System shall enforce per-order quantity limits
- Per-order notional value limits must be validated
- Gross position limits must be checked before order acceptance
- Risk limits must be evaluated in real-time
- System shall support configurable risk thresholds

### Risk Group Requirements
- System shall support user role-based risk controls
- Different risk limits may apply to different user groups
- View-only access must be enforced for appropriate roles
- Risk group hierarchies must be supported
- Emergency risk cutoff must be available
""",
            "matching-engine": """
### Price Validation Requirements
- System shall validate order prices against reference prices
- Price tolerance checks must be configurable
- Orders failing price validation must be rejected or flagged
- Manual price override procedures must be documented
- Price reasonableness must be evaluated based on market conditions

### Trading Hours Requirements
- System shall enforce trading session schedules
- TOM (Tomorrow) trading deadlines must be observed
- Trade input deadlines must be enforced
- Timezone handling must be accurate
- Holiday calendars must be respected

### Matching Logic Requirements
- System shall match orders using price-time priority
- First-In-First-Out (FIFO) must be used within price levels
- Trade executions must be reported accurately
- Execution prices must be validated
- Market impact must be minimized through efficient matching
""",
            "reliability": """
### Message Recovery Requirements
- System shall detect message gaps and request resends
- Resend requests must be processed correctly
- Duplicate messages must be identified and handled
- Out-of-sequence messages must be managed appropriately
- Message persistence must ensure durability

### Fault Tolerance Requirements
- System shall handle network disconnections gracefully
- Server failover must be supported
- Queue overflow conditions must be managed
- Resource exhaustion must not cause data loss
- Graceful degradation must maintain core functionality
""",
            "connectivity": """
### Protocol Support Requirements
- System shall support FIX 5.0 protocol for order entry
- Binary protocol must be available for high-performance needs
- Protocol-specific message formats must be validated
- Message sequencing must be maintained per protocol
- Checksum validation must ensure message integrity

### Integration Requirements
- System shall support multiple concurrent sessions
- Protocol translation must be accurate where required
- Message routing must be efficient and reliable
- Connection management must handle high throughput
""",
            "examples": """
### Example Requirements
- System documentation must include FIX message examples
- Binary message examples must be provided
- Examples must cover all order types
- Error scenarios must be illustrated
- Example messages must be validated as accurate
"""
        }
        
        return requirements.get(module_id, "*Functional requirements to be defined*\n")
    
    def _get_test_case_templates(self, module_id):
        """Get test case templates for a module"""
        return """
## Test Case Templates

### Template: Positive Path Test

**Test ID:** [MODULE]_[CAPABILITY]_POS_[001]

**Objective:** Verify successful [capability] under normal conditions

**Prerequisites:**
- System is operational
- Valid user credentials
- Sufficient test data

**Test Steps:**
1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

**Expected Results:**
- [Expected result 1]
- [Expected result 2]
- [Expected result 3]

**Test Data:**
- [Input data specifications]

**Cleanup:**
- [Cleanup actions if needed]

---

### Template: Negative Path Test

**Test ID:** [MODULE]_[CAPABILITY]_NEG_[001]

**Objective:** Verify proper error handling for invalid [capability] requests

**Prerequisites:**
- System is operational
- Valid user credentials

**Test Steps:**
1. [Step with invalid input]
2. [Step to verify rejection]

**Expected Results:**
- Error message: [expected error]
- No system crash or data corruption
- Proper logging of failure

**Test Data:**
- [Invalid input data]

---

### Template: Integration Test

**Test ID:** [MODULE]_[CAPABILITY]_INT_[001]

**Objective:** Verify [capability] works correctly across system components

**Prerequisites:**
- All dependent systems operational
- Network connectivity established

**Test Steps:**
1. [End-to-end workflow step 1]
2. [End-to-end workflow step 2]
3. [Verification step]

**Expected Results:**
- Complete workflow executes successfully
- Data consistency across systems
- Proper event propagation

**Test Data:**
- [Realistic production-like data]

---

### Template: Performance Test

**Test ID:** [MODULE]_[CAPABILITY]_PERF_[001]

**Objective:** Verify [capability] meets performance requirements

**Prerequisites:**
- Performance test environment
- Load generation tools

**Test Steps:**
1. Generate baseline load
2. Gradually increase load
3. Measure response times
4. Monitor resource utilization

**Expected Results:**
- Response time: < [threshold] ms at [load level]
- Throughput: > [threshold] messages/second
- No errors at expected load

**Test Data:**
- [High-volume test data]

**Acceptance Criteria:**
- [Specific performance targets]
"""
    
    def create_all_modules(self):
        """Create all OpenSpec modules"""
        print("Creating OpenSpec module structure...\n")
        
        # Clean and create output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)
        
        # Create each module
        for module_id, module_data in self.modules.items():
            self.create_module(module_id, module_data)
        
        print(f"\n{'='*60}")
        print(f"Created {len(self.modules)} OpenSpec modules in {self.output_dir}/")
        
        # Create README
        self._create_readme()
        
        return self.output_dir
    
    def _create_readme(self):
        """Create main README for the OpenSpec structure"""
        readme_content = """# LME Options Trading - OpenSpec Module Structure

This directory contains the standardized functional requirements for LME Options Trading Exchange, organized into self-contained modules.

## Module Overview

"""
        
        for module_id, module_data in self.modules.items():
            readme_content += f"### [{module_data['name']}]({module_id}/spec.md)\n\n"
            readme_content += f"{module_data['description']}\n\n"
            
            if module_data['capabilities']:
                # Count unique capabilities
                unique_caps = len(set(cap['capability'] for cap in module_data['capabilities']))
                readme_content += f"**Capabilities:** {unique_caps} defined\n\n"
        
        readme_content += """
## Testing Approach

Each module includes comprehensive test specifications based on industry best practices:

- **Positive Path Tests**: Verify successful execution under normal conditions
- **Negative Path Tests**: Ensure proper error handling and validation
- **Edge Case Tests**: Cover boundary conditions and unusual scenarios
- **Integration Tests**: Validate end-to-end workflows
- **Performance Tests**: Ensure system meets throughput and latency requirements

## Usage

1. Review the `spec.md` file in each module for functional requirements
2. Refer to `test.md` for testing strategies and test case templates
3. Use the capability summaries to understand system functionality
4. Implement tests following the provided templates

## Documentation Structure

```
openspec/specs/
├── session-management/     # Session and authentication management
│   ├── spec.md            # Functional requirements
│   └── test.md            # Test specifications
├── order-management/       # Order submission and management
│   ├── spec.md
│   └── test.md
├── risk-management/        # Pre-trade risk controls
│   ├── spec.md
│   └── test.md
├── matching-engine/        # Order matching and execution
│   ├── spec.md
│   └── test.md
├── reliability/            # Message recovery and fault tolerance
│   ├── spec.md
│   └── test.md
├── connectivity/           # Protocol support (FIX/Binary)
│   ├── spec.md
│   └── test.md
└── examples/               # Message examples and samples
    ├── spec.md
    └── test.md
```

## Source Documents

These modules are derived from the following LME specifications:

- Binary Order Entry Specification v1.9.1
- Order Entry Gateway FIX Specification v1.9.1
- Risk Management Gateway FIX Specification v1.8
- LME Matching Rules August 2022
- LMEselect v10 FIX and BINARY Message Examples v10

## Maintenance

When updating requirements:

1. Modify the relevant module's `spec.md` file
2. Update corresponding test specifications in `test.md`
3. Ensure all changes follow the established testing patterns
4. Review impact on dependent modules
"""
        
        with open(self.output_dir / "README.md", 'w') as f:
            f.write(readme_content)

def main():
    """Main function"""
    creator = OpenSpecModuleCreator()
    creator.create_all_modules()
    
    print("\nOpenSpec module structure created successfully!")
    print("\nNext steps:")
    print("1. Review the modules in openspec/specs/")
    print("2. Customize requirements in each spec.md as needed")
    print("3. Use test.md as a guide for test case development")
    print("4. Integrate with your testing framework")

if __name__ == "__main__":
    main()
