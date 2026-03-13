# AGENTS.md

## Project Goal

This repository is used to generate a simplified market model (digital twin) for exchange-style order matching.

The immediate goal is to implement a **deterministic, testable core matching engine** for a simplified options trading model, based on:
- parsed business specifications
- normalized FIX schema
- reference data examples
- sample test cases

This project is intended for code generation and iterative refinement.  
Agents should prioritize correctness, clarity, and deterministic behavior over completeness.

---

## Current Scope

At this stage, implement only the **core matching model** for **options orders**.

The model should support:
- order submission
- order cancellation
- order amendment/replace (only if clearly supported by the provided spec)
- order book maintenance
- price/time priority matching
- trade generation
- book state transitions
- deterministic expected-result generation for tests

Focus on the matching engine and its domain model only.

---

## Explicit Non-Goals

Do NOT implement the following unless explicitly requested in another spec:
- member-level validation
- user-level validation
- account / credit / risk validation
- persistence layer
- database integration
- message queue integration
- network servers
- REST API
- FIX session layer
- authentication / authorization
- UI
- production deployment concerns
- performance optimization beyond reasonable clean design

Do not invent exchange features that are not supported by the provided documents.

---

## Source of Truth

When generating code, use the following sources in order of priority:

1. `docs/specs/core_matching_spec.md`
   - Primary source for matching behavior and business rules.
2. `docs/parsed/normalized_fix_schema.json`
   - Source for message field names and message structure.
3. `docs/reference_data/`
   - Source for static initialization data and order book seed examples.
4. `docs/testcases/`
   - Source for sample scenarios and expected behavior.
5. `README.md`
   - High-level project context only.

If sources conflict:
- prefer the core matching spec over FIX schema wording
- prefer explicit rules over inferred behavior
- prefer deterministic/simple behavior over speculative completeness

---

## Implementation Priorities

Agents should work in the following order:

1. Define the minimal domain model
   - instrument
   - side
   - order type
   - time in force
   - order
   - trade
   - book level / order book
   - execution report / event model if needed

2. Implement the core matching engine
   - add order
   - cancel order
   - replace/amend order if in scope
   - match incoming aggressor against resting liquidity
   - maintain book state deterministically

3. Implement scenario/result generation
   - given reference data and test inputs, produce expected events and final book state

4. Implement unit tests and scenario tests
   - tests are first-class deliverables

5. Only after the above, improve ergonomics or adapters

---

## Domain Rules

Unless a more specific spec states otherwise, follow these rules:

- Matching is based on **price-time priority**.
- Resting orders remain on the book until filled, canceled, expired, or replaced.
- Incoming aggressive orders may trade against multiple resting orders.
- Partial fills must be supported.
- A trade reduces remaining quantity on both sides appropriately.
- If an incoming order is not fully filled, the remaining quantity is either booked or removed depending on its order constraints.
- Matching behavior must be deterministic and reproducible.
- All state transitions must be explicit and testable.
- Avoid hidden side effects.

If the exact rule is unclear, implement the simplest deterministic behavior and document the assumption in code comments or a markdown note.

---

## Architecture Guidance

Prefer a small, explicit, domain-driven structure.

Suggested package layout:

- `src/model/domain/`
  - domain entities and enums
- `src/model/engine/`
  - matching engine and order book logic
- `src/model/services/`
  - scenario runner / expected result generator
- `src/model/parsers/`
  - loaders for normalized schema, reference data, and test case files
- `tests/`
  - unit and scenario tests

Prefer pure Python business logic with minimal framework use.

Avoid premature abstractions.  
Use simple classes/dataclasses/enums unless a stronger abstraction is clearly needed.

---

## Coding Rules

- Use Python 3.11+.
- Prefer `dataclass`, `Enum`, and typed functions.
- Keep business logic pure and testable.
- Separate parsing/loading logic from matching logic.
- Keep I/O at the edges.
- Do not mix transport-layer FIX concerns into the core matching engine.
- Add docstrings only where they clarify domain intent.
- Keep functions small and explicit.
- Prefer readable code over clever code.

---

## Testing Expectations

Agents must generate tests alongside implementation.

At minimum include:
- unit tests for order book operations
- unit tests for matching behavior
- tests for partial fill
- tests for full fill
- tests for price priority
- tests for time priority within same price
- tests for cancel behavior
- tests for amend/replace behavior if implemented
- scenario tests using sample reference data and CSV test cases

Tests should validate:
- generated trades
- order state changes
- final remaining quantities
- final order book state

---

## Working Style for Agents

When modifying the repository:
- make the smallest coherent change first
- keep the project runnable
- prefer incremental commits/patches in spirit
- do not rewrite unrelated files
- do not add speculative infrastructure

If a required rule is missing from the source material:
- do not invent a large framework to handle uncertainty
- document the assumption clearly
- implement the narrowest viable behavior

---

## Definition of Done for This Phase

This phase is complete when the repository contains:

1. a minimal but coherent domain model
2. a working deterministic matching engine for options orders
3. loaders/parsers for provided sample inputs where needed
4. scenario-based expected result generation
5. automated tests proving the engine behavior
6. clear documentation of assumptions and unsupported features