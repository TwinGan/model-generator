Use the attached spec as the single source of truth.

Generate only the core matching engine logic for Option orders.
Do not implement futures logic.
Do not invent additional business workflows.
Do not add member validation, clearing logic, or multi-leg behavior.
If something is not explicitly required by the spec, keep the implementation minimal and deterministic.
Prefer readability and testability over abstraction.

## 1. Goal

Build a simplified electronic matching engine for LME-style option trading.

This engine must support only the core matching algorithm for:
- Options

The engine must focus only on:
- order acceptance into the matching flow
- price validation hook
- order matching
- partial fill handling
- book insertion of remaining quantity
- trade generation
- immutable executed trades
- post-trade fix handling through reversal/correction semantics

This spec intentionally excludes all non-core workflows.

---

## 2. In Scope

The engine must implement:

1. Single-leg outright matching for Options
2. Opposite-side matching only
3. Price-priority then time-priority matching
4. Partial fills
5. Resting-order-price execution
6. Limit orders
7. IOC orders
8. Independent order books per option instrument
9. Price validation as a pluggable rule
10. Post-trade fixes through reversal/correction records only

---

## 3. Out of Scope

The engine must NOT implement:

- futures trading
- member-level validation
- user-level validation
- account-level validation
- clearing workflows
- give-up
- UNA
- OTC bring-on
- transfer
- financing
- carry / multi-leg matching
- spread matching
- collateral checks
- margin checks
- position limits
- surveillance logic
- regulatory reporting
- persistence model
- API design
- UI behavior
- database schema
- distributed matching
- recovery / replay architecture
- market data dissemination format

If any of these are needed later, they must be added in separate specs.

---

## 4. Business Intent

The purpose of this engine is to provide a minimal executable core that can:
- accept eligible option orders,
- determine whether they can trade,
- match them deterministically,
- generate executions,
- leave residual resting liquidity on book when appropriate.

This engine is a simplified model, not a full reproduction of the full LME production ecosystem.

---

## 5. Instrument Scope

Supported instrument classes:
- Option

Unsupported instrument classes:
- Future
- carry
- multi-leg instruments
- strategy instruments
- transfer-only trade flows
- financing-only trade flows

For this version, only single-leg outright option instruments are matchable.

---

## 6. Matching Session Rules

### 6.1 Session Window

The engine must only allow real-time electronic matching during the configured electronic trading window.

The default implementation may use a single configured session window:
- `session_open`
- `session_close`

### 6.2 Behavior Outside Session

If a new order arrives outside the matching session window, the engine must reject it.

No queued-for-open behavior is required in this version.

---

## 7. Pre-Matching Acceptance Rules

An incoming order must pass all acceptance checks before entering the matching flow.

### 7.1 Required Checks

The engine must reject the order if any of the following is true:
- instrument is missing or not recognized
- instrument type is not Option
- side is missing or invalid
- quantity is missing or `<= 0`
- order type is missing or unsupported
- premium is missing for a priced order type
- order arrives outside session
- price validation fails

### 7.2 Supported Order Types

This version supports only:
- `LIMIT`
- `IOC`

Unsupported order types must be rejected.

### 7.3 Price Validation Hook

The engine must call a pluggable validation rule before matching:
- `is_price_valid(order, market_context) -> bool`

If price validation returns false, the order must be rejected.

This validation logic must be externalized and must not be hardcoded into the matching loop.

---

## 8. Match Eligibility Rules

An incoming order may match only against resting orders that satisfy all of the following:

1. opposite side
2. same option instrument identity
3. active state
4. remaining quantity greater than zero

### 8.1 Instrument Identity

Two orders are matchable only if they refer to the same option contract.

“Same option contract” must mean exact equality of the configured option instrument identity.

This spec does not prescribe the exact instrument key structure, but the identity should normally distinguish at least:
- underlying product
- expiry
- strike
- call/put

If the implementation has a canonical instrument identifier, exact identifier equality is sufficient.

---

## 9. Book Model

