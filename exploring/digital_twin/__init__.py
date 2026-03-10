"""
Digital Twin Test Case Generator

AI-generated test case generator for options on futures trading systems.
Produces hybrid CSV output with built-in coverage tracking and replay capabilities.
"""

__version__ = "0.1.0"

from .state import DigitalTwinState, Symbol, User, Member, Order, Position, Orderbook, PriceBand, RiskGroup
from .loader import load_initial_state, StateLoadError
from .selector import MessageSelector, NoValidMessageError
from .coverage import CoverageTracker, CoverageSummary, CoverageGap
from .csv_writer import CSVWriter, TestStep
from .generator import TestCaseGenerator, GeneratorResult

__all__ = [
    "DigitalTwinState",
    "Symbol",
    "User",
    "Member",
    "Order",
    "Position",
    "Orderbook",
    "PriceBand",
    "RiskGroup",
    "load_initial_state",
    "StateLoadError",
    "MessageSelector",
    "NoValidMessageError",
    "CoverageTracker",
    "CoverageSummary",
    "CoverageGap",
    "CSVWriter",
    "TestStep",
    "TestCaseGenerator",
    "GeneratorResult",
]
