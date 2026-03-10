# LME Validation Rules Reference

**Source**: FIX Specification v1.9.1, Binary Specification v1.9.1
**Last Synced**: 2026-03-08

## Session Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Heartbeat Interval | 30 seconds (configurable via HeartBtInt (108)) | FIX Spec §1.4 |
| Session Timeout | 3 heartbeat intervals (90 seconds default) | FIX Spec §1.4 |
| Max Failed Auth Attempts | Account locked after multiple failures | FIX Spec §1.1 |
| Sequence Number Range | 1 to 2,147,483,647 | FIX Spec §1.3 |

## Order Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Max Order Quantity | 9,999 lots | FIX Spec §3.3 |
| Max Order Price | 9,999,999 | FIX Spec §3.3 |
| Min Order Quantity | 1 lot | FIX Spec §3.3 |
| Max Display Quantity | Equal to Order Quantity (Iceberg) | FIX Spec §3.4 |
| Min Display Quantity | Greater than 0 (Iceberg) | FIX Spec §3.4 |

## Field Presence Rules

### Required Fields (Must be present)
- BeginString (8)
- BodyLength (9)
- MsgType (35)
- SenderCompID (49)
- TargetCompID (56)
- MsgSeqNum (34)
- SendingTime (52)
- CheckSum (10)

### Conditionally Required Fields
| Field | Condition | Source |
|-------|-----------|--------|
| Price (44) | Required for Limit orders (OrdType=2) and Stop-Limit orders (OrdType=4) | FIX Spec §4.11.3 |
| StopPx (99) | Required for Stop orders (OrdType=3) and Stop-Limit orders (OrdType=4) | FIX Spec §4.11.3 |
| DisplayQty (1138) | Required for Iceberg orders (OrdType=K) | FIX Spec §4.11.3 |
| ExpireDate (432) | Required for GTD orders (TimeInForce=6) | FIX Spec §4.11.3 |
| OrigClOrdID (41) | Required for Cancel (F) and Replace (G) requests | FIX Spec §4.11.6 |

## Data Type Constraints

| Field | Data Type | Constraints | Source |
|-------|-----------|-------------|--------|
| ClOrdID (11) | String | Max 20 characters, unique per trading day | FIX Spec §3.7 |
| Symbol (55) | String | Valid LME symbol (AL, CU, ZN, PB, NI, SN, AA, HN) | FIX Spec §3.1 |
| Side (54) | Char | Valid values: 1=Buy, 2=Sell | FIX Spec §4.11.3 |
| OrdType (40) | Char | Valid values: 1=Market, 2=Limit, 3=Stop, 4=StopLimit, K=Iceberg, L=PostOnly | FIX Spec §3.4 |
| OrderQty (38) | Qty | 1 to 9,999 lots | FIX Spec §3.3 |
| Price (44) | Price | Positive, max 9,999,999 | FIX Spec §3.3 |
| TimeInForce (59) | Char | Valid values: 0=Day, 1=GTC, 3=IOC, 4=FOK, 6=GTD | FIX Spec §3.5 |

## Cross-Field Validation Rules

### Order Type and Price Relationship
| OrdType | Price Required | StopPx Required |
|---------|----------------|-----------------|
| 1 (Market) | No | No |
| 2 (Limit) | Yes | No |
| 3 (Stop) | No | Yes |
| 4 (Stop-Limit) | Yes | Yes |
| K (Iceberg) | Yes | No |

### TimeInForce and Order Type Compatibility
| TimeInForce | Valid For | Source |
|--------------|-----------|--------|
| 0 (Day) | All order types | FIX Spec §3.6 |
| 1 (GTC) | Cash and 3M outright contracts only | FIX Spec §3.6 |
| 3 (IOC) | All order types | FIX Spec §3.6 |
| 4 (FOK) | All order types | FIX Spec §3.6 |
| 6 (GTD) | Cash and 3M outright contracts only | FIX Spec §3.6 |

## Business Rule Validation

### Market State Validation
- Orders accepted only during trading hours (01:00-19:00 LMEselect)
- Pre-open orders may be accepted but not matched until open
- Orders rejected outside trading hours with OrdRejReason=2 (Exchange Closed)

### Risk Limit Validation
- Per-order quantity limits checked before acceptance
- Gross position limits checked before acceptance
- Credit limits checked before acceptance
- Orders exceeding limits rejected with OrdRejReason=26 (Risk Limit Exceeded)

### Price Validation
- Price must be within valid range for instrument
- Price tolerance checks against reference price
- Orders failing price validation rejected with OrdRejReason=8 (Invalid Price)

## Cross-References

- Error Codes: See [error-codes.md](./error-codes.md)
- Symbols: See [symbols.md](./symbols.md)
- Trading Hours: See [trading-hours.md](./trading-hours.md)
