# Risk Limit Update Request

**Domain:** Risk Management  
**Message Type:** CB  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Risk Limit Update Request message for LME Risk Management Gateway. Used to request changes to risk limits for a party or member.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CB`
- **Message Name:** Risk Limit Update Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.3

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Risk Limit Update Request (CB)
Gateway → Client: Risk Limit Update Report (CD) with status=ACCEPTED
```

### Failure Scenario
```
Client → Gateway: Risk Limit Update Request (CB)
Gateway → Client: Risk Limit Update Report (CD) with status=REJECTED
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = CB |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 1757 | RiskLimitID | String | Required | Unique limit identifier |
| 1758 | RiskLimitType | Int | Required | Type of limit |
| 1753 | RiskLimitAmount | Amt | Required | New limit amount |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 453 | NoPartyIDs | NumInGroup | Conditional | Party identification group |
| 452 | PartyRole | Int | Conditional | Party role |
| 48 | SecurityID | String | Optional | Symbol for symbol-specific limits |
| 55 | Symbol | String | Optional | Symbol name |
| 1762 | RiskLimitAction | Int | Optional | Action type (add/modify/remove) |
| 1755 | RiskLimitWarningLevel | Percentage | Optional | Warning threshold % |
| 1754 | RiskLimitBreachLevel | Percentage | Optional | Breach threshold % |
| 1764 | RiskLimitCurrency | String | Optional | Limit currency (USD) |
| 58 | Text | String | Optional | Free-form text |

## RiskLimitType Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | GROSS_POSITION | Gross position limit | Risk Spec §3.2 |
| 2 | NET_POSITION | Net position limit | Risk Spec §3.2 |
| 3 | ORDER_QTY | Order quantity limit | Risk Spec §3.2 |
| 4 | ORDER_VALUE | Order value limit | Risk Spec §3.2 |
| 5 | DAILY_TURNOVER | Daily turnover limit | Risk Spec §3.2 |
| 6 | EXPOSURE | Total exposure limit | Risk Spec §3.2 |
| 7 | MARGIN | Margin requirement | Risk Spec §3.2 |

## RiskLimitAction Values
| Code | Name | Description |
|------|------|-------------|
| 1 | ADD | Add new limit |
| 2 | MODIFY | Modify existing limit |
| 3 | REMOVE | Remove limit |

## Message Example (Tabby CSV Format)

### Example: Update Gross Position Limit
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitID,RiskLimitType,RiskLimitAmount,NoPartyIDs,PartyID,PartyRole
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,LIMIT001,1,1000000,1,MEMBER001,1
```

### Example: Update Symbol-Specific Limit
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitID,RiskLimitType,RiskLimitAmount,Symbol
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,LIMIT002,1,500000,CA
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- User must have risk management permissions
- RiskLimitID must be valid for MODIFY/REMOVE
- RiskLimitAmount must be positive

### Limit Types by Category
1. **Position Limits**: Gross/Net position
2. **Order Limits**: Qty, Value
3. **Activity Limits**: Daily turnover
4. **Risk Limits**: Exposure, Margin

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.3
- **FIX Version:** 5.0 with LME extensions
