"""
LME Constants for Digital Twin Test Case Generator.

This module defines constants aligned with LME (London Metal Exchange) specifications.
Values sourced from doc/requirements/openspec/reference/symbols.md and FIX Specification v1.9.1.

Last Synced: 2026-03-08
Source: LME Contract Specifications (lme.com), FIX Spec §3.1
"""

from decimal import Decimal
from typing import Dict, Any

# LME Metal Symbols
# Each symbol includes lot_size (tonnes), tick_size (USD/tonne), and price_unit
LME_SYMBOLS: Dict[str, Dict[str, Any]] = {
    "CU": {
        "name": "Copper A",
        "contract_code": "CA",
        "lot_size": 25,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("7000.00"),
        "max_price": Decimal("12000.00"),
    },
    "AL": {
        "name": "Primary Aluminium",
        "contract_code": "AH",
        "lot_size": 25,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("2000.00"),
        "max_price": Decimal("3500.00"),
    },
    "NI": {
        "name": "Nickel",
        "contract_code": "NI",
        "lot_size": 6,
        "tick_size": Decimal("5.00"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("15000.00"),
        "max_price": Decimal("25000.00"),
    },
    "ZN": {
        "name": "Zinc (Special High Grade)",
        "contract_code": "ZS",
        "lot_size": 25,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("2500.00"),
        "max_price": Decimal("4000.00"),
    },
    "PB": {
        "name": "Lead (Refined Pig Lead)",
        "contract_code": "PB",
        "lot_size": 25,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("1800.00"),
        "max_price": Decimal("2800.00"),
    },
    "SN": {
        "name": "Tin (Refined)",
        "contract_code": "SN",
        "lot_size": 5,
        "tick_size": Decimal("5.00"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("25000.00"),
        "max_price": Decimal("40000.00"),
    },
    "AA": {
        "name": "Aluminium Alloy",
        "contract_code": "AADF",
        "lot_size": 25,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("1800.00"),
        "max_price": Decimal("3000.00"),
    },
    "HN": {
        "name": "Steel HRC (Ferrous)",
        "contract_code": "HN",
        "lot_size": 10,
        "tick_size": Decimal("0.50"),
        "price_unit": "USD/tonne",
        "min_price": Decimal("500.00"),
        "max_price": Decimal("900.00"),
    },
}

# Order validation limits (per FIX Spec §3.3)
MAX_ORDER_QTY = 9_999  # lots
MAX_ORDER_PRICE = Decimal("9_999_999")
MIN_ORDER_QTY = 1  # lot

# Session parameters (per FIX Spec §1.4)
HEARTBEAT_INTERVAL_SECONDS = 30
SESSION_TIMEOUT_INTERVALS = 3  # heartbeat intervals
SESSION_TIMEOUT_SECONDS = HEARTBEAT_INTERVAL_SECONDS * SESSION_TIMEOUT_INTERVALS  # 90 seconds

# Clearable currencies (per Matching Rules §9)
CLEARABLE_CURRENCIES = ["USD", "JPY", "GBP", "EUR"]

# FIX message type values
MSG_TYPE_NEW_ORDER_SINGLE = "D"
MSG_TYPE_ORDER_CANCEL_REQUEST = "F"
MSG_TYPE_ORDER_CANCEL_REPLACE = "G"
MSG_TYPE_ORDER_CANCEL_REJECT = "9"
MSG_TYPE_EXECUTION_REPORT = "8"
MSG_TYPE_NEW_ORDER_CROSS = "s"
MSG_TYPE_ORDER_MASS_CANCEL_REQUEST = "q"
MSG_TYPE_ORDER_MASS_CANCEL_REPORT = "r"
MSG_TYPE_LOGON = "A"
MSG_TYPE_LOGOUT = "5"
MSG_TYPE_HEARTBEAT = "0"
MSG_TYPE_TEST_REQUEST = "1"
MSG_TYPE_RESEND_REQUEST = "2"
MSG_TYPE_SEQUENCE_RESET = "4"
MSG_TYPE_REJECT = "3"
MSG_TYPE_BUSINESS_MESSAGE_REJECT = "j"
MSG_TYPE_NEWS = "B"
MSG_TYPE_QUOTE_REQUEST = "R"
MSG_TYPE_SECURITY_DEFINITION_REQUEST = "c"
MSG_TYPE_SECURITY_DEFINITION = "d"

# FIX tag numbers (common)
TAG_BEGIN_STRING = 8
TAG_BODY_LENGTH = 9
TAG_MSG_TYPE = 35
TAG_SENDER_COMP_ID = 49
TAG_TARGET_COMP_ID = 56
TAG_MSG_SEQ_NUM = 34
TAG_SENDING_TIME = 52
TAG_CHECKSUM = 10
TAG_CL_ORD_ID = 11
TAG_ORIG_CL_ORD_ID = 41
TAG_ORDER_ID = 37
TAG_SYMBOL = 55
TAG_SECURITY_ID = 48
TAG_SECURITY_ID_SOURCE = 22
TAG_SIDE = 54
TAG_ORDER_QTY = 38
TAG_ORD_TYPE = 40
TAG_PRICE = 44
TAG_STOP_PX = 99
TAG_TIME_IN_FORCE = 59
TAG_DISPLAY_QTY = 1138
TAG_EXPIRE_DATE = 432
TAG_EXEC_TYPE = 150
TAG_ORD_STATUS = 39
TAG_ORD_REJ_REASON = 103
TAG_CXL_REJ_REASON = 102
TAG_TEXT = 58
TAG_SESSION_STATUS = 1409
TAG_MASS_CANCEL_REQUEST_TYPE = 530
TAG_MASS_CANCEL_RESPONSE = 531
TAG_MASS_CANCEL_REJECT_REASON = 532
TAG_TOTAL_AFFECTED_ORDERS = 533
TAG_CROSS_ID = 548
TAG_CROSS_TYPE = 549
TAG_CROSS_PRIORITIZATION = 550
TAG_BUSINESS_REJECT_REASON = 380
TAG_SESSION_REJECT_REASON = 373
