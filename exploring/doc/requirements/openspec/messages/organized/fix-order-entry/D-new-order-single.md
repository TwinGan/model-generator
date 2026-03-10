# New Order Single

**Domain:** Order Entry  
**Message Type:** D  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Submit a new order for execution on the LME exchange.

## Message Specification

### FIX Protocol Details
- **Message Type:** `D`
- **Message Name:** New Order Single
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Client→Gateway

### Message Structure
```
New Order Single (D)
├── Standard Header
│   ├── BeginString (8)
│   ├── BodyLength (9)
│   ├── MsgType (35) = D
│   ├── SenderCompID (49)
│   ├── TargetCompID (56)
│   ├── MsgSeqNum (34)
│   └── SendingTime (52)
├── Message Body
│   ├── ClOrdID (11) - Unique client order ID
│   ├── Symbol (55) - Instrument symbol (e.g., CA)
│   ├── Side (54) - 1=Buy, 2=Sell
│   ├── OrderQty (38) - Order quantity
│   ├── OrdType (40) - 1=Market, 2=Limit, 3=Stop
│   ├── Price (44) - Order price (for limit orders)
│   └── TransactTime (60) - Transaction timestamp
└── Standard Trailer
    └── CheckSum (10)
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: New Order Single (D)
Gateway → Client: Execution Report (8) - New Acknowledgment
Gateway → Client: Execution Report (8) - Filled/Partial Fill
```

