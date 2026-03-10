# Risk Management

Pre-trade risk controls, limits, and compliance checking

## Capabilities

### Pre-Trade Risk Limits

**Source:** Risk Management Gateway FIX Specification v1 8.md

Per order quantity, notional value, gross position limits

### Risk Group Management

**Source:** Risk Management Gateway FIX Specification v1 8.md

User role-based risk controls, view-only access

## Functional Requirements


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
