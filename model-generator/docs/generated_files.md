# Generated Files

## src/model/engine/orderbook.py

**Description**: Core order book module containing domain models and order book logic for options trading.

**Contents**:
- Enums: Side, OrderType, TimeInForce, OrderStatus, ExecType, Action, Session, BookType
- Order: Main order domain model with all required normalized fields
- ExecutedOrderSummary: Order cache entry for completed orders
- BookSide: Individual bid/ask side with price-time priority
- NormalBook: Active trading book with bid and ask sides
- StopParkingBook: Stop orders waiting for trigger
- InstrumentOrderBook: Full book for one instrument
- OrderBookStore: Store for multiple instrument books

---

## src/model/engine/matching_engine.py

**Description**: Core matching engine module for option orders.

**Contents**:
- InstrumentType: Enum for OPTION/FUTURE instrument types
- Trade: Immutable execution record for matched trades
- TradeReversal: Record for reversing a trade
- TradeCorrection: Record for correcting a trade
- MatchingEngine: Core matching logic with:
  - Session validation
  - Order acceptance validation
  - Price validation hook
  - Price-time priority matching
  - Partial fill support
  - Resting order removal on full fill
  - Limit order residual placement
  - IOC order cancellation
  - Trade generation
  - Reversal/Correction support

---

## tests/test_orderbook.py

**Description**: Unit tests for order book module.

**Coverage**:
- BookSide: add, remove, price-time priority, FIFO for same price
- NormalBook: side management
- InstrumentOrderBook: add, remove, replace, activate stop, best bid/ask queries
- OrderBookStore: JSON loading
- Order: from_dict parsing, to_dict roundtrip

---

## tests/test_matching_engine.py

**Description**: Unit tests for matching engine module.

**Coverage**:
- Rejection: outside session, unsupported order type, invalid quantity, missing premium, price validation failure
- Buy crossing: crosses best ask correctly
- Sell crossing: crosses best bid correctly
- Non-crossing: limit rests on book, IOC cancelled
- Partial fill: against one resting order
- Full fill: against one resting order
- Multiple fills: one incoming fills multiple resting
- Execution price: equals resting order price
- FIFO: same price priority preserved
- Immutability: trade records immutable, reversal/correction records
