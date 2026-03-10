# LME Error Codes Reference

**Source**: FIX Specification v1.9.1, Binary Specification v1.9.1
**Last Synced**: 2026-03-08

## Session Reject Reasons (Tag 373)

Used in Reject (35=3) message.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | INVALID_TAG_NUMBER | Tag number is invalid | FIX Spec §4.8.7 |
| 1 | REQUIRED_TAG_MISSING | Required tag is missing | FIX Spec §4.8.7 |
| 2 | TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE | Tag not defined for this message type | FIX Spec §4.8.7 |
| 3 | UNDEFINED_TAG | Tag is undefined | FIX Spec §4.8.7 |
| 4 | TAG_SPECIFIED_WITHOUT_A_VALUE | Tag specified without a value | FIX Spec §4.8.7 |
| 5 | VALUE_IS_INCORRECT | Value is incorrect for this tag | FIX Spec §4.8.7 |
| 6 | INCORRECT_DATA_FORMAT_FOR_VALUE | Incorrect data format for value | FIX Spec §4.8.7 |
| 7 | DECRYPTION_PROBLEM | Decryption problem | FIX Spec §4.8.7 |
| 8 | SIGNATURE_PROBLEM | Signature problem | FIX Spec §4.8.7 |
| 9 | COMP_ID_PROBLEM | CompID problem | FIX Spec §4.8.7 |
| 10 | SENDINGTIME_ACCURACY_PROBLEM | SendingTime accuracy problem | FIX Spec §4.8.7 |
| 11 | INVALID_MSGTYPE | Invalid MsgType | FIX Spec §4.8.7 |
| 12 | XML_VALIDATION_ERROR | XML validation error | FIX Spec §4.8.7 |
| 13 | TAG_APPEARS_MORE_THAN_ONCE | Tag appears more than once | FIX Spec §4.8.7 |
| 14 | TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER | Tag specified out of required order | FIX Spec §4.8.7 |
| 15 | REPEATING_GROUP_FIELDS_OUT_OF_ORDER | Repeating group fields out of order | FIX Spec §4.8.7 |
| 16 | INCORRECT_NUMING_GROUP_COUNT_FOR_REPEATING_GROUP | Incorrect numing group count for repeating group | FIX Spec §4.8.7 |
| 17 | NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER | Non-data value includes field delimiter | FIX Spec §4.8.7 |
| 18 | INVALID/UNSUPPORTED_CHARACTER_SET | Invalid/unsupported character set | FIX Spec §4.8.7 |

## Business Reject Reasons (Tag 380)

Used in Business Message Reject (35=j) message.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | OTHER | Other - see Text (58) for details | FIX Spec §4.9.1 |
| 1 | UNKNOWN_ID | Unknown ID | FIX Spec §4.9.1 |
| 2 | UNKNOWN_SECURITY | Unknown security | FIX Spec §4.9.1 |
| 3 | UNSUPPORTED_MESSAGE_TYPE | Unsupported message type | FIX Spec §4.9.1 |
| 4 | APPLICATION_NOT_AVAILABLE | Application not available | FIX Spec §4.9.1 |
| 5 | CONDITIONALLY_REQUIRED_FIELD_MISSING | Conditionally required field missing | FIX Spec §4.9.1 |
| 6 | NOT_AUTHORIZED | Not authorized | FIX Spec §4.9.1 |
| 7 | DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME | Deliver to firm not available at this time | FIX Spec §4.9.1 |
| 8 | THROTTLE_LIMIT_EXCEEDED | Throttle limit exceeded | FIX Spec §4.9.1 |
| 9 | THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECTED | Throttle limit exceeded, session will be disconnected | FIX Spec §4.9.1 |

## Order Cancel Reject Reasons (Tag 102)

Used in Order Cancel Reject (35=9) message.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | TOO_LATE_TO_CANCEL | Too late to cancel | FIX Spec §4.11.7 |
| 1 | UNKNOWN_ORDER | Unknown order | FIX Spec §4.11.7 |
| 2 | ALREADY_PENDING_CANCEL | Already pending cancel | FIX Spec §4.11.7 |
| 3 | ALREADY_CANCELLED | Already cancelled | FIX Spec §4.11.7 |
| 4 | ALREADY_FILLED | Already filled | FIX Spec §4.11.7 |
| 5 | ORIG_ORD_MOD_NOT_ALLOWED | Original order modification not allowed | FIX Spec §4.11.7 |
| 6 | DUPLICATE_ORDER | Duplicate order (ClOrdID already used) | FIX Spec §4.11.7 |
| 7 | OTHER | Other - see Text (58) | FIX Spec §4.11.7 |

## Order Reject Reasons (Tag 103)

