# Risk Limit Update Report

**Domain:** Risk Management  
**Message Type:** CD  
**Category:** Application  
**Direction:** Gateway→Client  

## Message Overview

Risk Limit Update Report message from LME Risk Management Gateway. Sent in response to Risk Limit Update Request (CB) to confirm or reject limit changes.

## Message Specification

### FIX Protocol Details
- **Message Type:** `CD`
- **Message Name:** Risk Limit Update Report
- **FIX Version:** 5.0 (with LME extensions)
- **Source:** Risk Spec §4.4

## Message Interaction Flow

### Success Scenario
```
Client → Gateway: Risk Limit Update Request (CB)
Gateway → Client: Risk Limit Update Report (CD) with status=ACCEPTED
```

### Rejection Scenario
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
| 35 | MsgType | String | Required | Message type = CD |
| 49 | SenderCompID | String | Required | Sender company ID |
| 56 | TargetCompID | String | Required | Target company ID |
| 34 | MsgSeqNum | SeqNum | Required | Message sequence number |
| 52 | SendingTime | UTCTimestamp | Required | Message sending time |
| 1757 | RiskLimitID | String | Required | Limit ID from request |
| 1758 | RiskLimitType | Int | Required | Type of limit |
| 1753 | RiskLimitAmount | Amt | Required | New limit amount (if accepted) |
| 1760 | RiskLimitUpdateStatus | Int | Required | Update status |

### Optional Fields
| Tag | Field Name | Data Type | Presence | Description |
|-----|-----------|-----------|----------|-------------|
| 1761 | RiskLimitUpdateRejectReason | Int | Conditional | Rejection reason code |
| 1755 | RiskLimitWarningLevel | Percentage | Optional | Warning threshold |
| 1754 | RiskLimitBreachLevel | Percentage | Optional | Breach threshold |
| 453 | NoPartyIDs | NumInGroup | Optional | Party identification |
| 58 | Text | String | Optional | Free-form text |
| 60 | TransactTime | UTCTimestamp | Optional | Transaction time |

## RiskLimitUpdateStatus Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | ACCEPTED | Update accepted and applied | Risk Spec §4.4 |
| 1 | REJECTED | Update rejected | Risk Spec §4.4 |
| 2 | PENDING | Update pending approval | Risk Spec §4.4 |

## RiskLimitUpdateRejectReason Values
| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | INVALID_LIMIT_ID | Limit ID not found | Risk Spec §4.4 |
| 2 | INVALID_LIMIT_TYPE | Invalid limit type | Risk Spec §4.4 |
| 3 | INVALID_AMOUNT | Invalid limit amount | Risk Spec §4.4 |
| 4 | INSUFFICIENT_PERMISSIONS | No permission to update | Risk Spec §4.4 |
| 5 | LIMIT_ALREADY_EXISTS | Limit already exists (for ADD) | Risk Spec §4.4 |
| 6 | LIMIT_IN_USE | Cannot modify/remove active limit | Risk Spec §4.4 |
| 7 | OTHER | See Text field | Risk Spec §4.4 |

## Message Example (Tabby CSV Format)

### Example: Successful Limit Update
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUpdateStatus
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,LIMIT001,1,1500000,0
```

### Example: Rejected Limit Update
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUpdateStatus,RiskLimitUpdateRejectReason,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,LIMIT002,1,2000000,1,4,Insufficient permissions to update limits
```

### Example: Pending Approval
```csv
BeginString,BodyLength,CheckSum,MsgSeqNum,MsgType,SenderCompID,SendingTime,TargetCompID,RiskLimitID,RiskLimitType,RiskLimitAmount,RiskLimitUpdateStatus,Text
FIXT.1.1,,,1,,LME,20240101-12:00:01.000,CLIENT1,LIMIT003,1,3000000,2,Large limit change requires supervisor approval
```

## Processing Rules

### Update Validation
1. Verify user has risk management permissions
2. Validate limit exists (for MODIFY/REMOVE)
3. Check amount is valid and within bounds
4. Verify no conflicts with existing limits

### Status Determination
- **ACCEPTED**: Update applied successfully
- **REJECTED**: Validation failed with reason code
- **PENDING**: Requires supervisor approval

### Rejection Handling
- Always include RiskLimitUpdateRejectReason
- Include Text with additional details
- Original limit unchanged

## References

- **Source:** Risk Management Gateway FIX Specification v1.8 §4.4
- **FIX Version:** 5.0 with LME extensions
