# Execution Report

**Domain:** Order Entry  
**Message Type:** 8  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Report order execution status, fills, and updates to the client.

## Message Specification

### FIX Protocol Details
- **Message Type:** `8`
- **Message Name:** Execution Report
- **FIX Version:** 5.0 (with LME extensions)
- **Direction:** Gateway→Client

### Message Structure
```
Execution Report (8)
├── Standard Header
│   ├── BeginString (8)
│   ├── BodyLength (9)
│   ├── MsgType (35) = 8
│   ├── SenderCompID (49)
│   ├── TargetCompID (56)
│   ├── MsgSeqNum (34)
│   └── SendingTime (52)
├── Message Body
│   ├── OrderID (37) - Exchange order ID
│   ├── ClOrdID (11) - Client order ID
│   ├── ExecID (17) - Execution ID
│   ├── ExecType (150) - Execution type
│   ├── OrdStatus (39) - Order status
│   ├── Symbol (55) - Instrument symbol
│   ├── Side (54) - Order side
│   ├── OrderQty (38) - Order quantity
│   ├── LastQty (32) - Last executed quantity
│   ├── LastPx (31) - Last execution price
│   ├── LeavesQty (151) - Remaining quantity
│   ├── CumQty (14) - Cumulative executed quantity
│   └── TransactTime (60) - Transaction timestamp
└── Standard Trailer
    └── CheckSum (10)
```

## Message Interaction Flow

### New Order Acknowledgment
```
Client → Gateway: New Order Single (D)
Gateway → Client: Execution Report (8) - ExecType=0 (New), OrdStatus=0 (New)
```

### Fill Notification
```
Client → Gateway: New Order Single (D)
Gateway → Client: Execution Report (8) - ExecType=2 (Fill), OrdStatus=2 (Filled)
```

### Partial Fill
```
Client → Gateway: New Order Single (D)
Gateway → Client: Execution Report (8) - ExecType=1 (Partial Fill), OrdStatus=1 (Partially Filled)
Gateway → Client: Execution Report (8) - ExecType=2 (Fill), OrdStatus=2 (Filled)
```

### Cancel Confirmation
```
Client → Gateway: Order Cancel Request (F)
Gateway → Client: Execution Report (8) - ExecType=4 (Cancelled), OrdStatus=4 (Cancelled)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Description |
|-----|-----------|-----------|-------------|
| 8 | BeginString | String | FIX protocol version |
| 9 | BodyLength | Length | Message body length |
| 35 | MsgType | String | Message type = 8 |
| 49 | SenderCompID | String | Sender company ID |
| 56 | TargetCompID | String | Target company ID |
| 34 | MsgSeqNum | SeqNum | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Message sending time |
| 37 | OrderID | String | Order ID assigned by exchange |
| 11 | ClOrdID | String | Client order ID |
| 17 | ExecID | String | Unique execution ID |
| 150 | ExecType | Char | Execution type: 0=New, 1=PartialFill, 2=Fill, 4=Cancelled, 5=Replaced, 8=Rejected |
| 39 | OrdStatus | Char | Order status: 0=New, 1=PartiallyFilled, 2=Filled, 4=Cancelled, 5=Replaced, 8=Rejected |
| 54 | Side | Char | Order side: 1=Buy, 2=Sell |
| 38 | OrderQty | Qty | Original order quantity |
| 151 | LeavesQty | Qty | Remaining quantity |
| 14 | CumQty | Qty | Cumulative executed quantity |
| 60 | TransactTime | UTCTimestamp | Transaction timestamp |
| 10 | CheckSum | String | Message checksum |

### Conditional Fields
| Tag | Field Name | Data Type | Condition | Description |
|-----|-----------|-----------|-----------|-------------|
| 32 | LastQty | Qty | ExecType=1,2 | Quantity of last execution |
| 31 | LastPx | Price | ExecType=1,2 | Price of last execution |
| 6 | AvgPx | Price | ExecType=1,2 | Average execution price |
| 103 | OrdRejReason | Int | OrdStatus=8 | Reject reason code |
| 378 | ExecRestatementReason | Int | ExecType=D | Restatement reason |

## Message Example (Tabby CSV Format)

### Example: Execution Report (8)

```csv
AvgPx,BeginString,BodyLength,CheckSum,ClOrdID,CumQty,ExecID,LastPx,LastQty,MsgSeqNum,MsgType,OrderID,OrderQty,OrdStatus,SenderCompID,SendingTime,Side,TargetCompID,TransactTime,OrdRejReason,ExecType,LeavesQty,ExecRestatementReason
2505.00,FIXT.1.1,,,ORD20240001,10,EXEC001,2505.00,10,1,,LME123456,10,0,CLIENT1,20240101-12:00:00.000,1,LME,20240101-12:00:00.000,1,0,0,1
```

### Example: Execution Report - Fill

```csv
# Message: Execution Report (8) - Fill
# Direction: Gateway→Client
# Description: Order completely filled

