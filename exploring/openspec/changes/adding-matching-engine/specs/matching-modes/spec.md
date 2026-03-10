# Matching Modes

Support multiple LME matching modes (LMEselect continuous, TOM end-of-day, Ring open outcry).

## ADDED Requirements

### Requirement: LMEselect Continuous Matching

LMEselect mode SHALL provide continuous order matching during trading hours.

#### Scenario: Immediate matching in LMEselect mode

- **WHEN** an order is submitted in LMEselect mode
- **AND** crossing conditions exist
- **THEN** matching SHALL occur immediately

#### Scenario: Continuous matching throughout session

- **WHEN** LMEselect mode is active
- **THEN** orders SHALL be matched continuously as they arrive

#### Scenario: LMEselect mode is default

- **WHEN** no matching mode is specified
- **THEN** LMEselect continuous mode SHALL be used

### Requirement: TOM (Trade on Close) Mode

TOM mode SHALL defer matching to end-of-day batch processing.

#### Scenario: Orders collected during TOM session

- **WHEN** orders are submitted in TOM mode
- **THEN** they SHALL NOT be matched immediately
- **AND** they SHALL be collected for batch matching

#### Scenario: TOM matching at deadline

- **WHEN** TOM matching deadline is reached
- **THEN** all collected orders SHALL be matched in batch

#### Scenario: TOM single price clearing

- **WHEN** TOM batch matching occurs
- **THEN** all matches SHALL occur at a single clearing price

### Requirement: Ring Mode (Future)

Ring mode SHALL simulate open outcry periodic clearing.

#### Scenario: Ring mode placeholder

- **WHEN** Ring mode is selected
- **THEN** the system SHALL indicate it is not yet implemented

### Requirement: Mode Selection

Matching mode SHALL be selectable per test scenario.

#### Scenario: Mode configured in scenario

- **WHEN** a scenario specifies matching_mode: "tom"
- **THEN** the matching engine SHALL use TOM mode

#### Scenario: Mode configurable per symbol

- **WHEN** different symbols have different trading venues
- **THEN** matching mode SHALL be configurable per symbol

### Requirement: Mode-Specific Timing

Each mode SHALL respect its specific timing rules.

#### Scenario: LMEselect respects trading hours

- **WHEN** LMEselect mode is active
- **THEN** matching SHALL only occur during configured trading hours

#### Scenario: TOM respects deadline

- **WHEN** TOM mode is active
- **THEN** batch matching SHALL trigger at the configured deadline time

### Requirement: Mode Transition

Matching mode transitions SHALL be handled correctly.

#### Scenario: Mode change between test runs

- **WHEN** a test scenario changes matching mode
- **THEN** the matching engine SHALL reset and use the new mode

#### Scenario: Mode state cleared on change

- **WHEN** matching mode is changed
- **THEN** any pending orders from previous mode SHALL be cleared or handled