### 9.1 Per-Instrument Book

The engine must maintain an independent book per option instrument.

Each book must contain:
- bid side
- ask side

### 9.2 Price Ordering

For each option instrument:
- bids are ordered from highest premium to lowest premium
- asks are ordered from lowest premium to highest premium

### 9.3 Time Ordering

Within the same premium level, orders are ordered by arrival time:
- earlier order has higher priority than later order

This means the engine must use:
- price priority
- then time priority

---

## 10. Crossing Rules

### 10.1 Buy Order Cross Condition

An incoming buy order is marketable if:
- best resting ask premium `<= incoming buy premium`

### 10.2 Sell Order Cross Condition

An incoming sell order is marketable if:
- best resting bid premium `>= incoming sell premium`

If the cross condition is not satisfied, the order is non-marketable.

---

## 11. Core Matching Algorithm

When an order is accepted, the engine must run the following logic.

### 11.1 Matching Loop

Given an accepted incoming order:

1. Locate the opposite-side best resting order for the same option instrument.
2. Check whether the incoming order crosses that resting order.
3. If not crossing:
   - stop matching
   - process remaining quantity according to order type
4. If crossing:
   - execute against the highest-priority resting order
   - matched quantity = minimum of incoming remaining quantity and resting remaining quantity
   - trade premium = resting order premium
   - reduce both remaining quantities
   - if resting order remaining quantity becomes zero, remove it from book
   - if incoming order remaining quantity becomes zero, stop
   - otherwise continue matching against the next eligible resting order

### 11.2 Execution Price Rule

The trade premium must always be the resting order premium.

Examples:
- incoming buy matches resting ask -> execution premium = resting ask premium
- incoming sell matches resting bid -> execution premium = resting bid premium

### 11.3 Partial Fill Rule

Partial fills are allowed.

If the incoming order is larger than the current best resting order, it must continue matching against further eligible resting liquidity until:
- the incoming order is fully filled, or
- no further eligible liquidity remains

---

## 12. Residual Handling

### 12.1 Limit Order Residual

If a `LIMIT` order is not fully filled:
- the remaining quantity must rest on the book
- it must be inserted using standard price-time priority

### 12.2 IOC Residual

If an `IOC` order is not fully filled:
- any unfilled remainder must be cancelled immediately
- the remainder must not be placed on the book

---

## 13. Order States

The engine must use at least the following order states:

- `NEW`
- `REJECTED`
- `ACTIVE`
- `PARTIALLY_FILLED`
- `FILLED`
- `CANCELLED`

### 13.1 State Semantics

- `NEW`: received but not yet fully processed
- `REJECTED`: failed acceptance or validation
- `ACTIVE`: resting on book with remaining quantity
- `PARTIALLY_FILLED`: at least one execution occurred, remaining quantity still exists
- `FILLED`: no remaining quantity
- `CANCELLED`: explicitly cancelled or IOC residual removed

### 13.2 State Transitions

Allowed minimum transitions:
- `NEW -> REJECTED`
- `NEW -> ACTIVE`
- `NEW -> FILLED`
- `NEW -> PARTIALLY_FILLED`
- `ACTIVE -> PARTIALLY_FILLED`
- `ACTIVE -> FILLED`
- `PARTIALLY_FILLED -> FILLED`
- `ACTIVE -> CANCELLED`
- `PARTIALLY_FILLED -> CANCELLED`

---

## 14. Trade Generation

Each successful match must generate one execution record.

The execution record must represent:
- the option instrument traded
- the execution premium
- the execution quantity
- the aggressing order
- the resting order
- the execution timestamp

This spec does not prescribe the exact data schema of the trade record.

The engine must generate one execution event per matched pair interaction.

If one incoming order matches three resting orders, three execution records must be generated.

---

## 15. Immutability of Executed Trades

Executed trades must be immutable.

The engine must not modify an already executed trade in place.

If a previously executed result needs to be fixed, the engine must represent that fix through a new post-trade record.

Supported fix semantics:
- `REVERSAL`
- `CORRECTION`