Name,Value,Field Number,Data Type,Notes
BeginString,FIXT.1.1,8,String,FIX version
BodyLength,,9,Length,Will be calculated
MsgType,8,35,String,Message type
SenderCompID,LME,49,String,LME CompID
TargetCompID,CLIENT1,56,String,Your CompID
MsgSeqNum,12,34,SeqNum,Message sequence number
SendingTime,20240101-12:00:05.250,52,UTCTimestamp,Current timestamp
OrderID,LME123456,37,String,Exchange order ID
ClOrdID,ORD20240001,11,String,Client order ID
ExecID,EXEC002,17,String,Unique execution ID
ExecType,2,150,Char,2=Fill
OrdStatus,2,39,Char,2=Filled
Symbol,CA,55,String,Symbol: CA=Copper
Side,1,54,Char,1=Buy, 2=Sell
OrderQty,10,38,Qty,Original order quantity
LastQty,10,32,Qty,Quantity of this fill
LastPx,2505.00,31,Price,Fill price
LeavesQty,0,151,Qty,Remaining quantity (0 = fully filled)
CumQty,10,14,Qty,Cumulative executed quantity
AvgPx,2505.00,6,Price,Average execution price
TransactTime,20240101-12:00:05.250,60,UTCTimestamp,Transaction timestamp
CheckSum,,10,String,Will be calculated
```

### Notes:
- **BodyLength** (9) and **CheckSum** (10) are calculated automatically
- **SendingTime** (52) should be current UTC timestamp
- **MsgSeqNum** (34) must increment sequentially per session
- **ExecID** (17) must be unique per execution
- **ExecType** (150) and **OrdStatus** (39) indicate the type of update

## Processing Rules

### When Sent
- **New Order Ack:** Immediately after receiving valid New Order Single (D)
- **Fill Notification:** When order is executed (fully or partially)
- **Cancel Confirm:** After Order Cancel Request (F) processed
- **Reject Notification:** When order fails validation or business rules
- **Status Update:** When order status changes

### Validation Requirements
1. **Message Level:**
   - All required fields must be present
   - Field data types must be valid
   - OrdStatus must be consistent with ExecType
   - Quantities must be consistent (LeavesQty + CumQty = OrderQty)

2. **Business Rules:**
   - OrderID must reference a valid order
   - ClOrdID must match the original client order ID
   - ExecID must be unique per execution
   - Status transitions must be valid (e.g., New → Partial → Fill)

## Resulting Messages

### Related Messages
- **Triggered By:** New Order Single (D), Order Cancel Request (F), Order Cancel Replace (G)
- **May Trigger:** Risk limit updates, position updates, trade reporting
- **Alternative:** Business Message Reject (j) if order rejected

## Testing Considerations

### Positive Test Cases
1. ✅ New order acknowledgment (ExecType=0, OrdStatus=0)
2. ✅ Partial fill notification (ExecType=1, OrdStatus=1)
3. ✅ Full fill notification (ExecType=2, OrdStatus=2)
4. ✅ Cancel confirmation (ExecType=4, OrdStatus=4)
5. ✅ Reject notification (ExecType=8, OrdStatus=8)

### Negative Test Cases
1. ❌ Invalid OrderID - should not occur
2. ❌ Invalid status transition - should not occur
3. ❌ Quantity mismatch - should not occur

### Edge Cases
1. ⚠️ Multiple partial fills
2. ⚠️ Fill with remaining quantity (partial fill)
3. ⚠️ Cancel after partial fill
4. ⚠️ Replace after partial fill
5. ⚠️ Expired order (if supported)

## Business Rules

### Order Status Transitions
- **New (0)** → Partially Filled (1) → Filled (2)
- **New (0)** → Cancelled (4)
- **New (0)** → Rejected (8)
- **Partially Filled (1)** → Filled (2)
- **Partially Filled (1)** → Cancelled (4)

### Quantity Validation
- **LeavesQty + CumQty = OrderQty** (must always hold)
- **LastQty ≤ LeavesQty** (before fill)
- **LeavesQty = 0** when order is fully filled

## References

- **Source:** Order Entry Gateway FIX Specification v1.9.1
- **Section:** 4.11.7 Execution Report (8)
- **Examples:** LMEselect v10 FIX Message Examples
- **Matching Rules:** LME Matching Rules August 2022

## Implementation Notes

- **Multiple reports:** Single order may generate multiple Execution Reports (for partial fills)
- **State management:** Client must track order state based on OrdStatus
- **Execution tracking:** Client should track executions using ExecID
- **Position management:** Client should update positions based on fills
- **Trade reporting:** Filled orders may be reported to trade reporting systems
