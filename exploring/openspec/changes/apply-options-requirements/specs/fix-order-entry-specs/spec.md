# FIX Order Entry Specifications Enhancement

Enhance all 21 FIX order entry message specifications with complete field definitions, business rules, and concrete values.

## MODIFIED Requirements

### Requirement: Empty Message Specifications Filled

Six FIX message specifications that currently contain only header fields SHALL be completed with all message-specific fields.

The following files SHALL be updated:
- `fix-order-entry/F-Order-Cancel-Request.md`
- `fix-order-entry/G-Order-Cancel-Replace-Request.md`
- `fix-order-entry/9-Order-Cancel-Reject.md`
- `fix-order-entry/s-New-Order-Cross.md`
- `fix-order-entry/q-Order-Mass-Cancel-Request.md`
- `fix-order-entry/r-Order-Mass-Cancel-Report.md`

#### Scenario: Order Cancel Request has complete fields

- **WHEN** a developer reads F-Order-Cancel-Request.md
- **THEN** they SHALL find OrigClOrdID (41), OrderID (37), Symbol (55), Side (54), and all other message-specific fields with types and presence requirements

#### Scenario: Order Cancel Replace Request has complete fields

- **WHEN** a developer reads G-Order-Cancel-Replace-Request.md
- **THEN** they SHALL find OrigClOrdID (41), ClOrdID (11), and all modifiable fields (Price, OrderQty, etc.) with types and presence requirements

### Requirement: Complete Field Enumerations

All FIX message specifications SHALL include complete enumerations for enumerated fields.

#### Scenario: ExecType enumeration complete

- **WHEN** a developer reads the Execution Report spec
- **THEN** they SHALL find complete ExecType values: 0=New, 1=PartialFill, 2=Fill, 4=Cancelled, 5=Replaced, 8=Rejected, D=Restated, E=PendingReplace

#### Scenario: OrdStatus enumeration complete

- **WHEN** a developer reads the Execution Report spec
- **THEN** they SHALL find complete OrdStatus values: 0=New, 1=PartiallyFilled, 2=Filled, 4=Cancelled, 5=Replaced, 6=PendingCancel, 8=Rejected, C=Expired, E=PendingReplace

#### Scenario: OrdRejReason enumeration complete

- **WHEN** a developer reads the New Order Single spec
- **THEN** they SHALL find complete rejection reasons: 1=UnknownSymbol, 2=ExchangeClosed, 3=OrderExceedsLimit, 4=TooLateToEnter, 6=DuplicateOrder, 8=InvalidPrice, 11=InvalidQuantity, 18=InvalidOrderType, 99=Other

### Requirement: Business Rules Referenced

All FIX message specifications SHALL reference relevant business rule sections from the source specification.

#### Scenario: Order types reference section 3.4

- **WHEN** a developer reads about OrdType field
- **THEN** the spec SHALL include reference to FIX Spec §3.4 for complete order type behavior

#### Scenario: Speed bump rules referenced

- **WHEN** a developer reads about order handling
- **THEN** the spec SHALL include reference to FIX Spec §3.16 for speed bump behavior and ExecTypeReason values

#### Scenario: Inflight handling referenced

- **WHEN** a developer reads about order modification
- **THEN** the spec SHALL include reference to FIX Spec §3.21 and Appendix A/B for inflight order handling

### Requirement: Concrete Symbol Values

FIX message specifications using Symbol field SHALL reference the complete symbol list.

#### Scenario: Symbol field references symbol list

- **WHEN** a developer reads about Symbol (55) field
- **THEN** the spec SHALL reference `openspec/reference/symbols.md` for valid symbol values
