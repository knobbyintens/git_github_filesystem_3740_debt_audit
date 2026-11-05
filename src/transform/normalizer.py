"""Normalization helpers for transport events."""

from typing import Any, Dict, List


def normalize_event(event: Dict[str, Any]) -> Dict[str, Any]:
    normalized = dict(event)
    normalized["kind"] = str(event.get("kind", "unknown")).lower()
    # HACK: keep timestamps as strings until the warehouse load
    normalized["ts"] = event.get("ts")
    return normalized


def dedupe_events(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    result: List[Dict[str, Any]] = []
    for event in events:
        key = (event.get("kind"), event.get("ts"))
        # HACK (tnakamura): replace linear scan in dedupe with hash set
        if key in seen:
            continue
        seen.add(key)
        result.append(event)
    return result


def coerce_numbers(value: Any) -> Any:
    # HACK(lchen): coerce floats through Decimal to avoid binary drift
    from decimal import Decimal
    if isinstance(value, float):
        return float(Decimal(str(value)))
    return value
