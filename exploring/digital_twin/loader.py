"""
Loader for initial state from JSON.
"""

import json
from pathlib import Path
from typing import Optional
from copy import deepcopy

from .state import DigitalTwinState


class StateLoadError(Exception):
    """Error loading initial state."""
    pass


def load_initial_state(json_path: str) -> DigitalTwinState:
    """
    Load initial state from JSON file.
    
    Args:
        json_path: Path to initial_state.json file
        
    Returns:
        DigitalTwinState: Initialized state object
        
    Raises:
        StateLoadError: If file not found or invalid
    """
    path = Path(json_path)
    
    if not path.exists():
        raise StateLoadError(f"Initial state file not found: {json_path}")
    
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise StateLoadError(f"Invalid JSON in {json_path}: {e}")
    
    # Validate required components
    required_fields = ['symbols', 'users', 'members']
    missing = [f for f in required_fields if f not in data]
    if missing:
        raise StateLoadError(f"Missing required fields in initial state: {missing}")
    
    # Deserialize state
    try:
        state = DigitalTwinState.from_dict(data)
    except Exception as e:
        raise StateLoadError(f"Failed to create state from JSON: {e}")
    
    # Create independent working copy
    return deepcopy(state)
