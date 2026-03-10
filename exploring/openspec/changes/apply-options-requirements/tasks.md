# Implementation Tasks

## 1. Foundation - Reference Files

- [x] 1.1 Create `doc/requirements/openspec/reference/` directory
- [ ] 1.2 Create `symbols.md` with complete LME symbol list (AL, CU, ZN, PB, NI, SN, AA, HN) including lot sizes, tick sizes, and contract codes
- [ ] 1.3 Create `trading-hours.md` with venue schedules (LMEselect 01:00-19:00, Ring 11:40-17:00 London time)
- [ ] 1.4 Create `error-codes.md` with complete error/rejection code catalog (SessionRejectReason, BusinessRejectReason, CxlRejReason, OrdRejReason, MassCancelRejectReason)
- [ ] 1.5 Create `state-machines.md` with session, order, and risk state diagrams using Mermaid notation
- [ ] 1.6 Create `validation-rules.md` with field validation rule catalog (presence, data types, value ranges)

## 2. P0 Critical - Empty FIX Message Specs

- [ ] 2.1 Complete F-Order-Cancel-Request.md: Add OrigClOrdID (41), OrderID (37), Symbol (55), Side (54), all required/optional fields from FIX Spec §4.11.6
- [ ] 2.2 Complete G-Order-Cancel-Replace-Request.md: Add OrigClOrdID (41), ClOrdID (11), modifiable fields (Price, StopPx, OrderQty, DisplayQty, ExpireDate), inflight handling from §3.10
- [ ] 2.3 Complete 9-Order-Cancel-Reject.md: Add OrderID (37), ClOrdID (11), OrigClOrdID (41), CxlRejReason (102), RelatedHighPrice (1819), RelatedLowPrice (1820) from §4.11.7
- [ ] 2.4 Complete s-New-Order-Cross.md: Add CrossID (548), CrossType (549), CrossPrioritization (550), NoSide parameters, Auto Cross rules from §3.14
- [ ] 2.5 Complete q-Order-Mass-Cancel-Request.md: Add MassCancelRequestType (530), SecurityID (48), ProductComplex (1227), PartyRole (452) from §3.12 and §4.11.10
- [ ] 2.6 Complete r-Order-Mass-Cancel-Report.md: Add MassCancelResponse (531), MassCancelRejectReason (532), TotalAffectedOrders (533) from §4.11.11

## 3. P1 High - Binary Message Specs

- [ ] 3.1 Complete 1-Logon.md: Replace placeholder with CompID, Password, EncryptedPassword fields, RSA encryption rules from Binary Spec §1.1
- [ ] 3.2 Complete 2-Logout.md: Replace placeholder with Logout reason fields from Binary Spec §1.6
- [ ] 3.3 Complete 3-Heartbeat.md: Replace placeholder with TestReqID (112) field from Binary Spec §1.4
- [ ] 3.4 Complete 10-New-Order.md: Replace placeholder with all New Order fields from Binary Spec §4.10.10
- [ ] 3.5 Complete 11-Order-Cancel.md: Replace placeholder with cancel fields from Binary Spec §4.10.11
- [ ] 3.6 Complete 12-Order-Replace.md: Replace placeholder with replace fields from Binary Spec §4.10.12
- [ ] 3.7 Complete 20-Execution-Report.md: Replace placeholder with execution fields from Binary Spec §4.10.20
- [ ] 3.8 Complete 21-Order-Reject.md: Replace placeholder with rejection fields from Binary Spec §4.10.21
- [ ] 3.9 Add binary encoding rules (little-endian, message structure, field presence map) to all 8 Binary specs

## 4. P2 Medium - Risk Management Specs

- [ ] 4.1 Complete BE-User-Request.md: Add UserRequestType, UserRequestID, Username fields from Risk Spec §4.6.1
- [ ] 4.2 Complete BF-User-Response.md: Add UserStatus, Email fields from Risk Spec §4.6.2
- [ ] 4.3 Complete CA-Risk-Limit-Query-Request.md: Add RiskLimitRequestID, RiskLimitRequestType (1760), NoPartyDetails from Risk Spec §4.1
- [ ] 4.4 Complete CC-Risk-Limit-Query-Response.md: Add RiskLimitLevel, limit data fields from Risk Spec §4.2
- [ ] 4.5 Complete CB-Risk-Limit-Update-Request.md: Add RiskLimitID, RiskLimitAmount, RiskLimitType from Risk Spec §4.3
- [ ] 4.6 Complete CD-Risk-Limit-Update-Report.md: Add update result fields from Risk Spec §4.4
- [ ] 4.7 Complete remaining 12 Risk Management specs with missing application fields
- [ ] 4.8 Add party detail group structures (PartyDetailGroup, nested groups) to relevant specs
- [ ] 4.9 Add risk limit calculation methodology (net vs gross, multi-instrument aggregation)
- [ ] 4.10 Add MMP protection types and formulas from Risk Spec §3.8

