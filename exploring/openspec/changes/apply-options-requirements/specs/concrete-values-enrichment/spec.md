# Concrete Values Enrichment

Add all concrete numeric values, symbol lists, trading hours, limits, and thresholds from LME official specifications to requirement documentation.

## ADDED Requirements

### Requirement: LME Symbol Reference

The requirements documentation SHALL include a complete reference file listing all LME symbols with their contract specifications.

#### Scenario: Developer looks up symbol details

- **WHEN** a developer needs to know valid symbol values for order submission
- **THEN** they can find the complete symbol list in `openspec/reference/symbols.md` with symbol code, metal name, contract code, lot size, and tick size

#### Scenario: Symbol reference includes all LME metals

- **WHEN** the symbol reference is consulted
- **THEN** it SHALL contain: AL (Aluminium), CU (Copper), ZN (Zinc), PB (Lead), NI (Nickel), SN (Tin), AA (Aluminium Alloy), HN (Steel HRC)

### Requirement: Trading Hours Reference

The requirements documentation SHALL include a reference file documenting trading hours for all LME venues.

#### Scenario: Developer checks LMEselect hours

- **WHEN** a developer needs to know LMEselect trading hours
- **THEN** they can find in `openspec/reference/trading-hours.md` that LMEselect operates 01:00-19:00 London time

#### Scenario: Developer checks Ring hours

- **WHEN** a developer needs to know Ring trading hours
- **THEN** they can find in `openspec/reference/trading-hours.md` that Ring operates 11:40-17:00 London time (with reference to lme.com for current schedule)

### Requirement: Numeric Limit Values

All message and module specifications SHALL include concrete numeric limits extracted from source specifications.

#### Scenario: Order quantity limits documented

- **WHEN** a developer reads order submission requirements
- **THEN** they SHALL find that maximum order quantity is 9,999 lots (source: FIX Spec §3.3)

#### Scenario: Price limits documented

- **WHEN** a developer reads price validation requirements
- **THEN** they SHALL find that maximum order price is 9,999,999 (source: FIX Spec §3.3)

#### Scenario: Heartbeat interval documented

- **WHEN** a developer implements session management
- **THEN** they SHALL find that heartbeat interval is 30 seconds and session timeout is 3 heartbeat intervals (90 seconds) (source: FIX Spec §1.4)

### Requirement: Source Traceability

All concrete values extracted from source specifications SHALL include a citation to the source section.

#### Scenario: Value includes source reference

- **WHEN** a concrete value is provided in a spec file
- **THEN** it SHALL include the source specification name and section number (e.g., "FIX Spec §1.4")

#### Scenario: Inferred values marked

- **WHEN** a value is inferred from domain knowledge rather than source specs
- **THEN** it SHALL be marked with `[inferred]` tag
