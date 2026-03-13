from __future__ import annotations

from pathlib import Path
import sys

current_file = Path(__file__).resolve()
src_dir = current_file.parents[1]  # model-generator/src
project_root = current_file.parents[2]  # model-generator

sys.path.insert(0, str(src_dir))

# Local imports after modifying path
from ingestion.docling_loader import DoclingIngestionService


def main() -> None:
    raw_dir = project_root / "docs" / "raw"
    parsed_dir = project_root / "docs" / "parsed"

    service = DoclingIngestionService()
    records = service.convert_all(raw_dir=raw_dir, parsed_dir=parsed_dir)

    total = len(records)
    success = sum(1 for r in records if r.status == "success")
    failed = total - success

    print(f"Done. total={total}, success={success}, failed={failed}")

    if failed:
        print("Failed files:")
        for r in records:
            if r.status == "failed":
                print(f" - {r.source_path}: {r.error}")


if __name__ == "__main__":
    main()