This spec does not require implementation of approval workflows.

---

## 16. Reversal and Correction Rules

### 16.1 Reversal

A reversal is a new record that negates a previously executed trade.

Rules:
- a reversal must reference the original executed trade
- a reversal must economically offset the original trade
- partial reversal is not allowed in this version

### 16.2 Correction

A correction is a new record that supersedes or amends the economic meaning of a previous executed trade through explicit linked records.

Rules:
- a correction must reference the original executed trade
- corrections must not mutate the original trade record directly

### 16.3 Core Engine Boundary

The matching loop itself does not need to generate reversals or corrections automatically.

It only needs to support the semantic rule that:
- executed trades are immutable
- fixes are represented by linked new records, not in-place mutation

---

## 17. Option-Specific Semantics

This engine supports options only.

The priced field represents:
- option premium

The matching algorithm does not distinguish between call and put in the matching loop itself.
Call/put differences are part of instrument identity, not part of the matching procedure.

The matching algorithm does not distinguish between different strikes or expiries in the matching loop itself.
Those differences are part of instrument identity, not part of the matching procedure.

---

## 18. Determinism Requirements

The engine must be deterministic.

Given the same:
- starting book state
- incoming order sequence
- timestamps / sequence ordering
- validation results

the engine must always produce the same:
- fills
- execution premiums
- trade quantities
- final book state
- order states

If two orders arrive at the same premium, the earlier accepted order must always have priority.

If exact timestamp ties are possible, the implementation must use a stable secondary ordering key such as sequence number.

---

## 19. Non-Goals for the Matching Loop

The matching loop must not contain logic for:
- account permissions
- trader permissions
- give-up routing
- transfer logic
- financing categorization
- carry leg orchestration
- approval workflows
- manual intervention flows
- reporting deadlines
- downstream clearing semantics

These concerns must be implemented outside the core matching algorithm.

---

## 20. Explicit Assumptions

The following are intentional modeling assumptions for this simplified engine:

1. The engine uses price priority then time priority.
2. The execution premium is always the resting order premium.
3. Only single-leg outright options are supported.
4. Only `LIMIT` and `IOC` order types are supported.
5. Orders outside the trading session are rejected.
6. Price validation is delegated to an external rule hook.
7. Executed trades are immutable.
8. Partial reversal is not allowed.
9. The engine does not support futures, carry, spread, or other multi-leg matching.
10. The engine maintains one independent bid/ask book per option instrument.

These assumptions are part of this simplified design and must be preserved unless a later spec overrides them.

---

## 21. Acceptance Criteria

A generated implementation is acceptable only if it satisfies all of the following:

1. accepts Option orders only
2. rejects futures and all unsupported instruments
3. rejects invalid orders before matching
4. rejects orders outside session
5. invokes price validation before book entry
6. matches only opposite sides of the same option instrument
7. applies price priority then time priority
8. supports partial fills
9. uses resting-order-premium execution
10. leaves unfilled limit remainder resting on book
11. cancels unfilled IOC remainder
12. generates one execution record per actual matched interaction
13. treats executed trades as immutable
14. does not allow partial reversal
15. excludes all out-of-scope workflows from the core loop

---

## 22. Suggested Implementation Style

The generated code should keep the core matching logic small and explicit.

Preferred internal separation:
- session check
- acceptance validation
- price validation hook
- match eligibility logic
- matching loop
- residual handling
- trade generation
- reversal/correction semantic support

The matching loop should not depend on infrastructure concerns.

---

## 23. Final Summary

Build a deterministic, simplified, single-leg, price-time-priority matching engine for Option orders only.

The engine must:
- validate first,
- match against opposite-side resting liquidity of the same option instrument,
- execute at resting premium,
- allow partial fills,
- book residual limit quantity,
- cancel IOC residual,
- keep executed trades immutable,
- represent fixes only through reversal/correction semantics.

Do not implement futures, member/user/account/clearing/OTC/give-up/transfer/financing/carry workflows in this version.