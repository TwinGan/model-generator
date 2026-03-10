# LME Symbol Alignment

Configure digital twin with actual LME metal symbols (AL, CU, NI, ZN, PB, SN, AA, HN) including lot sizes, tick sizes, price bands, and validation constraints.

## ADDED Requirements

### Requirement: LME Metal Symbols Supported

The digital twin SHALL support all 8 LME base metals as tradeable symbols.

#### Scenario: Copper symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol CU (Copper A) SHALL be available with lot size 25 tonnes and tick size $0.50/tonne

#### Scenario: Aluminium symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol AL (Primary Aluminium) SHALL be available with lot size 25 tonnes and tick size $0.50/tonne

#### Scenario: Nickel symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol NI (Nickel) SHALL be available with lot size 6 tonnes and tick size $5.00/tonne

#### Scenario: Zinc symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol ZN (Zinc) SHALL be available with lot size 25 tonnes and tick size $0.50/tonne

#### Scenario: Lead symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol PB (Lead) SHALL be available with lot size 25 tonnes and tick size $0.50/tonne

#### Scenario: Tin symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol SN (Tin) SHALL be available with lot size 5 tonnes and tick size $5.00/tonne

#### Scenario: Aluminium Alloy symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol AA (Aluminium Alloy) SHALL be available with lot size 25 tonnes and tick size $0.50/tonne

#### Scenario: Steel HRC symbol configured

- **WHEN** the digital twin initializes
- **THEN** symbol HN (Steel HRC) SHALL be available with lot size 10 tonnes and tick size $0.50/tonne

### Requirement: Symbol Configuration Format

Symbol configuration SHALL include all fields required for order validation and test case generation.

#### Scenario: Symbol has lot size

- **WHEN** a symbol is configured
- **THEN** it SHALL include lot_size field in tonnes

#### Scenario: Symbol has tick size

- **WHEN** a symbol is configured
- **THEN** it SHALL include tick_size field in USD/tonne

#### Scenario: Symbol has price band

- **WHEN** a symbol is configured
- **THEN** it SHALL include price_band with min_price, max_price, and tick_size

### Requirement: Placeholder Symbols Removed

All placeholder symbols (ES-DEC24, NQ-DEC24, etc.) SHALL be removed from initial state.

#### Scenario: No placeholder symbols in initial state

- **WHEN** the digital twin loads initial_state.json
- **THEN** it SHALL NOT contain any ES-*, NQ-*, or other non-LME symbols

### Requirement: Symbol Data Source

Symbol data SHALL be traceable to official LME specifications.

#### Scenario: Symbol data includes source citation

- **WHEN** a symbol is defined
- **THEN** its configuration SHALL reference the LME contract specification source
