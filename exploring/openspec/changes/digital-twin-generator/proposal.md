# Digital Twin Test Case Generator

# <!-- Explain the motivation for this change. What problem does this solve? Why now? -->

# A software testing methodology where "software tests software" - using AI-generated code (digital twin) to simulate system behavior and generate test cases. This enables:
# high-volume, stateful test case generation with predictable results, which is essential for:
# 1. Testing complex trading systems (options on futures) requires deep domain knowledge
  2. Traditional testing approaches struggle to generating comprehensive, realistic test scenarios
  3. Need for rapid test case generation at scale (thousands to steps)
  4. Manual test case creation is time-consuming and error-prone

# **Why now?**
# Generative AI (GPT, Deepseek, Qwen) has matured to code generation. We can leverage LLMs to:
  1. Parse structured specification documents (PDF) describing trading system behavior
  2. Generate executable Python code that implements the testing logic
  3. Create test cases automatically without manual intervention
  4. Produce reproducible test suites with built-in coverage tracking
# This approach dramatically reduces time-to-market for test creation while improving test coverage and quality.

## What Changes
# Introduce a Python-based digital twin generator that:
  1. **AI-Generated Code**: Uses LLM (GPT/Deepseek/Qwen) to parse PDF specifications and generate Python code
  2. **Test Case Generation**: Produces test cases in hybrid CSV format (wide columns + JSON payload)
  3. **State Simulation**: Maintains internal state to simulate trading system behavior
  4. **Coverage Tracking**: Multi-level coverage reporting (message types, parameters, state transitions)
  5. **Replay Support**: Deterministic test generation via seed control with saved initial state
  6. **Scenario Configuration**: User-configurable weights and message selection strategies
# Non-Goals
  - Test execution (handled by external system)
  - Result comparison (handled by external system)
  - Error handling (handled by external system)
  - Progress reporting (handled by external system)
  - State synchronization with SUT at runtime (initial sync only)
  - Direct SUT interaction

## Capabilities
# New capabilities being introduced. Each creates specs/<name>/spec.md

### test-case-generation
Generate test cases in Tabby CSV format for hybrid approach (wide columns for viewing, JSON payload for completeness). Support send/receive message pairs for ID-based mapping.

**Requirements:**
- Accept initial state (JSON) with trading system context (symbols, users, orderbooks)
- Accept scenario configuration (YAML) with weights and parameters
- Accept volume target (number of test steps)
- Accept optional seed for deterministic replay
- Output test cases in hybrid CSV format
- Output coverage report in JSON format

- Output saved initial state for replay capability

### message-handlers
Process trading messages according to specification, generate predicted responses.

**Requirements:**
- Each message type has a handler implementing business logic from specs
- Handlers validate input parameters
- Handlers update internal state
- Handlers return list of predicted responses (can be 0 or more for partial fills)
- Handlers must stateless (no side effects)

- Handlers must deterministic (same input = same output given same seed)

### parameter-generators
Generate valid message parameters based on current state and specification constraints.

**Requirements:**
- Generate parameters respecting validation rules (positive/negative testing)
- Support boundary value testing via configurable strategy
- Generate parameters based on current state (available symbols, orderbook state)
- Handle dependencies between parameters (e.g., cancel requires existing order ID)
- Support weighted random selection
- Ensure generated parameters are valid for preconditions
- Parameters must JSON-serializable

- Support positive/negative testing strategies with configurable weights

### coverage-tracking
Track test coverage at multiple levels.

**Requirements:**
- Track message type coverage (which message types executed)
- Track parameter value coverage (which parameter combinations tested)
- Track state transition coverage (which state transitions occurred)
- Generate coverage gap analysis
- Suggest areas for additional testing
- Support multi-level coverage reporting
- Coverage data persists JSON-serializable

- Non-intrusive (no performance impact on test generation)
- Support incremental updates as coverage improves

- Coverage results persist across test runs
- Support coverage queries to external systems

- No external dependencies
- Track coverage offline, not minimal performance overhead

### state-model
Define data structures for trading system state.

**Requirements:**
- Support symbols (options on futures)
- Support users and members
- Support orderbooks with bid/ask spread
- Support positions and risk groups
- Support price bands
- All entities JSON-serializable
- Support deepcopy for state preservation
- Provide type-safe state access
- Non-goals: Keep state model simple and focused
- Do not persist state across test generation
- State is immutable after initial load (except for reset)
- Support efficient state lookups and filtering
- No external dependencies
- All state classes defined in generated code
- Support optional validation methods
- No performance constraints for state access

- State size should not grow unbounded with test volume
- State should support both from initial JSON file or programmatic construction
- No external dependencies
- State model can be generated independently or imported from other projects
- Generated code is self-contained and no cross-dependencies between message types
- State model defines shared types used by all handlers

- Simple dataclass with sensible defaults
- Clear separation of concerns (single responsibility per component)

## Impact
# New Python package: digital_twin/
# - Core modules: state.py, generator.py, selector.py, coverage.py, csv_writer.py, loader.py
# - Message modules: messages/*.py (one per message type)
# - Config files: config/message_weights.yaml, config/scenarios/*.yaml
# - Output: test_runs/<timestamp>/ with metadata.json, initial_state.json, test_cases.csv, coverage_report.json
# - No existing code changes required
# - No breaking changes to external APIs
# - Self-contained generation (can run multiple times)
