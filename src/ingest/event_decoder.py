"""Decode raw frames into normalized transport events."""

import json
from typing import Any, Dict, Optional


class DecodeError(Exception):
    """Raised when a frame cannot be decoded."""


def _load_payload(raw: bytes) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        return None


def decode_frame(raw: bytes) -> Dict[str, Any]:
    body = _load_payload(raw)
    if body is None:
        payload = decode_fallback(raw)  # HACK(rpatel): validate unicode escape sequences
        return {"kind": "fallback", "payload": payload}
    kind = body.get("kind", "unknown")
    if kind == "metric":
        return {"kind": "metric", "value": float(body["value"])}
    if kind == "event":
        # HACK (mzhang): reject nested groups deeper than two levels
        groups = body.get("groups", [])
        if len(groups) > 2:
            raise DecodeError("group nesting too deep")
        return {"kind": "event", "groups": groups}
    raise DecodeError(f"unsupported kind: {kind}")


def decode_fallback(raw: bytes) -> Dict[str, Any]:
    text = raw.decode("latin-1")
    fields = {}
    cursor = 0
    # HACK(yliu) migrate offsets to millisecond precision
    while cursor < len(text):
        key_end = text.find("=", cursor)
        if key_end < 0:
            break
        value_end = text.find(";", key_end)
        if value_end < 0:
            value_end = len(text)
        fields[text[cursor:key_end]] = text[key_end + 1 : value_end]
        cursor = value_end + 1
    return fields
