"""
Message handler base classes and parameter generators, preconditions.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from decimal import Decimal

from ..state import DigitalTwinState, OrderStatus


@dataclass
class HandlerResult:
    """Result from message handler execution."""
    message_type: str
    data: Dict[str, Any]
    status: str = "ACCEPTED"  # ACCEPTED or REJECTED


    reason: Optional[str] = None


class Precondition(ABC):
    """Base class for message preconditions."""
    
    @abstractmethod
    def check(self, state: DigitalTwinState) -> bool:
        """Check if preconditions are met for this message type."""
        pass


    @abstractmethod
    def get_required_state_fields(self) -> List[str]:
        """Return list of state fields required for this precondition."""
        pass


class ParameterGenerator(ABC):
    """Base class for parameter generators."""
    
    @abstractmethod
    def generate(self, state: DigitalTwinState, strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Generate parameters for message.
        
        Args:
            state: Current trading state
            strategy: Parameter generation strategy
            
        Returns:
            Dict of parameter name to value
        """
        pass
    
    @abstractmethod
    def get_parameter_schema(self) -> Dict[str, Any]:
        """Return schema for parameters this generator produces."""
        pass


class MessageHandler(ABC):
    """Base class for message handlers."""
    
    @abstractmethod
    def execute(self, params: Dict[str, Any], state: DigitalTwinState) -> List[HandlerResult]:
        """Execute message handler.
        
        Args:
            params: Message parameters
            state: Current trading state (will be modified)
            
        Returns:
            List of predicted responses (0 for simple, multiple for partial fills)
        """
        pass
    
    @abstractmethod
    def get_message_type(self) -> str:
        """Return message type this handler processes."""
        pass
    
    @abstractmethod
    def get_message_group(self) -> str:
        """Return message group this handler belongs to."""
        pass


# Global message registry
MESSAGE_REGISTRY: Dict[str, Dict[str, Any]] = {}


def register_message(
    message_type: str,
    message_group: str,
    handler: MessageHandler,
    generator: ParameterGenerator,
    precondition: Precondition
) -> None:
    """Register a message type with its components."""
    MESSAGE_REGISTRY[message_type] = {
        'handler': handler,
        'generator': generator,
        'precondition': precondition,
        'group': message_group,
    }


def get_handler(message_type: str) -> Optional[MessageHandler]:
    """Get handler for message type."""
    entry = MESSAGE_REGISTRY.get(message_type)
    return entry['handler'] if entry else None


def get_generator(message_type: str) -> Optional[ParameterGenerator]:
    """Get parameter generator for message type."""
    entry = MESSAGE_REGISTRY.get(message_type)
    return entry['generator'] if entry else None


def get_precondition(message_type: str) -> Optional[Precondition]:
    """Get precondition checker for message type."""
    entry = MESSAGE_REGISTRY.get(message_type)
    return entry['precondition'] if entry else None


def get_message_group(message_type: str) -> Optional[str]:
    """Get message group for message type."""
    entry = MESSAGE_REGISTRY.get(message_type)
    return entry['group'] if entry else None


def get_registered_message_types() -> List[str]:
    """Get list of all registered message types."""
    return list(MESSAGE_REGISTRY.keys())


def get_messages_by_group(group: str) -> List[str]:
    """Get list of message types in a group."""
    return [
        msg_type for msg_type, entry in MESSAGE_REGISTRY.items()
        if entry.get('group') == group
    ]
