from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass
class ParsedDocumentRecord:
    source_path: str
    output_markdown_path: str
    output_json_path: str
    status: str
    error: str | None = None
    meta: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)