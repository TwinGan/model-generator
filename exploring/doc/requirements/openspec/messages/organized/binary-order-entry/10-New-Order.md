# New Order

**Domain:** Binary Order Entry  
**Template ID:** 10  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

New Order message for LME Binary Order Entry protocol. Used to submit a new order to the exchange.

## Message Specification

### Binary Protocol Details
- **Template ID:** 10
- **Message Name:** New Order
- **Protocol:** LME Proprietary Binary Protocol v1.9.1
- **Source:** Binary Spec §4.10.10

## Message Structure
```
New Order (Template ID: 10)
├── Message Header (6 bytes)
│   ├── Message Length (2 bytes, UInt16)
│   ├── Template ID (2 bytes, UInt16) = 10
│   └── Schema ID (2 bytes, UInt16)
├── Field Presence Map (variable)
└── Message Body
    ├── ClOrdID (String)
    ├── SecurityID (String)
    ├── Side (UInt8)
    ├── OrderQty (Int32)
    ├── Price (Int64, optional)
    ├── OrdType (UInt8)
    ├── TimeInForce (UInt8)
    └── Additional optional fields
```

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: New Order (Binary Template 10)
Gateway → Client: Execution Report (Binary Template 20) with OrdStatus=NEW
```

### Rejection Scenario
```
Client → Gateway: New Order (Binary Template 10)
Gateway → Client: Order Reject (Binary Template 21) with OrdRejReason
```

## Fields Reference

### Header Fields (Always Present)
| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| MessageLength | 0 | 2 | UInt16 | Total message length |
| TemplateID | 2 | 2 | UInt16 | Message template ID = 10 |
| SchemaID | 4 | 2 | UInt16 | Schema version |

### Required Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| ClOrdID | String(20) | Required | Unique client order ID |
| SecurityID | String(20) | Required | Instrument symbol (e.g., "CA") |
| Side | UInt8 | Required | 1=Buy, 2=Sell |
| OrderQty | Int32 | Required | Order quantity in lots |
| OrdType | UInt8 | Required | Order type (1=Market, 2=Limit, etc.) |
| TimeInForce | UInt8 | Required | 0=Day, 1=GTC, 3=IOC, 4=FOK |

### Optional Message Body Fields
| Field Name | Type | Presence | Description |
|------------|------|----------|-------------|
| Price | Int64 | Conditional | Limit price (scaled by 10^8) |
| StopPx | Int64 | Conditional | Stop price (scaled by 10^8) |
| ExpireDate | UInt16 | Conditional | Expiration date (YYYYMMDD) |
| DisplayQty | Int32 | Optional | Display quantity (iceberg) |
| MinQty | Int32 | Optional | Minimum fill quantity |
| MaxFloor | Int32 | Optional | Maximum visible quantity |

## OrdType Values
| Code | Name | Description | Price Required |
|------|------|-------------|----------------|
| 1 | MARKET | Market order | No |
| 2 | LIMIT | Limit order | Yes |
| 3 | STOP | Stop order | No (StopPx required) |
| 4 | STOP_LIMIT | Stop-limit order | Yes (StopPx required) |
| K | ICEBERG | Iceberg order | Yes |
| L | POST_ONLY | Post-only order | Yes |

## TimeInForce Values
| Code | Name | Description |
|------|------|-------------|
| 0 | DAY | Good for day |
| 1 | GTC | Good till cancelled |
| 3 | IOC | Immediate or cancel |
| 4 | FOK | Fill or kill |
| 6 | GTD | Good till date (requires ExpireDate) |

## Price Encoding
Prices are encoded as 64-bit signed integers scaled by 10^8:
- Price 2500.50 → 250050000000 (0x3A29F06C0)
- Use little-endian byte order

## Message Example (Binary Hex Dump)

### Example: Limit Buy Order for 10 lots at 2500.50
```
00 32          # Message Length: 50 bytes
0A 00          # Template ID: 10
01 00          # Schema ID: 1
FF             # Presence Map: All fields present
08 43 4C 30 30 30 30 30 31  # ClOrdID: "CL000001" (8 bytes)
02 43 41       # SecurityID: "CA" (2 bytes)
01             # Side: 1 (Buy)
0A 00 00 00    # OrderQty: 10 lots
02             # OrdType: 2 (Limit)
00             # TimeInForce: 0 (Day)
00 E2 30 3A 00 00 00 00  # Price: 250050000000 (scaled)
```

## Processing Rules

### Validation Requirements
1. ClOrdID must be unique per trading day
2. SecurityID must be valid LME symbol
3. OrderQty must be 1-9,999 lots
4. Price must be positive (if required)
5. Valid session must be established

### Binary Encoding
1. **Strings:** Length-prefixed (1-byte length, UTF-8)
2. **Integers:** Little-endian byte order
3. **Prices:** Scaled by 10^8

## Testing Considerations

### Positive Test Cases
1. ✅ Valid limit order
2. ✅ Valid market order
3. ✅ Iceberg order with DisplayQty
4. ✅ GTD order with ExpireDate

### Negative Test Cases
1. ❌ Invalid SecurityID
2. ❌ OrderQty exceeds limit
3. ❌ Missing required Price for limit order
4. ❌ Duplicate ClOrdID

## References

- **Source:** Binary Order Entry Specification v1.9.1 §4.10.10
- **Price Encoding:** Binary Spec §2.3
- **Validation:** Binary Spec §3.3
