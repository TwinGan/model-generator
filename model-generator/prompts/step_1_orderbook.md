# Task: Generate OrderBook Module

## Goal
Generate the `orderbook` module for the simplified options matching model.

## Read First
Before coding, read:
- `AGENTS.md`
- `inputs/reference_data/orderbook.json`
- `inputs/generated_files.md`
- python files recorded in `inputs/generated_files.md`

## Scope
Implement only the order book module.

Expected responsibilities:
- initial the orderbook with `inputs/reference_data/orderbook.json`
- maintain bid and ask books
- preserve price-time priority at the book level
- add a resting order
- remove an order
- fetch best bid and best ask
- expose enough methods for the future matching engine

## Non-Goals
Do not implement:
- trade matching logic
- execution report generation
- persistence
- FIX parsing
- APIs

## Output
Create or update only:
- `src/model/engine/orderbook.py`
- related small helper files if truly necessary
- `tests/test_orderbook.py`
- add all generated code file *address* and *desciption* to `prompts/generated_files.md`

## Constraints
- Do not duplicate order or trade definitions
- Keep implementation simple and explicit
- Prefer dataclasses and typed methods
- Keep business logic deterministic

## Acceptance Criteria
- resting orders can be inserted into bid/ask side correctly
- same-price orders preserve FIFO ordering
- best bid/ask can be queried
- orders can be removed cleanly
- tests cover core behaviors