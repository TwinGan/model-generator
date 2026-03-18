# Task: Generate Matching Engine Module

## Goal
Generate the `matching engine` module for the simplified options matching model.

## Read First
Before coding, read:
- `AGENTS.md`
- `inputs/matching_rules/lme_matching_rules.md`
- `docs/generated_files.md`
- python files recorded in `docs/generated_files.md`
- especially the generated `orderbook` module from step 1

## Scope
Implement only the core matching engine module for **Option** orders.

Expected responsibilities:
- accept incoming option orders into the matching flow
- validate session window before matching
- validate incoming order fields before matching
- call a pluggable price validation hook before matching
- reuse the existing per-instrument orderbook module
- match only against opposite-side resting liquidity of the same option instrument
- apply price priority then time priority
- support partial fills
- execute trades at the resting order premium
- remove fully filled resting orders from the book
- place unfilled `LIMIT` remainder onto the book
- cancel unfilled `IOC` remainder immediately
- generate one immutable execution/trade record per matched interaction
- support post-trade fix semantics through linked `REVERSAL` / `CORRECTION` record models only
- keep matching behavior deterministic

## Non-Goals
Do not implement:
- futures logic
- multi-leg / carry / spread / strategy matching
- member-level validation
- user-level validation
- account-level validation
- clearing workflows
- give-up / UNA / OTC bring-on / transfer / financing flows
- persistence
- FIX parsing
- APIs
- market data dissemination
- distributed matching
- recovery / replay architecture
- UI behavior
- database schema
- approval workflows for reversals/corrections
- automatic reversal/correction generation inside the matching loop

## Read/Reuse Requirements
- Reuse the generated `orderbook` module from step 1
- Reuse existing domain definitions if they already exist
- Do not duplicate order or trade definitions if they are already present
- Extend the project incrementally instead of redesigning previously generated modules
- If step 1 interfaces are insufficient, make only the smallest necessary change

## Matching Rules That Must Be Preserved
- support **Option** instruments only
- reject unsupported instrument types
- reject orders outside configured trading session
- support only `LIMIT` and `IOC`
- reject invalid order input before matching
- use exact option instrument identity equality
- match only opposite sides
- match only active resting orders with remaining quantity > 0
- bids are prioritized from highest premium to lowest premium
- asks are prioritized from lowest premium to highest premium
- within the same premium level, earlier order has priority
- if exact timestamp ties are possible, use a stable secondary ordering key
- incoming buy crosses when best ask premium `<=` incoming buy premium
- incoming sell crosses when best bid premium `>=` incoming sell premium
- execution premium is always the resting order premium
- partial fills are allowed
- one matched pair interaction produces exactly one execution record
- executed trades must be immutable
- post-trade fixes must be represented by new linked records, not by mutating original trades
- partial reversal is not allowed

## Suggested Internal Responsibilities
Keep the module small and explicit. Prefer separate internal functions/methods for:
- session check
- incoming order acceptance validation
- price validation hook call
- match eligibility check
- crossing check
- core matching loop
- residual handling
- trade generation
- reversal/correction semantic support

## Output
Create or update only:
- `src/model/engine/matching_engine.py`
- related small helper files if truly necessary
- `tests/test_matching_engine.py`
- add all generated code file *address* and *desciption* to `docs/generated_files.md`

## Constraints
- Keep implementation simple and explicit
- Prefer dataclasses and typed methods
- Keep business logic deterministic
- Keep the matching loop independent from infrastructure concerns
- Do not hardcode price validation logic inside the matching loop
- Do not mutate executed trade records in place
- Do not introduce speculative abstractions or future workflows not required by this step

## Minimum Behavioral Requirements
The engine must reject an incoming order if any of the following is true:
- instrument is missing or not recognized
- instrument type is not Option
- side is missing or invalid
- quantity is missing or `<= 0`
- order type is missing or unsupported
- premium is missing for a priced order type
- order arrives outside session
- price validation fails

The engine must:
- maintain an independent book per option instrument
- continue matching across multiple resting orders until the incoming order is filled or no eligible liquidity remains
- mark resulting order states consistently using at least:
  - `NEW`
  - `REJECTED`
  - `ACTIVE`
  - `PARTIALLY_FILLED`
  - `FILLED`
  - `CANCELLED`

## Acceptance Criteria
- accepts Option orders only
- rejects futures and all unsupported instruments
- rejects invalid orders before matching
- rejects orders outside session
- invokes price validation before matching/book entry
- reuses the generated orderbook module instead of re-implementing the book
- matches only opposite sides of the same option instrument
- applies price priority then time priority
- supports partial fills
- uses resting-order-premium execution
- removes fully filled resting orders from the book
- leaves unfilled `LIMIT` remainder resting on book
- cancels unfilled `IOC` remainder
- generates one execution record per actual matched interaction
- keeps executed trades immutable
- models `REVERSAL` / `CORRECTION` as linked new records only
- does not allow partial reversal
- excludes all out-of-scope workflows from the core loop
- tests cover core behaviors and deterministic outcomes

## Minimum Test Coverage
Tests should include at least:
- reject order outside session
- reject unsupported instrument type
- reject unsupported order type
- reject invalid quantity
- reject missing premium for priced order
- reject failed price validation
- buy order crosses best ask correctly
- sell order crosses best bid correctly
- non-crossing `LIMIT` order rests on book
- non-crossing `IOC` order is cancelled
- partial fill against one resting order
- full fill against one resting order
- one incoming order fills against multiple resting orders
- execution premium equals resting order premium
- same-price FIFO priority is preserved through the orderbook
- immutable trade record behavior
- reversal record can reference original trade
- correction record can reference original trade
- partial reversal is rejected or unsupported explicitly