## 5. P3 Low - FIX Value Enrichment

- [ ] 5.1 Enrich D-New-Order-Single.md: Add complete OrdType enumeration (Iceberg, Post Only), TriggeringInstruction block, OrderAttributeGrp
- [ ] 5.2 Enrich 8-Execution-Report.md: Add ExecTypeReason (2431), TrdMatchID (880), complete ExecType/OrdStatus enums
- [ ] 5.3 Enrich A-Logon.md: Add EncryptedPassword (1402), NextExpectedMsgSeqNum (789), SessionStatus (1409)
- [ ] 5.4 Enrich c-Security-Definition-Request.md: Add strategy-related fields (SecuritySubType, LegSecurityID, LegRatioQty)
- [ ] 5.5 Enrich d-Security-Definition.md: Add complete instrument definition fields from §4.11.2
- [ ] 5.6 Enrich R-Quote-Request.md: Add QuoteReqID (131), QuoteRequestType (303), NoInstrument group from §4.11.12
- [ ] 5.7 Enrich j-Business-Message-Reject.md: Add complete BusinessRejectReason enum (0-9) from §4.9.1
- [ ] 5.8 Enrich 3-Reject.md: Add complete SessionRejectReason enum from §4.8.7
- [ ] 5.9 Enrich 5-Logout.md: Add complete SessionStatus enum (3-8, 100-101) from §4.8.6
- [ ] 5.10 Enrich remaining 11 FIX messages with concrete values and source references

## 6. Module Spec Enhancement

- [ ] 6.1 Update session-management/spec.md: Add heartbeat interval (30s), session timeout (90s), max failed auth attempts
- [ ] 6.2 Update order-management/spec.md: Add max order qty (9,999), max order price (9,999,999), order type details, state machine reference
- [ ] 6.3 Update risk-management/spec.md: Add concrete limit values, warning thresholds, risk state machine reference
- [ ] 6.4 Update matching-engine/spec.md: Add TOM deadlines (12:30, 13:30), trade input deadline (20:00), price tolerance defaults
- [ ] 6.5 Update reliability/spec.md: Add resend window size, duplicate detection window, recovery time objectives
- [ ] 6.6 Update connectivity/spec.md: Define FIX and Binary capabilities (currently placeholder), FIX version (4.4/5.0 with LME extensions)
- [ ] 6.7 Update examples/spec.md: Add references to actual FIX/Binary message examples from source

## 7. Test Specification Implementation

- [ ] 7.1 Create test case template with TC-{MODULE}-{NNN} ID format in test-specification-implementation spec
- [ ] 7.2 Replace session-management/test.md template with actual test cases (TC-SESSION-001 through TC-SESSION-010)
- [ ] 7.3 Replace order-management/test.md template with actual test cases (TC-ORDER-001 through TC-ORDER-020)
- [ ] 7.4 Replace risk-management/test.md template with actual test cases (TC-RISK-001 through TC-RISK-015)
- [ ] 7.5 Replace matching-engine/test.md template with actual test cases (TC-MATCH-001 through TC-MATCH-010)
- [ ] 7.6 Replace reliability/test.md template with actual test cases (TC-RELIABILITY-001 through TC-RELIABILITY-010)
- [ ] 7.7 Replace connectivity/test.md template with actual test cases (TC-CONN-001 through TC-CONN-010)
- [ ] 7.8 Replace examples/test.md template with validation test cases

## 8. Verification & Documentation

- [ ] 8.1 Verify all concrete values include source citations (FIX Spec §X.Y, Binary Spec §X.Y, etc.)
- [ ] 8.2 Verify all state machines use valid Mermaid stateDiagram-v2 syntax
- [ ] 8.3 Verify all message specs have consistent field table format (Tag, Field Name, Data Type, Presence, Description)
- [ ] 8.4 Add "Last Synced" metadata to each updated spec file with source spec version and date
- [ ] 8.5 Update README.md in openspec/messages/organized/ to reflect completion status
- [ ] 8.6 Update README.md in openspec/specs/ to reflect completion status
- [ ] 8.7 Create reference/README.md documenting the reference file structure and usage
