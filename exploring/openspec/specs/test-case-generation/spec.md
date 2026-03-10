# Test Case Generation Specification

# <!-- Requirement description for detail -->

# Defines the specification for what test cases this digital twin generator will produce.

 This includes:
# the format, structure, and expected output artifacts.

 Test case generation is controlled by scenarios that which
 be configurable through user-provided weights and volumes, and optional seeds for reproducibility.
# Test Case Generation Specification
# <!-- Requirement description in detail -->
# Test case generation produces test cases in hybrid CSV format
# support multiple scenarios ( configurable via YAML files)
# scenarios are stored as `config/scenarios/<name>.yaml` files
# - Users can define scenario weights for message groups and types
# - scenarios can reference initial state files for context setup
# We define custom test scenarios for enable test replay capability
# The:
## Dependencies
- **proposal**: Completed artifact from proposal.md
# <!-- Other artifacts this generated design depends on -->

# Validation rules per message type (what is valid vs invalid)
- Parameter generation respects validation rules (positive/negative testing,- Boundary value tested via configurable strategy
- Parameters generated based on current state (available symbols, orderbook state)
- Parameters JSON-serializable
- **csv-writer**: Writes hybrid CSV output (wide columns + JSON payload)

# <!-- Dependencies -->
- **proposal**: Test case generation spec from proposal.md
- **state-model**: State model from proposal.md
# <!-- other artifacts: None

