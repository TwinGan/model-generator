"""
Hybrid CSV writer for test case output.

Format: Wide columns for common fields + JSON payload for complete data.
"""

import csv
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
from dataclasses import dataclass


@dataclass
class TestStep:
    """Represents a single test step (send or receive)."""
    step_id: int
    direction: str  # "send" or "receive"
    message_type: str
    data: Dict[str, Any]


# Wide columns for easy viewing
WIDE_COLUMNS = [
    'step_id',
    'direction',
    'message_type',
    'symbol',
    'side',
    'quantity',
    'price',
    'order_id',
    'cl_ord_id',
    'orig_cl_ord_id',
    'status',
    'exec_type',
    'reason',
    'payload_json'
]


class CSVWriter:
    """Hybrid CSV writer with wide columns and JSON payload."""
    
    def __init__(self, output_path: str):
        """
        Initialize CSV writer.
        
        Args:
            output_path: Path to output CSV file
        """
        self.output_path = Path(output_path)
        self.file = None
        self.writer = None
    
    def write(
        self,
        test_steps: List[TestStep],
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Write test steps to CSV file.
        
        Args:
            test_steps: List of test steps to write
            metadata: Optional metadata to include as comments
        """
        with open(self.output_path, 'w', newline='') as f:
            # Write metadata as comments
            if metadata:
                for key, value in metadata.items():
                    f.write(f"# {key}: {value}\n")
                f.write("#\n")
            
            # Write header
            writer = csv.DictWriter(f, fieldnames=WIDE_COLUMNS)
            writer.writeheader()
            
            # Write rows
            for step in test_steps:
                row = self._build_row(step)
                writer.writerow(row)
    
    def _build_row(self, step: TestStep) -> Dict[str, Any]:
        """
        Build a CSV row from a test step.
        
        Args:
            step: Test step to convert
            
        Returns:
            Dict mapping column names to values
        """
        row = {
            'step_id': step.step_id,
            'direction': step.direction,
            'message_type': step.message_type,
        }
        
        # Extract common fields into wide columns
        data = step.data
        for col in ['symbol', 'side', 'quantity', 'price', 'order_id', 
                    'cl_ord_id', 'orig_cl_ord_id', 'status', 'exec_type', 'reason']:
            value = data.get(col)
            if value is not None:
                # Convert Decimal to string for CSV
                if hasattr(value, '__str__'):
                    value = str(value)
                # Convert enum to string
                elif hasattr(value, 'value'):
                    value = value.value
            row[col] = value if value is not None else ''
        
        # Add complete payload as JSON
        row['payload_json'] = self._serialize_payload(data)
        
        return row
    
    def _serialize_payload(self, data: Dict[str, Any]) -> str:
        """
        Serialize payload data to JSON string.
        
        Args:
            data: Data to serialize
            
        Returns:
            JSON string representation
        """
        def default_serializer(obj):
            """Custom JSON serializer for special types."""
            from decimal import Decimal
            from enum import Enum
            from datetime import datetime
            
            if isinstance(obj, Decimal):
                return str(obj)
            elif isinstance(obj, Enum):
                return obj.value
            elif isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
        
        return json.dumps(data, default=default_serializer)
    
    @staticmethod
    def escape_json_for_csv(json_str: str) -> str:
        """
        Escape JSON string for CSV format.
        
        Args:
            json_str: JSON string to escape
            
        Returns:
            Properly escaped string
        """
        # csv module handles escaping, but this is here for manual use
        return json_str
