# FIX Risk Management Specifications Enhancement

Add missing application fields and business rules for all 18 risk management messages.

## MODIFIED Requirements

### Requirement: User Request/Response Fields

BE-User-Request and BF-User-Response specifications SHALL include all application-specific fields.

#### Scenario: User Request has complete fields

- **WHEN** a developer reads BE-User-Request.md
- **THEN** they SHALL find UserRequestType, UserRequestID, Username, and all other application fields beyond standard header

#### Scenario: User Response has complete fields

- **WHEN** a developer reads BF-User-Response.md
- **THEN** they SHALL find UserStatus, Email, and all other application fields

### Requirement: Risk Limit Query Fields

CA-Risk-Limit-Query-Request and CC-Risk-Limit-Query-Response specifications SHALL include all application-specific fields.

#### Scenario: Query Request has complete fields

- **WHEN** a developer reads CA-Risk-Limit-Query-Request.md
- **THEN** they SHALL find RiskLimitRequestID, RiskLimitRequestType (1760), NoPartyDetails (1670), PartyDetailID (1691), RiskLimitLevel

#### Scenario: Query Response has complete fields

- **WHEN** a developer reads CC-Risk-Limit-Query-Response.md
- **THEN** they SHALL find all risk limit data fields including limits and utilization

### Requirement: Risk Limit Update Fields

CB-Risk-Limit-Update-Request and CD-Risk-Limit-Update-Report specifications SHALL include all application-specific fields.

#### Scenario: Update Request has complete fields

- **WHEN** a developer reads CB-Risk-Limit-Update-Request.md
- **THEN** they SHALL find RiskLimitID, RiskLimitAmount, RiskLimitType, RiskLimitGroupName, NoRiskLimits

#### Scenario: Update Report has complete fields

- **WHEN** a developer reads CD-Risk-Limit-Update-Report.md
- **THEN** they SHALL find all update result fields including status and rejection reasons

### Requirement: Party Detail Group Structure

All risk management specifications using party details SHALL document the repeating group structure.

#### Scenario: PartyDetailGroup documented

- **WHEN** a developer reads a spec with party details
- **THEN** they SHALL find the PartyDetailGroup structure with PartyDetailID, PartyDetailSubID, PartyDetailRole, PartyDetailStatus

#### Scenario: Nested groups documented

- **WHEN** a spec contains nested repeating groups
- **THEN** the structure SHALL be documented with clear parent-child relationships

### Requirement: Risk Limit Methodology

Risk management specifications SHALL document risk limit calculation methodology.

#### Scenario: Position calculation documented

- **WHEN** a developer reads risk limit specs
- **THEN** they SHALL find documentation of how positions are calculated (net vs gross)

#### Scenario: Multi-instrument aggregation documented

- **WHEN** a developer implements risk monitoring
- **THEN** the specs SHALL document how risk is aggregated across multiple instruments

### Requirement: MMP Protection Types

Party risk limit specifications SHALL document Market Maker Protection types and formulas.

#### Scenario: MMP types documented

- **WHEN** a developer reads CS-Party-Risk-Limits-Definition-Request.md
- **THEN** they SHALL find ProtectionType, ProtectionLimit, ProtectionPeriod fields with valid values

#### Scenario: MMP formulas documented

- **WHEN** a developer implements MMP
- **THEN** the specs SHALL document calculation formulas per Risk Spec §3.8
