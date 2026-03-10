# Validation Rule Catalogs

Create comprehensive validation rule catalogs for all message types covering field presence, value ranges, and cross-field validation.

## ADDED Requirements

### Requirement: Field Presence Rules

The requirements documentation SHALL include a validation rule catalog documenting field presence requirements for all message types.

#### Scenario: Developer checks required fields

- **WHEN** a developer needs to know which fields are required for New Order Single
- **THEN** they can find in `openspec/reference/validation-rules.md` a table showing each field with presence: REQUIRED, OPTIONAL, or CONDITIONAL

#### Scenario: Conditional field rules documented

- **WHEN** a field has conditional presence (e.g., Price required for Limit orders)
- **THEN** the validation rule SHALL specify the condition under which the field is required

### Requirement: Field Value Ranges

The validation rule catalog SHALL document valid value ranges for all fields.

#### Scenario: Numeric field ranges documented

- **WHEN** a developer needs to validate OrderQty
- **THEN** they can find the valid range (1-9,999 lots) in the validation rule catalog

#### Scenario: Enumerated values documented

- **WHEN** a developer needs valid values for Side field
- **THEN** they can find in the validation rule catalog: 1=Buy, 2=Sell

#### Scenario: String field lengths documented

- **WHEN** a developer needs to validate ClOrdID length
- **THEN** they can find the maximum length constraint in the validation rule catalog

### Requirement: Cross-Field Validation Rules

The validation rule catalog SHALL document validation rules involving multiple fields.

#### Scenario: Order type and price validation

- **WHEN** OrdType = 2 (Limit) is specified
- **THEN** Price field SHALL be required (cross-field rule)

#### Scenario: Stop order validation

- **WHEN** OrdType = 3 (Stop) or 4 (Stop-Limit) is specified
- **THEN** StopPx field SHALL be required (cross-field rule)

#### Scenario: TimeInForce validation

- **WHEN** TimeInForce = 6 (GTD) is specified
- **THEN** ExpireDate field SHALL be required (cross-field rule)

### Requirement: Error Code Mapping

The validation rule catalog SHALL map validation failures to specific error codes.

#### Scenario: Missing required field error

- **WHEN** a required field is missing
- **THEN** the catalog SHALL specify the rejection reason code to use (e.g., OrdRejReason=5 for missing field)

#### Scenario: Invalid value error

- **WHEN** a field value is outside valid range
- **THEN** the catalog SHALL specify the rejection reason code to use (e.g., OrdRejReason=8 for invalid price)
