from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any


INPUT_PATH = Path("docs/parsed/fix_messages.json")
OUTPUT_PATH = Path("docs/parsed/normalized_fix_schema.json")


COMPONENT_NAME_TO_SECTION = {
    "Standard Header": "13.1",
    "Standard Trailer": "13.2",
    "Instrument": "13.3",
    "Instrument Component Block": "13.3",
    "Parties": "13.4",
    "Parties Block": "13.4",
}


TAG_TO_NAME_FALLBACK = {
    # Standard Header
    "8": "BeginString",
    "9": "BodyLength",
    "35": "MsgType",
    "49": "SenderCompID",
    "56": "TargetCompID",
    "34": "MsgSeqNum",
    "43": "PossDupFlag",
    "52": "SendingTime",
    "97": "PossResend",
    "122": "OrigSendingTime",
    # Standard Trailer
    "10": "CheckSum",
    # Common FIX fields often seen in this spec
    "11": "ClOrdID",
    "14": "CumQty",
    "15": "Currency",
    "17": "ExecID",
    "31": "LastPx",
    "32": "LastQty",
    "37": "OrderID",
    "38": "OrderQty",
    "39": "OrdStatus",
    "40": "OrdType",
    "41": "OrigClOrdID",
    "44": "Price",
    "45": "RefSeqNum",
    "48": "SecurityID",
    "54": "Side",
    "55": "Symbol",
    "58": "Text",
    "59": "TimeInForce",
    "60": "TransactTime",
    "75": "TradeDate",
    "150": "ExecType",
    "151": "LeavesQty",
    "262": "MDReqID",
    "263": "SubscriptionRequestType",
    "264": "MarketDepth",
    "265": "MDUpdateType",
    "268": "NoMDEntries",
    "269": "MDEntryType",
    "270": "MDEntryPx",
    "271": "MDEntrySize",
    "279": "MDUpdateAction",
    "281": "MDReqRejReason",
    "320": "SecurityReqID",
    "322": "SecurityResponseID",
    "461": "CFICode",
    "559": "SecurityListRequestType",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def normalize_spaces(text: str | None) -> str | None:
    if text is None:
        return None
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def slugify_name(name: str | None) -> str | None:
    if not name:
        return None
    s = name.strip()
    s = s.replace("-", " ")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        return None
    return s.lower()


def infer_required_bool(raw: str | None) -> bool | None:
    if raw is None:
        return None
    value = raw.strip().upper()
    if value == "Y":
        return True
    if value == "N":
        return False
    return None


def is_component_name(name: str | None) -> bool:
    return bool(name and name in COMPONENT_NAME_TO_SECTION)


def looks_like_tag(value: str | None) -> bool:
    return bool(value and re.fullmatch(r"\d+", value.strip()))


def extract_msg_type(comment: str | None) -> str | None:
    if not comment:
        return None
    m = re.search(r"MsgType\s*=\s*([A-Za-z0-9]+)", comment)
    return m.group(1) if m else None


def field_name_from_source(field: dict[str, Any]) -> str | None:
    """
    优先取已有 field_name；
    如果为空，再尝试用 tag 映射补名字。
    """
    name = normalize_spaces(field.get("field_name"))
    if name:
        return name

    tag = normalize_spaces(field.get("tag"))
    if tag and tag in TAG_TO_NAME_FALLBACK:
        return TAG_TO_NAME_FALLBACK[tag]

    return None


def normalize_field(field: dict[str, Any], owner_kind: str) -> dict[str, Any]:
    raw_tag = normalize_spaces(field.get("tag"))
    raw_name = field_name_from_source(field)
    raw_required = normalize_spaces(field.get("required"))
    raw_comments = normalize_spaces(field.get("comments"))
    raw_component = bool(field.get("component"))
    raw_component_section = normalize_spaces(field.get("component_section"))
    msg_type_hint = normalize_spaces(field.get("msg_type_hint"))

    # 修复一些被抽坏的组件行：
    # 例如 tag="Standard Header", field_name="Y", required=None
    if raw_tag in COMPONENT_NAME_TO_SECTION and raw_name in {"Y", "N", "N*", "Y*"}:
        raw_comments = raw_comments or None
        raw_required = raw_name
        raw_name = raw_tag
        raw_tag = None

    # tag 为 "-" 时，多半也是组件占位或空tag
    if raw_tag == "-":
        raw_tag = None

    # 重新判断组件
    component = raw_component or is_component_name(raw_name)
    component_section = raw_component_section or (
        COMPONENT_NAME_TO_SECTION.get(raw_name) if component else None
    )

    required_bool = infer_required_bool(raw_required)

    # 普通字段如果名字还是空，就尽量用 tag fallback
    if not component and not raw_name and raw_tag:
        raw_name = TAG_TO_NAME_FALLBACK.get(raw_tag)

    python_name = slugify_name(raw_name)

    return {
        "kind": "component_ref" if component else "field",
        "tag": raw_tag,
        "name": raw_name,
        "python_name": python_name,
        "required_raw": raw_required,
        "required": required_bool,
        "comments": raw_comments,
        "component_section": component_section,
        "msg_type_hint": msg_type_hint or extract_msg_type(raw_comments),
        "source_component_flag": raw_component,
        "source_owner_kind": owner_kind,
    }


def dedupe_expanded_fields(fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[Any, ...]] = set()
    result: list[dict[str, Any]] = []

    for f in fields:
        key = (
            f.get("kind"),
            f.get("tag"),
            f.get("name"),
            f.get("component_section"),
            f.get("required_raw"),
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(f)

    return result


def expand_component_refs(
    fields: list[dict[str, Any]],
    components_by_section: dict[str, dict[str, Any]],
    stack: tuple[str, ...] = (),
) -> list[dict[str, Any]]:
    expanded: list[dict[str, Any]] = []

    for field in fields:
        expanded.append(deepcopy(field))

        if field.get("kind") != "component_ref":
            continue

        section = field.get("component_section")
        if not section or section in stack:
            continue

        component = components_by_section.get(section)
        if not component:
            continue

        component_fields = component.get("fields_normalized", [])
        nested = expand_component_refs(
            component_fields,
            components_by_section,
            stack=stack + (section,),
        )
        expanded.extend(nested)

    return dedupe_expanded_fields(expanded)


def normalize_component(section: str, comp: dict[str, Any]) -> dict[str, Any]:
    fields = comp.get("fields", [])
    normalized_fields = [normalize_field(f, owner_kind="component") for f in fields]

    issues: list[str] = []
    if comp.get("status") != "success":
        issues.append("component_extract_not_success")
    if not normalized_fields:
        issues.append("component_has_no_fields")
    if any(f["name"] is None and f["kind"] == "field" for f in normalized_fields):
        issues.append("component_has_fields_without_name")

    return {
        "section": section,
        "title": normalize_spaces(comp.get("title")),
        "table_ref": comp.get("table_ref"),
        "status": comp.get("status"),
        "fields_normalized": normalized_fields,
        "issues": issues,
    }


def normalize_message(msg: dict[str, Any]) -> dict[str, Any]:
    fields = msg.get("fields", [])
    normalized_fields = [normalize_field(f, owner_kind="message") for f in fields]

    issues: list[str] = []
    status = msg.get("status")

    if status != "success":
        issues.append("message_extract_not_success")

    if not normalized_fields:
        issues.append("message_has_no_fields")

    columns = msg.get("columns", [])
    if "req_d_comments" in columns:
        issues.append("broken_table_header")

    # 识别明显抽坏的行
    for f in normalized_fields:
        if (
            f["kind"] == "field"
            and f["tag"] is not None
            and not looks_like_tag(f["tag"])
            and f["name"] in {"Y", "N", "N*", "Y*"}
        ):
            issues.append("broken_field_alignment")
            break

    msg_type = normalize_spaces(msg.get("msg_type"))
    if not msg_type:
        for f in normalized_fields:
            if f.get("msg_type_hint"):
                msg_type = f["msg_type_hint"]
                break

    return {
        "section": normalize_spaces(msg.get("section")),
        "title": normalize_spaces(msg.get("title")),
        "python_class_name": build_python_class_name(msg.get("title")),
        "table_ref": msg.get("table_ref"),
        "status": status,
        "msg_type": msg_type,
        "fields_raw_normalized": normalized_fields,
        "issues": sorted(set(issues)),
    }


def build_python_class_name(title: str | None) -> str | None:
    if not title:
        return None
    s = re.sub(r"[^A-Za-z0-9]+", " ", title).strip()
    if not s:
        return None
    return "".join(part.capitalize() for part in s.split())


def build_tag_index(messages: list[dict[str, Any]], components: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}

    def consume(field: dict[str, Any]) -> None:
        tag = field.get("tag")
        name = field.get("name")
        if not tag or not name or not looks_like_tag(tag):
            return
        index.setdefault(tag, {"name": name, "python_name": slugify_name(name)})

    for comp in components.values():
        for field in comp.get("fields_normalized", []):
            consume(field)

    for msg in messages:
        for field in msg.get("fields_expanded", []):
            consume(field)

    return index


def main() -> None:
    raw = load_json(INPUT_PATH)

    raw_components = raw.get("components", {})
    raw_messages = raw.get("messages", [])

    normalized_components: dict[str, dict[str, Any]] = {}
    for section, comp in raw_components.items():
        normalized_components[section] = normalize_component(section, comp)

    normalized_messages: list[dict[str, Any]] = []
    for msg in raw_messages:
        normalized_messages.append(normalize_message(msg))

    # 第二阶段：展开组件
    for msg in normalized_messages:
        fields_raw = msg["fields_raw_normalized"]
        fields_expanded = expand_component_refs(fields_raw, normalized_components)
        msg["fields_expanded"] = fields_expanded

    # 给组件本身也补 expanded，便于调试
    for section, comp in normalized_components.items():
        comp["fields_expanded"] = expand_component_refs(
            comp["fields_normalized"],
            normalized_components,
        )

    tag_index = build_tag_index(normalized_messages, normalized_components)

    output = {
        "meta": {
            "source": str(INPUT_PATH),
            "message_count": len(normalized_messages),
            "component_count": len(normalized_components),
        },
        "components": normalized_components,
        "messages": normalized_messages,
        "tag_index": tag_index,
    }

    dump_json(OUTPUT_PATH, output)

    print(f"Normalized schema written to: {OUTPUT_PATH}")
    print(f"Messages: {len(normalized_messages)}")
    print(f"Components: {len(normalized_components)}")

    issue_count = sum(1 for m in normalized_messages if m["issues"])
    print(f"Messages with issues: {issue_count}")

    if issue_count:
        print("\nMessages with issues:")
        for msg in normalized_messages:
            if msg["issues"]:
                print(f"- {msg['section']} {msg['title']}: {', '.join(msg['issues'])}")


if __name__ == "__main__":
    main()