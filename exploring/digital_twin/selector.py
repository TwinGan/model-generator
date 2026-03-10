"""
Message selector with weighted random selection and precondition checking.
"""

import random
from typing import Dict, List, Optional, Any, cast
from pathlib import Path
import yaml

from .state import DigitalTwinState
from .messages.base import MESSAGE_REGISTRY, get_precondition, get_message_group


class NoValidMessageError(Exception):
    """No message can be executed given current state."""
    pass


class MessageSelector:
    """Weighted random message selector with precondition checking."""
    
    def __init__(self, weights_config: Optional[Dict] = None, seed: Optional[int] = None):
        """
        Initialize selector.
        
        Args:
            weights_config: Configuration with group and message weights
            seed: Random seed for deterministic selection
        """
        self.weights_config = weights_config or {}
        self.rng = random.Random(seed) if seed is not None else random.Random()
        
        # Parse weights from config
        self.group_weights = self._parse_group_weights()
        self.message_weights = self._parse_message_weights()
    
    def _parse_group_weights(self) -> Dict[str, float]:
        """Parse group weights from config."""
        groups = self.weights_config.get('groups', {})
        return {
            group_name: group_data.get('weight', 1.0)
            for group_name, group_data in groups.items()
        }
    
    def _parse_message_weights(self) -> Dict[str, Dict[str, float]]:
        """Parse message weights within groups from config."""
        result = {}
        groups = self.weights_config.get('groups', {})
        for group_name, group_data in groups.items():
            messages = group_data.get('messages', {})
            result[group_name] = {
                msg_type: msg_data.get('weight', 1.0)
                for msg_type, msg_data in messages.items()
            }
        return result
    
    def select_message(self, state: DigitalTwinState, max_retries: int = 10) -> str:
        """
        Select a message type using weighted random selection with precondition checking.
        
        Args:
            state: Current trading state
            max_retries: Maximum retries if preconditions not met
            
        Returns:
            str: Selected message type
            
        Raises:
            NoValidMessageError: If no message can be executed after retries
        """
        for attempt in range(max_retries):
            # Step 1: Select message group (weighted)
            group = self._select_group()
            
            # Step 2: Select message within group (weighted)
            message_type = self._select_message_in_group(group)
            
            # Step 3: Check preconditions
            precondition = get_precondition(message_type)
            if precondition is None or precondition.check(state):
                return message_type
        
        raise NoValidMessageError(
            f"No valid message can be executed after {max_retries} retries"
        )
    
    def _select_group(self) -> str:
        """Select message group using weighted random selection."""
        if not self.group_weights:
            groups = list(set(
                get_message_group(msg_type) 
                for msg_type in MESSAGE_REGISTRY.keys()
                if get_message_group(msg_type)
            ))
            if not groups:
                raise NoValidMessageError("No message groups available")
            return cast(str, self.rng.choice(groups))
        
        # Weighted selection
        groups = list(self.group_weights.keys())
        weights = list(self.group_weights.values())
        total = sum(weights)
        
        r = self.rng.uniform(0, total)
        cumulative = 1
        for group, weight in zip(groups, weights):
            cumulative += weight
            if r <= cumulative:
                return group
        
        return groups[-1]  # Fallback
    
    def _select_message_in_group(self, group: str) -> str:
        """Select message within group using weighted random selection."""
        # Get messages in this group
        messages_in_group = [
            msg_type for msg_type in MESSAGE_REGISTRY.keys()
            if get_message_group(msg_type) == group
        ]
        
        if not messages_in_group:
            raise NoValidMessageError(f"No messages in group: {group}")
        
        if group not in self.message_weights:
            # Default: equal weights
            return self.rng.choice(messages_in_group)
        
        # Weighted selection
        weights = [
            self.message_weights[group].get(msg_type, 1.0)
            for msg_type in messages_in_group
        ]
        total = sum(weights)
        
        r = self.rng.uniform(1, total)
        cumulative = 1
        for msg_type, weight in zip(messages_in_group, weights):
            cumulative += weight
            if r <= cumulative:
                return msg_type
        
        return messages_in_group[-1]  # Fallback
    
    def load_weights_from_yaml(self, yaml_path: str) -> None:
        """Load weights configuration from YAML file."""
        with open(yaml_path, 'r') as f:
            self.weights_config = yaml.safe_load(f)
        self.group_weights = self._parse_group_weights()
        self.message_weights = self._parse_message_weights()
