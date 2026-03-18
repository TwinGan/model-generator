from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


JSON_PATH = Path("docs/parsed/LMESelect_93_FIX_Specification_v11.json")
OUTPUT_PATH = Path("docs/parsed/fix_messages.json")


MESSAGE_DETAILS_SECTIONS = {
    "4.5",
    "6.2",
    "8.2",
    "9.2",
    "10.2",
    "11.2",
    "12.2",
}

COMPONENT_SECTIONS = {
    "13.1": "Standard Header",
    "13.2": "Standard Trailer",
    "13.3": "Instrument Component Block",
    "13.4": "Parties Block",
}

COMPONENT_NAME_TO_SECTION = {
    "Standard Header": "13.1",
    "Standard Trailer": "13.2",
    "Instrument": "13.3",
    "Instrument Component Block": "13.3",
    "Parties": "13.4",
    "Parties Block": "13.4",
}


SECTION2_PATTERN = re.compile(r"^(\d+\.\d+)\s+(.+)$")
SECTION3_PATTERN = re.compile(r"^(\d+\.\d+\.\d+)\s+(.+)$")

def ref_to_obj(data: dict[str, Any], ref: str) -> Any:
    parts = ref.lstrip("#/").split("/")
    obj: Any = data
    for p in parts:
        obj = obj[int(p)] if p.isdigit() else obj[p]
    return obj


def normalize_cell_text(cell: Any) -> str:
    if cell is None:
        return ""

    if isinstance(cell, str):
        return cell.strip()

    if isinstance(cell, dict):
        for key in ("text", "content", "cell_text", "label"):
            value = cell.get(key)
            if isinstance(value, str):
                return value.strip()

        for key in ("texts",):
            value = cell.get(key)
            if isinstance(value, list):
                parts = [str(x).strip() for x in value if str(x).strip()]
                if parts:
                    return " ".join(parts)

        return ""

    if isinstance(cell, list):
        parts = [normalize_cell_text(x) for x in cell]
        parts = [x for x in parts if x]
        return " ".join(parts)

    return str(cell).strip()


def table_to_rows(table_obj: dict[str, Any]) -> list[list[str]]:
    data = table_obj.get("data", {})
    grid = data.get("grid", [])
    return [[normalize_cell_text(cell) for cell in row] for row in grid]


def clean_rows(rows: list[list[str]]) -> list[list[str]]:
    cleaned: list[list[str]] = []
    for row in rows:
        normalized = [cell.strip() for cell in row]
        if any(normalized):
            cleaned.append(normalized)
    return cleaned


def looks_like_fix_message_table(rows: list[list[str]]) -> bool:
    if not rows:
        return False

    head = " | ".join(" ".join(r) for r in rows[:3]).lower()
    return (
        "tag" in head
        and "field" in head
        and ("req'd" in head or "req" in head or "required" in head)
        and "comments" in head
    )


def looks_like_component_table(rows: list[list[str]]) -> bool:
    if not rows:
        return False

    head = " | ".join(" ".join(r) for r in rows[:3]).lower()
    return (
        "tag" in head
        and ("name" in head or "field name" in head)
        and ("req'd" in head or "req" in head or "required" in head)
        and "comments" in head
    )


def normalize_header_name(name: str) -> str:
    n = name.strip().lower()
    if n == "tag":
        return "tag"
    if n in {"field name", "field"}:
        return "field_name"
    if n in {"req'd", "reqd", "req", "required"}:
        return "required"
    if n == "comments":
        return "comments"
    return re.sub(r"[^a-z0-9]+", "_", n).strip("_")


def rows_to_fields(rows: list[list[str]]) -> tuple[list[str], list[dict[str, Any]]]:
    if not rows:
        return [], []

    headers = [normalize_header_name(h) for h in rows[0]]
    fields: list[dict[str, Any]] = []

    for row in rows[1:]:
        padded = row + [""] * (len(headers) - len(row))
        padded = padded[: len(headers)]

        item = dict(zip(headers, padded))

        tag = (item.get("tag") or "").strip()
        field_name = (item.get("field_name") or "").strip()
        required = (item.get("required") or "").strip()
        comments = (item.get("comments") or "").strip()

        is_component = (
            not tag
            and field_name in COMPONENT_NAME_TO_SECTION
        )

        component_section = (
            COMPONENT_NAME_TO_SECTION.get(field_name) if is_component else None
        )

        msg_type = None
        if comments:
            m = re.search(r"MsgType\s*=\s*([A-Za-z0-9]+)", comments)
            if m:
                msg_type = m.group(1)

        fields.append(
            {
                "tag": tag or None,
                "field_name": field_name or None,
                "required": required or None,
                "required_bool": (
                    True if required == "Y" else False if required == "N" else None
                ),
                "comments": comments or None,
                "component": is_component,
                "component_section": component_section,
                "msg_type_hint": msg_type,
            }
        )

    return headers, fields


