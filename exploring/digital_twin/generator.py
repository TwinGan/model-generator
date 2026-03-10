"""
Main test case generator.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from copy import deepcopy
import yaml

from .state import DigitalTwinState
from .loader import load_initial_state
from .selector import MessageSelector, NoValidMessageError
from .coverage import CoverageTracker
from .csv_writer import CSVWriter, TestStep
from .messages.base import (
    MESSAGE_REGISTRY,
    get_handler,
    get_generator,
    get_precondition,
    get_registered_message_types,
)


@dataclass
class GeneratorResult:
    """Result from test case generation."""
    test_steps: List[TestStep]
    coverage_report: Dict[str, Any]
    metadata: Dict[str, Any]
    initial_state: DigitalTwinState
    final_state: DigitalTwinState


class TestCaseGenerator:
    """Main test case generator for digital twin."""

    def __init__(
        self,
        scenario_config: Optional[Dict[str, Any]] = None,
        initial_state: Optional[DigitalTwinState] = None,
        initial_state_path: Optional[str] = None,
        seed: Optional[int] = None,
    ):
        if initial_state is None and initial_state_path:
            initial_state = load_initial_state(initial_state_path)
        elif initial_state is None:
            initial_state = DigitalTwinState()

        self.initial_state = deepcopy(initial_state)
        self.state = deepcopy(initial_state)
        self.seed = seed
        self.run_id = str(uuid.uuid4())[:8]
        self.timestamp = datetime.now().isoformat()

        self.scenario_config = scenario_config or {}
        self.selector = MessageSelector(
            weights_config=scenario_config.get('message_weights') if scenario_config else None,
            seed=seed
        )
        self.coverage = CoverageTracker()
        self.coverage.set_total_message_types(len(get_registered_message_types()))

        self._cl_ord_id_counter = 0
        self._order_id_counter = 0
        self._exec_id_counter = 0
        self._step_counter = 0

    def generate(self, num_steps: int) -> GeneratorResult:
        """Generate test cases for specified number of steps."""
        test_steps: List[TestStep] = []

        for _ in range(num_steps):
            try:
                step = self._generate_single_step()
                test_steps.extend(step)
            except NoValidMessageError:
                continue

        return GeneratorResult(
            test_steps=test_steps,
            coverage_report=self.coverage.to_dict(),
            metadata=self._build_metadata(num_steps),
            initial_state=self.initial_state,
            final_state=deepcopy(self.state),
        )

    def _generate_single_step(self) -> List[TestStep]:
        """Generate a single test step (send + receive(s))."""
        message_type = self.selector.select_message(self.state)
        self._step_counter += 1

        generator = get_generator(message_type)
        if generator:
            strategy = self.scenario_config.get('parameter_strategies', {}).get(message_type, {})
            params = generator.generate(self.state, strategy)
        else:
            params = {}

        params.setdefault('cl_ord_id', self._next_cl_ord_id())

        handler = get_handler(message_type)
        results = []
        if handler:
            results = handler.execute(params, self.state)

        self.coverage.record_message_type(message_type)

        steps = []
        steps.append(TestStep(
            step_id=self._step_counter,
            direction="send",
            message_type=message_type,
            data=params,
        ))

        for result in results:
            self.coverage.record_transition(
                params.get('status', 'UNKNOWN'),
                result.status
            )
            steps.append(TestStep(
                step_id=self._step_counter,
                direction="receive",
                message_type=result.message_type,
                data=result.data,
            ))

        return steps

    def _next_cl_ord_id(self) -> str:
        """Generate next client order ID."""
        self._cl_ord_id_counter += 1
        return f"CL{self._cl_ord_id_counter:06d}"

    def _next_order_id(self) -> str:
        """Generate next order ID."""
        self._order_id_counter += 1
        return f"ORD{self._order_id_counter:06d}"

    def _next_exec_id(self) -> str:
        """Generate next execution ID."""
        self._exec_id_counter += 1
        return f"EXEC{self._exec_id_counter:06d}"

    def _build_metadata(self, num_steps: int) -> Dict[str, Any]:
        """Build metadata for this generation run."""
        return {
            "run_id": self.run_id,
            "timestamp": self.timestamp,
            "seed": self.seed,
            "num_steps_requested": num_steps,
            "num_steps_generated": self._step_counter,
            "scenario": self.scenario_config.get('name', 'default'),
            "version": "0.1.0",
        }

    def save(self, result: GeneratorResult, output_dir: str) -> Dict[str, Path]:
        """Save all generation artifacts to output directory."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        paths = {}

        csv_path = output_path / "test_cases.csv"
        CSVWriter(str(csv_path)).write(
            result.test_steps,
            metadata={"run_id": result.metadata["run_id"], "seed": result.metadata["seed"]}
        )
        paths["csv"] = csv_path

        coverage_path = output_path / "coverage_report.json"
        with open(coverage_path, 'w') as f:
            json.dump(result.coverage_report, f, indent=2)
        paths["coverage"] = coverage_path

        metadata_path = output_path / "metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(result.metadata, f, indent=2)
        paths["metadata"] = metadata_path

        initial_state_path = output_path / "initial_state.json"
        with open(initial_state_path, 'w') as f:
            json.dump(result.initial_state.to_dict(), f, indent=2)
        paths["initial_state"] = initial_state_path

        return paths

    @classmethod
    def from_config(
        cls,
        config_path: str,
        initial_state_path: str,
        seed: Optional[int] = None,
    ) -> "TestCaseGenerator":
        """Create generator from config file."""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return cls(
            scenario_config=config,
            initial_state_path=initial_state_path,
            seed=seed,
        )
