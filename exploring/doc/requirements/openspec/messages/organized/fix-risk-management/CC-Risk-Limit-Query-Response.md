# Risk Limit Query Response

**Domain:** Risk Management  
**Message Type:** CC  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Risk Limit Query Response message from LME Risk Management Gateway. Contains current risk limits and utilization for the queried party.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CC`
- **Message Name:** Risk Limit Query Response
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.2

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Risk Limit Query Request (CA)
Gateway → Client: Risk Limit Query Response (CC) with limits
```

### No Results Scenario
```
Client → Gateway: Risk Limit Query Request (CA)
Gateway → Client: Risk Limit Query Response (CC) with empty results
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = CC |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 1759 | RiskLimitRequestID | String | Required | ID from the request |
| 16 | NoRiskLimits | NumInGroup | Required | Number of limit records |

### Risk Limit Group Fields (NoRiskLimits)
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 1757 | RiskLimitID | String | Required | Unique limit identifier |
| 1758 | RiskLimitType | Int | Required | Type of limit |
| 1753 | RiskLimitAmount | Amt | Required | Limit amount |
| 1750 | RiskLimitUtilization | Amt | Required | Current utilization |
| 1751 | RiskLimitRemaining | Amt | Required | Remaining capacity |
| 1755 | RiskLimitWarningLevel | Percentage | Optional | Warning threshold |
| 1754 | RiskLimitBreachLevel | Percentage | Optional | Breach threshold |
| 1752 | RiskLimitStatus | Int | Optional | Current status |
| 453 | NoPartyIDs | NumInGroup | Optional | Party identification |

## RiskLimitStatus Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | NORMAL | Within limits | Risk Spec §3.2 |
| 1 | WARNING | Approaching limit | Risk Spec §3.2 |
| 2 | BREACH | Limit exceeded | Risk Spec §3.2 |
| 3 | BLOCKED | Trading blocked | Risk Spec §3.2 |

## RiskLimitType Values
| Code | Name | Description |
|------|------|-------------|
| 1 | GROSS_POSITION | Gross position limit |
| 2 | NET_POSITION | Net position limit |
| 3 | ORDER_QTY | Order quantity limit |
| 4 | ORDER_VALUE | Order value limit |
| 5 | DAILY_TURNOVER | Daily turnover limit |
| 6 | EXPOSURE | Total exposure limit |
| 7 | MARGIN | Margin requirement |

## Message Example (Tabby CSV Format)

### Example: Query Response with Multiple Limits
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,NoRiskLimits
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,REQ001,3

# Limit 1: Gross Position
RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUtilization,RiskLimitRemaining,RiskLimitStatus
LIMIT001,1,1000000,750000,250000,1

# Limit 2: Order Value
RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUtilization,RiskLimitRemaining,RiskLimitStatus
LIMIT002,4,500000,125000,375000,0

# Limit 3: Daily Turnover
RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUtilization,RiskLimitRemaining,RiskLimitStatus
LIMIT003,5,2000000,450000,1550000,0
```

## Processing Rules

### Response Generation
1. Query risk management system for matching limits
2. Include all limits matching request criteria
3. Calculate utilization and remaining capacity
4. Set status based on utilization percentage

### Utilization Calculation
- **Utilization**: Current usage (positions, orders, etc.)
- **Remaining**: Limit - Utilization
- **Warning**: Utilization > WarningLevel
- **Breach**: Utilization > BreachLevel

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.2
- **FIX Version:** 5.0 with LME extensions