def find_first_table_after(
    data: dict[str, Any],
    children: list[dict[str, Any]],
    start_idx: int,
) -> tuple[str | None, list[list[str]]]:
    for j in range(start_idx + 1, min(start_idx + 15, len(children))):
        ref = children[j]["$ref"]
        kind = ref.split("/")[1]

        if kind == "texts":
            obj = ref_to_obj(data, ref)
            label = obj.get("label")
            text = (obj.get("text") or "").strip()

            if label == "section_header" and SECTION3_PATTERN.match(text):
                return None, []

        if kind != "tables":
            continue

        table_obj = ref_to_obj(data, ref)
        rows = clean_rows(table_to_rows(table_obj))
        if rows:
            return ref, rows

    return None, []


def find_first_fix_table_after(
    data: dict[str, Any],
    children: list[dict[str, Any]],
    start_idx: int,
) -> tuple[str | None, list[list[str]]]:
    for j in range(start_idx + 1, min(start_idx + 15, len(children))):
        ref = children[j]["$ref"]
        kind = ref.split("/")[1]

        if kind == "texts":
            obj = ref_to_obj(data, ref)
            label = obj.get("label")
            text = (obj.get("text") or "").strip()

            if label == "section_header" and SECTION3_PATTERN.match(text):
                return None, []

        if kind != "tables":
            continue

        table_obj = ref_to_obj(data, ref)
        rows = clean_rows(table_to_rows(table_obj))
        if looks_like_fix_message_table(rows):
            return ref, rows

    return None, []


def extract_components(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    children = data["body"]["children"]
    components: dict[str, dict[str, Any]] = {}

    for i, child in enumerate(children):
        ref = child["$ref"]
        kind = ref.split("/")[1]
        if kind != "texts":
            continue

        obj = ref_to_obj(data, ref)
        text = re.sub(r"\s+", " ", (obj.get("text") or "")).strip()
        if not text:
            continue

        m2 = SECTION2_PATTERN.match(text)
        if not m2:
            continue

        section = m2.group(1)
        title = m2.group(2).strip()

        if section not in COMPONENT_SECTIONS:
            continue

        table_ref, rows = find_first_table_after(data, children, i)
        if not table_ref or not rows or not looks_like_component_table(rows):
            components[section] = {
                "section": section,
                "title": title,
                "table_ref": None,
                "columns": [],
                "fields": [],
                "status": "table_not_found",
            }
            continue

        columns, fields = rows_to_fields(rows)

        components[section] = {
            "section": section,
            "title": title,
            "table_ref": table_ref,
            "columns": columns,
            "fields": fields,
            "status": "success",
        }

    return components


def extract_messages(data: dict[str, Any]) -> list[dict[str, Any]]:
    children = data["body"]["children"]
    current_message_details_prefix: str | None = None
    messages: list[dict[str, Any]] = []

    for i, child in enumerate(children):
        ref = child["$ref"]
        kind = ref.split("/")[1]
        if kind != "texts":
            continue

        obj = ref_to_obj(data, ref)
        label = obj.get("label")
        text = (obj.get("text") or "").strip()

        if label != "section_header":
            continue

        m2 = SECTION2_PATTERN.match(text)
        if m2:
            prefix = m2.group(1)
            title = m2.group(2)
            if prefix in MESSAGE_DETAILS_SECTIONS and "Message Details" in title:
                current_message_details_prefix = prefix
            else:
                current_message_details_prefix = None
            continue

        m3 = SECTION3_PATTERN.match(text)
        if not (m3 and current_message_details_prefix):
            continue

        section = m3.group(1)
        title = m3.group(2).strip()

        if not section.startswith(current_message_details_prefix + "."):
            continue

        table_ref, rows = find_first_fix_table_after(data, children, i)
        if not table_ref or not rows:
            messages.append(
                {
                    "section": section,
                    "title": title,
                    "table_ref": None,
                    "columns": [],
                    "fields": [],
                    "msg_type": None,
                    "status": "table_not_found",
                }
            )
            continue

        columns, fields = rows_to_fields(rows)

        msg_type = None
        for f in fields:
            if f.get("msg_type_hint"):
                msg_type = f["msg_type_hint"]
                break

        messages.append(
            {
                "section": section,
                "title": title,
                "table_ref": table_ref,
                "columns": columns,
                "fields": fields,
                "msg_type": msg_type,
                "status": "success",
            }
        )

    return messages


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    components = extract_components(data)
    messages = extract_messages(data)

    OUTPUT_PATH.write_text(
        json.dumps(
            {
                "components": components,
                "messages": messages,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"Extracted {len(messages)} messages and {len(components)} components to {OUTPUT_PATH}"
    )

    print("\nMessages:")
    for msg in messages:
        print(f"- {msg['section']} {msg['title']} [{msg['status']}]")

    print("\nComponents:")
    for section, comp in components.items():
        print(f"- {section} {comp['title']} [{comp['status']}]")


if __name__ == "__main__":
    main()