### Failure Scenario
```
Client → Gateway: New Order Single (D)
Gateway → Client: Business Message Reject (j) - Invalid order
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = D |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 11 | ClOrdID | String | Unique client order ID |
| 55 | Symbol | String | Instrument symbol (e.g., CA, PB, ZS) |
| 54 | Side | Char | Order side: 1=Buy, 2=Sell |
| 38 | OrderQty | Qty | Order quantity |
| 40 | OrdType | Char | Order type: 1=Market, 2=Limit, 3=Stop, 4=StopLimit |
| 60 | TransactTime | UTCTimestamp | Transaction timestamp |
| 10 | CheckSum | String | Message checksum |

### Optional Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 44 | Price | Price | Order price (required for limit orders) |
| 59 | TimeInForce | Char | Time in force: 0=Day, 1=GTC, 3=IOC, 4=FOK |
| 110 | MinQty | Qty | Minimum quantity |
| 111 | MaxFloor | Qty | Maximum floor |

### Conditional Fields
| Tag | Field Name | Data Type | Condition | Description |
|-----|-----------|-----------|-----------|-------------|
| 44 | Price | Price | OrdType = 2,4 | Required for limit orders |
| 99 | StopPx | Price | OrdType = 3,4 | Required for stop orders |

## Message Example (Tabby CSV Format)

### Example: New Order Single (D)

```csv
BeginString,BodyLength,CheckSum,ClOrdID,MsgSeqNum,MsgType,OrderQty,OrdType,Price,SenderCompID,SendingTime,Side,Symbol,TargetCompID,TimeInForce,TransactTime,StopPx,MinQty,MaxFloor
FIXT.1.1,,,ORD20240001,1,,10,2,2500.00,CLIENT1,20240101-12:00:00.000,1,CA,LME,0,20240101-12:00:00.000,100.00,10,10
```

### Notes:
- **BodyLength** (9) and **CheckSum** (10) are calculated automatically
- **SendingTime** (52) and **TransactTime** (60) should be current UTC timestamp
- **MsgSeqNum** (34) must increment sequentially per session
- **ClOrdID** (11) must be unique per order per trading day
- **Price** (44) is required for limit orders (OrdType = 2 or 4)
- **Symbol** (55) values: CA=Copper, PB=Lead, ZS=Zinc, AL=Aluminum, NI=Nickel, SN=Tin

## Processing Rules

### When to Send
- **Pre-condition:** Valid FIX session must be established (Logon completed)
- **Timing:** During trading hours as defined in LME Matching Rules
- **Sequence:** MsgSeqNum must be the next expected sequence number
- **Rate limits:** Subject to message throttling rules (see specification section 3.17)

### Validation Requirements
1. **Session Level:**
   - Valid session must be established (Logon completed)
   - Sequence numbers must be in order
   - SenderCompID and TargetCompID must match session credentials

2. **Message Level:**
   - All required fields must be present
   - Field data types must be valid
   - Field values must be within acceptable ranges:
     - OrderQty: 1-9999 lots (subject to instrument limits)
     - Price: Must pass price validation checks
     - Symbol: Must be valid LME symbol
   - ClOrdID must be unique per trading day

3. **Business Level:**
   - User must have appropriate trading permissions
   - Operation must be allowed in current market state
   - Risk limits must be checked and not exceeded:
     - Per-order quantity limits
     - Gross position limits
     - Credit limits
   - Instrument must be tradable (not suspended)
   - Order must be within trading hours

## Resulting Messages

### Success Path
1. **Immediate Acknowledgment:**
   - **Message Type:** Execution Report (8)
   - **ExecType:** 0 (New)
   - **OrdStatus:** 0 (New)
   - **Fields:** OrderID (37), ExecID (17), TransactTime (60)

2. **Execution Notification:**
   - **Message Type:** Execution Report (8)
   - **ExecType:** 1 (Partial fill) or 2 (Fill)
   - **OrdStatus:** 1 (Partially filled) or 2 (Filled)
   - **Fields:** LastQty (32), LastPx (31), LeavesQty (151), CumQty (14)

### Error Path
- **Message Type:** Business Message Reject (j) or Order Reject
- **OrdRejReason:** (103) indicating reason:
  - 1 = Unknown symbol
  - 2 = Exchange closed
  3 = Order exceeds limit
  4 = Too late to enter
  5 = Unknown order
  6 = Duplicate order
  8 = Invalid price
  11 = Invalid quantity
  13 = Incorrect allocation
  18 = Invalid order type
  99 = Other

### Related Messages
- **Preceding:** Logon (A) - to establish session
- **Following:** Order Cancel Request (F) - to cancel order
- **Alternative:** Order Cancel Replace Request (G) - to modify order
- **Alternative:** Order Mass Cancel Request (q) - to mass cancel

## Testing Considerations

### Positive Test Cases
1. ✅ Valid limit order with all required fields
2. ✅ Valid market order (no price)
3. ✅ Order with optional fields (TimeInForce, etc.)
4. ✅ Order with maximum allowed quantity
5. ✅ Order with minimum allowed quantity

### Negative Test Cases
1. ❌ Missing ClOrdID - should reject
2. ❌ Missing Symbol - should reject
3. ❌ Invalid Symbol - should reject
4. ❌ OrderQty = 0 - should reject
5. ❌ OrdType = 2 (Limit) without Price - should reject
6. ❌ Price outside valid range - should reject
7. ❌ Duplicate ClOrdID - should reject
8. ❌ User without trading permission - should reject
9. ❌ Order exceeds risk limits - should reject
10. ❌ Order outside trading hours - should reject
11. ❌ Invalid MsgSeqNum - should handle per session rules

### Edge Cases
1. ⚠️ OrderQty at boundary values (min/max)
2. ⚠️ Price at boundary values (min/max)
3. ⚠️ Concurrent order submissions
4. ⚠️ Session recovery scenarios
5. ⚠️ Market state transitions (pre-open to open)
6. ⚠️ Order during market close and re-open
7. ⚠️ Partial fills with remaining quantity
8. ⚠️ Multiple partial fills

## Business Rules

### Pre-Trade Risk Checks
- **Per-order quantity limits:** Must not exceed configured maximum
- **Gross position limits:** Must not exceed risk limits
- **Credit limits:** Must have sufficient credit
- **Order value limits:** Must not exceed notional value limits
- **Self-trade prevention:** Block if would self-match (if configured)

### Market State Validation
- **Instrument status:** Must be tradable (not suspended/halted)
- **Market phase:** Must be in valid trading phase
- **Trading hours:** Must be within defined trading hours
- **Price validation:** Must pass price reasonableness checks

### Order Validation
- **Symbol validation:** Must be valid LME symbol
- **Quantity validation:** Must be within instrument limits
- **Price validation:** Must be valid for order type
- **TimeInForce validation:** Must be valid for order type
- **Order type validation:** Must be supported by instrument

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
- **Section:** 4.11.3 New Order Single (D)
- **Examples:** LMEselect v10 FIX Message Examples
- **Matching Rules:** LME Matching Rules August 2022

## Implementation Notes

- **ClOrdID uniqueness:** Must be unique per trading day per client
- **Order persistence:** Orders persist until executed, cancelled, or expired
- **Partial fills:** Supported - order remains working until fully filled or cancelled
- **Amendments:** Price and quantity can be amended (subject to validation)
- **Cancellations:** Full cancellation supported, partial cancellation not supported
- **Order states:** New → Partially Filled → Filled or New → Cancelled
- **Execution priority:** Price-time priority (see LME Matching Rules)

## Example Use Cases

### Use Case 1: Submit Limit Order
```
ClOrdID: ORD20240001
Symbol: CA (Copper)
Side: 1 (Buy)
OrderQty: 10
OrdType: 2 (Limit)
Price: 2500.00
TimeInForce: 0 (Day)
```

### Use Case 2: Submit Market Order
```
ClOrdID: ORD20240002
Symbol: PB (Lead)
Side: 2 (Sell)
OrderQty: 5
OrdType: 1 (Market)
TimeInForce: 3 (IOC)
```

### Use Case 3: Submit Stop Order
```
ClOrdID: ORD20240003
Symbol: ZS (Zinc)
Side: 1 (Buy)
OrderQty: 8
OrdType: 3 (Stop)
StopPx: 2800.00
TimeInForce: 1 (GTC)
```
