from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from docling.document_converter import DocumentConverter, PdfFormatOption
from .record import ParsedDocumentRecord
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".html",
    ".htm",
    ".md",
    ".png",
    ".jpg",
    ".jpeg",
    ".tiff",
    ".bmp",
}


class DoclingIngestionService:
    def __init__(self) -> None:
        pdf_pipeline_options = PdfPipelineOptions(do_table_structure=True)
        pdf_pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE

        # pdf_pipeline_options.table_structure_options.do_cell_matching = False

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pdf_pipeline_options
                )
            }
        )

    def iter_source_files(self, raw_dir: Path) -> Iterable[Path]:
        for path in raw_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
                yield path

    def convert_one(self, source_path: Path, parsed_dir: Path) -> ParsedDocumentRecord:
        rel_stem = source_path.stem
        safe_name = rel_stem.replace(" ", "_")

        md_path = parsed_dir / f"{safe_name}.md"
        json_path = parsed_dir / f"{safe_name}.json"

        try:
            result = self.converter.convert(str(source_path))
            document = result.document

            markdown = document.export_to_markdown()

            # try json export first
            json_payload = None

            if hasattr(document, "export_to_dict"):
                json_payload = document.export_to_dict()
            elif hasattr(document, "model_dump"):
                json_payload = document.model_dump()
            else:
                # keep base information
                json_payload = {
                    "source": str(source_path),
                    "markdown_preview": markdown[:2000],
                }

            parsed_dir.mkdir(parents=True, exist_ok=True)

            md_path.write_text(markdown, encoding="utf-8")
            json_path.write_text(
                json.dumps(json_payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            meta = {
                "filename": source_path.name,
                "suffix": source_path.suffix.lower(),
            }

            return ParsedDocumentRecord(
                source_path=str(source_path),
                output_markdown_path=str(md_path),
                output_json_path=str(json_path),
                status="success",
                meta=meta,
            )

        except Exception as exc:
            return ParsedDocumentRecord(
                source_path=str(source_path),
                output_markdown_path=str(md_path),
                output_json_path=str(json_path),
                status="failed",
                error=f"{type(exc).__name__}: {exc}",
            )

    def convert_all(self, raw_dir: Path, parsed_dir: Path) -> list[ParsedDocumentRecord]:
        records: list[ParsedDocumentRecord] = []

        for source_path in self.iter_source_files(raw_dir):
            record = self.convert_one(source_path, parsed_dir)
            records.append(record)

        manifest_path = parsed_dir / "manifest.json"
        parsed_dir.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            json.dumps([r.to_dict() for r in records], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        return records