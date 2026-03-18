# step_orderbook_module.md

## Goal

Generate a Python `orderbook` module based on the provided `orderbook.json` snapshot.

The module should model the **core order book state and state transitions**, not all exchange integration details.
Focus on a clean in-memory domain model that can be used later by a matching engine and by tests.

The JSON snapshot shows that the order book state is organized under:

- `BOOKSHELF_STATE`
- per `symbol` / `SecurityID`
- with:
  - `normal_book`
    - `BUY`
    - `SELL`
  - `STOP_PARKING`
  - `order_cache`
  - `done_for_day`
  - `trading_prices`
  - `session_info`

This module should support the first three as the main scope.

---

## What to build

Create a Python module that provides:

- domain models / dataclasses / pydantic models for:
  - `Order`
  - `ExecutedOrderSummary` (for order_cache)
  - `BookSide`
  - `NormalBook`
  - `StopParkingBook`
  - `InstrumentOrderBook`
  - `OrderBookStore`

- behavior for:
  - loading an instrument order book from the snapshot JSON structure
  - inserting a new order
  - amending/replacing an existing order
  - canceling/removing an order
  - activating a stop order from `STOP_PARKING` into `normal_book`
  - querying best bid / best ask
  - querying price levels
  - retrieving an order by id
  - exporting current state back to JSON-friendly dict form

Do **not** implement the full exchange gateway, FIX parsing, member validation, or compliance validation.

---

## Domain interpretation from snapshot

### 1. Main containers

For each symbol, the book contains:

- `normal_book`
  - active tradable orders
  - split into `BUY` and `SELL`
- `STOP_PARKING`
  - stop orders waiting for trigger
  - contains both `BUY` and `SELL`
- `order_cache`
  - trade/completion summaries for already executed orders

### 2. Order kinds visible in snapshot

Support at least:

- `LIMIT`
- `STOPLIMIT`

You may define an enum for order types.

### 3. Sides

Support:

- `BUY`
- `SELL`

### 4. Sessions

The snapshot shows at least:

- `PRE-OPEN`
- `OPEN`

Treat session as a stored attribute, not a validation rule.
Do not implement session-based trading restrictions yet.

### 5. Order lifecycle hints from snapshot

The snapshot contains examples of:

- `Action = NEW`
- `Action = AMEND`
- `ExecType = NEW`
- `ExecType = REPLACED`
- `ExecType = TRADE`
- `ExecType = ACTIVATED`
- `OrdStatus = NEW`
- `OrdStatus = PARTIALLY_FILLED`

The module should therefore support a lifecycle where an order can be:

- created
- amended/replaced
- partially filled
- fully filled / moved to cache
- stop-activated from parking into active book

Do not build a full execution engine here, but the state model must make these transitions possible.

---

## Required field design

The raw snapshot contains many protocol-specific and customer-specific fields.
For core order book logic, normalize and retain only the essential fields below as first-class fields.

### Required normalized fields for `Order`

- `internal_id`: from `ID`
- `order_id`: from `OrderID`
- `symbol`: from `Symbol` or `SecurityID`
- `security_id`
- `side`
- `order_type`
- `price`
- `quantity`: from `OrderQty`
- `cum_qty`: from `CumQty`
- `leaves_qty`: from `LeavesQty`
- `time_priority`: from `#TimePriority`
- `tif`: from `TIF`
- `status`: from `OrdStatus`
- `exec_type`: from `ExecType`
- `action`: from `Action`
- `session`
- `book`
- `user`
- `broker_client_id`: from `BrokerClientID`
- `stop_price`: from `StopPx` when present
- `trigger_type`: from `TriggerType` when present
- `trigger_price_type`: from `TriggerPriceType` when present
- `activated`: normalized from `Activated` when present
- `original_id`: from `OriginalID`
- `previous_id`: from `PreviousID`
- `orig_time_priority`: from `#OrigTimePriority`
- `raw`: dict of all remaining untouched fields

### Required normalized fields for `ExecutedOrderSummary`

- `order_id`
- `user`
- `side`
- `symbol`
- `broker_client_id`
- `order_qty`
- `cum_qty`
- `exec_type`
- `last_trade`
- `number_of_trades`
- `book`

### Type normalization rules

Normalize numeric-like fields into proper Python types:

- `price` -> `Decimal | None`
- `stop_price` -> `Decimal | None`
- `quantity`, `cum_qty`, `leaves_qty`, `order_qty`, `number_of_trades` -> `int | None`
- `time_priority`, `orig_time_priority` -> `int | None`

Normalize booleans:

- `"TRUE"` -> `True`
- `"FALSE"` -> `False`
- `"UNKNOWN"` or missing -> `None`

Keep timestamps as strings for now unless a separate utility parser is created.

Use `Decimal` instead of float for prices.

---

## Sorting and book behavior

### Active book sorting rules

For `normal_book`:

- BUY side priority:
  1. higher price first
  2. lower `time_priority` first if using ascending priority semantics, OR earlier timestamp first if your design stores it that way
- SELL side priority:
  1. lower price first
  2. then time priority

You must make the priority rule explicit in code and docstrings.

Assume `#TimePriority` represents exchange-assigned time precedence.
Do not infer priority from `Time` when `#TimePriority` is available.

### Stop parking behavior

For `STOP_PARKING`:

- orders are stored separately from active tradable orders
- they are not part of best bid / best ask
- they can be activated later and moved into `normal_book`
- when activated, the order should appear on the correct side of `normal_book`

Do not implement real market-trigger evaluation yet.
Provide a method like:

- `activate_stop_order(order_id: str)`

which moves the order manually from parking to active book and updates:
- `book`
- `activated`
- `exec_type` if needed

---

## Identity and replace/amend behavior

The snapshot suggests there are multiple identifiers:

- `ID`
- `OrderID`
- `OriginalID`
- `PreviousID`

Use the following design:

- primary runtime key for locating an order in the book: `internal_id` (`ID`)
- business order id: `order_id` (`OrderID`)
- replacement chain fields:
  - `original_id`
  - `previous_id`

When amending/replacing an order:

- locate the current order
- remove the prior version from the active container
- insert the new version
- preserve replacement lineage fields
- allow time priority to change only if the incoming snapshot says so

Expose a method like:

- `replace_order(order: Order)`

Do not guess exchange rules beyond the snapshot.
Just model the state transition cleanly.

---

## order_cache behavior

`order_cache` is not an active order book side.
Treat it as a list or dictionary of executed/completed order summaries.

Provide methods like:

- `add_execution_summary(summary: ExecutedOrderSummary)`
- `get_execution_summary(order_id: str)`

This cache is read-only from the order book perspective except for append/update operations.

---

## JSON loading requirements

Implement a loader that can parse the snapshot structure:

- root -> `BOOKSHELF_STATE`
- each symbol key -> one `InstrumentOrderBook`

The loader should:

1. iterate all instruments
2. parse `normal_book.BUY`
3. parse `normal_book.SELL`
4. parse `normal_book.STOP_PARKING` if present inside `normal_book`
   or top-level `STOP_PARKING` if future snapshots differ
5. parse `order_cache`
6. ignore unsupported containers safely

The implementation must be defensive:
- missing fields should not crash the loader
- unknown extra fields must be preserved in `raw`

---

## Recommended module structure

Generate something close to:

```text
src/
  orderbook/
    __init__.py
    models.py
    side.py
    instrument_book.py
    store.py
    loader.py
    enums.py