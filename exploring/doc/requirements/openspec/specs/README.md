# LME Options Trading - OpenSpec Module Structure

This directory contains the standardized functional requirements for LME Options Trading Exchange, organized into self-contained modules.

## Module Overview

### [Session Management](session-management/spec.md)

FIX session establishment, authentication, and lifecycle management

**Capabilities:** 1 defined

### [Order Management](order-management/spec.md)

Order submission, modification, cancellation, and status tracking

**Capabilities:** 3 defined

### [Risk Management](risk-management/spec.md)

Pre-trade risk controls, limits, and compliance checking

**Capabilities:** 2 defined

### [Matching Engine](matching-engine/spec.md)

Order matching, price validation, and trade execution rules

**Capabilities:** 3 defined

### [Reliability & Recovery](reliability/spec.md)

Message recovery, gap fill, and fault tolerance mechanisms

**Capabilities:** 1 defined

### [Connectivity](connectivity/spec.md)

Protocol support (FIX and Binary) and message formats

### [Message Examples](examples/spec.md)

Sample messages and usage examples for all protocols

**Capabilities:** 2 defined


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
