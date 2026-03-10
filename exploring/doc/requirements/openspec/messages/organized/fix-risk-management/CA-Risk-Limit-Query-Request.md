# Risk Limit Query Request

**Domain:** Risk Management  
**Message Type:** CA  
**Category:** Application  
**Direction:** Client→Gateway  

## Message Overview

Risk Limit Query Request message for LME Risk Management Gateway. Used to query risk limits for a party or member.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CA`
- **Message Name:** Risk Limit Query Request
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.1

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Risk Limit Query Request (CA)
Gateway → Client: Risk Limit Query Response (CC)
```

## Fields Reference

### Required Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 8 | BeginString | String | Required | FIX protocol version |
| 9 | BodyLength | Length | Required | Message body length |
| 10 | CheckSum | String | Required | Message checksum |
| 35 | MsgType | String | Required | Message type = CA |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 1759 | RiskLimitRequestID | String | Required | Unique request ID |
| 1760 | RiskLimitRequestType | Int | Required | Type of risk limit request |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 453 | NoPartyIDs | NumInGroup | Optional | Party identification group |
| 452 | PartyRole | Int | Conditional | Party role (1=Clearing Firm, 7=Trading Firm) |
| 802 | NoPartySubIDs | NumInGroup | Optional | Party sub-IDs group |
| 48 | SecurityID | String | Optional | Filter by symbol |
| 55 | Symbol | String | Optional | Filter by symbol |
| 1756 | RiskLimitLevel | Int | Optional | Level of limit detail |
| 58 | Text | String | Optional | Free-form text |

## RiskLimitRequestType Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | ALL_LIMITS | Query all limits | Risk Spec §4.1 |
| 2 | LIMITS_FOR_PARTY | Query limits for specific party | Risk Spec §4.1 |
| 3 | LIMITS_FOR_SYMBOL | Query limits for specific symbol | Risk Spec §4.1 |
| 4 | LIMITS_FOR_PARTY_AND_SYMBOL | Query limits for party and symbol | Risk Spec §4.1 |

## RiskLimitLevel Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | SUMMARY | Summary level limits only | Risk Spec §4.1 |
| 2 | DETAILED | Detailed limits breakdown | Risk Spec §4.1 |

## Party Role Codes
| Code | Name | Description |
|------|------|-------------|
| 1 | ClearingFirm | Clearing member firm |
| 7 | TradingFirm | Trading member firm |
| 12 | Trader | Individual trader |
| 36 | PositionAccount | Position account |

## Message Example (Tabby CSV Format)

### Example: Query All Limits for Party
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,RiskLimitRequestType,NoPartyIDs,PartyID,PartyRole
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,REQ001,2,1,MEMBER001,1
```

### Example: Query Limits for Symbol
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitRequestID,RiskLimitRequestType,Symbol
FIXT.1.1,,,1,,CLIENT1,20240101-12:00:00.000,LME,REQ002,3,CA
```

## Processing Rules

### Validation Requirements
- Valid session must be established
- User must have risk management permissions
- RiskLimitRequestID must be unique

### Response Generation
1. Query risk limits from risk management system
2. Generate Risk Limit Query Response (CC)
3. Include all matching limits based on request criteria

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.1
- **FIX Version:** 5.0 with LME extensions
