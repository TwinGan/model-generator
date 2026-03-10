# LME Options Trading - Capability Modules

This document summarizes the functional capabilities extracted from LME specifications.

## Modules Overview

### Session Management

FIX session establishment, authentication, and lifecycle management

**Capabilities:**

- **FIX Session Establishment and Authentication**
  - *Source:* Order Entry Gateway FIX Specification v 1 9 1.md
  - *Description:* Logon, authentication, password management, session termination
- **FIX Session Establishment and Authentication**
  - *Source:* Binary Order Entry Specification v1 9  1.md
  - *Description:* Logon, authentication, password management, session termination

### Order Management

Order submission, modification, cancellation, and status tracking

**Capabilities:**

- **Order Type Support**
  - *Source:* Order Entry Gateway FIX Specification v 1 9 1.md
  - *Description:* Market, Limit, Stop, Stop-Limit, Iceberg, Fill-or-Kill, Good-for-Day, Good-Till-Cancel, Good-Till-Date
- **Order Submission**
  - *Source:* Order Entry Gateway FIX Specification v 1 9 1.md
  - *Description:* New order placement with validation
- **Order Modification and Cancellation**
  - *Source:* Order Entry Gateway FIX Specification v 1 9 1.md
  - *Description:* Amend order parameters, cancel orders, mass cancellation
- **Order Type Support**
  - *Source:* Binary Order Entry Specification v1 9  1.md
  - *Description:* Market, Limit, Stop, Stop-Limit, Iceberg, Fill-or-Kill, Good-for-Day, Good-Till-Cancel, Good-Till-Date
- **Order Submission**
  - *Source:* Binary Order Entry Specification v1 9  1.md
  - *Description:* New order placement with validation
- **Order Modification and Cancellation**
  - *Source:* Binary Order Entry Specification v1 9  1.md
  - *Description:* Amend order parameters, cancel orders, mass cancellation

### Risk Management

Pre-trade risk controls, limits, and compliance checking

**Capabilities:**

- **Pre-Trade Risk Limits**
  - *Source:* Risk Management Gateway FIX Specification v1 8.md
  - *Description:* Per order quantity, notional value, gross position limits
- **Risk Group Management**
  - *Source:* Risk Management Gateway FIX Specification v1 8.md
  - *Description:* User role-based risk controls, view-only access

### Matching Engine

Order matching, price validation, and trade execution rules

**Capabilities:**

- **Price Validation**
  - *Source:* LME Matching Rules August 2022.md
  - *Description:* Pre-execution price checks, failed check handling
- **Trading Hours and Deadlines**
  - *Source:* LME Matching Rules August 2022.md
  - *Description:* Session schedules, TOM deadlines, trade input deadlines
- **Order Matching Logic**
  - *Source:* LME Matching Rules August 2022.md
  - *Description:* Price-time priority, trade reporting, execution rules

### Reliability & Recovery

Message recovery, gap fill, and fault tolerance mechanisms

**Capabilities:**

- **Message Recovery**
  - *Source:* Order Entry Gateway FIX Specification v 1 9 1.md
  - *Description:* Gap fill, resend requests, duplicate detection
- **Message Recovery**
  - *Source:* Binary Order Entry Specification v1 9  1.md
  - *Description:* Gap fill, resend requests, duplicate detection

### Connectivity

Protocol support (FIX and Binary) and message formats

*No capabilities identified in this module*

### Message Examples

Sample messages and usage examples for all protocols

**Capabilities:**

- **FIX Message Examples**
  - *Source:* LMEselect v10  FIX and BINARY Message Examples v10.md
  - *Description:* Sample FIX messages for all order types and scenarios
- **Binary Message Examples**
  - *Source:* LMEselect v10  FIX and BINARY Message Examples v10.md
  - *Description:* Sample binary messages for all order types and scenarios

