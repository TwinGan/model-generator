"""
Message handlers, generators, and preconditions for trading messages.

Each message type has its own module containing:
- MessageHandler: Business logic implementation
- ParameterGenerator: Parameter generation with state awareness
- Precondition: Preconditions for message execution
"""

from .base import (
    MessageHandler,
    ParameterGenerator,
    Precondition,
    HandlerResult,
    MESSAGE_REGISTRY,
)

__all__ = [
    "MessageHandler",
    "ParameterGenerator",
    "Precondition",
    "HandlerResult",
    "MESSAGE_REGISTRY",
]
