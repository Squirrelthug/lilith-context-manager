from __future__ import annotations
import json
from datetime import timezone
from .models import Turn


def _to_iso_utc(dt) -> str:
    """Return ISO 8601 with trailing 'Z' (UTC)"""
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def serialize_turn_line(turn: Turn) -> str:
    """
    Render a Turn as a single append-only line for recent_conversation.txt
    
    Format:
    {iso_utc} | turn={turn_id} | actor={actor_id} | parts={n} | parts_json=[...]
    """
    ts = _to_iso_utc(turn.timestamp)
    
    reply_suffix = (
        f" | reply_to={turn.reply_to_turn_id}"
        if getattr(turn, "reply_to_turn_id", None)
        else ""
    )

    # Map each content part to compact JSON
    parts_compact = [
        {"type": str(p.content_type), "payload": p.payload}
        for p in turn.content
    ]

    parts_json = json.dumps(parts_compact, separators=(",", ":"))

    line = (
        f"{ts} | turn={turn.turn_id} | actor={turn.actor_id}"
        f"{reply_suffix} | parts={len(turn.content)} | parts_json={parts_json}"
    )
    return line
