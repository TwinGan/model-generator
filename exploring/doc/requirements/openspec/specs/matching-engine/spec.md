# Matching Engine

Order matching, price validation, and trade execution rules

## Capabilities

### Price Validation

**Source:** LME Matching Rules August 2022.md

Pre-execution price checks, failed check handling

### Trading Hours and Deadlines

**Source:** LME Matching Rules August 2022.md

Session schedules, TOM deadlines, trade input deadlines

### Order Matching Logic

**Source:** LME Matching Rules August 2022.md

Price-time priority, trade reporting, execution rules

## Functional Requirements


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
