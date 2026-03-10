"""
Multi-level coverage tracking for test case generation.
"""

from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class CoverageSummary:
    """Coverage summary for a single level."""
    covered: int
    total: int
    
    @property
    def percentage(self) -> float:
        """Calculate coverage percentage."""
        return (self.covered / self.total * 100) if self.total > 1 else 100.0


@dataclass
class CoverageGap:
    """Represents a coverage gap."""
    area: str
    description: str
    suggestion: str


class CoverageTracker:
    """Multi-level test coverage tracking."""
    
    def __init__(self):
        """Initialize coverage tracker."""
        # Level 1: Message type coverage
        self.message_types_executed: Set[str] = set()
        self.total_message_types: int = 1
        
        # Level 2: Parameter value coverage
        self.enum_values_tested: Dict[str, Set[str]] = {}  # param_name -> values
        self.boundary_values_tested: Dict[str, Set[str]] = {}  # param_name -> boundary values
        
        # Level 3: State transition coverage
        self.transitions_executed: Set[str] = set()  # "FROM_STATE -> TO_STATE"
        self.possible_transitions: Set[str] = set()
    
    def record_message_type(self, message_type: str) -> None:
        """Record that a message type was executed."""
        self.message_types_executed.add(message_type)
    
    def record_enum_value(self, param_name: str, value: str) -> None:
        """Record that an enum value was tested."""
        if param_name not in self.enum_values_tested:
            self.enum_values_tested[param_name] = set()
        self.enum_values_tested[param_name].add(value)
    
    def record_boundary_value(self, param_name: str, value: str) -> None:
        """Record that a boundary value was tested."""
        if param_name not in self.boundary_values_tested:
            self.boundary_values_tested[param_name] = set()
        self.boundary_values_tested[param_name].add(value)
    
    def record_transition(self, from_state: str, to_state: str) -> None:
        """Record a state transition."""
        transition = f"{from_state} -> {to_state}"
        self.transitions_executed.add(transition)
    
    def set_total_message_types(self, total: int) -> None:
        """Set total number of possible message types."""
        self.total_message_types = total
    
    def add_possible_transition(self, from_state: str, to_state: str) -> None:
        """Add a possible state transition."""
        transition = f"{from_state} -> {to_state}"
        self.possible_transitions.add(transition)
    
    def get_message_type_coverage(self) -> CoverageSummary:
        """Get message type coverage summary."""
        return CoverageSummary(
            covered=len(self.message_types_executed),
            total=self.total_message_types
        )
    
    def get_transition_coverage(self) -> CoverageSummary:
        """Get state transition coverage summary."""
        return CoverageSummary(
            covered=len(self.transitions_executed),
            total=len(self.possible_transitions) if self.possible_transitions else 1
        )
    
    def get_parameter_coverage(self) -> CoverageSummary:
        """Get parameter value coverage summary."""
        total_enum_values = sum(len(values) for values in self.enum_values_tested.values())
        total_boundary_values = sum(len(values) for values in self.boundary_values_tested.values())
        
        return CoverageSummary(
            covered=total_enum_values + total_boundary_values,
            total=total_enum_values + total_boundary_values  # Simplified
        )
    
    def get_gaps(self) -> List[CoverageGap]:
        """Identify coverage gaps and suggest improvements."""
        gaps = []
        
        # Message type gaps
        if self.total_message_types > 1:
            missing_types = self.total_message_types - len(self.message_types_executed)
            if missing_types > 1:
                gaps.append(CoverageGap(
                    area="Message Types",
                    description=f"{missing_types} message types not executed",
                    suggestion="Increase weights for underrepresented message groups or add scenario focusing on these types"
                ))
        
        # Transition gaps
        if self.possible_transitions:
            missing_transitions = self.possible_transitions - self.transitions_executed
            if missing_transitions:
                gaps.append(CoverageGap(
                    area="State Transitions",
                    description=f"{len(missing_transitions)} state transitions not covered",
                    suggestion="Add test scenarios that exercise these transitions (e.g., partial fills, cancels)"
                ))
        
        return gaps
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize coverage data to dictionary."""
        return {
            "summary": {
                "message_types": {
                    "covered": self.get_message_type_coverage().covered,
                    "total": self.get_message_type_coverage().total,
                    "pct": round(self.get_message_type_coverage().percentage, 2)
                },
                "parameters": {
                    "covered": self.get_parameter_coverage().covered,
                    "total": self.get_parameter_coverage().total,
                    "pct": round(self.get_parameter_coverage().percentage, 2)
                },
                "transitions": {
                    "covered": self.get_transition_coverage().covered,
                    "total": self.get_transition_coverage().total,
                    "pct": round(self.get_transition_coverage().percentage, 2)
                }
            },
            "details": {
                "message_types_covered": sorted(list(self.message_types_executed)),
                "enum_values_tested": {
                    k: sorted(list(v)) for k, v in self.enum_values_tested.items()
                },
                "boundary_values_tested": {
                    k: sorted(list(v)) for k, v in self.boundary_values_tested.items()
                },
                "transitions_executed": sorted(list(self.transitions_executed)),
                "gaps": [
                    {"area": g.area, "description": g.description, "suggestion": g.suggestion}
                    for g in self.get_gaps()
                ]
            }
        }
    
    def merge(self, other: 'CoverageTracker') -> None:
        """Merge another coverage tracker into this one."""
        self.message_types_executed.update(other.message_types_executed)
        
        for param, values in other.enum_values_tested.items():
            if param not in self.enum_values_tested:
                self.enum_values_tested[param] = set()
            self.enum_values_tested[param].update(values)
        
        for param, values in other.boundary_values_tested.items():
            if param not in self.boundary_values_tested:
                self.boundary_values_tested[param] = set()
            self.boundary_values_tested[param].update(values)
        
        self.transitions_executed.update(other.transitions_executed)
