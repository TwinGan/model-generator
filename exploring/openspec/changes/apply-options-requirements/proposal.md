## Why

The LME options trading requirements documentation in `doc/requirements/` has significant quality gaps that prevent it from being truly self-contained and implementation-ready. Analysis identified **5 systematic gap categories** affecting all 7 functional modules and 36 message specifications:

1. **Missing concrete values** - specs use vague terms like "configurable", "must be validated", "see section X.Y.Z"
2. **Incomplete capabilities** - some modules have placeholder text ("to be defined")
3. **Missing state machines** - no formal lifecycle definitions for sessions, orders, risk states
4. **Missing validation rules** - no concrete field validation or business rule validation
5. **Test specification gaps** - all test.md files contain only template placeholders

This change improves requirement quality with the goals of **clarity** and **self-containedness**.

## What Changes

### Message Specification Enhancements

- **FIX Order Entry (21 messages)**: 6 messages are nearly empty (only header fields), 15 missing concrete values
  - Fill empty specs: F-Order-Cancel-Request, G-Order-Cancel-Replace-Request, 9-Order-Cancel-Reject, s-New-Order-Cross, q-Order-Mass-Cancel-Request, r-Order-Mass-Cancel-Report
  - Add concrete LME values: symbols (AL, CU, ZN, PB, NI, SN, AA, HN), lot sizes, tick sizes, trading hours
  - Add complete field enumerations: ExecType, OrdStatus, OrdRejReason, CxlRejReason
  - Add business rules from source spec sections 3.4-3.23

- **Binary Order Entry (8 messages)**: All have placeholder text "*Field definitions to be extracted from binary spec*"
  - Replace placeholders with actual field definitions from source spec Section 4.10
  - Add binary encoding rules (little-endian, message structure)
  - Add session management rules (password encryption, heartbeat intervals)

- **FIX Risk Management (18 messages)**: Missing application-specific fields
  - Add missing fields for BE/BF (User Request/Response), CA/CC (Risk Limit Query), CB/CD (Risk Limit Update)
  - Add party detail group structures
  - Add risk limit calculation methodology
  - Add MMP protection types and formulas

### Module Specification Enhancements

- **All 7 modules**: Add concrete numeric values
  - Trading hours: LMEselect 01:00-19:00 London time, Ring 11:40-17:00
  - Heartbeat interval: 30 seconds
  - Session timeout: 3 heartbeat intervals
  - Max order quantity: 9,999 lots
  - Max order price: 9,999,999
  - Message throttle limits: per-second limits by message type

- **State machine definitions**: Add formal state diagrams
  - Session: DISCONNECTED → CONNECTING → AUTHENTICATING → CONNECTED → CLOSING
  - Order: NEW → PARTIALLY_FILLED → FILLED / CANCELLED / REJECTED
  - Risk: WITHIN_LIMITS → APPROACHING_LIMIT → AT_LIMIT → BREACHED

- **Validation rule catalogs**: Add concrete validation rules
  - Field presence rules (required/optional/conditional)
  - Field value ranges and data types
  - Cross-field validation rules

### Test Specification Completion

- Replace template placeholders with actual test cases
- Add specific test data values (valid/invalid symbols, quantities, prices)
- Add expected results for each test scenario

## Capabilities

### New Capabilities

- `concrete-values-enrichment`: Add all concrete numeric values, symbol lists, trading hours, limits, and thresholds from LME official specifications
- `state-machine-definitions`: Define formal state machines for session lifecycle, order states, risk states, and matching states
- `validation-rule-catalogs`: Create comprehensive validation rule catalogs for all message types
- `test-specification-implementation`: Replace test templates with actual test cases using specific values

### Modified Capabilities

- `fix-order-entry-specs`: Enhance all 21 FIX order entry message specifications with complete field definitions, business rules, and concrete values
- `binary-order-entry-specs`: Replace placeholder text with actual field definitions from source specification
- `fix-risk-management-specs`: Add missing application fields and business rules for all 18 risk management messages
- `module-specs`: Add concrete values, state machines, and validation rules to all 7 functional modules

## Impact

### Affected Files

**Message Specifications (36 files)**:
- `doc/requirements/openspec/messages/organized/fix-order-entry/*.md` (21 files)
- `doc/requirements/openspec/messages/organized/binary-order-entry/*.md` (8 files)
- `doc/requirements/openspec/messages/organized/fix-risk-management/*.md` (18 files)

**Module Specifications (14 files)**:
- `doc/requirements/openspec/specs/*/spec.md` (7 files)
- `doc/requirements/openspec/specs/*/test.md` (7 files)

**Reference Data (new)**:
- `doc/requirements/openspec/reference/symbols.md` - Complete LME symbol list with lot sizes, tick sizes
- `doc/requirements/openspec/reference/trading-hours.md` - Trading hours by venue and session
- `doc/requirements/openspec/reference/error-codes.md` - Complete error/rejection code catalog
- `doc/requirements/openspec/reference/state-machines.md` - State machine diagrams

### Dependencies

- Source specifications in `doc/requirements/docs/specs/` provide authoritative values
- `doc/requirements/docs/analysis/capabilities.json` defines capability structure
- Domain knowledge from LME official documentation (trading calendar, contract specs)

### Breaking Changes

None - this is purely an enhancement to existing documentation quality.
