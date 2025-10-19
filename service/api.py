from fastapi import FastAPI, Body, HttpException
from pathlib import Path
import json
from .core.tracker import create_new_session
from .core.models import Session, Turn, Branch
from .core.formatters import serialize_turn_line

# create the app intance
app = FastAPI()

# --- Session/branch helpers used by POST /session/{session_id}/turn ---


def _session_dir(session_id: str) -> Path:
    # Filesystem root for an active session
    return Path("active_sessions") / session_id

def _read_session_json(session_id: str):
    # Raw JSON loader (dict) so we can read active_branch_id without model import loops
    sdir = _session_dir(session_id)
    sfile = sdir / "session.json"
    if not sfile.exists():
        raise HttpException(status_code=404, detail="Session not found")
    return json.loads(sfile.read_text())

def _write_json_atomic(path: Path, data: dict) -> None:
    # Cross-platform atomic-ish write (temp -> replace)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2))
    tmp.replace(path)

def _ensure_active_branch(session_id: str, session_data: dict) -> dict:
    """
    Ensure session_data has an active_branch_id and that the branch directory/files exist.
    If missing, create a minimal branch and persist it back to session.json
    Returns possibly-updated session_data.
    """
    sdir = _session_dir(session_id)
    active_branch_id = session_data.get("active_branch_id")

    # If already set and folder exists, nothing to do
    if active_branch_id:
        bdir = sdir / active_branch_id
        if bdir.exists():
            return session_data

    # Create a new branch id
    if not active_branch_id:
        active_branch_id = "branch-1"
        # Ensure value is unique if it already exists
        idx = 1
        while (sdir / f"branch-{idx}").exists():
            idx += 1
        active_branch_id = f"branch-{idx}"
        session_data["active_branch_id"] = active_branch_id
        session_data.setdefault("branch_ids", [])
        if active_branch_id not in session_data["branch_ids"]:
            session_data["branch_ids"].append(active_branch_id)
    
    # Ensure branch directory and minimal files
    bdir = sdir / active_branch_id
    bdir.mkdir(parents=True, exist_ok=True)
    (bdir / "recent_conversation.txt").touch()
    (bdir / "full_transcript.txt").touch()
    (bdir / "branch_knowledge.json").write_text(json.dumps(
        {"summaries": [], "established_facts": {}}, indent=2

    ))

    # Persist session.json with updated active_branch_id / branch_ids (atomic)
    _write_json_atomic(sdir / "session.json", session_data)
    return session_data


# the 'response_model=Session' tells FastAPI to expect a Session object
@app.post("/session", response_model=Session)
def create_session():
    """
    Handles the API request to create a new session.
    """
    # Call a function from tracker.py and return its result
    return create_new_session()


@app.post("/session/{session_id}/turn", status_code=200)
def add_turn(session_id: str, turn: Turn = Body(...)):
    """
    Accept a Turn, resolve active branch, serialize, and atomically append to recent_conversation
    Returns 200 OK with {"ok": true} on success
    """

    # Reject empty content early
    if not turn.content:
        raise HttpException(status_code=400, detail="Turn.content must contain at least 1 part.")

    # Read sesson.json (dict) and ensure branch exists
    session_data = _read_session_json(session_id)
    session_data = _ensure_active_branch(session_id, session_data)

    # Resolve active branch file path
    active_branch_id = session_data["active_branch_id"]
    bdir = _session_dir(session_id) / active_branch_id
    rc_file = bdir / "recent_conversation.txt"
    if not rc_file.exists():
        rc_file.touch()

    # Serialize one line and atomically append
    line = serialize_turn_line(turn) + "\n"

    # Atomic append via read + replace (portable)
    existing = rc_file.read_text() if rc_file.exists() else ""
    tmp = rc_file.with_suffix(rc_file.suffix + ".tmp")
    tmp.write_text(existing + line)
    tmp.replace(rc_file)

    return {"ok": True}