Used in Execution Report (35=8) when order is rejected.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | BROKER | Broker option | FIX Spec §4.11.7 |
| 1 | UNKNOWN_SYMBOL | Unknown symbol | FIX Spec §4.11.7 |
| 2 | EXCHANGE_CLOSED | Exchange closed | FIX Spec §4.11.7 |
| 3 | ORDER_EXCEEDS_LIMIT | Order exceeds limit | FIX Spec §4.11.7 |
| 4 | TOO_LATE_TO_ENTER | Too late to enter | FIX Spec §4.11.7 |
| 5 | UNKNOWN_ORDER | Unknown order | FIX Spec §4.11.7 |
| 6 | DUPLICATE_ORDER | Duplicate order (ClOrdID already used) | FIX Spec §4.11.7 |
| 7 | DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER | Duplicate of a verbally communicated order | FIX Spec §4.11.7 |
| 8 | INVALID_PRICE | Invalid price | FIX Spec §4.11.7 |
| 9 | INVALID_QUANTITY | Invalid quantity | FIX Spec §4.11.7 |
| 10 | INVALID_ORDER_TYPE | Invalid order type | FIX Spec §4.11.7 |
| 11 | INVALID_SIDE | Invalid side | FIX Spec §4.11.7 |
| 12 | INVALID_TIF | Invalid TimeInForce | FIX Spec §4.11.7 |
| 13 | INVALID_PRICE_TOLERANCE | Invalid price tolerance | FIX Spec §4.11.7 |
| 14 | INVALID_STOP_PRICE | Invalid stop price | FIX Spec §4.11.7 |
| 15 | INVALID_VISIBILITY_INSTRUCTION | Invalid visibility instruction | FIX Spec §4.11.7 |
| 16 | INVALID_ORDER_FOR_ASK | Invalid order for ask | FIX Spec §4.11.7 |
| 17 | INVALID_ORDER_FOR_BID | Invalid order for bid | FIX Spec §4.11.7 |
| 18 | INVALID_ORDER_FOR_MARKET | Invalid order for market | FIX Spec §4.11.7 |
| 19 | EXCEEDS_MAXIMUM_QUANTITY | Exceeds maximum quantity | FIX Spec §4.11.7 |
| 20 | EXCEEDS_MAXIMUM_VALUE | Exceeds maximum value | FIX Spec §4.11.7 |
| 21 | INVALID_MINIMUM_QUANTITY | Invalid minimum quantity | FIX Spec §4.11.7 |
| 22 | INVALID_DISPLAY_QUANTITY | Invalid display quantity | FIX Spec §4.11.7 |
| 23 | INVALID_PARTICIPANT_TYPE | Invalid participant type | FIX Spec §4.11.7 |
| 24 | INVALID_TRIGGER_PRICE_TYPE | Invalid trigger price type | FIX Spec §4.11.7 |
| 25 | INSUFFICIENT_CREDIT | Insufficient credit | FIX Spec §4.11.7 |
| 26 | RISK_LIMIT_EXCEEDED | Risk limit exceeded | FIX Spec §4.11.7 |
| 99 | OTHER | Other - see Text (58) for details | FIX Spec §4.11.7 |

## Mass Cancel Reject Reasons (Tag 532)

Used in Order Mass Cancel Report (35=r) message.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 0 | MASS_CANCEL_NOT_SUPPORTED | Mass cancel not supported | FIX Spec §4.11.11 |
| 1 | INVALID_PRODUCT_COMPLEX | Invalid product complex | FIX Spec §4.11.11 |
| 2 | INVALID_INSTRUMENT | Invalid instrument | FIX Spec §4.11.11 |
| 3 | INVALID_SECURITY_ID | Invalid security ID | FIX Spec §4.11.11 |
| 4 | INVALID_UNDERLYING | Invalid underlying | FIX Spec §4.11.11 |
| 5 | NO_ORDERS_FOUND | No orders found to cancel | FIX Spec §4.11.11 |
| 6 | OTHER | Other - see Text (58) | FIX Spec §4.11.11 |

## Session Status Values (Tag 1409)

Used in Logout (35=5) message.

| Code | Name | Description | Source |
|------|------|-------------|--------|
| 1 | SESSION_ACTIVE | Session active | FIX Spec §4.8.6 |
| 2 | SESSION_LOGOUT_REQUESTED | Session logout requested | FIX Spec §4.8.6 |
| 3 | NEW_SESSION_PASSWORD_DOES_NOT_COMPLY_WITH_POLICY | New session password does not comply with policy | FIX Spec §4.8.6 |
| 4 | SESSION_LOGOUT_COMPLETE | Session logout complete | FIX Spec §4.8.6 |
| 5 | INVALID_USERNAME_OR_PASSWORD | Invalid username or password | FIX Spec §4.8.6 |
| 6 | ACCOUNT_LOCKED | Account locked | FIX Spec §4.8.6 |
| 7 | LOGONS_ARE_NOT_ALLOWED_AT_THIS_TIME | Logons are not allowed at this time | FIX Spec §4.8.6 |
| 8 | PASSWORD_EXPIRED | Password expired | FIX Spec §4.8.6 |
| 100 | PASSWORD_CHANGE_IS_REQUIRED | Password change is required | FIX Spec §4.8.6 |
| 101 | OTHER | Other | FIX Spec §4.8.6 |

## Cross-References

- FIX Messages: See [fix-messages.md](./fix-messages.md) (when available)
- Validation Rules: See [validation-rules.md](./validation-rules.md)
